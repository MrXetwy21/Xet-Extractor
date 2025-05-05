def Ext( data, first, last ): 
    try: 
        start = data.index( first ) + len( first ) 
        end = data.index( last, start ) 
        return data[start:end] 
    except ValueError: 
        return None    
