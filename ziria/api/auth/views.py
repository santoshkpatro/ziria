import shortuuid
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from django.db import transaction, DatabaseError
from ziria.models.user import User
from ziria.models.store import Store
from ziria.models.store_member import StoreMember
from ziria.api.auth.serializers import (
    LoginSerializer,
    StoreSerializer,
    LoginProfileSerializer,
    RegisterSerializer,
)


class AuthViewSet(ViewSet):
    @action(detail=False, methods=["post"])
    def register(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        validated_data = serializer.validated_data
        try:
            User.objects.get(email=validated_data["email"])

            return Response(
                data={
                    "detail": "An account is already associated with this email address"
                },
                status=status.HTTP_403_FORBIDDEN,
            )
        except User.DoesNotExist:
            # Start Creating a user and a store
            password = validated_data.pop("password")
            user = User(**validated_data)
            user.set_password(password)

            store = Store(
                name=f"{user.full_name}'s Store",
                slug=shortuuid.ShortUUID().random(length=10),
                currency="INR",
                country="IND",
            )

            try:
                with transaction.atomic():
                    user.save()
                    store.save()
                    StoreMember.objects.create(
                        store=store, user=user, role=StoreMember.Role.OWNER
                    )
            except DatabaseError as e:
                # log the error as critical error
                return Response(
                    data={
                        "detail": "Something went wrong while creating user and store"
                    },
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
            store_serializer = StoreSerializer(instance=store)
            login_profile_serializer = LoginProfileSerializer(instance=user)

            return Response(
                data={
                    "detail": "Rgeister success",
                    "user": login_profile_serializer.data,
                    "store": store_serializer.data,
                },
                status=status.HTTP_200_OK,
            )

    @action(detail=False, methods=["post"])
    def login(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        validated_data = serializer.validated_data
        try:
            user: User = User.objects.get(email=validated_data["email"])
            if not user.check_password(validated_data["password"]):
                return Response(
                    data={
                        "detail": "Login failed, please check your email id or password"
                    },
                    status=status.HTTP_401_UNAUTHORIZED,
                )

            if user.password_reset_required:
                return Response(
                    data={"detail": "Please reset your password to continue"},
                    status=status.HTTP_403_FORBIDDEN,
                )

            stores = Store.objects.filter(store_members__user=user)

            store_serializer = StoreSerializer(instance=stores, many=True)
            login_profile_serializer = LoginProfileSerializer(instance=user)

            return Response(
                data={
                    "detail": "Login success",
                    "user": login_profile_serializer.data,
                    "stores": store_serializer.data,
                },
                status=status.HTTP_200_OK,
            )

        except User.DoesNotExist:
            return Response(
                data={"detail": "Login failed, please check your email id or password"},
                status=status.HTTP_401_UNAUTHORIZED,
            )
