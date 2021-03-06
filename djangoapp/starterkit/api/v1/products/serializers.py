from django.db.models import Q
from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from .models import *
from drf_writable_nested.serializers import WritableNestedModelSerializer


class SexCreateSeriazlizer(ModelSerializer):
    class Meta:
        model = Sex
        fields = "__all__"

    def create(self, validated_data):
        category = Sex.objects.update_or_create(
            slug=validated_data.get('slug', None),
            defaults=validated_data)
        return category


class SexSeriazlizer(ModelSerializer):
    class Meta:
        model = Sex
        fields = "__all__"


class ParentCategorySerializer(ModelSerializer):
    parent = PrimaryKeyRelatedField(queryset=Category.objects.all())
    sex = SexSeriazlizer()

    class Meta:
        model = Category
        fields = ('title', 'slug', 'id', 'parent', 'sex',)


class CategorySeriazlizer(ModelSerializer):
    parent = ParentCategorySerializer()
    sex = SexSeriazlizer()

    class Meta:
        model = Category
        fields = ('title', 'slug', 'pk', 'parent', 'sex',)


class CategoryCreateSeriazlizer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

    def create(self, validated_data):
        category = Category.objects.update_or_create(slug=validated_data.get('slug', None),
                                                     sex=validated_data.get('sex', None),
                                                     defaults=validated_data)
        return category


class SizeCreateSeriazlizer(ModelSerializer):
    class Meta:
        model = Size
        fields = "__all__"

    def create(self, validated_data):
        size = Size.objects.update_or_create(slug=validated_data.get('slug', None), defaults=validated_data)
        return size


class ColorCreateSeriazlizer(ModelSerializer):
    class Meta:
        model = Color
        fields = "__all__"

    def create(self, validated_data):
        color = Color.objects.update_or_create(slug=validated_data.get('slug', None), defaults=validated_data)
        return color


class TagCreateSeriazlizer(ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"

    def create(self, validated_data):
        print(validated_data)
        tag = Tag.objects.update_or_create(slug=validated_data.get('slug', None), defaults=validated_data)
        return tag[0]


class SizeCreateSeriazlizer(ModelSerializer):
    class Meta:
        model = Size
        fields = "__all__"

    def create(self, validated_data):
        size = Size.objects.update_or_create(title=validated_data.get('title', None), defaults=validated_data)
        return size[0]


class SizeTypeCreateSeriazlizer(ModelSerializer):
    class Meta:
        model = SizeType
        fields = "__all__"

    def create(self, validated_data):
        print(validated_data)
        size_type = SizeType.objects.update_or_create(slug=validated_data.get('slug', None), defaults=validated_data)
        return size_type[0]


class LeftoverCreateSeriazlizer(ModelSerializer):
    class Meta:
        model = Leftover
        fields = "__all__"


class BrandCreateSeriazlizer(ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"


class SeasonSeriazlizer(ModelSerializer):
    class Meta:
        model = Season
        fields = "__all__"


class ProductCreateSeriazlizer(WritableNestedModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class BrandSeriazlizer(ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"


class VariantsSerializer(ModelSerializer):
    category = CategorySeriazlizer()
    brand = BrandSeriazlizer()

    class Meta:
        model = Product
        exclude = ('variants',)


class ProductViewSerializer(ModelSerializer):
    category = CategorySeriazlizer()
    brand = BrandSeriazlizer()
    variants = VariantsSerializer(many=True)
    sex = SexSeriazlizer()
    class Meta:
        model = Product
        fields = '__all__'
