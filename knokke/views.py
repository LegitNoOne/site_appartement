from django.shortcuts import render
from knokke.models import Mois
from knokke.models import Annee
from knokke.models import Calendrier
from knokke.models import Prix
from knokke.models import reduction
from knokke.models import Nettoyage
from django.db.models import Q
import calendar
import json
from django.core.paginator import Paginator, EmptyPage
from .forms import Formulaire_Reservation
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.messages import get_messages

from datetime import datetime
import requests
def accueil(request):
    '''Vue générant l'accueil du site'''
    
    messages = get_messages(request)
    return render(request,'knokke/accueil.html',locals())

def booking(request, page=1,liste_memoire='0,0',premier_jour=0):
    '''Vue générant la premiere page du calendrier'''

    calendrier=Calendrier.objects.all()
    cal=calendrier[0]
    #jours_reserves=calendrier[0].jours_reserves
    liste_jours_reserves=cal.get_list()
    jours_reserves=[]
    for i in liste_jours_reserves:
        jours_reserves.append(i)
    
    #convertion d'une liste en python en js
    jours_reserves=json.dumps(jours_reserves)
    liste_memoire=liste_memoire.split(',')
    compteur_memoire=liste_memoire[0]
    prix_memoire=liste_memoire[1]
    an=Annee.objects.all()
    #mois=Mois.objects.filter(Q(annee=an[0]))


    liste_mois=['janvier','fevrier','mars','avril','mai','juin','juillet','aout','septembre','octobre','novembre','decembre']
    
    #code servant a mettre le calendrier a la date actuelle et qu'on ne puisse revenir a des dates anterieures
    mois_actuel=datetime.now().month
    annee_actuelle=datetime.now().year
    mois_recherche = Mois.objects.all()

    i=0
    for element in mois_recherche:
    	i+=1
    	if element.annee.an == annee_actuelle and element.nom == liste_mois[mois_actuel-1]:
    		current=i
    if page < current:
    	page = current


    # Partie de code qui s'occupe de la pagination
    mois=Mois.objects.all()
    print(mois)
    paginator=Paginator(mois,1)
    try:
        mois = paginator.page(page)
    except EmptyPage:
        mois=paginator.page(paginator.num_pages)
    #fin pagination




    for i in mois:
        annee_js=i.annee.an
        mois_js=i.nom
    
    liste_jours=[]
    liste_objets=[]
    for moi in mois:
        liste_objets.append(moi.annee.an)
        liste_objets.append(moi.nom)
    for jours in calendar.monthcalendar(liste_objets[0],liste_mois.index(liste_objets[1])+1):
        liste_jours.append(jours)

    #Sélection de la bonne table SQL du model Prix

    prix=Prix.objects.all()
    for element in prix:
        if element.annee.an == liste_objets[0]:
                prix=element
    #Fin Sélection
    liste_prix=[]

    #Creation de la liste des reductions
    reductions=reduction.objects.all()
    r=0
    liste_reduction=[]
    while r < reductions.count():
        liste_reduction.append(reductions[r].reduction_jours)
        liste_reduction.append(reductions[r].reduction_pourcent)
        r+=1

    liste_reduction=str(liste_reduction)
    liste_reduction=liste_reduction.replace('[','')
    liste_reduction=liste_reduction.replace(']','')

    #Sélection de la bonne liste de prix en fonction du mois en cours sur la page
    if liste_objets[1] == 'janvier':
        liste_prix.extend([prix.janvier_jour1,prix.janvier_jour2,prix.janvier_jour3,prix.janvier_jour4,
                prix.janvier_jour5,prix.janvier_jour6,prix.janvier_jour7,prix.janvier_jour8,prix.janvier_jour9,
                prix.janvier_jour10,prix.janvier_jour11,prix.janvier_jour12,prix.janvier_jour13,prix.janvier_jour14,
                prix.janvier_jour15,prix.janvier_jour16,prix.janvier_jour17,prix.janvier_jour18,prix.janvier_jour19,
                prix.janvier_jour20,prix.janvier_jour21,prix.janvier_jour22,prix.janvier_jour23,prix.janvier_jour24,
                prix.janvier_jour25,prix.janvier_jour26,prix.janvier_jour27,prix.janvier_jour28,prix.janvier_jour29,
                prix.janvier_jour30,prix.janvier_jour31])

    if liste_objets[1] == 'fevrier':
        liste_prix.extend([prix.fevrier_jour1,prix.fevrier_jour2,prix.fevrier_jour3,prix.fevrier_jour4,
            prix.fevrier_jour5,prix.fevrier_jour6,prix.fevrier_jour7,prix.fevrier_jour8,prix.fevrier_jour9,
            prix.fevrier_jour10,prix.fevrier_jour11,prix.fevrier_jour12,prix.fevrier_jour13,prix.fevrier_jour14,
            prix.fevrier_jour15,prix.fevrier_jour16,prix.fevrier_jour17,prix.fevrier_jour18,prix.fevrier_jour19,
            prix.fevrier_jour20,prix.fevrier_jour21,prix.fevrier_jour22,prix.fevrier_jour23,prix.fevrier_jour24,
            prix.fevrier_jour25,prix.fevrier_jour26,prix.fevrier_jour27,prix.fevrier_jour28,prix.fevrier_jour29
            ])

    if liste_objets[1] == 'mars':
        liste_prix.extend([prix.mars_jour1,prix.mars_jour2,prix.mars_jour3,prix.mars_jour4,
            prix.mars_jour5,prix.mars_jour6,prix.mars_jour7,prix.mars_jour8,prix.mars_jour9,
            prix.mars_jour10,prix.mars_jour11,prix.mars_jour12,prix.mars_jour13,prix.mars_jour14,
            prix.mars_jour15,prix.mars_jour16,prix.mars_jour17,prix.mars_jour18,prix.mars_jour19,
            prix.mars_jour20,prix.mars_jour21,prix.mars_jour22,prix.mars_jour23,prix.mars_jour24,
            prix.mars_jour25,prix.mars_jour26,prix.mars_jour27,prix.mars_jour28,prix.mars_jour29,
            prix.mars_jour30,prix.mars_jour31])

    if liste_objets[1] == 'avril':
        liste_prix.extend([prix.avril_jour1,prix.avril_jour2,prix.avril_jour3,prix.avril_jour4,
            prix.avril_jour5,prix.avril_jour6,prix.avril_jour7,prix.avril_jour8,prix.avril_jour9,
            prix.avril_jour10,prix.avril_jour11,prix.avril_jour12,prix.avril_jour13,prix.avril_jour14,
            prix.avril_jour15,prix.avril_jour16,prix.avril_jour17,prix.avril_jour18,prix.avril_jour19,
            prix.avril_jour20,prix.avril_jour21,prix.avril_jour22,prix.avril_jour23,prix.avril_jour24,
            prix.avril_jour25,prix.avril_jour26,prix.avril_jour27,prix.avril_jour28,prix.avril_jour29,
            prix.avril_jour30])

    if liste_objets[1] == 'mai':
        liste_prix.extend([prix.mai_jour1,prix.mai_jour2,prix.mai_jour3,prix.mai_jour4,
            prix.mai_jour5,prix.mai_jour6,prix.mai_jour7,prix.mai_jour8,prix.mai_jour9,
            prix.mai_jour10,prix.mai_jour11,prix.mai_jour12,prix.mai_jour13,prix.mai_jour14,
            prix.mai_jour15,prix.mai_jour16,prix.mai_jour17,prix.mai_jour18,prix.mai_jour19,
            prix.mai_jour20,prix.mai_jour21,prix.mai_jour22,prix.mai_jour23,prix.mai_jour24,
            prix.mai_jour25,prix.mai_jour26,prix.mai_jour27,prix.mai_jour28,prix.mai_jour29,
            prix.mai_jour30,prix.mai_jour31])

    if liste_objets[1] == 'juin':
        liste_prix.extend([prix.juin_jour1,prix.juin_jour2,prix.juin_jour3,prix.juin_jour4,
            prix.juin_jour5,prix.juin_jour6,prix.juin_jour7,prix.juin_jour8,prix.juin_jour9,
            prix.juin_jour10,prix.juin_jour11,prix.juin_jour12,prix.juin_jour13,prix.juin_jour14,
            prix.juin_jour15,prix.juin_jour16,prix.juin_jour17,prix.juin_jour18,prix.juin_jour19,
            prix.juin_jour20,prix.juin_jour21,prix.juin_jour22,prix.juin_jour23,prix.juin_jour24,
            prix.juin_jour25,prix.juin_jour26,prix.juin_jour27,prix.juin_jour28,prix.juin_jour29,
            prix.juin_jour30])

    if liste_objets[1] == 'juillet':
        liste_prix.extend([prix.juillet_jour1,prix.juillet_jour2,prix.juillet_jour3,prix.juillet_jour4,
            prix.juillet_jour5,prix.juillet_jour6,prix.juillet_jour7,prix.juillet_jour8,prix.juillet_jour9,
            prix.juillet_jour10,prix.juillet_jour11,prix.juillet_jour12,prix.juillet_jour13,prix.juillet_jour14,
            prix.juillet_jour15,prix.juillet_jour16,prix.juillet_jour17,prix.juillet_jour18,prix.juillet_jour19,
            prix.juillet_jour20,prix.juillet_jour21,prix.juillet_jour22,prix.juillet_jour23,prix.juillet_jour24,
            prix.juillet_jour25,prix.juillet_jour26,prix.juillet_jour27,prix.juillet_jour28,prix.juillet_jour29,
            prix.juillet_jour30,prix.juillet_jour31])

    if liste_objets[1] == 'aout':
        liste_prix.extend([prix.aout_jour1,prix.aout_jour2,prix.aout_jour3,prix.aout_jour4,
            prix.aout_jour5,prix.aout_jour6,prix.aout_jour7,prix.aout_jour8,prix.aout_jour9,
            prix.aout_jour10,prix.aout_jour11,prix.aout_jour12,prix.aout_jour13,prix.aout_jour14,
            prix.aout_jour15,prix.aout_jour16,prix.aout_jour17,prix.aout_jour18,prix.aout_jour19,
            prix.aout_jour20,prix.aout_jour21,prix.aout_jour22,prix.aout_jour23,prix.aout_jour24,
            prix.aout_jour25,prix.aout_jour26,prix.aout_jour27,prix.aout_jour28,prix.aout_jour29,
            prix.aout_jour30,prix.aout_jour31])

    if liste_objets[1] == 'septembre':
        liste_prix.extend([prix.septembre_jour1,prix.septembre_jour2,prix.septembre_jour3,prix.septembre_jour4,
            prix.septembre_jour5,prix.septembre_jour6,prix.septembre_jour7,prix.septembre_jour8,prix.septembre_jour9,
            prix.septembre_jour10,prix.septembre_jour11,prix.septembre_jour12,prix.septembre_jour13,prix.septembre_jour14,
            prix.septembre_jour15,prix.septembre_jour16,prix.septembre_jour17,prix.septembre_jour18,prix.septembre_jour19,
            prix.septembre_jour20,prix.septembre_jour21,prix.septembre_jour22,prix.septembre_jour23,prix.septembre_jour24,
            prix.septembre_jour25,prix.septembre_jour26,prix.septembre_jour27,prix.septembre_jour28,prix.septembre_jour29,
            prix.septembre_jour30])

    if liste_objets[1] == 'octobre':
        liste_prix.extend([prix.octobre_jour1,prix.octobre_jour2,prix.octobre_jour3,prix.octobre_jour4,
            prix.octobre_jour5,prix.octobre_jour6,prix.octobre_jour7,prix.octobre_jour8,prix.octobre_jour9,
            prix.octobre_jour10,prix.octobre_jour11,prix.octobre_jour12,prix.octobre_jour13,prix.octobre_jour14,
            prix.octobre_jour15,prix.octobre_jour16,prix.octobre_jour17,prix.octobre_jour18,prix.octobre_jour19,
            prix.octobre_jour20,prix.octobre_jour21,prix.octobre_jour22,prix.octobre_jour23,prix.octobre_jour24,
            prix.octobre_jour25,prix.octobre_jour26,prix.octobre_jour27,prix.octobre_jour28,prix.octobre_jour29,
            prix.octobre_jour30,prix.octobre_jour31])

    if liste_objets[1] == 'novembre':
        liste_prix.extend([prix.novembre_jour1,prix.novembre_jour2,prix.novembre_jour3,prix.novembre_jour4,
            prix.novembre_jour5,prix.novembre_jour6,prix.novembre_jour7,prix.novembre_jour8,prix.novembre_jour9,
            prix.novembre_jour10,prix.novembre_jour11,prix.novembre_jour12,prix.novembre_jour13,prix.novembre_jour14,
            prix.novembre_jour15,prix.novembre_jour16,prix.novembre_jour17,prix.novembre_jour18,prix.novembre_jour19,
            prix.novembre_jour20,prix.novembre_jour21,prix.novembre_jour22,prix.novembre_jour23,prix.novembre_jour24,
            prix.novembre_jour25,prix.novembre_jour26,prix.novembre_jour27,prix.novembre_jour28,prix.novembre_jour29,
            prix.novembre_jour30])

    if liste_objets[1] == 'decembre':
        liste_prix.extend([prix.decembre_jour1,prix.decembre_jour2,prix.decembre_jour3,prix.decembre_jour4,
            prix.decembre_jour5,prix.decembre_jour6,prix.decembre_jour7,prix.decembre_jour8,prix.decembre_jour9,
            prix.decembre_jour10,prix.decembre_jour11,prix.decembre_jour12,prix.decembre_jour13,prix.decembre_jour14,
            prix.decembre_jour15,prix.decembre_jour16,prix.decembre_jour17,prix.decembre_jour18,prix.decembre_jour19,
            prix.decembre_jour20,prix.decembre_jour21,prix.decembre_jour22,prix.decembre_jour23,prix.decembre_jour24,
            prix.decembre_jour25,prix.decembre_jour26,prix.decembre_jour27,prix.decembre_jour28,prix.decembre_jour29,
            prix.decembre_jour30,prix.decembre_jour31])

    #Modification de la liste pour qu'elle soit valide en JS
    prix=str(liste_prix)
    prix=prix.replace('[','')
    prix=prix.replace(']','')
    semaine1=liste_jours[0]
    
    #Remplacement des 0 par des '' dans le calendrier
    semaine1=[' ' if x==0 else x for x in semaine1]
    semaine2=liste_jours[1]
    semaine3=liste_jours[2]
    semaine4=liste_jours[3]
    try:
        semaine5=liste_jours[4]
    except IndexError:
        #dans certains mois il n'y a que 4 semaines donc il faut traiter ce cas
        semaine5=[0,0,0,0,0,0,0]

    #Remplacement des 0 par des '' dans le calendrier
    semaine5=[' ' if x==0 else x for x in semaine5]

    #Tester s'il y a une 6eme semaine
    try:
        semaine6=liste_jours[5]
    except IndexError:
        semaine6=[' ',' ',' ',' ',' ',' ',' ']

    #Remplacement des 0 par des '' dans le calendrier
    semaine6=[' ' if x==0 else x for x in semaine6]

    # Semaine 1
    jour1=semaine1[0]
    jour2=semaine1[1]
    jour3=semaine1[2]
    jour4=semaine1[3]
    jour5=semaine1[4]
    jour6=semaine1[5]
    jour7=semaine1[6]
    
    # Semaine2
    jour8=semaine2[0]
    jour9=semaine2[1]
    jour10=semaine2[2]
    jour11=semaine2[3]
    jour12=semaine2[4]
    jour13=semaine2[5]
    jour14=semaine2[6]

    #Semaine3
    jour15=semaine3[0]
    jour16=semaine3[1]
    jour17=semaine3[2]
    jour18=semaine3[3]
    jour19=semaine3[4]
    jour20=semaine3[5]
    jour21=semaine3[6]

    #Semaine4
    jour22=semaine4[0]
    jour23=semaine4[1]
    jour24=semaine4[2]
    jour25=semaine4[3]
    jour26=semaine4[4]
    jour27=semaine4[5]
    jour28=semaine4[6]

    #Semaine5
    jour29=semaine5[0]
    jour30=semaine5[1]
    jour31=semaine5[2]
    jour32=semaine5[3]
    jour33=semaine5[4]
    jour34=semaine5[5]
    jour35=semaine5[6]

    #Semaine6
    jour36=semaine6[0]
    jour37=semaine6[1]
    jour38=semaine6[2]
    jour39=semaine6[3]
    jour40=semaine6[4]
    jour41=semaine6[5]
    jour42=semaine6[6]

    		

    
    #Renvoie les attributs de Mois et les jours d'un mois
    return render(request,'knokke/reservation.html',{'premier_jour':premier_jour,'compteur_memoire':compteur_memoire,'prix_memoire':prix_memoire,
        'liste_reduction':liste_reduction,'prix':prix,'liste_jours':liste_jours,'annee_js':annee_js,'mois_js':mois_js,
        'jours_reserves':jours_reserves,'semaine1':semaine1,'semaine2':semaine2,
        'semaine3':semaine3,'semaine4':semaine4,'mois':mois,'jour1':jour1,'jour2':jour2,'jour3':jour3,
        'jour4':jour4,'jour5':jour5,'jour6':jour6,'jour7':jour7,'jour8':jour8,'jour9':jour9,'jour10':jour10,
        'jour11':jour11,'jour11':jour11,'jour12':jour12,'jour13':jour13,'jour14':jour14,'jour15':jour15,
        'jour16':jour16,'jour17':jour17,'jour18':jour18,'jour19':jour19,'jour20':jour20,'jour21':jour21,
        'jour22':jour22,'jour23':jour23,'jour24':jour24,'jour25':jour25,'jour26':jour26,'jour27':jour27,
        'jour28':jour28,'jour29':jour29,'jour30':jour30,'jour31':jour31,'jour32':jour32,'jour33':jour33,
        'jour34':jour34,'jour35':jour35,'jour36':jour36,'jour37':jour37,'jour38':jour38,'jour39':jour39,
        'jour40':jour40,'jour41':jour41,'jour42':jour42})

