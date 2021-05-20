# -*- coding: utf-8 -*-
# AIzaSyCRatbfviWkPCfTqaF787rPjhB9-MQSPLE
#AIzaSyB8Y_aM9nj7OBj6n7uZMQNM4pQWAGPWD50
"""
Created on Sat May  8 01:14:44 2021

@author: אביב
"""
#//maps.googleapis.com/maps/api/distancematrix/json?origins=Boston,MA|Charlestown,MA&destinations=Lexington,MA|Concord,MA&departure_time=now&key=YOUR_API_KEY
#https://maps.googleapis.com/maps/api/geocode/json?address=Winnetka&key=YOUR_API_KEY
import json
import requests
import pprint

file= open("dests.txt", 'r', encoding='utf8')
hendler=file.readlines()

def get_dests(hendler):
    lst=list()
    for line in hendler:
        line=line.strip('\n')
        lst.append(line)
    return (lst)

#print(get_dests(hendler))

def get_dist(lst):
    dist_lst=list()
    origin='תל אביב'
    key='AIzaSyB8Y_aM9nj7OBj6n7uZMQNM4pQWAGPWD50'
    for dest in lst:
        url="https://maps.googleapis.com/maps/api/distancematrix/json?origins=%s&destinations=%s&key=%s" % (origin,dest,key)
        info=requests.get(url).json()
        dist=info['rows'][0]['elements'][0]['distance']['text']
        #print(dist)
        dist_lst.append(dist)
    return (dist_lst)
        
#print(get_dist(get_dests(hendler)))

def get_duration(lst):
    duration_lst=list()
    origin='תל אביב'
    key='AIzaSyB8Y_aM9nj7OBj6n7uZMQNM4pQWAGPWD50'
    for dest in lst:
        url="https://maps.googleapis.com/maps/api/distancematrix/json?origins=%s&destinations=%s&key=%s" % (origin,dest,key)
        info=requests.get(url).json()
        duration=info['rows'][0]['elements'][0]['duration']['text']
        #print(duration)
        duration_lst.append(duration)
    return (duration_lst)
        
#print(get_duration(get_dests(hendler)))

def get_GeoCode(lst):
    GeoCode_lst=list()
    key='AIzaSyB8Y_aM9nj7OBj6n7uZMQNM4pQWAGPWD50'
    for dest in lst:
      url="https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s" % (dest,key)
      info=requests.get(url).json()
      geocode=info["results"][0]["geometry"]["location"]
      #print(geocode)
      GeoCode_lst.append(geocode)
    return (GeoCode_lst)
    
#print(get_GeoCode(get_dests(hendler)))    
    
def set_dict(lst):
    dct=dict()
    counter=0
    for dest in lst:
        dct[dest]={ 'distance': get_dist(get_dests(hendler))[counter],'duration': get_duration(get_dests(hendler))[counter],'latitude':get_GeoCode(get_dests(hendler))[counter]['lat'] ,'longitude':get_GeoCode(get_dests(hendler))[counter]['lng']}
        counter=counter+1
        #print(dct[dest],'\n')
    return(pprint.pprint(dct))

set_dict(get_dests(hendler))   

def get_biggest_distance(lst):
    dct=dict()
    counter=0
    keys_lst=list()
    values_lst=list()
    for dest in lst:
        dct[dest]=(get_dist(get_dests(hendler)))[counter]
        counter=counter+1
        
    sorted_values = sorted(dct.values(),reverse=True) # Sort the values
    sorted_dct=dict()
    for dist in sorted_values:
        for dest in dct.keys():
            if dct[dest] == dist:
                sorted_dct[dest] = dct[dest]
                break
            
    keys_lst=sorted_dct.keys()
    new_keys_lst = list()
    for key in keys_lst:
        new_keys_lst.append(key)
    
    values_lst=sorted_dct.values()
    new_values_lst = list()
    for value in values_lst:
        new_values_lst.append(value)
    
    big_dct=dict()    
    for i in range(3):
      big_dct[new_keys_lst[i]]=new_values_lst[i]  
    
    return(big_dct)

print('\n The three cities furthest from Tel Aviv', get_biggest_distance(get_dests(hendler)))     