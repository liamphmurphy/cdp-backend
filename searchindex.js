Search.setIndex({docnames:["cdp_backend","cdp_backend.bin","cdp_backend.database","cdp_backend.infrastructure","cdp_backend.utils","cdp_backend.utils.resources","contributing","database_schema","index","installation","modules"],envversion:{"sphinx.domains.c":1,"sphinx.domains.changeset":1,"sphinx.domains.citation":1,"sphinx.domains.cpp":1,"sphinx.domains.index":1,"sphinx.domains.javascript":1,"sphinx.domains.math":2,"sphinx.domains.python":1,"sphinx.domains.rst":1,"sphinx.domains.std":1,"sphinx.ext.viewcode":1,sphinx:56},filenames:["cdp_backend.rst","cdp_backend.bin.rst","cdp_backend.database.rst","cdp_backend.infrastructure.rst","cdp_backend.utils.rst","cdp_backend.utils.resources.rst","contributing.rst","database_schema.rst","index.rst","installation.rst","modules.rst"],objects:{"":{cdp_backend:[0,0,0,"-"]},"cdp_backend.bin":{create_cdp_database_uml:[1,0,0,"-"]},"cdp_backend.bin.create_cdp_database_uml":{Args:[1,1,1,""],main:[1,2,1,""]},"cdp_backend.database":{exceptions:[2,0,0,"-"],models:[2,0,0,"-"],types:[2,0,0,"-"],validators:[2,0,0,"-"]},"cdp_backend.database.exceptions":{UniquenessError:[2,3,1,""]},"cdp_backend.database.exceptions.UniquenessError":{conflicting_ids:[2,4,1,""],pk_values:[2,4,1,""]},"cdp_backend.database.models":{Body:[2,1,1,""],Event:[2,1,1,""],EventMinutesItem:[2,1,1,""],EventMinutesItemFile:[2,1,1,""],File:[2,1,1,""],Matter:[2,1,1,""],MatterFile:[2,1,1,""],MatterSponsor:[2,1,1,""],MatterStatus:[2,1,1,""],MinutesItem:[2,1,1,""],Person:[2,1,1,""],Role:[2,1,1,""],Seat:[2,1,1,""],Session:[2,1,1,""],Transcript:[2,1,1,""],Vote:[2,1,1,""]},"cdp_backend.database.models.Body":{Example:[2,4,1,""],Meta:[2,5,1,""],collection:[2,5,1,""],collection_name:[2,5,1,""],description:[2,5,1,""],end_datetime:[2,5,1,""],external_source_id:[2,5,1,""],is_active:[2,5,1,""],name:[2,5,1,""],start_datetime:[2,5,1,""],tag:[2,5,1,""]},"cdp_backend.database.models.Event":{Example:[2,4,1,""],Meta:[2,5,1,""],agenda_uri:[2,5,1,""],body_ref:[2,5,1,""],collection:[2,5,1,""],collection_name:[2,5,1,""],event_datetime:[2,5,1,""],external_source_id:[2,5,1,""],hover_thumbnail_ref:[2,5,1,""],minutes_uri:[2,5,1,""],static_thumbnail_ref:[2,5,1,""]},"cdp_backend.database.models.EventMinutesItem":{Example:[2,4,1,""],Meta:[2,5,1,""],collection:[2,5,1,""],collection_name:[2,5,1,""],decision:[2,5,1,""],event_ref:[2,5,1,""],external_source_id:[2,5,1,""],index:[2,5,1,""],minutes_item_ref:[2,5,1,""]},"cdp_backend.database.models.EventMinutesItemFile":{Example:[2,4,1,""],Meta:[2,5,1,""],collection:[2,5,1,""],collection_name:[2,5,1,""],event_minutes_item_ref:[2,5,1,""],external_source_id:[2,5,1,""],name:[2,5,1,""],uri:[2,5,1,""]},"cdp_backend.database.models.File":{Example:[2,4,1,""],Meta:[2,5,1,""],collection:[2,5,1,""],collection_name:[2,5,1,""],description:[2,5,1,""],media_type:[2,5,1,""],name:[2,5,1,""],uri:[2,5,1,""]},"cdp_backend.database.models.Matter":{Example:[2,4,1,""],Meta:[2,5,1,""],collection:[2,5,1,""],collection_name:[2,5,1,""],external_source_id:[2,5,1,""],matter_type:[2,5,1,""],name:[2,5,1,""],title:[2,5,1,""]},"cdp_backend.database.models.MatterFile":{Example:[2,4,1,""],Meta:[2,5,1,""],collection:[2,5,1,""],collection_name:[2,5,1,""],external_source_id:[2,5,1,""],matter_ref:[2,5,1,""],name:[2,5,1,""],uri:[2,5,1,""]},"cdp_backend.database.models.MatterSponsor":{Example:[2,4,1,""],Meta:[2,5,1,""],collection:[2,5,1,""],collection_name:[2,5,1,""],external_source_id:[2,5,1,""],matter_ref:[2,5,1,""],person_ref:[2,5,1,""]},"cdp_backend.database.models.MatterStatus":{Example:[2,4,1,""],Meta:[2,5,1,""],collection:[2,5,1,""],collection_name:[2,5,1,""],external_source_id:[2,5,1,""],matter_ref:[2,5,1,""],status:[2,5,1,""],update_datetime:[2,5,1,""]},"cdp_backend.database.models.MinutesItem":{Example:[2,4,1,""],Meta:[2,5,1,""],collection:[2,5,1,""],collection_name:[2,5,1,""],description:[2,5,1,""],external_source_id:[2,5,1,""],matter_ref:[2,5,1,""],name:[2,5,1,""]},"cdp_backend.database.models.Person":{Example:[2,4,1,""],Meta:[2,5,1,""],collection:[2,5,1,""],collection_name:[2,5,1,""],email:[2,5,1,""],external_source_id:[2,5,1,""],is_active:[2,5,1,""],name:[2,5,1,""],phone:[2,5,1,""],picture_ref:[2,5,1,""],router_string:[2,5,1,""],website:[2,5,1,""]},"cdp_backend.database.models.Role":{Example:[2,4,1,""],Meta:[2,5,1,""],body_ref:[2,5,1,""],collection:[2,5,1,""],collection_name:[2,5,1,""],end_datetime:[2,5,1,""],external_source_id:[2,5,1,""],person_ref:[2,5,1,""],seat_ref:[2,5,1,""],start_datetime:[2,5,1,""],title:[2,5,1,""]},"cdp_backend.database.models.Seat":{Example:[2,4,1,""],Meta:[2,5,1,""],collection:[2,5,1,""],collection_name:[2,5,1,""],electoral_area:[2,5,1,""],electoral_type:[2,5,1,""],external_source_id:[2,5,1,""],image_ref:[2,5,1,""],name:[2,5,1,""]},"cdp_backend.database.models.Session":{Example:[2,4,1,""],Meta:[2,5,1,""],caption_uri:[2,5,1,""],collection:[2,5,1,""],collection_name:[2,5,1,""],event_ref:[2,5,1,""],external_source_id:[2,5,1,""],session_datetime:[2,5,1,""],session_index:[2,5,1,""],video_uri:[2,5,1,""]},"cdp_backend.database.models.Transcript":{Example:[2,4,1,""],Meta:[2,5,1,""],collection:[2,5,1,""],collection_name:[2,5,1,""],confidence:[2,5,1,""],created:[2,5,1,""],file_ref:[2,5,1,""],session_ref:[2,5,1,""]},"cdp_backend.database.models.Vote":{Example:[2,4,1,""],Meta:[2,5,1,""],collection:[2,5,1,""],collection_name:[2,5,1,""],decision:[2,5,1,""],event_minutes_item_ref:[2,5,1,""],event_ref:[2,5,1,""],external_source_id:[2,5,1,""],in_majority:[2,5,1,""],matter_ref:[2,5,1,""],person_ref:[2,5,1,""]},"cdp_backend.database.types":{IndexedField:[2,1,1,""],IndexedFieldSet:[2,1,1,""],Order:[2,1,1,""]},"cdp_backend.database.types.IndexedField":{name:[2,5,1,""],order:[2,5,1,""]},"cdp_backend.database.types.IndexedFieldSet":{fields:[2,5,1,""]},"cdp_backend.database.types.Order":{ASCENDING:[2,5,1,""],DESCENDING:[2,5,1,""]},"cdp_backend.database.validators":{email_is_valid:[2,2,1,""],model_is_unique:[2,2,1,""],resource_exists:[2,2,1,""],router_string_is_valid:[2,2,1,""]},"cdp_backend.infrastructure":{cdp_stack:[3,0,0,"-"]},"cdp_backend.infrastructure.cdp_stack":{CDPStack:[3,1,1,""]},"cdp_backend.utils":{file_utils:[4,0,0,"-"],resources:[5,0,0,"-"]},"cdp_backend.utils.file_utils":{get_media_type:[4,2,1,""]},cdp_backend:{bin:[1,0,0,"-"],database:[2,0,0,"-"],get_module_version:[0,2,1,""],infrastructure:[3,0,0,"-"],utils:[4,0,0,"-"]}},objnames:{"0":["py","module","Python module"],"1":["py","class","Python class"],"2":["py","function","Python function"],"3":["py","exception","Python exception"],"4":["py","method","Python method"],"5":["py","attribute","Python attribute"]},objtypes:{"0":"py:module","1":"py:class","2":"py:function","3":"py:exception","4":"py:method","5":"py:attribute"},terms:{"class":[1,2,3],"default":[3,8],"import":[2,8],"new":[2,6,8],"public":9,"return":[2,4],"short":6,"while":7,For:[2,7,8],The:[2,3,4,9],Then:6,Useful:2,access:8,account:8,action:[6,8],activist:8,add:6,admin:8,afternoon:2,agenda_uri:2,alia:2,all:[3,6,8],alphabet:2,also:[2,6],alwai:[6,9],anaconda:6,ani:[2,3,6,8],api:7,app:8,appreci:6,arg:[1,2],argpars:1,ascend:2,attende:2,auto:8,avail:8,backend:[0,3,6,9],base:[1,2,3],befor:8,between:2,bill:2,bin:[0,10],bit:6,bodi:2,body_ref:2,bool:2,branch:6,bucket:3,budget:2,bugfix:6,build:6,bump2vers:6,call:[3,7],can:[2,3,6,9],caption_uri:2,cdp:[0,2,3,6,9],cdp_backend:[8,9],cdp_stack:[0,10],cdpstack:3,chair:2,chang:[6,8],charact:2,check:6,checkout:6,citi:2,citywid:2,classmethod:2,clone:[6,9],cloud:[3,7],code:8,collect:2,collection_nam:2,com:[3,6,8,9],combin:8,command:9,commit:6,committe:2,commun:8,compar:2,compil:8,compon:8,componentresourc:3,confer:2,confid:2,conflicting_id:2,conflicting_result:2,connect:2,contain:[2,8],content:10,cookiecutt:8,copi:9,could:[2,4],council:[2,8],councildataproject:[8,9],creat:[2,3,6,8],create_cdp_database_uml:[0,10],creation:3,credit:6,curl:9,data:[2,8],databas:[0,3,8,10],date:6,debat:2,decis:2,dedic:8,denot:7,deploy:8,descend:2,descript:[2,6],detail:[6,7],dev:[6,8],dev_releas:6,diagram:7,differ:8,district:2,doc:[3,7],document:[2,7],domain:8,don:9,done:6,dot:8,download:9,dure:[2,3,6],each:[7,8],edit:6,either:9,elect:2,electoral_area:2,electoral_typ:2,email:2,email_is_valid:2,empow:8,enabl:3,end_datetim:2,ensur:8,entir:[3,8],environ:6,etc:[2,3],event:2,event_datetim:2,event_minutes_item:2,event_minutes_item_fil:2,event_minutes_item_ref:2,event_ref:2,eventminutesitem:2,eventminutesitemfil:2,everi:6,everyon:8,exampl:[2,8],except:[0,10],exist:2,external_source_id:2,extra:3,featur:6,field:[2,7],file:[2,3,6],file_ref:2,file_util:[0,10],financ:2,firebas:3,fireo:2,firestor:[3,7],firestore_loc:3,five:3,fork:6,found:[4,6],four:2,free:8,from:2,full:[2,8],gather:8,gcp:3,gcp_project:3,gcp_project_id:3,gener:8,get:4,get_media_typ:4,get_module_vers:0,git:[6,8,9],github:[6,8,9],given:[2,6],goe:6,googl:3,govern:8,graphviz:[6,8],greatli:6,guid:9,handl:6,has:[2,3,8],have:[2,8,9],head:8,help:6,here:[6,8],histor:2,hold:8,host:[3,8],hover_thumbnail_ref:2,how:[3,6],html:6,http:[3,8,9],hyphen:2,iana:4,image_ref:2,in_major:2,includ:[2,6],index:[2,8],indexedfield:2,indexedfieldset:2,inform:8,infrastructur:[0,2,10],initi:[2,3],instanc:[2,3,8],is_act:2,issu:8,item:2,job:2,journalist:8,kei:2,kwarg:2,land:8,larg:8,legisl:2,level:0,librari:6,licens:8,like:8,limit:3,lint:6,list:[2,3],littl:6,local:[6,8],locat:3,log:8,lowercas:2,m2r:6,made:8,main:[1,9],maintain:[6,8],major:6,make:6,manag:2,mani:3,match:4,matter:2,matter_fil:2,matter_ref:2,matter_sponsor:2,matter_statu:2,matter_typ:2,matterfil:2,mattersponsor:2,matterstatu:2,max:3,mayor:2,media:4,media_typ:2,meet:[2,8],member:[2,8],meta:2,method:9,minor:6,minut:2,minutes_item:2,minutes_item_ref:2,minutes_uri:2,minutesitem:2,mit:8,mode:6,model:[0,7,8,10],model_is_uniqu:2,modul:[8,10],more:7,morn:2,most:[6,9],mtype:4,multipl:2,municip:8,name:[2,3],namespac:1,need:8,none:[1,2,3,4],normal:2,nosql:7,note:3,now:6,number:2,object:2,off:2,offic:2,onc:9,one:4,onli:2,open:8,opt:3,option:[2,3,4],order:2,origin:6,other:[2,3,6,8],our:[6,7,8],packag:[6,8,10],page:8,parallel:3,paramet:[2,3,4],particip:8,pass:[2,6],patch:6,per:2,period:2,person:2,person_ref:2,phone:2,picture_ref:2,pip:[6,8,9],pipelin:8,pk_valu:2,pleas:[6,8],point:[2,6],posit:2,possibl:6,prefer:9,prefix:3,present:2,press:2,primari:2,primarili:2,process:[8,9],project:[6,8],properti:2,provid:[2,4,8],publish:6,pull:6,pulumi:3,push:6,pypi:6,python:[6,8,9],rais:2,raw:6,read:6,readi:6,recent:9,recommend:[3,6],refer:2,referenc:2,relat:[2,8],releas:[6,8],remind:6,remot:2,repo:[6,8,9],repositori:[8,9],request:6,requir:[3,7],research:8,resolut:2,resolv:6,resourc:[0,2,3,4,8],resource_exist:2,resourceopt:3,role:2,router:2,router_str:2,router_string_is_valid:2,run:[3,6,8,9],same:2,save:2,schedul:2,script:1,search:8,seat:2,seat_ref:2,seattl:3,see:[6,7,8],serv:8,server:[3,8],servic:3,session:2,session_datetim:2,session_index:2,session_ref:2,set:[3,6],setup:9,should:[2,8],sign:2,simpli:8,simplifi:8,singl:8,softwar:8,someth:6,sourc:[0,1,2,3,4,8],special:2,specif:2,spend:2,sponsor:2,stabl:[6,8],stack:3,stai:8,start_datetim:2,static_thumbnail_ref:2,statu:2,status:2,still:7,storag:[3,8],store:[2,7,8],str:[0,2,3,4],string:2,subcommitte:2,submit:[2,6],submodul:[0,10],subpackag:10,support:[2,8],sure:6,tag:[2,6],tarbal:9,technic:2,templat:8,term:2,termin:9,test:[6,8],text:8,thei:[6,8],them:8,thi:[2,3,6,8,9],through:[6,9],tied:2,tiff:6,time:2,timelin:2,titl:2,togeth:2,tool:8,top:0,track:2,transcript:2,transport:2,tupl:2,two:2,tying:2,type:[0,4,10],typescript:8,uml:7,under:8,uniqu:2,uniquenesserror:2,upcom:2,updat:8,update_datetim:2,upload:2,upstream:6,uri:[2,4],use:[3,8],used:8,useful:7,using:3,usual:2,util:[0,7,8,10],valid:[0,10],version:6,video_uri:2,view:7,virtualenv:6,visit:8,vote:2,want:8,web:8,websit:[2,6],welcom:6,west2:3,when:[2,3,6],where:8,which:8,work:[2,6,8],would:[3,8],write:8,written:8,wrong:6,you:[3,6,8,9],your:[6,9],your_development_typ:6,your_name_her:6},titles:["cdp_backend package","cdp_backend.bin package","cdp_backend.database package","cdp_backend.infrastructure package","cdp_backend.utils package","cdp_backend.utils.resources package","Contributing","CDP Database Schema","Welcome to cdp-backend\u2019s documentation!","Installation","cdp_backend"],titleterms:{about:8,backend:8,bin:1,cdp:[7,8],cdp_backend:[0,1,2,3,4,5,10],cdp_stack:3,content:[0,1,2,3,4,5],contribut:[6,8],create_cdp_database_uml:1,databas:[2,7],deploi:6,develop:[6,8],document:8,except:2,file_util:4,from:9,get:6,implement:7,indic:8,infrastructur:[3,8],instal:[6,8,9],model:2,modul:[0,1,2,3,4,5],note:7,packag:[0,1,2,3,4,5],releas:9,resourc:5,schema:7,sourc:9,stabl:9,start:6,submodul:[1,2,3,4],subpackag:[0,4],tabl:8,type:2,util:[4,5],valid:2,welcom:8}})