main_value_1 = input()
main_value_2 = input()

code_of_product_1, number_of_units_of_product_1, the_price_for_one_unit_of_product_1 = main_value_1.split()

code_of_product_2, number_of_units_of_product_2, the_price_for_one_unit_of_product_2 = main_value_2.split()

code_of_product_1 = int(code_of_product_1)
number_of_units_of_product_1 = int(number_of_units_of_product_1)
the_price_for_one_unit_of_product_1 = float(the_price_for_one_unit_of_product_1)

code_of_product_2 = int(code_of_product_2)
number_of_units_of_product_2 = int(number_of_units_of_product_2)
the_price_for_one_unit_of_product_2 = float(the_price_for_one_unit_of_product_2)



VALOR_A_PAGAR = (number_of_units_of_product_1 * the_price_for_one_unit_of_product_1) + (number_of_units_of_product_2 * the_price_for_one_unit_of_product_2)

print("VALOR A PAGAR: R$ {:.2f}".format(VALOR_A_PAGAR))
