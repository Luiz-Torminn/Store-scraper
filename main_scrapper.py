from get_main_info import get_product_info as gpi

print("""What are the products' URL you want to check the stock?
(Seperate the URLs with a '*') - Ex: www.gts/product1.com * www.gts/product2\n""")

url_input = input("URL(s): ")
loop_repeat = input("How many times would you like the scrapper to recheck the prices? ()")
urls = url_input.split("*")

i = 0

while i < loop_repeat:
    gpi(urls)
    i += 1
