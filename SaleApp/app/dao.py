def load_categories():
    return[{
        'id': 1,
        'name': 'Mobile'
    }, {'id': 2,
        'name': 'Tablet'
        }
    ]
def load_products(kw=None):
    products = [{
        'id': 1,
        'name': 'iPhone 15 pro max',
        'price': 40000000,
        'image': 'https://www.google.com/imgres?imgurl=https%3A%2F%2Fcdn.viettelstore.vn%2FImages%2FProduct%2FProductImage%2F291703442.jpeg&tbnid=-_v_L6Y2LmONgM&vet=12ahUKEwiqmPq20pCCAxUtplYBHUUWBVEQMygCegUIARCUAQ..i&imgrefurl=https%3A%2F%2Fm.viettelstore.vn%2Fdien-thoai%2Fiphone-15-pro-max-pid317067.html&docid=2AHz_suBE13yIM&w=500&h=500&q=iphone%2015%20pro%20max&ved=2ahUKEwiqmPq20pCCAxUtplYBHUUWBVEQMygCegUIARCUAQ'
    }, {
        'id': 2,
        'name': 'iPhone 14',
        'price': 30000000,
        'image':'https://www.google.com/imgres?imgurl=https%3A%2F%2Fcdn.hoanghamobile.com%2Fi%2Fproductlist%2Fdsp%2FUploads%2F2022%2F09%2F08%2F2222.png&tbnid=X7JMRF8qBkpLlM&vet=12ahUKEwivxf3o0pCCAxX6vVYBHTfRDroQMygAegUIARDGAQ..i&imgrefurl=https%3A%2F%2Fhoanghamobile.com%2Fdien-thoai-di-dong%2Fapple-iphone-14-128gb-chinh-hang-vn-a&docid=l9HzRss-TtPgeM&w=370&h=370&q=iphone%2014&ved=2ahUKEwivxf3o0pCCAxX6vVYBHTfRDroQMygAegUIARDGAQ'
    }, {
        'id': 3,
        'name': 'ROG Gaming',
        'price': 20000000,
        'image': 'https://www.google.com/imgres?imgurl=https%3A%2F%2Fdlcdnwebimgs.asus.com%2Fgain%2F918ED9E4-12F1-4D35-A63F-BA80E930A626%2Fw1000%2Fh732&tbnid=HWJSrcrxnD4YAM&vet=12ahUKEwiFwbuW05CCAxX7mlYBHblGCCMQMygJegQIARBo..i&imgrefurl=https%3A%2F%2Frog.asus.com%2Fid%2Fphones%2Frog-phone-6-pro-model%2Fgallery%2F&docid=YFHbK_lmO8x40M&w=996&h=732&q=rog%20phone%206&ved=2ahUKEwiFwbuW05CCAxX7mlYBHblGCCMQMygJegQIARBo'
    }]
    if kw:
        products =[p for p in products if p['name'].find(kw) >=0 ]
    return products