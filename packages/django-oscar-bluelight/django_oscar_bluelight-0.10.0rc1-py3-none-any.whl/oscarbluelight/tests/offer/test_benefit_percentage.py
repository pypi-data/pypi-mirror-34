from decimal import Decimal as D
from django.core import exceptions
from django.test import TestCase
from oscar.test import factories
from oscar.test.basket import add_product, add_products
from oscarbluelight.offer.models import (
    Condition,
    Range,
    Benefit,
    BluelightCountCondition,
    BluelightValueCondition,
    BluelightPercentageDiscountBenefit,
)
import mock



class TestAPercentageDiscountAppliedWithCountCondition(TestCase):
    def setUp(self):
        range = Range.objects.create(
            name="All products", includes_all_products=True)
        self.condition = BluelightCountCondition(
            range=range,
            type=Condition.COUNT,
            value=2)
        self.benefit = BluelightPercentageDiscountBenefit(
            range=range,
            type=Benefit.PERCENTAGE,
            value=20)
        self.offer = mock.Mock()
        self.basket = factories.create_basket(empty=True)


    def test_applies_correctly_to_empty_basket(self):
        result = self.benefit.apply(self.basket, self.condition, self.offer)
        self.assertEqual(D('0.00'), result.discount)
        self.assertEqual(0, self.basket.num_items_with_discount)
        self.assertEqual(0, self.basket.num_items_without_discount)


    def test_applies_correctly_to_basket_with_no_discountable_products(self):
        product = factories.create_product(is_discountable=False)
        add_product(self.basket, D('12.00'), 2, product=product)
        result = self.benefit.apply(self.basket, self.condition, self.offer)
        self.assertEqual(D('0.00'), result.discount)
        self.assertEqual(0, self.basket.num_items_with_discount)
        self.assertEqual(2, self.basket.num_items_without_discount)


    def test_applies_correctly_to_basket_which_matches_condition(self):
        add_product(self.basket, D('12.00'), 2)
        result = self.benefit.apply(self.basket, self.condition, self.offer)
        self.assertEqual(2 * D('12.00') * D('0.2'), result.discount)
        self.assertEqual(2, self.basket.num_items_with_discount)
        self.assertEqual(0, self.basket.num_items_without_discount)


    def test_applies_correctly_to_basket_which_exceeds_condition(self):
        add_product(self.basket, D('12.00'), 3)
        result = self.benefit.apply(self.basket, self.condition, self.offer)
        self.assertEqual(3 * D('12.00') * D('0.2'), result.discount)
        self.assertEqual(3, self.basket.num_items_with_discount)
        self.assertEqual(0, self.basket.num_items_without_discount)


    def test_records_reason_for_discount_no_voucher(self):
        self.offer.name = "My Offer Name"
        self.offer.description = "My Offer Description"
        self.offer.get_voucher = mock.Mock()
        self.offer.get_voucher.return_value = None

        add_product(self.basket, D('5.00'))
        self.benefit.apply(self.basket, self.condition, self.offer)

        line = self.basket.all_lines()[0]
        descrs = line.get_discount_descriptions()
        self.assertEqual(len(descrs), 1)
        self.assertEqual(descrs[0].amount, D('1.00'))
        self.assertEqual(descrs[0].offer_name, 'My Offer Name')
        self.assertEqual(descrs[0].offer_description, 'My Offer Description')
        self.assertIsNone(descrs[0].voucher_name)
        self.assertIsNone(descrs[0].voucher_code)


    def test_records_reason_for_discount_with_voucher(self):
        voucher = mock.Mock()
        voucher.name = "My Voucher"
        voucher.code = "SWEETDEAL"
        self.offer.name = "Offer for Voucher"
        self.offer.description = ""
        self.offer.get_voucher = mock.Mock()
        self.offer.get_voucher.return_value = voucher

        add_product(self.basket, D('5.00'))
        self.benefit.apply(self.basket, self.condition, self.offer)

        line = self.basket.all_lines()[0]
        descrs = line.get_discount_descriptions()
        self.assertEqual(len(descrs), 1)
        self.assertEqual(descrs[0].amount, D('1.00'))
        self.assertEqual(descrs[0].offer_name, 'Offer for Voucher')
        self.assertEqual(descrs[0].offer_description, '')
        self.assertEqual(descrs[0].voucher_name, 'My Voucher')
        self.assertEqual(descrs[0].voucher_code, 'SWEETDEAL')


class TestAPercentageDiscountWithMaxItemsSetAppliedWithCountCondition(TestCase):
    def setUp(self):
        range = Range.objects.create(
            name="All products", includes_all_products=True)
        self.condition = BluelightCountCondition(
            range=range,
            type=Condition.COUNT,
            value=2)
        self.benefit = BluelightPercentageDiscountBenefit(
            range=range,
            type=Benefit.PERCENTAGE,
            value=20,
            max_affected_items=1)
        self.offer = mock.Mock()
        self.basket = factories.create_basket(empty=True)


    def test_applies_correctly_to_empty_basket(self):
        result = self.benefit.apply(self.basket, self.condition, self.offer)
        self.assertEqual(D('0.00'), result.discount)
        self.assertEqual(0, self.basket.num_items_with_discount)
        self.assertEqual(0, self.basket.num_items_without_discount)


    def test_applies_correctly_to_basket_which_matches_condition(self):
        add_product(self.basket, D('12.00'), 2)
        result = self.benefit.apply(self.basket, self.condition, self.offer)
        self.assertEqual(1 * D('12.00') * D('0.2'), result.discount)
        self.assertEqual(2, self.basket.num_items_with_discount)
        self.assertEqual(0, self.basket.num_items_without_discount)


    def test_applies_correctly_to_basket_which_exceeds_condition(self):
        add_products(self.basket, [(D('12.00'), 2), (D('20.00'), 2)])
        result = self.benefit.apply(self.basket, self.condition, self.offer)
        self.assertEqual(1 * D('12.00') * D('0.2'), result.discount)
        # Should only consume the condition products
        self.assertEqual(2, self.basket.num_items_with_discount)
        self.assertEqual(2, self.basket.num_items_without_discount)


