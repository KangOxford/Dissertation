def get_price_list(flow):    price_list = []    column_index = [i*2 for i in range(0,flow.shape[1]//2)]    for i in range(flow.shape[0]):        price_list.extend(flow.iloc[i,column_index].to_list())    price_set = set(price_list)    price_list = sorted(list(price_set), reverse = True)    return price_listdef get_adjusted_obs(stream, price_list):    result = [0 for _ in range(len(price_list))]    for i in range(len(price_list)):        for j in range(stream.shape[0]//2):            if price_list[i] == stream.iloc[j*2]:                result[i] = stream.iloc[j*2+1]    return result def get_max_quantity(flow):    price_list = []    column_index = [i*2 + 1 for i in range(0,flow.shape[1]//2)]    for i in range(flow.shape[0]):        price_list.extend(flow.iloc[i,column_index].to_list())    price_set = max(price_list)    return price_set