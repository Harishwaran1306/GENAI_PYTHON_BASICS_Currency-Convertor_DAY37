#Currency Convertor:

print('='*30)
print('Currency Convertor')
print('='*30)


def Curr():
    while True:

        #Getting Input from users:
        
        From_Conversion = input('\nFrom Conversion (USD/EUR/GBP/JPY) OR Type Exit:')
        if From_Conversion == 'exit':
            break
        To_Conversion = input('To Conversion (USD/EUR/GBP/JPY):')

        Conversion_Value= float(input('Enter From Conversion Value: '))

        #Conversion Formulas:

        USD_EUR       = Conversion_Value * 0.8905
        USD_GBP       = Conversion_Value * 0.7510
        USD_JPY       = Conversion_Value * 158.07
        USD_CNY       = Conversion_Value * 6.6912
        EUR_USD       = Conversion_Value * 1.1229
        EUR_GBP       = Conversion_Value * 0.8433
        EUR_JPY       = Conversion_Value * 177.50
        EUR_CNY       = Conversion_Value * 7.5140
        GBP_USD       = Conversion_Value * 1.3316
        GBP_EUR       = Conversion_Value * 1.1858
        GBP_JPY       = Conversion_Value * 210.47
        GBP_CNY       = Conversion_Value * 8.9097
        JPY_USD       = Conversion_Value * 0.0063
        JPY_EUR       = Conversion_Value * 0.0056
        JPY_GBP       = Conversion_Value * 0.0048
        JPY_CNY       = Conversion_Value * 0.0423
        CNY_USD       = Conversion_Value * 0.1495
        CNY_EUR       = Conversion_Value * 0.1331
        CNY_GBP       = Conversion_Value * 0.1122
        CNY_JPY       = Conversion_Value * 23.62


        if From_Conversion == 'USD' and To_Conversion == 'EUR':
            print('The Output is :', USD_EUR)
        elif From_Conversion == 'USD' and To_Conversion == 'GBP':
            print('The Output is :', USD_GBP)
        elif From_Conversion == 'USD' and To_Conversion == 'JPY':
            print('The Output is :', USD_JPY)
        elif From_Conversion == 'USD' and To_Conversion == 'CNY':
            print('The Output is :', USD_CNY)
        elif From_Conversion == 'EUR' and To_Conversion == 'USD':
            print('The Output is :', EUR_USD)
        elif From_Conversion == 'EUR' and To_Conversion == 'GBP':
            print('The Output is :', EUR_GBP)
        elif From_Conversion == 'EUR' and To_Conversion == 'JPY':
            print('The Output is :', EUR_JPY)
        elif From_Conversion == 'EUR' and To_Conversion == 'CNY':
            print('The Output is :', EUR_CNY)
        elif From_Conversion == 'GBP' and To_Conversion == 'USD':
            print('The Output is :', GBP_USD)
        elif From_Conversion == 'GBP' and To_Conversion == 'EUR':
            print('The Output is :', GBP_EUR)
        elif From_Conversion == 'GBP' and To_Conversion == 'JPY':
            print('The Output is :', GBP_JPY)
        elif From_Conversion == 'GBP' and To_Conversion == 'CNY':
            print('The Output is :', GBP_CNY)
        elif From_Conversion == 'JPY' and To_Conversion == 'USD':
            print('The Output is :', JPY_USD)
        elif From_Conversion == 'JPY' and To_Conversion == 'EUR':
            print('The Output is :', JPY_EUR)
        elif From_Conversion == 'JPY' and To_Conversion == 'GBP':
            print('The Output is :', JPY_GBP)
        elif From_Conversion == 'JPY' and To_Conversion == 'CNY':
            print('The Output is :', JPY_CNY)
        elif From_Conversion == 'CNY' and To_Conversion == 'USD':
            print('The Output is :', CNY_USD)
        elif From_Conversion == 'CNY' and To_Conversion == 'EUR':
            print('The Output is :', CNY_EUR)
        elif From_Conversion == 'CNY' and To_Conversion == 'GBP':
            print('The Output is :', CNY_GBP)
        elif From_Conversion == 'CNY' and To_Conversion == 'JPY':
            print('The Output is :', CNY_JPY)
        else:
            print('Invalid conversion pair')
            break


        Start_Converter = input('Continue? (YES/NO): \n').lower()
        if Start_Converter != 'yes':
                print('Unit Convertor Closed')
                break
        

            
Curr()