class TestAPercentageDiscountAppliedWithValueCondition(TestCase):
    def setUp(self):
        range = Range.objects.create(
            name="All products", includes_all_products=True)
        self.condition = BluelightValueCondition.objects.create(
            range=range,
            type=Condition.VALUE,
            value=D('10.00'))
        self.benefit = BluelightPercentageDiscountBenefit.objects.create(
            range=range,
            type=Benefit.PERCENTAGE,
            value=20)
        self.offer = mock.Mock()
        self.basket = factories.create_basket(empty=True)


    def test_applies_correctly_to_empty_basket(self):
        result = self.benefit.apply(self.basket, self.condition, self.offer)
        self.assertEqual(D('0.00'), result.discount)
        self.assertEqual(0, self.basket.num_items_with_discount)
        self.assertEqual(0, self.basket.num_items_without_discount)


    def test_applies_correctly_to_basket_which_matches_condition(self):
        add_product(self.basket, D('5.00'), 2)
        result = self.benefit.apply(self.basket, self.condition, self.offer)
        self.assertEqual(2 * D('5.00') * D('0.2'), result.discount)
        self.assertEqual(2, self.basket.num_items_with_discount)
        self.assertEqual(0, self.basket.num_items_without_discount)


    def test_applies_correctly_to_basket_which_exceeds_condition_but_matches_on_boundary(self):
        add_product(self.basket, D('5.00'), 3)
        result = self.benefit.apply(self.basket, self.condition, self.offer)
        self.assertEqual(3 * D('5.00') * D('0.2'), result.discount)
        self.assertEqual(3, self.basket.num_items_with_discount)
        self.assertEqual(0, self.basket.num_items_without_discount)


    def test_applies_correctly_to_basket_which_exceeds_condition(self):
        add_product(self.basket, D('4.00'), 3)
        result = self.benefit.apply(self.basket, self.condition, self.offer)
        self.assertEqual(3 * D('4.00') * D('0.2'), result.discount)
        self.assertEqual(3, self.basket.num_items_with_discount)
        self.assertEqual(0, self.basket.num_items_without_discount)



class TestAPercentageDiscountWithMaxItemsSetAppliedWithValueCondition(TestCase):
    def setUp(self):
        range = Range.objects.create(
            name="All products", includes_all_products=True)
        self.condition = BluelightValueCondition.objects.create(
            range=range,
            type=Condition.VALUE,
            value=D('10.00'))
        self.benefit = BluelightPercentageDiscountBenefit.objects.create(
            range=range,
            type=Benefit.PERCENTAGE,
            value=20,
            max_affected_items=1)
        self.offer = mock.Mock()
        self.basket = factories.create_basket(empty=True)


    def test_applies_correctly_to_empty_basket(self):
        result = self.benefit.apply(self.basket, self.condition, self.offer)
        self.assertEqual(D('0.00'), result.discount)
        self.assertEqual(0, self.basket.num_items_with_discount)
        self.assertEqual(0, self.basket.num_items_without_discount)


    def test_applies_correctly_to_basket_which_matches_condition(self):
        add_product(self.basket, D('5.00'), 2)
        result = self.benefit.apply(self.basket, self.condition, self.offer)
        self.assertEqual(1 * D('5.00') * D('0.2'), result.discount)
        self.assertEqual(2, self.basket.num_items_with_discount)
        self.assertEqual(0, self.basket.num_items_without_discount)


    def test_applies_correctly_to_basket_which_exceeds_condition_but_matches_on_boundary(self):
        add_product(self.basket, D('5.00'), 3)
        result = self.benefit.apply(self.basket, self.condition, self.offer)
        self.assertEqual(1 * D('5.00') * D('0.2'), result.discount)
        self.assertEqual(2, self.basket.num_items_with_discount)
        self.assertEqual(1, self.basket.num_items_without_discount)


    def test_applies_correctly_to_basket_which_exceeds_condition(self):
        add_product(self.basket, D('4.00'), 3)
        result = self.benefit.apply(self.basket, self.condition, self.offer)
        self.assertEqual(1 * D('4.00') * D('0.2'), result.discount)
        self.assertEqual(3, self.basket.num_items_with_discount)
        self.assertEqual(0, self.basket.num_items_without_discount)



class TestAPercentageDiscountBenefit(TestCase):
    def test_requires_a_benefit_value(self):
        rng = Range.objects.create(
            name="", includes_all_products=True)
        benefit = Benefit.objects.create(
            type=Benefit.PERCENTAGE, range=rng
        )
        with self.assertRaises(exceptions.ValidationError):
            benefit.clean()
