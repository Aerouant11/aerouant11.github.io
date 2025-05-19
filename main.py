from tkinter import *
import sqlite3
from datetime import datetime

root = Tk()
root.title('Renseignement Base de Donnees')
root.geometry("500x600")

# Creation Base de Donnees Article
conn = sqlite3.connect('articles.db')

#Create cursor
c = conn.cursor()

# Create table
c.execute("""CREATE TABLE IF NOT EXISTS artsecfrais(
    Name_Art TEXT,
    Marq_Art text,
    Fam_Art text,
    Dlc1_Art integer,
    Qty1_Art integer,
    Dlc2_Art integer,
    Qty2_Art integer,
    Dlc3_Art integer,
    Qty3_Art integer,
    Dentree_Art integer    
)""")

# Creation fonction delete enregistrement
def delete():
    # Creation base de donnees article
    conn = sqlite3.connect('articles.db')
    #Create cursor
    c = conn.cursor()
    
    c.execute("DELETE FROM artsecfrais WHERE oid = " +delete_box.get())
    
    delete_box.delete(0, END)
    
    #Commit changes
    conn.commit()
    #Close connection
    conn.close()

# Creaion fonction submit pour Database
def submit():
    # Creation Base de Donnees Article
    conn = sqlite3.connect('articles.db')
    #Create cursor
    c = conn.cursor()    
    
    # Insertion enregistrement dans Base de Donnees
    c.execute("INSERT INTO artsecfrais VALUES (:f_name, :f_marq, :f_fam, :f_dlc1, :f_qty1, :f_dlc2, :f_qty2, :f_dlc3, :f_qty3, :f_dentree)",
              {
                  'f_name': f_name.get(),
                  'f_marq': f_marq.get(),
                  'f_fam': f_fam.get(),
                  'f_dlc1': f_dlc1.get(),
                  'f_qty1': f_qty1.get(),
                  'f_dlc2': f_dlc2.get(),
                  'f_qty2': f_qty2.get(),
                  'f_dlc3': f_dlc3.get(),
                  'f_qty3': f_qty3.get(),
                  'f_dentree': f_dentree.get()
              })    
    
    #Commit changes
    conn.commit()
    #Close connection
    conn.close()

    # Effacement des infos saisies apres validation
    f_name.delete(0, END)
    f_marq.delete(0, END)
    f_fam.delete(0, END)
    f_dlc1.delete(0, END)
    f_qty1.delete(0, END)
    f_dlc2.delete(0, END)
    f_qty2.delete(0, END)
    f_dlc3.delete(0, END)
    f_qty3.delete(0, END)
    f_dentree.delete(0, END)
    
# Creation fonction requete
def query():
    # Creation Base de Donnees Article
    conn = sqlite3.connect('articles.db')
    #Create cursor
    c = conn.cursor()
    
    # Requete Database
    c.execute("SELECT *, oid FROM artsecfrais")
    records = c.fetchall()
    print("Enregistrement :", records)
    
    fen1 = Tk()
    fen1.title('Liste des produits')
    fen1.geometry("500x600")
    # Loop thru results
    print_records = ''
    irw = 0
    irec = 0
    for record in records:
        iebd = 0
        while iebd < 11:
            print_records += str(record[iebd])
            print("Enreg. fenetre :", print_records)
            iebd += 1
        irec += 1
        print("indice irec :", irec)
        query_label = Label(fen1, text=print_records)
        irw += 1
        query_label.grid(row=irw, column=0, columnspan=2, pady=10, padx=10, ipadx=100)
        print_records = ''
 
   
    #Commit changes
    conn.commit()
    #Close connection
    conn.close()
    
# Creation fonction interrogation date limite

def ctrldat():
    #return()
    date_ctrl = int(saisdat_box.get())
    if date_ctrl == 0 :
        print("Date erronee")
    else :
        print(date_ctrl)
    
    # Creation Base de Donnees Article
    conn = sqlite3.connect('articles.db')
    #Create cursor
    c = conn.cursor()
    

### Creation Menu de saisie ###

# Creation texte de la box
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20,pady=(10,0))

f_marq = Entry(root, width=30)
f_marq.grid(row=1, column=1)

f_fam = Entry(root, width=30)
f_fam.grid(row=2, column=1)

f_dlc1 = Entry(root, width=30)
f_dlc1.grid(row=3, column=1)

f_qty1 = Entry(root, width=30)
f_qty1.grid(row=4, column=1)

f_dlc2 = Entry(root, width=30)
f_dlc2.grid(row=5, column=1)

f_qty2 = Entry(root, width=30)
f_qty2.grid(row=6, column=1)

f_dlc3 = Entry(root, width=30)
f_dlc3.grid(row=7, column=1)

f_qty3 = Entry(root, width=30)
f_qty3.grid(row=8, column=1)

f_dentree = Entry(root, width=30)
f_dentree.grid(row=9, column=1)

delete_box = Entry(root, width=30)
delete_box.grid(row=12, column=1)

saisdat_box = Entry(root, width=30)
saisdat_box.grid(row=14, column=1)

# Creation texte box label
f_name_label = Label(root, text="Libelle article")
f_name_label.grid(row=0, column=0, pady=(10,0))

f_marq_label = Label(root, text="Marque")
f_marq_label.grid(row=1, column=0)

f_fam_label = Label(root, text="Sec ou Frais")
f_fam_label.grid(row=2, column=0)

f_dlc1_label = Label(root, text="Date LC1")
f_dlc1_label.grid(row=3, column=0)

f_qty1_label = Label(root, text="Quantite DLC1")
f_qty1_label.grid(row=4, column=0)

f_dlc2_label = Label(root, text="Date LC2")
f_dlc2_label.grid(row=5, column=0)

f_qty2_label = Label(root, text="Quantite DLC2")
f_qty2_label.grid(row=6, column=0)

f_dlc3_label = Label(root, text="Date LC3")
f_dlc3_label.grid(row=7, column=0)

f_qty3_label = Label(root, text="Quantite DLC3")
f_qty3_label.grid(row=8, column=0)

f_dentree_label = Label(root, text="Date Entree")
f_dentree_label.grid(row=9, column=0)

delete_box_label = Label(root, text="ID a supprime")
delete_box_label.grid(row=12,column=0)

saisdat_box_label = Label(root, text="Date du jour (jjmmaaaa)")
saisdat_box_label.grid(row=14,column=0)

# Creation Bouton de validation
submit_btn = Button(root, text="Addition d'enregistrement", command=submit)
submit_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=133)

# Creation Bouton de requete
query_btn = Button(root, text="Consultation enregistrement", command=query)
query_btn.grid(row=11, column=0, columnspan=2, padx=10, pady=10, ipadx=135)

# Creation bouton Delete
delet_btn = Button(root, text="Suppression enregistrement", command=delete)
delet_btn.grid(row=13, column=0, columnspan=2, padx=10, pady=10, ipadx=137)

# Creation bouton controle date
ctrldat_btn = Button(root, text="Confirmation date du jour", command=ctrldat)
ctrldat_btn.grid(row=15,column=0,columnspan=2, padx=10, pady=10, ipadx=138)

#Commit changes
conn.commit()

#Close connection
conn.close()

root.mainloop()