def formulaire(request,premier_jour='0',dernier_jour='0',compteur=0,prix=0,nettoyage_verification='oui'):
        form = Formulaire_Reservation(request.POST or None)
        

        if form.is_valid():
                
                email = form.cleaned_data['email']
                nom = form.cleaned_data['nom']
                prenom = form.cleaned_data['prenom']
                nettoyage= form.cleaned_data['nettoyage']
                
                # Nous pourrions ici envoyer l'e-mail grâce aux données 
                # que nous venons de récupérer
                envoi = True
                premier_jour=premier_jour.replace(' ','')
                dernier_jour=dernier_jour.replace(' ','')
                url_suppression='http://Henneaux_appartement/suppression/' + premier_jour + '/' + dernier_jour + '/'


                if nettoyage:
                    nettoyage=Nettoyage.objects.all()[0]
                    nettoyage=nettoyage.prix
                    message_nettoyage="Ps: Cette personne a aussi inclut le nettoyage dans sa réservation.\n"
                    message_nettoyage2="( Nettoyage compris )"
                else:
                        message_nettoyage=""
                        message_nettoyage2="( Sans nettoyage )"
                        nettoyage=0
                send_mail(
                        "Demande de réservation de l'appartement",
                        "Bonjour chers propriétaires,\n je vous informe que {} {} désire réserver l'appartement du {} au {} ce qui vous fera un pactole de {} €. \n {} Voulez-vous vous confirmer cette demande ? \n Si oui, voici son email pour commencer a dialoguer : {} \n Si non : veuillez appuyer sur ce lien qui annulera la réservation en cours : {}".format(nom,prenom,premier_jour,dernier_jour,prix+nettoyage,message_nettoyage,email,url_suppression),
                        'lucashenneaux@icloud.com',
                        ['annickwarichet@yahoo.com'],
                        fail_silently=False,
                        )
                send_mail(
                        "Demande de réservation de l'appartement",
                        "Bonjour {} {},\n je vous informe que vous avez envoyé une demande de réservation du {} au {} pour un total de {} € {}.\nSi ces dates ne sont pas correctes, veuillez en discuter avec les propriétaires via cette adresse mail :\n annickwarichet@yahoo.com\n Sinon attendez juste une réponse qui confirmera votre demande en cours.\n Merci d'avoir choisi cet appartement !".format(nom,prenom,premier_jour,dernier_jour,prix+nettoyage,message_nettoyage2),
                        'lucashenneaux@icloud.com',
                        [email],
                        fail_silently=False,
                        )
                messages.add_message(request, messages.INFO, 'Votre demande a bien été envoyée, vous recevrez une réponse par mail !')
                #selection de la liste des jours reserves
                jours_reserves=Calendrier.objects.all()
                jours_reserves=jours_reserves[0]


                liste_jours=[]
                liste_mois=['janvier','fevrier','mars','avril','mai','juin','juillet','aout','septembre','octobre','novembre','decembre']
                from datetime import date, timedelta
                import re
                #isolations de jour et annee qui sont des nombres dans une chaine de caracteres et mois qui est un string
                liste_debut=re.findall(r'\d+', premier_jour)
                jour_debut=int(liste_debut[0])
                annee_debut=int(liste_debut[1])
                mois_debut= ''.join([i for i in premier_jour if not i.isdigit()])
                mois_debut=mois_debut.strip()

                liste_fin=re.findall(r'\d+', dernier_jour)
                jour_fin=int(liste_fin[0])
                annee_fin=int(liste_fin[1])
                mois_fin= ''.join([i for i in dernier_jour if not i.isdigit()])
                mois_fin=mois_fin.strip()
                #Creation du premier et dernier jour afin de calculuer leur delta
                d1=date(annee_debut,liste_mois.index(mois_debut)+1,jour_debut)
                d2=date(annee_fin,liste_mois.index(mois_fin)+1,jour_fin)

                delta = d2 - d1
                #Transformation des dates en format x-x-x en xxx afin que notre code puisse le lire par la suite (ex: 1janvier2019)
                for i in range(delta.days + 1):
                    date = str(d1 + timedelta(i))
                    date=date.split('-')
                    if date[2] != '10' and date[2] != '20' and date[2] != '30':
                    	date[2]=date[2].replace('0','')
                    if date[1] != '10' and date[1] != '20' and date[1] != '30':
                    	date[1]=date[1].replace('0','')
                    jour=date[2]
                    mois=liste_mois[int(date[1])-1]
                    annee=date[0]
                    date_ordre=jour+mois+annee
                    jours_reserves.set_list(date_ordre)
                jours_reserves.save()
                return HttpResponseRedirect('/Henneaux_appartement/accueil')

        nettoyage=Nettoyage.objects.all()
        nettoyage=nettoyage[0].prix
        # Quoiqu'il arrive, on affiche la page du formulaire.
        return render(request, 'knokke/formulaire.html', locals())


