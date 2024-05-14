meme_dict = {
            "LOL" : "komik bir şeye verilen cevap",
            "CRINGE" : "garip ya da utandırıcı bir şey",
            "ROFL" : "bir şakaya karşılık cevap",
            "SHEESH" : "onaylamamak",
            "CREEPY" : "korkunç",
            "AGGRO": "agresifleşmek/sinirlenmek",
            }
word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")
if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("https://www.google.com/search?q=",word,"+ne+","demek""&amp;amp;sca_esv=bbbf2f4e60da03cb&amp;amp;sca_upv=1&amp;amp;sxsrf=ADLYWILfTzQTheYnVaZyTqT9rEXfG7mL1w%3A1715703058446&amp;amp;ei=Eo1DZqDuGuuH7NYPrPa_2Ao&amp;amp;udm=&amp;amp;ved=0ahUKEwigv9r6w42GAxXrA9sEHSz7D6sQ4dUDCA8&amp;amp;uact=5&amp;amp;oq=a+a&amp;amp;gs_lp=Egxnd3Mtd2l6LXNlcnAiA2EgYTIFEAAYgAQyChAuGIAEGEMYigUyChAAGIAEGEMYigUyChAAGIAEGEMYigUyChAAGIAEGEMYigUyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABEj8BVAAWMICcAB4AJABAJgBnAGgAakCqgEDMC4yuAEDyAEA-AEBmAICoALMAsICChAjGIAEGCcYigXCAgsQLhiABBjRAxjHAZgDAJIHAzAuMqAHyw8&amp;amp;sclient=gws-wiz-serp", sep="")
