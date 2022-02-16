from tkinter import *
from tkinter import ttk
import re
import sys
import webbrowser
from datetime import date
import cx_Oracle
global root
root=Tk()

conn=cx_Oracle.connect('system/oracle1@//localhost:1521/orcl')

cur=conn.cursor()

root.geometry("800x600")

root.title(" RESORTS BOOKER: LOG IN PAGE")

global myLabel
global NEXT
global name1
global user1
global password1
name1=Entry(root)
user1=Entry(root)
password1=Entry(root)
type_room="ROOMS"
room_values=[0]*15
myLabel=Label(root)
NEXT=Button(root)
root.configure(bg="bisque")

def submit1():
        global myLabel
        global NEXT

        def Next():
                global top2
                top2=Toplevel()
                top2.geometry("800x600")
                top2.configure(bg="antiquewhite")
                top2.title(" IMAGES OF PALM RESORTS ")
                top3=Label(top2,text=" PALM RESORTS FROM OUTER ")
                top3.grid(row=0,column=1)
                def myclick10():
                        webbrowser.open("https://travelmail.in/wp-content/uploads/2018/04/Azaya-Beach-Resort-Goa.jpg")
                def myclick11():
                        webbrowser.open("https://images.unsplash.com/photo-1520250497591-112f2f40a3f4?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&w=1000&q=80")
                def myclick12():
                        webbrowser.open("https://img.traveltriangle.com/blog/wp-content/tr:w-700,h-400/uploads/2017/04/11.jpg")
                def myclick13():
                        webbrowser.open("https://i.pinimg.com/originals/ce/b9/ac/ceb9acb0ad27872cec02e838de7339c3.jpg")
                def myclick14():
                        webbrowser.open("https://trailblazertours.com/domestic_pages/images/slider/ocean_palms_goa_resort_calangute_01.jpg")
                def myclick15():
                        webbrowser.open("https://www.azayabeachresortgoa.com/images/Azaya.jpg")
                def myclick16():
                        webbrowser.open("https://img.traveltriangle.com/blog/wp-content/uploads/2019/12/Shri-Mangueshi-temple-15_dec.jpg")
                def myclick17():
                        webbrowser.open("https://www.mapsofindia.com/maps/goa/goa-resorts.gif")
                def myclick18():
                        webbrowser.open("https://www.hotelsingoa.co.in/logos/varca_palms_beach_resort.jpg")
                
                def next1():
                        global top4
                        top2.destroy()
                        top4=Toplevel()
                        top4.configure(bg="mintcream")
                        top4.geometry("800x500")
                        top4.title(" FAMOUS PLACES TO VISIT NEAR PALM RESORTS ")
                        top5=Label(top4,text=" FAMOUS PLACES IN GOA ")
                        top5.grid(row=0,column=1)
                        
                        def myclick19():
                                webbrowser.open("https://img.traveltriangle.com/blog/wp-content/tr:w-700,h-400/uploads/2015/12/Anjuna-Beach-Sunset.jpg")
                        def myclick20():
                                webbrowser.open("https://img.traveltriangle.com/blog/wp-content/tr:w-700,h-400/uploads/2015/12/Anjuna-Beach-Sunset.jpg")
                        def myclick21():
                                webbrowser.open("https://img.traveltriangle.com/blog/wp-content/tr:w-700,h-400/uploads/2015/12/bicholim-market.jpg")
                        def myclick22():
                                webbrowser.open("https://img.traveltriangle.com/blog/wp-content/tr:w-700,h-400/uploads/2015/12/club-cabana.jpg")
                        def myclick23():
                                webbrowser.open("https://img.traveltriangle.com/blog/wp-content/tr:w-700,h-400/uploads/2015/07/Bom-Jesus-Basilica-Goa.jpg")
                        def myclick24():
                                webbrowser.open("https://img.traveltriangle.com/blog/wp-content/tr:w-700,h-400/uploads/2019/12/Dreamland_Beach_Bali_Indonesia.jpg")
                        def myclick25():
                                webbrowser.open("https://img.traveltriangle.com/blog/wp-content/tr:w-700,h-400/uploads/2019/12/Magnolia-Beach.jpg")
                        def myclick26():
                                webbrowser.open("https://img.traveltriangle.com/blog/wp-content/tr:w-700,h-400/uploads/2017/04/kw-110417-A-boat-near-the-Butterfly-Beach-with-the-forest-cover-in-the-background.jpg")
                        def myclick27():
                                webbrowser.open("https://img.traveltriangle.com/blog/wp-content/tr:w-700,h-400/uploads/2014/11/Dona-Paula-beach-bungalow.jpg")
                        
                        def interiors():
                                global top_int
                                top4.destroy()
                                top_int=Toplevel()
                                top_int.configure(bg="cornsilk")
                                top_int.geometry("800x600")
                                top_int.configure(bg="beige") 
                                top_int.title("INTERIORS OF PALM_RESORTS")
                                ## LABLES
                                label_int1=Label(top_int,text="...THE INTERIORS OF PALM RESORTS...")
                                label_int1.grid(row=0,column=10)
                                label_int2=Label(top_int,text="THE HALLWAY")
                                label_int2.grid(row=2,column=3)
                                label_int2=Label(top_int,text="SINGLE_ROOM")
                                label_int2.grid(row=6,column=3)
                                label_int2=Label(top_int,text="DOUBLE_ROOM")
                                label_int2.grid(row=8,column=3)
                                label_int2=Label(top_int,text="SUITE_ROOMS")
                                label_int2.grid(row=11,column=3)


                                def click_rec():
                                        webbrowser.open("https://res.cloudinary.com/simplotel/image/upload/w_5000,h_3400/x_0,y_294,w_5000,h_2812,r_0,c_crop,q_80,fl_progressive/w_400,f_auto,c_fit/misty-mountain-resort-munnar/Reception_at_Munnar_Halls,_Misty_Munnar_Resort_Top_munnar_resorts,__67")
                                def lounge_1():
                                        webbrowser.open("https://cf.bstatic.com/images/hotel/max1024x768/136/136886066.jpg")
                                def lounge_2():
                                        webbrowser.open("https://www.poggesiusa.com/wp-content/uploads/2018/02/pool-side-chairs-resort.jpg")
                                def room_1():
                                        webbrowser.open("https://setupmyhotel.com/images/Room-Type-Hollywood-Twin-Room.jpg")
                                def bath_1():
                                        webbrowser.open("https://media-cdn.tripadvisor.com/media/photo-s/06/93/17/8c/lahari-resorts.jpg")
                                def view_1():
                                        webbrowser.open("https://www.asiawebdirect.com/media/images/hotels/1253/389233.jpg")
                                def room_2():
                                        webbrowser.open("https://longuinhosgoa.com/wp-content/uploads/2018/12/Luxury-Sea-View-Room.jpg")
                                def bath_2():
                                        webbrowser.open("https://tiimg.tistatic.com/fp/1/005/326/best-finish-resorts-bathroom-enclosure-791.jpg")
                                def views_2():
                                        webbrowser.open("https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSpmM8TLcv1adwcGozql800iP9_7nXSQzbyvw&usqp=CAU")
                                def suite_room():
                                        webbrowser.open("https://i.pinimg.com/originals/8a/73/8f/8a738f7543c0ac3db3e333d28e7227c2.jpg")
                                def suite_bath():
                                        webbrowser.open("https://media-cdn.tripadvisor.com/media/photo-s/02/7f/f2/71/filename-p1000247-jpg.jpg")
                                def view_suit():
                                        webbrowser.open("https://ik.imagekit.io/grgdihc3l/getmedia/bd57835a-d85d-48ed-9067-5eb6a5e781a2/Loews_Miami_Beach_balcony_view_1440x900.aspx?width=768&height=480&ext=.jpg")

                                def nextt():
                                        top_int.destroy()
                                        global top7,g_id
                                        top7=Toplevel()
                                        top7.configure(bg="lightcyan")
                                        top7.geometry("800x600")
                                        top7.title(" FAMOUS PLACES TO VISIT NEAR PALM RESORTS ")

                                        warn_1=Label(top7)
                                        warn_2=Label(top7)
                                        warn_3=Label(top7)
                                        warn_4=Label(top7)
                                        na_label=Label(top7)

                                        def address_book():
                                                top7.destroy()
                                                global top6,g_id
                                                top6=Toplevel()
                                                top6.geometry("800x800")
                                                top6.title("ADDRESS BOOK")

                                                alert_1=Label(top6)
                                                alert_2=Label(top6)
                                                alert_3=Label(top6)
                                                alert_4=Label(top6)
                                                alert_5=Label(top6)
                                                alert_6=Label(top6)

                                                def types_of_room():
                                                        global clicked_number,type17,type18,num1,top11
                                                        top6.destroy()
                                                        top11=Toplevel()
                                                        top11.geometry("800x600")
                                                        top11.configure(bg="papayawhip")
                                                        #type_room="ROOMS"
                                                        room_values=[0]*15
                                                        clicked_number=StringVar()
                                                        clicked_number.set("ROOM_NO")
                                                        drop_number=OptionMenu(top11,clicked_number,*room_values)
                                                        drop_number.grid(row=1,column=2,columnspan=2,padx=20,pady=20)

                                                        def selected(event):
                                                            global type_room,Total_cost,Total_amount,room_num1;
                                                            global drop_number,numb,spend_days,GST
                                                            type_room=clicked_room.get()
                                                            print(type_room)
                                                            click_values()
                                                            
                                                        def click_values():
                                                            rooms=type_room
                                                            print(rooms)
                                                            global drop_number,num
                                                            global room_entry,cost_room,date_of_entry,data_of_exit,room_num,type10,type13
                                                            
                                                            #drop_number.destroy()
                                                            table_select="""SELECT ROOM_NO FROM CHECKING_TABLE_3 WHERE ROOM_TYPE =:rooms"""
                                                            cur.execute(table_select,[rooms])
                                                            room_no=cur.fetchall()
                                                            clicked_number=IntVar()
                                                            clicked_number.set(room_no[0])
                                                            drop_number=OptionMenu(top11,clicked_number,*room_no)
                                                            drop_number.grid(row=1,column=2,columnspan=2,padx=20,pady=20)
                                                            print(drop_number)
                                                            label_room_select=Label(top11,text="SELECT ROOM NO FROM THE LIST")
                                                            label_room_select.grid(row=1,column=5)
                                                            
                                                        def final_result():
                                                            def bill():
                                                                top10=Toplevel()
                                                                top10.configure(bg="honeydew")
                                                                top10.geometry("800x600")
                                                                room_num1=room_num.get()
                                                                def check1():

                                                                    def nextc1():
                                                                        top20=Toplevel()
                                                                        top20.geometry("700x700")
                                                                        thanks=Button(top20,text=" THANK YOU FOR BOOKING !! HOPE YOU ENJOY WELL ",padx=40,pady=40)
                                                                        thanks.grid(row=2,column=2)
                                                                    Pattern = re.compile("[0-9]{16}")
                                                                    pattern1=re.compile("[0-9]{3}")
                                                                    if Pattern.match(type11.get())==None:
                                                                        type17=Label(top10,text=" RE ENTER THE ACCOUNT NUMBER AGAIN ! IT CONTAINS 16 DIGITS ")
                                                                        type17.grid(row=30,column=1)
                                                                        type11.delete(0,END)
                                                                    elif pattern1.match(type13.get())==None:
                                                                        type17.destroy()
                                                                        type18=Label(top10,text=" RE ENTER THE CVV AGAIN ! IT CONTAINS 3 DIGITS")
                                                                        type18.grid(row=30,column=1)
                                                                        type13.delete(0,END)
                                                                    else:
                                                                        nextc=Button(top10,text="NEXT >>>>",padx=20,pady=20,command=changing)
                                                                        nextc.grid(row=30,column=2)
                                                                        
                                                                    label_cancellation=Label(top10,text="DO YOU WANT TO CANCEL THE TICKETS!!!")
                                                                    label_cancellation.grid(row=32,column=1)
                                                                    YES=Button(top10,text="YES",command=cancellation,padx=10,pady=10)
                                                                    YES.grid(row=34,column=1)
                                                                    NO=Button(top10,text="NO",command=nextc1,padx=10,pady=10)
                                                                    NO.grid(row=34,column=2)
                                                                    
                                                                def end():
                                                                    return

                                
                                                                def changing():
                                                                
                                                                  print(room_num1)
                                                                  insertion_unc="""INSERT INTO OCCUPIED
                                                                              SELECT * FROM CHECKING_TABLE_3
                                                                              WHERE ROOM_NO=:room_num1"""
                                                                  cur.execute(insertion_unc,[room_num1])
                                                                  conn.commit()
                                                                  print("data_copied_successfully")
                                                                  deletion_unc="""DELETE FROM CHECKING_TABLE_3
                                                                                 WHERE ROOM_NO=:room_num1"""
                                                                  cur.execute(deletion_unc,[room_num1])
                                                                  conn.commit()
                                                                  print("data deleted successfully")
                                                                  table_id="""SELECT G_ID FROM PERSONAL_3"""
                                                                  room_no=room_num1;
                                                                  cur.execute(table_id)
                                                                  ids=cur.fetchall()
                                                                  last_length=len(ids)
                                                                  ids=ids[last_length-1]
                                                                  ids=list(ids)
                                                                  ids=ids[0]
                                                                  table_name="""SELECT G_NAME FROM PERSONAL_3"""
                                                                  cur.execute(table_name)
                                                                  names=cur.fetchall()
                                                                  last_length_1=len(names)
                                                                  names=names[last_length_1-1]
                                                                  names=list(names)
                                                                  names=names[0]
                                                                  d_o_en=str(clicked_1.get())+"/"+str(clicked.get())+"/"+str(clicked_2.get())
                                                                  d_o_ex=str(dexit_2.get())+"/"+str(dexit_1.get())+"/"+str(dexit_3.get())
                                                                  n_o_p=numb
                                                                  if(type_room=="SINGLE_BED"):
                                                                      c_o_r=4000
                                                                  if(type_room=="DOUBLE_BED"):
                                                                      c_o_r=6500
                                                                  if(type_room=="SUITE_ROOM"):
                                                                      c_o_r=7000
                                                                  gst=GST
                                                                  total_1=Total_amount
                                                                  Nop=No_of_person
                                                                  print(ids,names,room_no,type_room,n_o_p,d_o_en,d_o_ex,c_o_r,gst,total_1) 
                                                                  book_insert="""INSERT INTO BOOKING_DETAILS VALUES(:G_ID,:G_NAME,:ROOM_NO,:R_TYPE,:NO_OF_PERSONS,TO_DATE(:D_O_EN,'DD/MM/YYYY'),TO_DATE(:D_O_EX,'DD/MM/YYYY'),:C_OF_ROOM,:GST,:TOTAL_AMOUNT)""" 
                                                                  cur.execute(book_insert,[ids,names,room_no,type_room,n_o_p,d_o_en,d_o_ex,c_o_r,gst,total_1])
                                                                  conn.commit()
                                                                  print("DETAILS INSERTED INTO BOOKING DETAILS!!!")
                                                            
                                                                def cancellation():
                                                                    global name_can,room_can,type_can,err5
                                                                    
                                                                    top_cancel=Toplevel()
                                                                    top_cancel.geometry("800x600")

                                                                    def ex():
                                                                        print("ENTERED TO THE FUNCTION")
                                                                        name_can=name_cancel.get()
                                                                        room_can=room_cancel.get()
                                                                        type_can=room_type_entry.get()
                                                                        print(name_can,type_can,room_can)
                                                                        if(len(name_cancel.get())!=0) and (len(room_type_entry.get())!=0) and ((len(room_type_entry.get())!=0)):
                                                                            print("ENTERED TO SELECTION")
                                                                            sql3="""select G_NAME,R_TYPE,R_NO FROM BOOKING_DETAILS WHERE G_NAME=:name_can and R_TYPE=:type_can and R_NO=:room_can"""
                                                                            cur.execute(sql3,[name_can,type_can,room_can])
                                                                            row=cur.fetchall()
                                                                            print(row)
                                                                            if(row):
                                                                                    print("ENTERED TO IF")
                                                                                    insertion_unc="""INSERT INTO CHECKING_TABLE_3
                                                                                    SELECT * FROM OCCUPIED
                                                                                    WHERE ROOM_NO=:room_num1"""
                                                                                    cur.execute(insertion_unc,[room_num1])
                                                                                    conn.commit()
                                                                                    print("data_copied_successfully")

                                                                                    sql4="""DELETE FROM BOOKING_DETAILS WHERE G_NAME=:name_can and R_TYPE=:type_can and R_NO=:room_can"""
                                                                                    cur.execute(sql4,[name_can,type_can,room_can])
                                                                                    print("DELETED BOOKING_DETAILS SUCCESSFULLY")
                                                                                    
                                                                                    deletion_unc="""DELETE FROM OCCUPIED
                                                                                    WHERE ROOM_NO=:room_num1"""
                                                                                    cur.execute(deletion_unc,[room_num1])
                                                                                    conn.commit()
                                                                                    print("DELETED SUCCESSFULLY")

                                                                                    conn.commit()
                                                                                    
                                                                            
                                                                            done_label=Label(top_cancel,text="CANCELLATION IS SUCCESSFULLY DONE!!!")
                                                                            done_label.grid(row=30,column=10)
                                                                            money_label=Label(top_cancel,text="YOUR AMOUNT WILL BE TRANSFERED TO YOUR ACCOUNT WITHIN 2 DAYS!!")
                                                                            money_label.grid(row=35,column=10)
                                                                        
                                                                    flag_cancel=[True]*5;
                                                                    name_cancel_entry=Label(top_cancel,text="ENTER YOUR NAME PLEASE!!")
                                                                    name_cancel_entry.grid(row=0,column=0)
                                                                    name_cancel=Entry(top_cancel,justify=LEFT,width=40)
                                                                    name_cancel.grid(row=0,column=1,padx=50,pady=50)
                                                                    room_type_cancel=Label(top_cancel,text="ENTER THE TYPE OF ROOM")
                                                                    room_type_cancel.grid(row=1,column=0)
                                                                    room_type_entry=Entry(top_cancel,justify=LEFT,width=40)
                                                                    room_type_entry.grid(row=1,column=1,padx=50,pady=50)
                                                                    room_cancel_entry=Label(top_cancel,text="ENTER THE ROOM_NUMBER YOU BOOKED")
                                                                    room_cancel_entry.grid(row=2,column=0)
                                                                    room_cancel=Entry(top_cancel,justify=LEFT,width=40)
                                                                    room_cancel.grid(row=2,column=1,padx=50,pady=50)
                                                                    submit_cancel=Button(top_cancel,text="SUBMIT FOR CANCEL",command=ex,padx=20,pady=20)
                                                                    submit_cancel.grid(row=3,column=1)
                                                                    

                                                                bill1=Label(top10,text="PAYMENT_DETAILS",font="times 20 bold")
                                                                bill1.grid(row=0,column=1)
                                                                
                                                                type1=Label(top10,text="ROOM TYPE:         "+str(type_room),font="times 20 bold")
                                                                type1.grid(row=2,column=0)

                                                                type15=Label(top10,text="ROOM NUM:         "+str(room_num1),font="times 20 bold")
                                                                type15.grid(row=3,column=0)

                                                                type14=Label(top10,text="DATE OF ENTRY:    "+str(date_of_entry),font="times 20 bold")
                                                                type14.grid(row=4,column=0)

                                                                type15=Label(top10,text="DATE OF EXIT:     "+str(date_of_exit),font="times 20 bold")
                                                                type15.grid(row=6,column=0)


                                                                type2=Label(top10,text="ROOM COST:         "+str(cost_room),font="times 20 bold")
                                                                type2.grid(row=8,column=0)

                                                                type3=Label(top10,text="NO OF BOOKINGS:    "+str(numb),font="times 20 bold")
                                                                type3.grid(row=10,column=0)

                                                                type4=Label(top10,text="SPEND DAYS:        "+str(spend_days),font="times 20 bold")
                                                                type4.grid(row=12,column=0)

                                                                type5=Label(top10,text="TOTAL COST:        "+str(Total_cost),font="times 20 bold")
                                                                type5.grid(row=14,column=0)

                                                                type6=Label(top10,text="SERVICE TAX        "+str(GST),font="times 20 bold")
                                                                type6.grid(row=16,column=0)

                                                                type7=Label(top10,text="TOTAL AMOUNT:      "+str(Total_amount),font="times 20 bold")
                                                                type7.grid(row=18,column=0)

                                                                payment=['CREDIT CARD','DEBIT CARD']

                                                                payment1=StringVar()
                                                                payment1.set("CHOICE IS YOURS!")

                                                                type8=Label(top10,text="PAYMENT OPTIONS:",font="times 20 bold")
                                                                type8.grid(row=20,column=0)

                                                                type8_label=OptionMenu(top10,payment1,*payment)
                                                                type8_label.grid(row=21,column=0,columnspan=2,padx=20,pady=20)

                                                                
                                                                type10=Label(top10,text="ENTER YOUR ACCOUNT NUMBER:")
                                                                type10.grid(row=24,column=0)
                                                                
                                                                type11=Entry(top10,justify=LEFT,width=40,borderwidth=5)
                                                                type11.grid(row=24,column=1)

                                                        
                                                                type12=Label(top10,text="ENTER YOUR CVV:")
                                                                type12.grid(row=28,column=0)

                                                                type13=Entry(top10,justify=LEFT,width=40,borderwidth=5)
                                                                type13.grid(row=28,column=1)

                                                                check=Button(top10,text="SUBMIT>>",command=check1,padx=20,pady=20)
                                                                check.grid(row=32,column=2)
                                                                

                                                                    

                                                            vals=[True]*8;
                                                            if(type_room=="ROOMS"):
                                                                vals[0]=False;
                                                            numb=No_of_person.get()
                                                            print(numb)
                                                            if(type_room=="SINGLE_BED" and int(numb)>2):
                                                                print("Single can contain only 2 members")
                                                                vals[5]=False
                                                            if(type_room=="DOUBLE_BED" and int(numb)>4):
                                                                print("Double can contain only 4 members")
                                                                vals[6]=False
                                                            if(type_room=="SUITE_ROOM" and int(numb)>6):
                                                                print("Suites can contain only 6 members")
                                                                vals[7]=False
                                                            if(clicked_number.get()==0):
                                                                vals[1]=False;
                                                            if(car_parks.get()=="Choose!!"):
                                                                vals[2]=False;
                                                            if((clicked_1.get()!="DAYS") and (clicked.get()!="MONTHS") and (clicked_2.get()!="YEAR")):
                                                                date_of_entry=str(clicked_1.get())+"/"+str(clicked.get())+"/"+str(clicked_2.get())
                                                                print(date_of_entry)
                                                            else:
                                                                vals[3]=False;
                                                                print("ENTER THE DATE CORRECTLY")
                                                            if((dexit_1.get()!="DAYS") and (dexit_2.get()!="MONTH") and  (dexit_3.get()!="YEAR")):
                                                                date_of_exit=str(dexit_1.get())+"/"+str(dexit_2.get())+"/"+str(dexit_3.get())
                                                                print(date_of_exit)
                                                            else:
                                                                vals[4]=False
                                                                print("ENTER THE DATE OF EXIT CORRECTLY")
                                                            if((vals[1]==True) and (vals[2]==True) and (vals[3]==True) and (vals[4]==True) and (vals[0]==True) and (vals[5]==True) and (vals[6]==True) and (vals[7]==True)):
                                                                table_id="""SELECT G_ID FROM PERSONAL_3"""
                                                                cur.execute(table_id)
                                                                ids=cur.fetchall()
                                                                last_length=len(ids)
                                                                ids=ids[last_length-1]
                                                                f_date = date(int(clicked_2.get()),int(clicked.get()), int(clicked_1.get()))
                                                                l_date = date(int(dexit_3.get()),int(dexit_1.get()),int(dexit_2.get()))
                                                                delta = l_date - f_date
                                                                print(delta.days)
                                                                spend_days=delta.days
                                                                table_select_1="""SELECT ROOM_COST FROM CHECKING_TABLE_3 WHERE ROOM_TYPE =:type_room"""
                                                                cur.execute(table_select_1,[type_room])
                                                                room_cost=cur.fetchone()
                                                                print(room_cost)
                                                                cost_room=room_cost
                                                                Total_cost=room_cost*spend_days
                                                                Total_cost=sum(Total_cost)
                                                                GST=0.12*Total_cost;
                                                                Total_amount=Total_cost+GST
                                                                print(Total_amount)
                                                                next5=Button(top11,text="NEXT >>>>",padx=10,pady=10,command=bill)
                                                                next5.grid(row=10,column=3)



                                                        type1=Label(top11,text="SELECT THE ROOM_TYPE")
                                                        type1.grid(row=1,column=0)
                                                        ROOMS=["SINGLE_BED","DOUBLE_BED","SUITE_ROOM"]
                                                        clicked_room=StringVar()
                                                        clicked_room.set("ROOMS")
                                                        dropdown_room=OptionMenu(top11,clicked_room,*ROOMS,command=selected)
                                                        dropdown_room.grid(row=1,column=1,columnspan=2,padx=20,pady=20)

                                                        person=Label(top11,text="NUMBER OF PERSONS")
                                                        person.grid(row=2,column=0)

                                                        No_of_person=Entry(top11,justify=LEFT,width=40,borderwidth=5)
                                                        No_of_person.grid(row=2,column=1)

                                                        room_num2=Label(top11,text="ROOM_NUMBER")
                                                        room_num2.grid(row=3,column=0)

                                                        room_num=Entry(top11,justify=LEFT,width=40,borderwidth=5)
                                                        room_num.grid(row=3,column=1)
                                                        

                                                        DOE_label=Label(top11,text=" ENTRY DATE (YEAR) ")
                                                        DOE_label.grid(row=4,column=0)

                                                        DOE_label1=Label(top11,text=" ENTRY DATE (MONTH) ")
                                                        DOE_label1.grid(row=5,column=0)

                                                        DOE_label2=Label(top11,text=" ENTRY DATE (DAYS) ")
                                                        DOE_label2.grid(row=6,column=0)

                                                        DE_label=Label(top11,text=" EXIT DATE (YEAR) ")
                                                        DE_label.grid(row=7,column=0)

                                                        DE_label1=Label(top11,text=" EXIT DATE (MONTH) ")
                                                        DE_label1.grid(row=8,column=0)

                                                        DE_label2=Label(top11,text=" EXIT DATE (DAYS) ")
                                                        DE_label2.grid(row=9,column=0)

                                                        month=[k for k in range(1,13)]
                                                        days=[i for i in range(1,32)]
                                                        year=[i for i in range(2020,2025)]

                                                        clicked=StringVar()
                                                        clicked.set("MONTH")
                                                        clicked_1=StringVar()
                                                        clicked_1.set("DAYS")
                                                        clicked_2=StringVar()
                                                        clicked_2.set("YEAR")
                                                        dexit_1=StringVar()
                                                        dexit_1.set("MONTH")
                                                        dexit_2=StringVar()
                                                        dexit_2.set("DAYS")
                                                        dexit_3=StringVar()
                                                        dexit_3.set("YEAR")


                                                        drop=OptionMenu(top11,clicked,*month)
                                                        drop.grid(row=5,column=1,columnspan=2,padx=20,pady=20)

                                                        drop_1=OptionMenu(top11,clicked_1,*days)
                                                        drop_1.grid(row=6,column=1,columnspan=2,padx=20,pady=20)

                                                        drop_2=OptionMenu(top11,clicked_2,*year)
                                                        drop_2.grid(row=4,column=1,columnspan=2,padx=20,pady=20)

                                                        drop_3=OptionMenu(top11,dexit_1,*month)
                                                        drop_3.grid(row=8,column=1,columnspan=2,padx=20,pady=20)

                                                        drop_4=OptionMenu(top11,dexit_2,*days)
                                                        drop_4.grid(row=9,column=1,columnspan=2,padx=20,pady=20)

                                                        drop_5=OptionMenu(top11,dexit_3,*year)
                                                        drop_5.grid(row=7,column=1,columnspan=2,padx=20,pady=20)

                                                        cars=Label(top11,text=" DO YO WANNA ACCESS CAR PARKING ?")
                                                        cars.grid(row=10,column=0)

                                                        CAR_PARKING=["YES","NO"]
                                                        car_parks=StringVar()
                                                        car_parks.set("CHOOSE!!")
                                                        car=OptionMenu(top11,car_parks,*CAR_PARKING)
                                                        car.grid(row=10,column=1,columnspan=2,padx=20,pady=20)

                                                        submit_room=Button(top11,text=">>SUBMIT>>",command=final_result,padx=40,pady=40)
                                                        submit_room.grid(row=10,column=2)





                                                def checking1():
                                                    global alert_1,alert_2,alert_3,alert_4,alert_5,alert_6
                                                    pattern=re.compile("[0-9]{6}")
                                                    pattern1=re.compile("[0-9]{1}[/][0-9]{2}")
                                                    regex=re.compile("[a-zA-Z]+[]+[a-zA-Z]")
                                                    if pattern.match(zip.get())==None:
                                                        alert_1=Label(top6,text="ENTER THE CORRECT ZIPCODE")
                                                        alert_1.grid(row=8,column=1)
                                                        zip.delete(0,END)
                                                    
                                                    elif pattern1.match(Door_Nos.get())==None:
                                                        alert_1.destroy()
                                                        alert_2=Label(top6,text=" ENTER THE CORRECT DOOR NUMBER LIKE [1/2]")
                                                        alert_2.grid(row=8,column=1)
                                                        Door_Nos.delete(0,END)
                                                    
                                                    elif regex.match(streets.get())==None:
                                                        alert_2.destroy()
                                                        alert_3=Label(top6,text=" ENTER THE CORRECT AREA NAME")
                                                        alert_3.grid(row=8,column=1)
                                                        streets.delete(0,END)
                                                    elif regex.match(district.get())==None:
                                                        alert_3.destroy()
                                                        alert_4=Label(top6,text=" ENTER THE CORRECT DISTRICT NAME")
                                                        alert_4.grid(row=8,column=1)
                                                        district.delete(0,END)
                                                    elif regex.match(Area_Name.get())==None:
                                                        alert_4.destroy()
                                                        alert_5=Label(top6,text=" ENTER THE CORRECT AREA NAME")
                                                        alert_5.grid(row=8,column=1)
                                                        Area_Name.delete(0,END)
                                                    else:
                                                        bud=Button(top6,text="NEXT >>>>",command=types_of_room,padx=20,pady=20)
                                                        bud.grid(row=8,column=1)
                                                        area=Area_Name.get()
                                                        dis=district.get()
                                                        state1=cli.get()
                                                        count=cli1.get()
                                                        sql_check="""SELECT * FROM PERSONAL_3"""
                                                        cur.execute(sql_check)
                                                        row=cur.fetchall()
                                                        row_length=(len(row))+100
                                                        g_id="G"+str(row_length)+"PMB"+str(clicked_1.get())
                                                        print(g_id)

                                                        cur.execute("INSERT INTO PERSONAL_3 (G_ID,G_NAME,G_AGE,G_PHONE,G_EMAIL,G_DOB,G_AREA_NAME,G_DISTRICT,G_STATE,G_COUNTRY) VALUES (:G_ID,:G_NAME,:G_AGE,:G_PHONE,:G_EMAIL,TO_DATE(:G_DOB,'DD/MM/YYYY'),:G_AREA_NAME,:G_DISTRICT,:G_STATE,:G_COUNTRY)",
                                                                    {
                                                                            'G_ID':g_id,
                                                                            'G_NAME':name_in,
                                                                            'G_AGE':age_in,
                                                                            'G_PHONE':phone_in,
                                                                            'G_EMAIL':email_in,
                                                                            'G_DOB':date_var_1,
                                                                            'G_AREA_NAME':area,
                                                                            'G_DISTRICT':dis,
                                                                            'G_STATE':state1,
                                                                            'G_COUNTRY':count
                                                                            }
                                                                    )
                                                        
                                                        print("DATA INSERTED SUCCESSFULLY")
                                                        conn.commit()




                                                    
                                                Door_Nos=Entry(top6,width=60,borderwidth=10)
                                                Door_Nos.grid(row=0,column=1,padx=50,pady=50)

                                                streets=Entry(top6,width=60,borderwidth=10)
                                                streets.grid(row=1,column=1,padx=50,pady=50)

                                                Area_Name=Entry(top6,width=60,borderwidth=10)
                                                Area_Name.grid(row=2,column=1,padx=50,pady=50)

                                                district=Entry(top6,width=60,borderwidth=10)
                                                district.grid(row=3,column=1,padx=50,pady=50)

                                                zip=Entry(top6,width=60,borderwidth=10)
                                                zip.grid(row=4,column=1,padx=50,pady=50)

                                                Door_No=Label(top6,text=" ENTER DOOR NO ")
                                                Door_No.grid(row=0,column=0)

                                                street_name=Label(top6,text=" ENTER STREET NAME ")
                                                street_name.grid(row=1,column=0)

                                                Area_name=Label(top6,text=" ENTER AREA NAME ")
                                                Area_name.grid(row=2,column=0)

                                                District=Label(top6,text=" ENTER THE DISTRICT ")
                                                District.grid(row=3,column=0)

                                                zipcode=Label(top6,text=" ZIP CODE ")
                                                zipcode.grid(row=4,column=0)

                                                state=Label(top6,text=" ENTER STATE ")
                                                state.grid(row=5,column=0)

                                                country=Label(top6,text= " ENTER COUNTRY ")
                                                country.grid(row=6,column=0)

                                                submit=Button(top6,text=" SUBMIT => ",command=checking1)
                                                submit.grid(row=7,column=1)

                                                states=['Andhra Pradesh','Arunachal Pradesh','Assam','Bihar','Chhattisgarh','Goa,Gujarat','Haryana','Himachal Pradesh','Jammu and Kashmir','Jharkhand','Karnataka','Kerala','Madhya Pradesh','Maharashtra','Manipur','Meghalaya','Mizoram','Nagaland','Odisha','Punjab','Rajasthan','Sikkim','Tamil Nadu','Telangana','Tripura','Uttar Pradesh','Uttarakhand','West Bengal','Andaman and Nicobar','Chandigarh','Dadra and Nagar Haveli','Daman and Diu','Lakshadweep','Delhi','Puducherry']
                                                countries=['INDIA','other']

                                                cli=StringVar()
                                                cli.set(states[0])

                                                drop=OptionMenu(top6,cli,*states)
                                                drop.grid(row=5,column=1)

                                                cli1=StringVar()
                                                cli1.set(countries[0])

                                                drop1=OptionMenu(top6,cli1,*countries)
                                                drop1.grid(row=6,column=1)


                                        #sql="""CREATE TABLE PERSONAL_3(G_ID VARCHAR2(30) PRIMARY KEY,G_NAME VARCHAR2(40),G_AGE NUMBER,G_PHONE VARCHAR2(11),G_EMAIL VARCHAR2(30),G_DOB DATE,G_AREA_NAME varchar2(30),G_DISTRICT varchar2(30),G_STATE varchar2(30),G_COUNTRY varchar2(30))"""
                                        #cur.execute(sql)

                                        def checking():
                                            n=name_entry.get()
                                            age_1=(age_entry.get())
                                            global warn_1,warn_2,warn_3,warn_4,na_label,name_in,age_in,phone_in,email_in,date_var_1

                                            flags=[True]*5
                                            try:
                                                 if int(age_1) < 0 or int(age_1) >100:
                                                  age_entry.delete(0,END)
                                                  warn_1=Label(top7,text="ENTER THE CORRECT AGE")
                                                  warn_1.grid(row=15,column=1)
                                                  flags[0]=False
                                            except:
                                                  flags[0]=False
                                                  warn_1=Label(top7,text="ENTER THE CORRECT AGE")
                                                  warn_1.grid(row=15,column=1)
                                                  age_entry.delete(0,END)
                                            if(len(name_entry.get())==0):
                                               na_label=Label(top7,text="PLEASE ENTER THE NAME")
                                               flags[1]=False
                                               na_label.grid(row=10,column=1)
                                            #finally:
                                            #       na_label=Label(root,text="WELCOME "+name_entry.get()+" HAVE A NICE DAY!" )
                                            #       na_label.grid(row=10,column=1)
                                            Pattern = re.compile("(0/91)?[7-9][0-9]{9}") 
                                            if Pattern.match(phone_entry.get())==None:
                                                warn_2=Label(top7,text="ENTER THE CORRECT NUMBER:")
                                                flags[2]=False 
                                                warn_2.grid(row=11,column=1)
                                                phone_entry.delete(0,END)
                                            regex=re.compile("^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$")
                                            if regex.match(email_entry.get())==None:
                                                  warn_3=Label(top7,text="ENTER THE CORRECT MAIL_ID:")
                                                  warn_3.grid(row=13,column=1)
                                                  flags[3]=False
                                                  email_entry.delete(0,END) 
                                            ## FOR DATE:
                                            try:
                                                mylabel=Label(top7,text="the date is "+str(clicked.get())+"/"+str(clicked_1.get())+"/"+str(clicked_2.get()))
                                                mylabel.grid(row=30,column=2)
                                            except:
                                                  flags[4]=False
                                                  warn_4=Label(top7,text="PLEASE ENTER THE DATE CORRECTLY!!",fg="red")
                                                  warn_4.grid(row=29,column=2)
                                            if(flags[0]==True and flags[1]==True and flags[2]==True and flags[3]==True and flags[4]==True):
                                                date_var_1=str(clicked_1.get())+"/"+str(clicked.get())+"/"+str(clicked_2.get())
                                                print(date_var_1)
                                                confirm_label=Label(top7,text="CLICK ON NEXT BUTTON TO PROCEED")
                                                confirm_label.grid(row=60,column=10)
                                                N_b=Button(top7,text=">>NEXT>>",command=address_book)
                                                N_b.grid(row=65,column=10)
                                                name_in=name_entry.get()
                                                age_in=age_entry.get()
                                                phone_in=phone_entry.get()
                                                email_in=email_entry.get()


                                        ## lets create buttons and text boxes:
                                        name_label=Label(top7,text="ENTER THE NAME")
                                        name_label.grid(row=1,column=0)
                                        age_label=Label(top7,text="ENTER THE AGE")
                                        age_label.grid(row=2,column=0)
                                        name_entry=Entry(top7,width=60,borderwidth=10)
                                        age_entry=Entry(top7,width=60,borderwidth=10)
                                        phone_label=Label(top7,text="ENTER THE PHONE_NUMBER")
                                        phone_label.grid(row=3,column=0)
                                        phone_entry=Entry(top7,width=60,borderwidth=10)
                                        email_label=Label(top7,text="ENTER THE MAIL_ID:")
                                        email_label.grid(row=4,column=0)
                                        email_entry=Entry(top7,width=60,borderwidth=10)
                                        submit=Button(top7,text="SUBMIT->",command=checking,padx=40,pady=30,width=20)
                                        submit.grid(row=7,column=1)     
                                        ## lets display that:

                                        name_entry.grid(row=1,column=1,padx=50,pady=50)

                                        age_entry.grid(row=2,column=1,padx=50,pady=50)

                                        phone_entry.grid(row=3,column=1,padx=50,pady=50)

                                        email_entry.grid(row=4,column=1,padx=50,pady=50)

                                        ## date drop down boxes:
                                        ## if there are more items that needs to be present in the box .... then..we can put it in the list:

                                        month=[k for k in range(1,13)]
                                        days=[i for i in range(1,32)]
                                        year=[i for i in range(1950,2021)]
                                        year.reverse()
                                        ## drop_down boxes:

                                        clicked=IntVar()
                                        clicked.set("MONTH")
                                        clicked_1=IntVar()
                                        clicked_1.set("DAYS")
                                        clicked_2=IntVar()
                                        clicked_2.set("YEAR")
                                        ##

                                        drop=OptionMenu(top7,clicked,*month)
                                        drop.grid(row=5,column=0)
                                        drop_1=OptionMenu(top7,clicked_1,*days)
                                        drop_1.grid(row=5,column=1)
                                        drop_2=OptionMenu(top7,clicked_2,*year)
                                        drop_2.grid(row=5,column=2)

                                        #mybutton=Button(root,text="show selection",command=checking)
                                        #mybutton.grid(row=22,column=5)



                                ## BUTTONS
                                rec_button=Button(top_int,text="RECEPTION",padx=40,pady=30,width=20,command=click_rec,relief=GROOVE)
                                wait_button=Button(top_int,text="LOBBY_01",padx=40,pady=30,width=20,command=lounge_1,relief=GROOVE)
                                wait_button_1=Button(top_int,text="LOBBY_02",padx=40,pady=30,width=20,command=lounge_2,relief=GROOVE)
                                rec_button.grid(row=4,column=10)
                                wait_button.grid(row=4,column=11)
                                wait_button_1.grid(row=4,column=12)
                 
                                ## single_room:
                                sin_button=Button(top_int,text="ROOM",padx=40,pady=30,width=20,command=room_1,relief=GROOVE)
                                sin_button_2=Button(top_int,text="BATHROOM",padx=40,pady=30,width=20,command=bath_1,relief=GROOVE)
                                sin_button_3=Button(top_int,text="VIEWS",padx=40,pady=30,width=20,command=view_1,relief=GROOVE)
                                sin_button.grid(row=7,column=10)
                                sin_button_2.grid(row=7,column=11)
                                sin_button_3.grid(row=7,column=12)

                                ## DOUBLE_ROOM:
                                dub_button=Button(top_int,text="ROOM",padx=40,pady=30,width=20,command=room_2,relief=GROOVE)
                                dub_button_2=Button(top_int,text="BATHROOM",padx=40,pady=30,width=20,command=bath_2,relief=GROOVE)
                                dub_button_3=Button(top_int,text="VIEWS",padx=40,pady=30,width=20,command=views_2,relief=GROOVE)
                                dub_button.grid(row=10,column=10)
                                dub_button_2.grid(row=10,column=11)
                                dub_button_3.grid(row=10,column=12)
                                
                                ##suite rooms:
                                sui_button=Button(top_int,text="ROOM",padx=40,pady=30,width=20,command=suite_room,relief=GROOVE)
                                sui_button_2=Button(top_int,text="BATHROOM",padx=40,pady=30,width=20,command=suite_bath,relief=GROOVE)
                                sui_button_3=Button(top_int,text="VIEWS",padx=40,pady=30,width=20,command=view_suit,relief=GROOVE)
                                sui_button.grid(row=13,column=10)
                                sui_button_2.grid(row=13,column=11)
                                sui_button_3.grid(row=13,column=12)

                                butt=Button(top_int,text="NEXT",padx=40,pady=30,width=20,command=nextt)
                                butt.grid(row=14,column=18,columnspan=3)
                          

                        button10=Button(top4,text="ANJUNA BEACH",padx=40,width=25,pady=50,command=myclick19)
                        button11=Button(top4,text="BOGDESHWARA",padx=40,width=25,pady=50,command=myclick20)
                        button12=Button(top4,text="BICHOLIM",padx=40,width=25,pady=50,command=myclick21)
                        button13=Button(top4,text="CLUB CABANA",padx=40,width=25,pady=50,command=myclick22)
                        button14=Button(top4,text="BOM-JESUS-BASILICA",padx=40,width=25,pady=50,command=myclick23)
                        button15=Button(top4,text="COCO BEACH",padx=40,width=25,pady=50,command=myclick24)
                        button16=Button(top4,text="VAIGUINIM BEACH",padx=40,width=25,pady=50,command=myclick25)
                        button17=Button(top4,text="BUTTERFLY BEACH",padx=40,width=25,pady=50,command=myclick26)
                        button18=Button(top4,text="DONA-PAULA-BEACH",padx=40,width=25,pady=50,command=myclick27)
                        button19=Button(top4,text="NEXT >>",padx=40,width=25,pady=40,command=interiors)

                        button10.grid(row=1,column=0)
                        button11.grid(row=1,column=1)
                        button12.grid(row=1,column=2)
                        button13.grid(row=2,column=0)
                        button14.grid(row=2,column=1)
                        button15.grid(row=2,column=2)
                        button16.grid(row=3,column=0)
                        button17.grid(row=3,column=1)
                        button18.grid(row=3,column=2)
                        button19.grid(row=4,column=2)

                        
                button0=Button(top2,text="PALM RESORTS GOA",padx=40,width=25,pady=50,command=myclick10,bg="dimgray",fg="white")
                button1=Button(top2,text="OUTER",padx=40,width=25,pady=50,command=myclick11,bg="cyan",fg="black")
                button2=Button(top2,text="SWIMMING POOL",padx=40,width=25,pady=50,command=myclick12,bg="dimgray",fg="white")
                button3=Button(top2,text="BEACH NEAR RESORT",padx=40,width=25,pady=50,command=myclick13,bg="cyan",fg="black")
                button4=Button(top2,text="TOP VIEW",padx=40,width=25,pady=50,command=myclick14,bg="dimgray",fg="white")
                button5=Button(top2,text="ENTRANCE VIEW",padx=40,width=25,pady=50,command=myclick15,bg="cyan",fg="black")
                button6=Button(top2,text="FAMOUS PLACE",padx=40,width=25,pady=50,command=myclick16,bg="dimgray",fg="white")
                button7=Button(top2,text="MAP VIEW",padx=40,width=25,pady=50,command=myclick17,bg="cyan",fg="black")
                button8=Button(top2,text="PARK VIEW",padx=40,width=25,pady=50,command=myclick18,bg="dimgray",fg="white")
                button9=Button(top2,text="NEXT >>",padx=40,width=25,pady=40,command=next1,bg="white")

                button0.grid(row=1,column=0)
                button1.grid(row=1,column=1)
                button2.grid(row=1,column=2)
                button3.grid(row=2,column=0)
                button4.grid(row=2,column=1)
                button5.grid(row=2,column=2)
                button6.grid(row=3,column=0)
                button7.grid(row=3,column=1)
                button8.grid(row=3,column=2)
                button9.grid(row=4,column=2)
                

                
 
        u_name=name1.get()
        u_user=user1.get()
        u_pass=password1.get()
        myLabel.destroy()

        lab1="""select * from signup2 where name=:u_name and username=:u_user and password=:u_pass"""
        cur.execute(lab1,[u_name,u_user,u_pass])
        row=cur.fetchone()
        try:
            if((u_name==str(row[0])) and (u_user==str(row[1])) and (u_pass==str(row[2]))):
                   myLabel=Label(root,text="WELCOME TO THE PALM RESORTS:",fg="BLUE")
                   myLabel.grid(row=3,column=1)
                   NEXT=Button(root,text="NEXT WINDOW",command=Next)
                   NEXT.grid(row=3,column=2)
            
        except TypeError:
            NEXT.destroy()
            myLabel=Label(root,text="USERNAME AND THE PASSWORD DOESNT MATCH")
            myLabel.grid(row=3,column=1)
            name1.delete(0,END)
            user1.delete(0,END)
            password1.delete(0,END)
            

