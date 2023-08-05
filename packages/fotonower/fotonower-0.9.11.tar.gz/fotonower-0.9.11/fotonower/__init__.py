# -*- coding: utf-8 -*-
import requests
import json
import sys

# le token doit venir de mongodb ainsi qu'eventuellement l'host

class FotonowerConnect:
    def __init__(self, token, host = "www.fotonower.com", protocol = "https"):
        self.protocol = protocol
        self.host = host
        self.api_version = "/api/v1"
        self.upload_endpoint = "/secured/photo/upload"

        self.face_bucket = "/secured/velours/faceBucket"
        self.features = "/secured/velours/features"
        self.set_current = "/secured/datou/current/set"
        self.portfolioAppend = "/secured/portfolio/save"
        self.portfolioSavePost = "/portfolio/savePost"
        self.getNewPortfolio = "/secured/portfolio/new"
        self.pids_to_add = "list_pids_to_add"
        self.only_add_arg = "only_add=1"
        self.port_id_arg = "portfolio_id"
        self.token_arg = "token"
        self.token = str(token)
        self.lf_arg = "list_photo_ids"
        self.bibn_arg = "bibnumber"
        self.nb_bucket_arg = "nb_bucket"
        self.photo_hashtag_type_arg = "photo_hashtag_type"
        self.photo_desc_type_arg = "photo_desc_type"


    def get_new_portfolio(self, portfolio_name = "", verbose = False):

        url = self.protocol + "://" + self.host + self.api_version + self.getNewPortfolio

        args_get = {}
        if portfolio_name != "":
            args_get["name"] = portfolio_name

        args_get["access_token"] = self.token

        if args_get != {} :
            url += "?" + "&".join(map(lambda x : str(x) + "=" + str(args_get[x]),args_get))

        r = requests.get(url)

        if r.status_code == 200 :
            res_json = json.loads(r.content.decode("utf8"))
            if verbose :
                print (res_json)
            if type(res_json) == type(0) :
                portfolio_id = res_json
            elif type(res_json) == type({}) :
                if 'portfolio_id' in res_json :
                    portfolio_id = res_json['portfolio_id']
        else :
            print (" Status : " + str(r.status_code))
            print (" Content : " + str(r.content))
            print (" All Response : " + str(r))

        return portfolio_id

    def create_portfolio(self, portfolio_name, list_photo_ids = [], verbose = False, arg_aux = {}):

        url = self.protocol +"://" + self.host + self.api_version + self.portfolioSavePost

        list_photo_ids_csv = ",".join(map(str, list_photo_ids))

        data_to_send = {'portfolio_name':portfolio_name, "access_token" : self.token, "list_photos_ids" : list_photo_ids_csv}

        data_to_send.update(arg_aux)

        r = requests.post(url, data=data_to_send)

        portfolio_id = 0

        if r.status_code == 200 :
            res_json = json.loads(r.content)
            if verbose :
                print (res_json)
            portfolio_id = res_json['portfolio_id']
            #print portfolio_id
        else :
            print (" Status : " + str(r.status_code))
            print (" Content : " + str(r.content))
            print (" All Response : " + str(r))

        return portfolio_id


    def create_portfolio_by_batch(self, portfolio_name, list_photo_ids = [], verbose = False, batch_size=500,arg_aux = {}):
        url = self.protocol +"://" + self.host + self.api_version + self.portfolioSavePost


        list_photo_ids_csv = ",".join(map(str, list_photo_ids))

        data_to_send = {'portfolio_name': portfolio_name, "access_token": self.token,
                        "list_photos_ids": list_photo_ids_csv[:batch_size]}

        data_to_send.update(arg_aux)

        r = requests.post(url, data=data_to_send)
        portfolio_id = 0

        if r.status_code == 200:
            res_json = json.loads(r.content)
            if verbose:
                print (res_json)
            portfolio_id = res_json['portfolio_id']
            # print portfolio_id
        else:
            print (" Status : " + str(r.status_code))
            print (" Content : " + str(r.content))
            print (" All Response : " + str(r))

        count=0
        data_to_send={}
        list_photo_to_send=[]
        for el in list_photo_ids_csv[batch_size:]:

            if count==batch_size:
                data_to_send={'portfolio_id':portfolio_id, "acces_token":self.token, "list_photo_ids":list_photo_to_send}
                data_to_send.update(arg_aux)

                r=requests.post(url, data=data_to_send)
                count=0
                list_photo_to_send=[]
                if r.status_code==200:
                    res_json=json.loads(r.content)
                    if verbose:
                        print(res_json)
                else:
                    print (" Status : " + str(r.status_code))
                    print (" Content : " + str(r.content))
                    print (" All Response : " + str(r))
            else:
                list_photo_to_send.append(el)
                count += 1
        if count>0:
            data_to_send={'portfolio_id':portfolio_id, "access_token":self.token, "list_photo_ids":list_photo_to_send}
            data_to_send.update(arg_aux)

            r=requests.post(url,data=data_to_send)
            if r.status_code==200:
                res_json.loads(r.content)
                if verbose:
                    print(res_json)
            else:
                print (" Status : " + str(r.status_code))
                print (" Content : " + str(r.content))
                print (" All Response : " + str(r))

        return portfolio_id

    def append_to_port(self,list_pids_csv,port_id,verbose = False):
        if list_pids_csv == "":
            print("please provide a list of pids to append")
            return 0
        if int(port_id) == 0:
            print("please provide a valid portfolio_id")
            return 0

        url = self.protocol+"://" + self.host + self.api_version + self.portfolioAppend + "?" + self.only_add_arg + "&"
        url += self.port_id_arg + "=" + str(port_id) + "&" + self.lf_arg + "=" + list_pids_csv + "&" + self.token_arg + "=" + self.token
        r = requests.get(url)
        if r.status_code == 200 :
            res_json = json.loads(r.content.decode("utf8"))
            if verbose :
                print (res_json)
            if type(res_json) == type(0) :
                portfolio_id = res_json
            elif type(res_json) == type({}) :
                if 'portfolio_id' in res_json :
                    portfolio_id = res_json['portfolio_id']
        else :
            print (" Status : " + str(r.status_code))
            print (" Content : " + str(r.content))
            print (" All Response : " + str(r))

        return portfolio_id

    def upload_medias(self, list_filenames, portfolio_id = 0, upload_small = False, hashtags = [], verbose = False, arg_aux = {}, compute_classification=False) :
      try :
        if verbose:
            print("in upload media")
            sys.stdout.flush()
        url = self.protocol+ "://" + self.host + self.api_version + self.upload_endpoint + "?" + self.token_arg + "=" + self.token

        if verbose :
            print (" Upload medias :  " + str(list_filenames) + " : url : " + url)
            sys.stdout.flush()

        files = {}
        map_file_id_filename= {}
        for i in range(len(list_filenames)) :
            if verbose :
                print(list_filenames[i])
                sys.stdout.flush()
            key = "file" + str(i)
            map_file_id_filename[key] = list_filenames[i]
            try:
                files[key] = open(list_filenames[i], 'rb')
            except Exception as e:
                print(e)
                print(list_filenames[i])
                print("error while trying to upload this file need to reupload it manually in portfolio " + str(portfolio_id))

        # we could pass others arguments if needed
        data_to_send = {'portfolio_id':portfolio_id, "upload_small" : upload_small, "compute_classification" : compute_classification, "hashtags":";".join(hashtags)}
        data_to_send.update(arg_aux)
        if verbose:
            print("after data_to_send, before sending request")
        r = requests.post(url, files=files, data=data_to_send)
        if verbose:
            print("after request")
        sys.stdout.flush()
        if verbose :
            print (r)
            #print (r.response)
            print (r.content)

        if r.status_code == 200 :
            print ("Result OK !")
            sys.stdout.flush()
            res_json = json.loads(r.content.decode("utf8"))

            if "map_files_photo_id" in res_json:
                map_filename_photo_id = {}
                map_files_photo_id = res_json["map_files_photo_id"]
                for f in map_files_photo_id :
                    photo_id = map_files_photo_id[f]
                    if f in map_file_id_filename :
                        filename = map_file_id_filename[f]
                        map_filename_photo_id[filename] = photo_id
                    else :
                        print("Missing filename !")
                dict_cur = {"list_datou_current": ""}
                if "list_datou_current" in res_json:
                    dict_cur["list_datou_current"] = res_json["list_datou_current"]
                return map_filename_photo_id,dict_cur

            if 'photo_id' in res_json :
                if len(list_filenames) > 1 :
                    print ("Some filename were not uploaded !")
                return {list_filenames[0]:res_json['photo_id']}
        else :
            print(str(r.status_code))

        for line in r.content.split("\n") :
            if "This exception" in line:
                print (line)

        return 0
      except Exception as e:
          sys.stdout.flush()
          print("ERROR IN API l 184 " + str(e))
          return 0

    def faceBucket(self, list_of_face_as_photo_id, bibnumber = 0, nb_bucket = 6, photo_hashtag_type = 67, photo_desc_type = 0, verbose = False) :
      try :
        if len(list_of_face_as_photo_id) <= 3:
            if verbose :
                sys.stdout.write("3")
                #print "Less than three is useless !"
            return {}
        if len(list_of_face_as_photo_id) >= 100 :
            if verbose :
                print ("  list_of_face_as_photo_id : " + str(len(list_of_face_as_photo_id)))
            return {}

        list = ",".join(map(str, list_of_face_as_photo_id))
        url = self.protocol+ "://" + self.host + self.api_version + self.face_bucket + "?" + self.token_arg + "=" + self.token + "&" + self.lf_arg + "=" + list
        url += "&" + self.nb_bucket_arg + "=" + nb_bucket
        url += "&" + self.photo_hashtag_type_arg + "=" + str(photo_hashtag_type)
        url += "&" + self.photo_desc_type_arg + "=" + str(photo_desc_type)

        if bibnumber != 0 :
            url += "&" + self.bibn_arg + "=" + str(bibnumber)

        if verbose :
            print (" faceBucket : url : " + url)

        r = requests.post(url)

        if r.status_code == 200 :
            print ("Result OK !")
            res_json = json.loads(r.content)

            res_to_send = {}
            for k in res_json :
                res_to_send[int(k)] = res_json[k]

            return res_to_send

        return {}
      except Exception as e :
          print (str(e))
          return {}



    def veloursFeature(self, list_photo_ids, photo_desc_type = 0, verbose = False) :
        list = ",".join(map(str, list_photo_ids))
        url = self.protocol+ "://" + self.host + self.api_version + self.features + "?" + self.token_arg + "=" + self.token + "&" + self.lf_arg + "=" + list
        url += "&" + self.photo_desc_type_arg + "=" + str(photo_desc_type)

        if verbose :
            print (" faceBucket : url : " + url)

        r = requests.get(url)

        if r.status_code == 200 :
            print ("Result OK !")
            res_json = json.loads(r.content)

            return res_json

        return {}

    def set_datou_current(self,mtr_portfolio_id = 0,list_photo_csv = "",mtd_id= 0,mtr_user_id = 0,input_csv = "",verbose = False):
        url = self.protocol + "://" + self.host + self.api_version + self.set_current + "?"
        list_param = ["token="+self.token]
        if mtr_portfolio_id != 0:
            list_param.append("mtr_portfolio_id=" + str(mtr_portfolio_id))
        elif list_photo_csv != "":
            list_param.append("mtr_photo_id=" + list_photo_csv)
        if mtd_id != 0:
            list_param.append("mtr_datou_id="+str(mtd_id))
        if mtr_user_id != 0:
            list_param.append("user="+str(mtr_user_id))
        if input_csv != "":
            list_param.append("input_csv="+input_csv)
        url += "&".join(list_param)
        r = requests.get(url)
        if r.status_code == 200:
            if verbose:
                print("Result OK")
            return json.loads(r.content)
        return {}