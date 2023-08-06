# -*- coding:UTF-8 -*-
r"""
author: Dennis, TongJia
version: 0.2.0
function: Handle json string
update function: add money_unit_91
bug report: js_substr function return '' when not found
next version: will change class name, put data process function out
"""
import simplejson
import time


class JsonGet:

    def __init__(self):
        self.js = {}

    def js_prov_get(self, dictName, matchField):
        for i in dictName.keys():
            if i.find(matchField) >= 0:
                return dictName[i]

    def __json_get(self, fileName):
        fp = open(fileName, encoding='utf8')
        self.js = simplejson.load(fp)
        fp.close()

    def js_get(self, fileName):
        self.__json_get(fileName)

    def js_count(self, json, reference=None, position=None, reference_json=None):
        r"""
        :param json: subtree of origin json strem
        :param reference: like condition
        :param position: like condition position
                None : %xx%
                former : xx%
                latter : %xx
                middle : yy||%xx%||yy
        :param reference_json: sub json for reference
        :return: times reference appeared in json[sub_json] by position
        """

        return self.__js_count(json, reference, position, reference_json)

    def js_dict_count(self, json, reference=None, position=None, reference_json=None):
        r"""
        dictionary count
        :param json: subtree of origin json strem
        :param reference: like condition
        :param position: like condition position
                None : %xx%
                former : xx%
                latter : %xx
                middle : yy||%xx%||yy
        :param reference_json: sub json for reference
        :return:
        """
        return self.__js_dict_count(json, reference, position, reference_json)

    def js_substr(self, json, condition, reference=None, reference_json=None, length=None, position='left',
                  end_reference=None):
        r"""
        :param json: subtree of origin json stream
        :param condition: substring condition
            None is not accepted
            former : string appeared at the start of json stream
            latter: string appeared at the start of json stream
            middle: string appeared at the middle of json stream
        :param reference: example
            reference = 'percentage like'
            json = 'percentage like 85.4%'
            condition = 'latter'
            result = '85.4%'
            in former and latter condition, if reference is not null, length will not be considered
            in middle condition, reference is necessary
        :param reference_json: sub json for reference
        :param length: length of result
            only when reference is null, length is used
            reference and length should not be null at the same time
            length is suggested when condition is middle
        :param position: only used in middle condition, default is left
            right: reference||xx
            left: xx||reference
        :param end_reference:
            reference||xxx||end_reference
        :return: string appeared in json[sub_json] by condition and reference
        """
        return self.__js_substr(json, condition, reference, reference_json, length, position, end_reference)

    def js_mapping(self, json, rule, reference_json=None):
        """
        return mapping ruled values
        :param json: json stream
        :param rule: rules:
            1.Bool -> Number :
                False = 0 & True = 1
            2.phone call times
            3.string not found
            4.for 91 json, get min amount
            5.for 91 json, get max amount
            6.for br json, get min amount
            7.for br json, get max amount
        :param reference_json: referenced json
        :return: ruled data
        """
        return self.__js_mapping(json, rule,reference_json)

    def js_store(self, json, storenum, basename, res_dict, reference_json=None, delimiter=None, position=None):
        r"""
            store list data in columns
        :param json: json stream
        :param storenum: number of the columns need stored
        :param basename: column base name
        :param res_dict: member variable of the result dictionary
        :param reference_json: referenced json
        :param delimiter: delimiter of the list member, used when position is effect
        :param position: position of the list member, start by 0, used when delimiter is effect
        :return: return self dictonary
        """
        return self.__js_store(json, storenum, basename, res_dict, reference_json, delimiter, position)

    def js_group(self, json, func=1, reference_json_list=None, delimiter=None, sumnum=None, sumfunc=None, sumfuncarg=None):
        r"""
            tmp_dict = json.js_group(json=jsmod_TOP10CTP, func=1, reference_json_list=['phone_num', 'contact_name'])
        :param json: json stream
        :param func:
            1: appeared times -- count (default)
            2: use numbers -- sum (numbers)
        :param reference_json_list: referenced json list
        :param delimiter for json member contact
        :param sumnum: when func = 2 used, reference for sum
        :param sumfunc: when sumnum is used, sumfunc is effect for function used in jsonget for sumnum
        :param sumfuncarg : arg for sumfunc, list
        :return: return a list
        """
        return self.__js_group(json, func, reference_json_list, delimiter, sumnum, sumfunc, sumfuncarg)

    def js_null(self, json, args, nullset=None):
        r"""
        null json execution
        NONBKLN1 += json.js_null(jsmod_NONBKLN1, ['m1', 'cell', 'nbank', 'p2p'], ['', '', '', 0])
        :param json: json string
        :param args: json sub set list
        :param nullset: null list
        :return: return result or nullset
        """
        return self.__js_null(json, args, nullset)

    def time_change(self, timenum):
        return self.__time_change(timenum)

    def __js_count(self, json, reference=None, position=None, reference_json=None):
        if reference is None:
            return len(json)
        else:
            _i = 0
            _len_reference = len(reference)
            if position is None:
                for _js in json:
                    try:
                        # print(_js)
                        _js = _js[reference_json]
                    except KeyError:
                        _js = _js
                        print('reference_json not match any child in json!')

                    if _js.find(reference) >= 0:
                        _i += 1

            elif position == 'former':
                for _js in json:
                    try:
                        _js = _js[reference_json]
                    except KeyError:
                        _js = _js
                        print('reference_json not match any child in json!')

                    if _js.find(reference) == 0:
                        _i += 1

            elif position == 'latter':
                for _js in json:
                    try:
                        _js = _js[reference_json]
                    except KeyError:
                        _js = _js
                        print('reference_json not match any child in json!')

                    if _js.find(reference) + _len_reference == len(_js):
                        _i += 1

            elif position == 'middle':
                for _js in json:
                    try:
                        _js = _js[reference_json]
                    except KeyError:
                        _js = _js
                        print('reference_json not match any child in json!')

                    if (_js.find(reference) < len(_js) - _len_reference) & (_js.find(reference) > 0):
                        _i += 1

            else:
                print('Argument does not match any used type!')

            return _i

    def __js_dict_count(self, json, reference=None, position=None, reference_json=None):
        if reference is None:
            return len(json)
        else:
            _i = 0
            _len_reference = len(reference)
            if position is None:
                for _js_key in json:
                    try:
                        # print(_js)
                        _js = json[_js_key][reference_json]
                    except KeyError:
                        _js = ''
                        print('reference_json not match any child in json!')

                    if _js.find(reference) >= 0:
                        _i += 1

            elif position == 'former':
                for _js_key in json:
                    try:
                        _js = json[_js_key][reference_json]
                    except KeyError:
                        _js = ''
                        print('reference_json not match any child in json!')

                    if _js.find(reference) == 0:
                        _i += 1

            elif position == 'latter':
                for _js_key in json:
                    try:
                        _js = json[_js_key][reference_json]
                    except KeyError:
                        _js = ''
                        print('reference_json not match any child in json!')

                    if _js.find(reference) + _len_reference == len(_js):
                        _i += 1

            elif position == 'middle':
                for _js_key in json:
                    try:
                        _js = json[_js_key][reference_json]
                    except KeyError:
                        _js = ''
                        print('reference_json not match any child in json!')

                    if (_js.find(reference) < len(_js) - _len_reference) & (_js.find(reference) > 0):
                        _i += 1

            else:
                print('Argument does not match any used type!')

            return _i

    def __js_substr(self, json, condition, reference=None, reference_json=None, length=None, position='left',
                    end_reference=None):

        if condition == 'former':
            if reference is None:
                if length is None:
                    print('ERROR: reference and length can not be null at the same time!')
                    return -1
                else:
                    _js = json
                    if reference_json is not None:
                        try:
                            _js = _js[reference_json]
                        except KeyError:
                            _js = _js
                            print('ERROR: reference_json not match any child in json!')
                    _result_str = _js[:length]
                    return _result_str
            else:
                _js = json
                if reference_json is not None:
                    try:
                        _js = _js[reference_json]
                    except KeyError:
                        print('ERROR: reference_json not match any child in json!')
                        return -1
                _js_find = _js.find(reference)
                if _js_find >= 0:
                    _result_str = _js[:_js_find]
                else:
                    #not found
                    _result_str = ''
                return _result_str

        elif condition == 'latter':
            if reference is None:
                if length is None:
                    print('ERROR: reference and length can not be null at the same time!')
                    return -1
                else:
                    _js = json
                    if reference_json is not None:
                        try:
                            _js = _js[reference_json]
                        except KeyError:
                            print('ERROR: reference_json not match any child in json!')
                            return -1
                    _result_str = _js[len(_js) - length:]
                    return _result_str
            else:
                _len_reference = len(reference)
                _js = json
                if reference_json is not None:
                    try:
                        _js = _js[reference_json]
                    except KeyError:
                        print('reference_json not match any child in json!')
                        return -1
                _js_find = _js.find(reference)
                if _js_find >= 0:
                    _result_str = _js[_js_find + _len_reference:]
                else:
                    # not found
                    _result_str = ''
                return _result_str

        elif condition == 'middle':
            if reference is None:
                print('ERROR: In middle condition, reference must be declared!')
                return -1

            else:
                _len_reference = len(reference)
                if length is None:
                    if end_reference is None:
                        print('WARNING: under middle condition, length is suggested to use with reference!')
                    _js = json
                    if reference_json is not None:
                        try:
                            _js = _js[reference_json]
                        except KeyError:
                            print('ERROR: reference_json not match any child in json!')
                            return -1
                    _js_find = _js.find(reference)
                    if _js_find >= 0:
                        if position == 'left':
                            if end_reference is None:
                                _result_str = _js[:_js_find]
                            else:
                                _i = 0
                                _j = 0
                                _end_len = len(end_reference)
                                while _js.find(end_reference, _i, _js_find) < _js_find - _end_len:
                                    if _js.find(end_reference, _i, _js_find) < 0:
                                        return _js[_j + _end_len:_js_find]
                                    else:
                                        _j = _js.find(end_reference, _i, _js_find)
                                        _i = _j + 1
                                # _result_str = _js[_i+_end_len:_js_find]
                        elif position == 'right':
                            if end_reference is None:
                                _result_str = _js[_js_find+_len_reference:]
                            else:
                                _i = _js.find(end_reference, _js_find)
                                if _i >= 0:
                                    _result_str = _js[_js_find+_len_reference:_i]
                                else:
                                    _result_str = _js[_js_find + _len_reference:]
                        else:
                            print('ERROR: position argument does not match any function!')
                            return -1
                    else:
                        # not found
                        _result_str = ''
                    return _result_str
                else:
                    _js = json
                    if reference_json is not None:
                        try:
                            _js = _js[reference_json]
                        except KeyError:
                            print('ERROR: reference_json not match any child in json!')
                            return -1
                    _js_find = _js.find(reference)
                    if _js_find >= 0:
                        if position == 'left':
                            _result_str = _js[_js_find-length:_js_find]
                        elif position == 'right':
                            _result_str = _js[_js_find+len(reference):_js_find+len(reference)+length]
                        else:
                            print('ERROR: position argument does not match any function!')
                            return -1
                    else:
                        # not found
                        _result_str = ''
                    return _result_str
        else:
            print('Argument does not match any used type!')
            return -1

    def __js_mapping(self, json, rule, reference_json=None):
        _js = json
        money_unit_91 = 10000

        if reference_json is None:
            _js = _js
        else:
            try:
                _js = _js[reference_json]
            except KeyError:
                print('ERROR: reference_json not match any child in json!')
                return -1

        if rule == 4:
            map_dict_min = {
                -7: 0,
                -6: 0.1,
                -5: 0.2,
                -4: 0.3,
                -3: 0.4,
                -2: 0.6,
                -1: 0.8,
                0: 'unknown',
                1: 1,
                2: 2
            }
            if int(_js) < 3:
                return map_dict_min[_js] * money_unit_91
            else:
                return 2 * (int(_js) - 1) * money_unit_91

        elif rule == 5:
            map_dict_max = {
                -7: 0.1,
                -6: 0.2,
                -5: 0.3,
                -4: 0.4,
                -3: 0.6,
                -2: 0.8,
                -1: 1,
                0: 'unknown',
                1: 2,
                2: 4
            }
            if int(_js) < 3:
                return map_dict_max[_js] * money_unit_91
            else:
                return 2 * int(_js) * money_unit_91

        elif rule == 6:
            if _js[0] == '-':
                return 0
            else:
                ten = int(_js, 16)
                ten1 = ten // 10
                ten2 = 1000 * pow(10, ten1)
                res = ten2 * (ten % 10 + ten1)
                return res

        elif rule == 7:
            if _js[0] == '-':
                return 0
            else:
                ten = int(_js, 16)
                ten1 = ten // 10
                ten2 = 1000 * pow(10, ten1)
                res = ten2 * (ten % 10 + ten1 + 1)
                return res

        else:
            print('ERROR: value not within rule!')
            return -1

    def __js_store(self, json, storenum, basename, res_dict, reference_json=None, delimiter=None, position=None):
        _js = json
        if reference_json is None:
            _js = _js
        else:
            try:
                _js = _js[reference_json]
            except KeyError:
                print('ERROR: reference_json not match any child in json!')
                return -1

        createVar = locals()
        listTemp = range(1, storenum+1)
        for i in listTemp:
            try:
                if (delimiter is None) or (position is None):
                    createVar[basename + str(i)] = _js[i-1]
                else:
                    createVar[basename + str(i)] = _js[i-1].split(delimiter)[position]
            except IndexError:
                createVar[basename + str(i)] = ''

            res_dict[basename + str(i)] = createVar[basename + str(i)]

        return res_dict

    def __js_group(self, json, func, reference_json_list=None, delimiter=None, sumnum=None, sumfunc=None, sumfuncarg=None):
        group_dict = {}

        if func == 1:
            tmplist = []
            for _js1 in json:
                _js = ''
                if reference_json_list is None:
                    _js = _js1
                else:
                    try:
                        for reference_json in reference_json_list:
                            if delimiter is None:
                                _js += str(_js1[reference_json])
                            else:
                                _js += str(_js1[reference_json]) + delimiter
                    except KeyError:
                        print('ERROR: reference_json not match any child in json!')
                        return -1

                if _js in tmplist:
                    group_dict[_js] += 1
                else:
                    tmplist.append(_js)
                    group_dict[_js] = 1
        elif func == 2:
            if sumnum is None:
                print('ERROR: when function is 2, sumnum is necessary!')
                return -1
            else:
                tmplist = []
                for _js1 in json:
                    _js = ''
                    if reference_json_list is None:
                        _js = _js1
                    else:
                        try:
                            for reference_json in reference_json_list:
                                if delimiter is None:
                                    _js += str(_js1[reference_json])
                                else:
                                    _js += str(_js1[reference_json]) + delimiter

                        except KeyError:
                            print('ERROR: reference_json not match any child in json!')
                            return -1
                    if _js in tmplist:
                        try:
                            if sumfunc is None:
                                group_dict[_js] += float(_js1[sumnum])
                            elif sumfunc == 'js_mapping':
                                try:
                                    args1 = sumfuncarg[0]
                                except IndexError:
                                    print('ERROR: important arguments missing!')
                                    return -1

                                try:
                                    args2 = sumfuncarg[1]
                                except IndexError:
                                    args2 = None

                                resfunc = self.__js_mapping(json=_js1[sumnum], rule=args1, reference_json=args2)
                                group_dict[_js] += float(resfunc)
                        except KeyError:
                            print('ERROR: sumnum not match any child in json!')
                            return -1
                    else:
                        tmplist.append(_js)
                        try:
                            if sumfunc is None:
                                group_dict[_js] = float(_js1[sumnum])
                            elif sumfunc == 'js_mapping':
                                try:
                                    args1 = sumfuncarg[0]
                                except IndexError:
                                    print('ERROR: important arguments missing!')
                                    return -1

                                try:
                                    args2 = sumfuncarg[1]
                                except IndexError:
                                    args2 = None

                                resfunc = self.__js_mapping(json=_js1[sumnum], rule=args1, reference_json=args2)
                                group_dict[_js] = float(resfunc)

                        except KeyError:
                            print('ERROR: sumnum not match any child in json!')
                            return -1

        return group_dict

    def __js_null(self, json, args, nullset=None):
        res = ''
        for i in range(0, len(args)):
            try:
                res = json[args[i]]
                json = res
            except KeyError or IndexError:
                try:
                    res = nullset[i]
                except IndexError or KeyError:
                    res = ''
                finally:
                    return res
        typ = nullset[len(nullset)-1]
        if isinstance(typ, int):
            return int(res)
        elif isinstance(typ, str):
            return str(res)
        else:
            print('WARNING: WE DONT KNOW WHAT U ARE TALKING ABOUT!', type(typ))
            return res

    def __time_change(self, timenum):
        x = time.localtime(int(timenum) / 1000)
        x = time.strftime('%Y%m%d', x)
        return x