name1=Entry(root,width=60,borderwidth=10)
name1.grid(row=0,column=1,padx=50,pady=50)

user1=Entry(root,width=60,borderwidth=10)
user1.grid(row=1,column=1,padx=50,pady=50)

password1=Entry(root,width=60,borderwidth=10)
password1.grid(row=2,column=1,padx=50,pady=50)

def submit():
    global top
    top=Toplevel()
    top.title("RESORTS BOOKER: SIGN UP PAGE")
    top.geometry("800x600")
    top1=Label(top,text="SIGN UP FOR RESORTS BOOKER")
    top1.grid(row=0,column=0)
    top.configure(bg="bisque")
    global mylabel
    global click

    def signing_up():
        global mylabel
        global click

        name_n=name2.get()
        name_u=user2.get()
        name_pass=password2.get()
        if(len(name_n)!=0  and len(name_u)!=0 and len(name_pass)!=0):
                cur.execute("INSERT INTO signup2 VALUES(:name2,:user2,:password2)",
                        {
                            'name2': name2.get(),
                            'user2': user2.get(),
                            'password2': password2.get()
                        })
                conn.commit()
                mylabel=Label(top,text=" YOUR ACCOUNT HAS BEEN ADDED ! GO TO LOGIN PAGE")
                mylabel.grid(row=4,column=1,pady=20,padx=50)
                click=Button(top,text="[CLICK]",command=top.destroy)
                click.grid(row=4,column=2,pady=20,padx=50)
        else:
                mylabel=Label(top,text=" YOUR ACCOUNT NOT ADDED ")
                mylabel.grid(row=4,column=1,pady=20,padx=50)
            
        name2.delete(0,END)
        user2.delete(0,END)
        password2.delete(0,END)

    # creating entry boxes:
    name2=Entry(top,width=60,borderwidth=10)
    name2.grid(row=1,column=1,padx=50,pady=50)

    user2=Entry(top,width=60,borderwidth=10)
    user2.grid(row=2,column=1,padx=50,pady=50)

    password2=Entry(top,width=60,borderwidth=10)
    password2.grid(row=3,column=1,padx=50,pady=50)

    # creating label:
    name2_label=Label(top,text="NAME")
    name2_label.grid(row=1,column=0)

    user2_label=Label(top,text="USERNAME")
    user2_label.grid(row=2,column=0)

    password2_label=Label(top,text="PASSWORD")
    password2_label.grid(row=3,column=0)

    sign_up1=Button(top,text="SIGN UP",command=signing_up)
    sign_up1.grid(row=4,column=0,pady=20,padx=50)


    
#creating label:

name_label=Label(root,text="NAME")
name_label.grid(row=0,column=0)

user_label=Label(root, text="USERNAME")
user_label.grid(row=1,column=0)

password_label=Label(root, text="PASSWORD")
password_label.grid(row=2,column=0)

#creating Button:
log_in=Button(root,text="LOG IN",command=submit1,bg="red",fg="white")
log_in.grid(row=3,column=0,pady=20,padx=50)

sign_up=Button(root,text="NOT HAVING ACCOUNT IN RESORTS BOOKER!",command=submit)
sign_up.grid(row=4,column=1,pady=20,padx=50)

mainloop()
