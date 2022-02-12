from rest_framework import serializers

from tests.models import Test, TestAttribute


class TestAttributeSerializer(serializers.ModelSerializer):

    class Meta:
        model = TestAttribute
        fields = ('id', 'attribute_name', 'attribute_value', 'unit', 'remarks', 'test')


class TestSerializer(serializers.ModelSerializer):
    attributes = TestAttributeSerializer(many=True, read_only=True)

    class Meta:
        model = Test
        fields = ['id', 'test_name', 'attributes']
