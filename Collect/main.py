from fastcampus.dees2.projectteam2.bithumb import ParserBithumb
from fastcampus.dees2.projectteam2.coinone import ParserCoinone
from fastcampus.dees2.projectteam2.korbit import ParserKorbit
# from rogers.model.database import Database
# from utils.slack import send_message



def main():
    parser_class = {
        "bithumb": ParserBithumb,
        "coinone": ParserCoinone,
        "korbit": ParserKorbit
    }

    # db = Database()
    for Parser in parser_class.values():
        parser = Parser()
       
        for currency in parser.currency:
            params = {"currency": currency}
            
            response = parser.get_response(params)

            print (currency + " : Response Success!")

            parser.save(response, currency)
            print (currency + " : Save Success!")

            # model = parser.parse(response, currency)
            print ("================================")
           
    #         db.insert(model)

    # send_message("#data-monitoring", "Save data finished!")
    print ("Save data finished!")

if __name__ == '__main__':
    main()
