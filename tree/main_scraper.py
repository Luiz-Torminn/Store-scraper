from get_main_info import get_product_info as gpi

print("""What are the products' URL you want to check the stock?
(Seperate the URLs with a '*') - Ex: www.gts/product1.com * www.gts/product2\n""")

url_input = input("URL(s): ")
urls = url_input.split("*")

i = 0
while i < 5:
    gpi(urls)
    i += 1

# https://www.emag.ro/telefon-mobil-samsung-galaxy-a52s-dual-sim-128gb-6gb-ram-5g-black-sm-a528bzkceue/pd/D2D55XMBM/?ref=profiled_categories_home_1_2&provider=rec&recid=rec_50_4e2d13108fc4049da7b7f8407857b864b94968c4ddeb1eff5be2d572c2cf0cbb_1643234926&scenario_ID=50*https://www.emag.ro/laptop-hp-250-g8-cu-procesor-intel-celeron-n4020-15-6-full-hd-8gb-256gb-ssd-intel-uhd-graphics-600-windows-10-asteroid-silver-2x7l6ea/pd/D14CYFMBM/?ref=profiled_categories_home_3_4&provider=rec&recid=rec_50_4e2d13108fc4049da7b7f8407857b864b94968c4ddeb1eff5be2d572c2cf0cbb_1643234926&scenario_ID=50*https://www.emag.ro/laptop-apple-macbook-air-13-inch-true-tone-procesor-apple-m1-8-nuclee-cpu-si-7-nuclee-gpu-8gb-256gb-gold-int-kb-mgnd3ze-a/pd/DY6BL7MBM/?ref=profiled_categories_home_3_2&provider=rec&recid=rec_50_4e2d13108fc4049da7b7f8407857b864b94968c4ddeb1eff5be2d572c2cf0cbb_1643489150&scenario_ID=50