def suppression(request,premier_jour='0',dernier_jour='0'):
    jours_reserves=Calendrier.objects.all()
    jours_reserves=jours_reserves[0]




    liste_jours=[]
    liste_mois=['janvier','fevrier','mars','avril','mai','juin','juillet','aout','septembre','octobre','novembre','decembre']
    from datetime import date, timedelta
    import re
    #isolations de jour et annee qui sont des nombres dans une chaine de caracteres et mois qui est un string
    liste_debut=re.findall(r'\d+', premier_jour)
    jour_debut=int(liste_debut[0])
    annee_debut=int(liste_debut[1])
    mois_debut= ''.join([i for i in premier_jour if not i.isdigit()])
    mois_debut=mois_debut.strip()
    liste_fin=re.findall(r'\d+', dernier_jour)
    jour_fin=int(liste_fin[0])
    annee_fin=int(liste_fin[1])
    mois_fin= ''.join([i for i in dernier_jour if not i.isdigit()])
    mois_fin=mois_fin.strip()
    #Creation du premier et dernier jour afin de calculuer leur delta
    d1=date(annee_debut,liste_mois.index(mois_debut)+1,jour_debut)
    d2=date(annee_fin,liste_mois.index(mois_fin)+1,jour_fin)
    delta = d2 - d1
    #Transformation des dates en format x-x-x en xxx afin que notre code puisse le lire par la suite (ex: 1janvier2019)
    for i in range(delta.days + 1):
    	date = str(d1 + timedelta(i))
    	date=date.split('-')
    	if date[2] != '10' and date[2] != '20' and date[2] != '30':
    		date[2]=date[2].replace('0','')
    	if date[1] != '10' and date[1] != '20' and date[1] != '30':
    		date[1]=date[1].replace('0','')
    	jour=date[2]
    	mois=liste_mois[int(date[1])-1]
    	annee=date[0]
    	date_ordre=jour+mois+annee
    	jours_reserves.delete_list(date_ordre)

    jours_reserves.save()
    return render(request, 'knokke/suppression.html', locals())



def generalites(request):
    return render(request,'knokke/generalites.html',locals())

def comment_y_arriver(request):
    return render(request,'knokke/comment_y_arriver.html',locals())

def en_pratique(request):
    return render(request,'knokke/en_pratique.html',locals())

def avant_de_quitter(request):
    return render(request,'knokke/avant_de_quitter.html',locals())

def commerces_et_activites(request):
    return render(request,'knokke/commerces_et_activites.html',locals())

def index(request):
    r = requests.get('http://httpbin.org/status/418')
    print(r.text)
    return HttpResponse('<pre>' + r.text + '</pre>')
