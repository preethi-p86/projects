#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstdlib>
#include <conio.h>
#include <cstring>
#include <time.h>
#include <windows.h>
#include <limits>
#include <string>
#include <sstream>
#include <iomanip>

#define MAX_SEATS 33

using namespace std;

void repeat(char ch);
void processing();

class BUS;                    //base
class AC_BUS;                 //derived of BUS
class NON_AC;                 //derived of BUS
class Sleeper_AC;             //derived of AC_BUS
class Sleeper_NON_AC;         //derived of NON_AC
class Non_Sleeper_AC;         //derived of AC_BUS
class Non_Sleeper_NON_AC;     //derived of NON_AC

template<typename U>
U amtcalc(U rate,double taxrate)
{
    return(taxrate*rate);
}

class BUS
{
    // members
    // default private
protected:
    char *name;
    string from_place,destination,bus_no1,date,time1;
    int *seat1;
    int tickets;
    char name1[20][20];
    float o=0;
    int tax=0,rate=0,amount1=0,count=0,tax1=0;

    char *seat_no[MAX_SEATS]={"DRIVER","EMPTY","EMPTY","EMPTY","EMPTY","EMPTY","EMPTY","EMPTY","EMPTY","EMPTY","EMPTY","EMPTY",
    "EMPTY","EMPTY","EMPTY","EMPTY","EMPTY","EMPTY","EMPTY","EMPTY","EMPTY","EMPTY","EMPTY","EMPTY","EMPTY","EMPTY","EMPTY",
    "EMPTY","EMPTY","EMPTY","EMPTY","EMPTY","EMPTY"};
    char *arr[8] = {"a7#*1&5","6Df%4$1","tS7*%1v","D3*&n1#","5%6g*(1","6o#0)1*","a4%&yUj","f#$tG&1"};

public:
    BUS(int i=0)
    {
        this->tax = this->rate = this->amount1 = i;

        try
        {
          name = new char[25];
 // allocate character array
        }
        catch(bad_alloc xa)
        {
            cout<<"Allocatation Failure"<<endl;
        }
        try
        {
            seat1 = new int[10];
        }
        catch(bad_alloc xa)
        {
            cout<<"Allocation Failure"<<endl;
        }
    }

    ~BUS()
    {
        delete []name;
        delete []seat1;
    }

    int login(char,char*,char*);
    char* password_login(char);
    void get_details();
    string from_desti(char);
    void seat_alloted();
    void Booking_Process();
    void bus_routes();
    int Capcan(int); //CAPTCHA-CANCELLATION(FUNCTION OVERLOADING)
    void Capcan();
    void Modification();
    void ratings();
    void view_ratings();
    void booked();
    void validation(char name[]);
    void num_validation();
    void tick_valid(char d1[]);

    virtual void online_transaction()
    {
        cout<<"\n\n\t\t\t THE AMOUNT DETAILS\n\n";
        tax1=tax;
        cout<<"\n\t\t\t Rate for individual person : "<<rate<<"\n\t\t\t Tax per ticket : "<<tax;
        cout<<"\n\t\t\t Number of tickets : "<<tickets<<endl<<endl;
        Sleep(2000);
        amount1 = (rate + tax)*tickets;
        cout<<"\n\t\t\t The Total amount is Rs. "<<amount1<<endl<<endl;
        Sleep(2000);
        repeat('*');
        cout<<"\n\t\t\t ONLINE TANSACTIONS\n\n";
        repeat('*');
        char d1[4];
        char ch;
        cout<<"\n\n\t\t\t 1. GOOGLE PAY\n\t\t\t 2. PAYTM\n\t\t\t 3. PHONE PE\n\t\t\t 4. CREDIT CARD\n\t\t\t 5. DEBIT CARD\n\n";
        cout<<"\t\t\t Enter your choice !\n\n";
        scanf(" %[^\n]s",d1);
        while((strlen(d1)!=1) ||(!(d1[0]>='1' && d1[0]<='5')))
	    {
				cout<<"\t\t\t\tRe_enter the option:"<<endl;
				cout<<"\t\t";
				scanf(" %[^\n]s",d1);
	    }
        ch=d1[0];
        cout<<endl<<endl;
        int k,j=0,cap1=0;
        char acct_no[12],cvv[5];

        while(j==0)
        {
            if(ch=='4' || ch=='5')
            {
                cout<<"Enter your Account number : ";
                cin>>acct_no;
                while(strlen(acct_no)!=10)
                {
                    cout<<"\n\n\t\t\t The Account number should have 10 digits\n\nRe enter valid Account number\n\n\t\t\t ";
                    cin>>acct_no;
                }
                cout<<"\n\n\t\t\t Enter cvv\n\n\t\t\t ";
                cin>>cvv;
                while(strlen(cvv)!=3)
                {
                    cout<<"A cvv should have 3 digits\n\nRe enter valid cvv\n\n\t\t\t";
                    cin>>cvv;
                }
                processing();
            }

                srand(time(NULL));
                cap1= rand()%7;  // 0 to 7 random numbers
                k=Capcan(cap1);
                if(k==0)
                    cout<<"\t\t\t ONLINE TRANSACTION UNSUCCESSFUL !\n\nDO IT ONCE AGAIN !!";
                else if (k==1)
                {
                    j=1;
                    processing();
                    cout<<"\n\n\t\t\t The Amount of Rs. "<<amount1<<" has been debited.\n\n\t\t\t ";
                    cout<<"Enjoy your journey !\n\n\t\t\t ";
                }
        }
    }
};

int BUS :: login(char c2='0', char x[30]="MAKE MY TRIP", char y[25]="F#456")
{
    char login_id[30],password[25];
    char log[30],pass[25];
    int i=5,cap;

    // c2==1 - change password, c2==2 - change both login id & password, c2==0 - default parameters act as login id, password

    if (c2=='0')
    {
        strcpy(log,x);
        strcpy(pass,y);
    }
    else if (c2=='1' || c2=='2')
    {
        Sleep(2000);
        system("cls");
        cout<<endl<<endl;
        srand(time(NULL));
        cap = rand()%7; // random numbers from 0 to 7
        cout<<"\n\t\t\t "<<arr[cap];
        char type[8];
        cout<<"\n\n\nInput the captcha you see on the screen\n\n\t\t\t ";
        scanf(" %[^\n]*c",type);

        if(strcmp(type,arr[cap])!=0)
        {
            cout<<"You have an another chance to re enter captcha\n\t\t\t ";
            scanf(" %[^\n]*c",type);
            if(strcmp(type,arr[cap])!=0)
            {
                cout<<"You have No Permission to login\n\n";
                exit(1);
            }
        }
        Sleep(1000);
        system("cls");
        if(c2=='1')
        {
            cout<<"\n\n\t\t\t Enter new Password : ";
            strcpy(pass,password_login(c2));
            strcpy(log,x);
            cout<<"\n\nNew Password Updated !\n\n";
        }
        else if(c2=='2')
        {
            cout<<"\n\n\t\t\t Enter New Login id : ";
            scanf(" %[^\n]s",log);
            cout<<"\n\n\t\t\t Enter new Password : ";
            strcpy(pass,password_login(c2));
            cout<<"\n\nNew Login ID and Password Updated !\n\n";
        }
        int j=0;
        char c;
        cout<<"\n\nDo you want to view your password :\nPress 1 to view.\nPress any other digit to move\n";
        cin>>j;
        if(j==1)
            cout<<"YOUR PASSWORD IS : "<<pass<<endl;
        cout<<"\n\nPRESS ANY KEY TO CONTINUE\n\n";
        cin>>c;
        system("cls");
    }
    else
        return 0;

    do
    {
        system("cls");
        system("color 2F");
        c2='5';
        cout<<"\n\n\n\n\n\t\t\tLogin ID : ";
        scanf(" %[^\n]s",login_id);
        cout<<"\n\t\t\tPassword : ";
        strcpy(password,password_login(c2));

        if(strcmp(log,login_id)==0 && strcmp(pass,password)==0)
            return 1;
        else
        {
            if(strcmp(login_id,log)!=0)
                cout<<"Invalid login Id\n";
            else if (strcmp(password,pass)!=0)
                cout<<"Invalid password\n";

            if(i>2)
                cout<<"You have "<<i-1<<" chances left\n\n";
            else
                cout<<"You have "<<i-1<<" chance left\n\n";
            Sleep(2000);
            system("cls");
            i--;
        }
    } while(i!=0);

    cout<<"INVALID ATTEMPT MORE THAN 5 TIMES\n\n";
    return 0;
}

char* BUS:: password_login(char c2)
{
    char pass_temp[25];
    int j=0,k=1;
    char ab;

    while(k==1)
    {
        for(j=0;;)
        {
            ab=getch();
            if(ab>31 && ab<126)
            {
                pass_temp[j]=ab;
                ++j; // letter count
                cout<<"*";
            }
            if(ab=='\b' && j>0)
            {
                cout<<"\b \b";
                --j;
            }
            if(ab=='\r')
            {
                pass_temp[j]='\0';
                break;
            }
        }
        if(c2=='1' || c2=='2')
        {
            if(strlen(pass_temp)<5)
            {
                k=1;
                cout<<"\n\nRe enter password\nA strong password should have at least 5 characters\n\n";
            }
            else
            {
                k=0;
                return pass_temp;
            }
        }
        else
        {
            return pass_temp;
        }
    }
}


int BUS :: Capcan(int cap1)
{
    int i=0;
    char type[8];
    cout<<"\n\n\t\t\t"<<arr[cap1];
    cout<<"\n\nEnter the above captcha : ";
    cin>>type;
    while(strcmp(type,arr[cap1])!=0 && i!=3)
    {
        cout<<"\n\n\t\t\t Enter again\t\t\t ";
        cin>>type;
        i++;
    }
    if(strcmp(type,arr[cap1])!=0)
    {
        cout<<"Your turn is over\n\nTry again!\n\n\n";
        return 0;
    }
    return 1;
}

void repeat(char ch)
{
    int i;
    cout<<endl<<endl;
    for(i=0;i<80;i++)
       cout<<ch;
    cout<<endl<<endl;
}

void processing()
{
    cout<<endl<<endl;
    for(int i=0;i<35;i++)
        cout<<".";
    cout<<"PROCESSING";
    for(int i=0;i<35;i++)
        cout<<".";
    cout<<endl<<endl;
}

string BUS :: from_desti(char t1)
{
    int i=0;
    string word="no_name";
    while(i==0)
    {
        if(t1=='1' || t1=='2' || t1=='3' || t1=='4' || t1=='5')
        {
            i=1;
            if (t1=='1')
                word = "CHENNAI";
            else if (t1=='2')
                word = "BANGALORE";
            else if (t1=='3')
                word = "HYDERABAD";
            else if (t1=='4')
                word = "COCHIN";
            else if (t1=='5')
                word = "AMARAVATI";
            }
            else
                cout<<"\t\t\tInvalid Place\n\n\n\t\t\tRe enter again\n";
    }
    return word;
}
void BUS ::validation(char name[])
{
	int i,not_alpha=0,first_second=0;
	do
    {
        if(not_alpha!=0 || first_second!=0)
        {
            cout<<"\n\t\t\tName should contain only alphabets, spaces and full stop.\n\t\t\tName should have at least two letters.\n\t\t\tThe first two letters of the name should be Letters only.\n\n";
            cout<<"\t\t\tRe enter valid name\n\t\t\t";
            scanf(" %[^\n]s",name);
            cout<<endl;
        }

        not_alpha=0,first_second=0;

        for(i=0;i<strlen(name);i++)
        {
            if((!(name[i]>='a' && name[i]<='z') && !(name[i]>='A' && name[i]<='Z')) && (name[i]!=' ') && (name[i]!='.'))
                not_alpha++;
        }

        if ((!(name[0]>='a' && name[0]<='z') && !(name[0]>='A' && name[0]<='Z')) || (!(name[1]>='a' && name[1]<='z') && !(name[1]>='A' && name[1]<='Z')))
            first_second++;

    }while(not_alpha!=0 || first_second!=0);

}

 void BUS :: get_details()
{
    char d1[10];
    int i,not_alpha=0,first_second=0;
	Sleep(2000);
    cout<<"\n\n\n\n\n\t\t\t Enter name\n\n\t\t\t ";
    scanf(" %[^\n]s",name);
    validation(name);
    char t1;
    do
    {
        cout<<"\n\n\t\t\t Leaving from :\n\n\t\t\t 1. CHENNAI\n\n\t\t\t 2. BANGALORE\n\n\t\t\t 3. HYDERABAD\n\n\t\t\t 4. COCHIN\n\n\t\t\t 5. AMARAVATI\n\n\n\t\t\t";
        scanf(" %[^\n]s",d1);
        while((strlen(d1)!=1) ||(!(d1[0]>='1' && d1[0]<='5')))
	    {
				cout<<"\t\t\tRe_enter the option:"<<endl;
				cout<<"\t\t";
				scanf(" %[^\n]s",d1);
	    }
        t1=d1[0];
        from_place = from_desti(t1);

        cout<<"\n\n\t\t\t Destination :\n\n\t\t\t 1. CHENNAI\n\n\t\t\t 2. BANGALORE\n\n\t\t\t 3. HYDERABAD\n\n\t\t\t 4. COCHIN\n\n\t\t\t 5. AMARAVATI\n\n\n\t\t\t";
        scanf(" %[^\n]s",d1);
        while((strlen(d1)!=1) ||(!(d1[0]>='1' && d1[0]<='5')))
	        {
				cout<<"\t\t\tRe_enter the option:"<<endl;
				scanf(" %[^\n]s",d1);
	        }
        t1=d1[0];
        destination = from_desti(t1);
        if(from_place==destination)
            cout<<"\n\t\t\tBoth the places can't be the same\n\n\t\t\tRe enter again\n\n";
        if(from_place!="CHENNAI" && destination!="CHENNAI")
            cout<<"\n\t\t\tChennai must be either the leaving place or destination\n\n";

    }while(from_place==destination || (from_place!="CHENNAI" && destination!="CHENNAI"));

    Sleep(2000);
    if(from_place=="CHENNAI" || destination=="CHENNAI")
    {
        if(destination=="BANGALORE" || from_place=="BANGALORE")
            bus_no1="TN123";
        else if(destination=="HYDERABAD" || from_place=="HYDERABAD")
            bus_no1="TN142";
        else if(destination=="COCHIN" || from_place=="COCHIN")
            bus_no1="TN152";
        else if(destination=="AMARAVATI" || from_place=="AMARAVATI")
            bus_no1="TN165";
        cout<<endl<<endl;
        repeat('*');
        cout<<"\n\n\t\t\tYour Leaving place : "<<from_place<<"\n\n\t\t\tYour Destination   : "<<destination;
        cout<<"\n\n\t\t\tYour Bus number is "<<bus_no1<<endl<<endl;
        repeat('*');
        cout<<endl<<endl;
    }
        i=0;
        while(i==0)
        {
            cout<<"\n\n\t\t\t Date of Registration :\n\n\t\t\t1. 16/07/2020\n\n\t\t\t2. 17/07/2020\n\n\t\t\t3. 18/07/2020\n\n\t\t\t4. 19/07/2020\n\n\t\t\t5. 20/07/2020\n\n\t\t\t6. 21/07/2020\n\n\t\t\t7. 22/07/2020"<<endl<<endl<<"\t\t\t ";
            scanf(" %[^\n]s",d1);
             while((strlen(d1)!=1) ||(!(d1[0]>='1' && d1[0]<='7')))
	        {
				cout<<"\t\t\tRe_enter the option:"<<endl;
				cout<<"\t\t";
				scanf(" %[^\n]s",d1);
	        }
            t1=d1[0];
            if(t1=='1' || t1=='2' || t1=='3' || t1=='4' || t1=='5' || t1=='6' ||t1=='7')
            {
                i=1;
                if (t1=='1')
                    date = "16/07/2020";
                else if (t1=='2')
                    date = "17/07/2020";
                else if (t1=='3')
                    date = "18/07/2020";
                else if (t1=='4')
                    date = "19/07/2020";
                else if (t1=='5')
                    date = "20/07/2020";
                else if (t1=='6')
                    date = "21/07/2020";
                else if (t1=='7')
                    date = "22/07/2020";
            }
            else
                cout<<"Invalid date\n\n\n\t\t\tRe enter again\n";
        }

        i=0;
        while(i==0)
        {
            cout<<"\n\n\t\t\tTimings available :\n\n\t\t\t1. 9:00 AM to 5:00 PM\n\n\t\t\t2. 3:00 PM to 11:00 PM\n\n\t\t\t3. 10:00 PM to 6:00 AM\n\n\n\t\t\t";
            scanf(" %[^\n]s",d1);
            while((strlen(d1)!=1) ||(!(d1[0]>='1' && d1[0]<='3')))
	        {
				cout<<"\t\t\tRe_enter the option:"<<endl;
				cout<<"\t\t";
				scanf(" %[^\n]s",d1);
	        }
			t1=d1[0];
            if(t1=='1' || t1=='2' || t1=='3')
            {
                i=1;
                if(t1=='1')
                    time1="9:00 AM to 5:00 PM";
                else if(t1=='2')
                    time1="3:00 PM to 11:00 PM";
                else if(t1=='3')
                    time1="10:00 PM to 6:00 AM";
            }
            else
                cout<<"\t\t\tInvalid timing\n\n\n\t\t\tRe enter again\n";
        }
    }

    void BUS :: Booking_Process()
    {
         int i=0;
         char d1[3];
        cout<<"\n\n\t\t\t Enter how many tickets\n\n\t\t\t ";
        scanf(" %[^\n]s",d1);
        tick_valid(d1);
        tickets=atoi(d1);
        for(int i=0;i<tickets;i++)
        {
        int k=0;
        cout<<endl<<endl;
        do
        {
            cout<<"\t\t\t Enter Seat number :\n\n\t\t\t ";
            scanf(" %[^\n]s",d1);
	        tick_valid(d1);
	        seat1[i]=atoi(d1);

            if (strcmp(seat_no[seat1[i]],"EMPTY")==0)
            {
                k=1;
                cout<<"\n\t\t\t Enter Passenger name :\n\n\t\t\t ";
                scanf(" %[^\n]s",name1[i]);
                validation(name1[i]);
                seat_no[seat1[i]] = name1[i];
                cout<<"\n\nThe Name "<<seat_no[seat1[i]]<<" is registered in the seat number " <<seat1[i]<<endl;
                seat_alloted();
            }
            else if(strcmp(seat_no[seat1[i]],"EMPTY")!=0)
            {
                cout<<"\n\n\t\t\t The Seat number is already reserved !";
                cout<<"\n\n\t\t\t Please change the seat number"<<endl<<endl;
                k=0;
            }
        }while(k==0);
    }
    }

    void BUS :: seat_alloted()
    {
        repeat('*');
        cout<<endl<<endl;
        for(int i=0; i<MAX_SEATS; i++)
            cout<<i<<"\t"<<seat_no[i]<<"\t";
        cout<<endl<<endl;
        repeat('*');
    }

    void BUS :: booked()
	{
    	int count1;
    	count1=(count*rate)+(count*tax1);
    	tax = (tickets*tax)-(count*tax);
        repeat('*');
        cout<<"\t\t\t REGISTERED DETAILS ";
        repeat('.');
        cout<<"\t\t\t Name : \t"<<name<<"\n\n\t\t\t Leaving From :\t"<<from_place;
        cout<<"\n\n\t\t\t Destination  :\t"<<destination<<"\n\n\t\t\t Journey Date :\t "<<date;
        cout<<"\n\n\t\t\t Timing : \t"<<time1<<"\n\n\t\t\t Tickets Booked:\t"<<tickets<<endl<<endl;
        cout<<"\n\n\t\t\t TICKETS CANCELLED : \t"<<count<<endl<<endl;
        for(int i=0;i<tickets;i++)
        {
            if(seat_no[seat1[i]] == "EMPTY")
                cout<<"\t\t\t Seats Booked : "<<seat1[i]<<" : "<<seat_no[seat1[i]]<<" (CANCELLED)"<<endl<<endl;
            else
                cout<<"\t\t\t Seats Booked : "<<seat1[i]<<" : "<<seat_no[seat1[i]]<<endl<<endl;
        }
        cout<<"\t\t\t Tax paid :\t"<<tax1*(tickets-count)<<"\n\n\t\t\t Amount Paid :\t"<<amount1-count1<<endl<<endl;
        cout<<"\t\t\t Amount should be credited :\t"<<(rate+tax1)*count<<endl<<endl;
        repeat('*');
    }


     void BUS :: bus_routes()
    {
        cout<<"\n\n\t\tList of Buses available : ";
        repeat('.');
        cout<<"\nS.NO\t\t BUS NO\t\t FROM\t\t TO "<<endl<<endl;
        cout<<" 1 \t\t  TN123 \t CHENNAI\t BANGALORE \n\n"<<" 2 \t\t  TN123 \t BANGALORE\t CHENNAI \n\n";
        cout<<" 3 \t\t  TN142 \t CHENNAI\t HYDERABAD \n\n"<<" 4 \t\t  TN142 \t HYDERABAD\t CHENNAI \n\n";
        cout<<" 5 \t\t  TN152 \t CHENNAI\t COCHIN   \n\n" <<" 6 \t\t  TN152 \t COCHIN\t\t CHENNAI   \n\n";
        cout<<" 7 \t\t  TN165 \t CHENNAI\t AMARAVATI \n\n"<<" 8 \t\t  TN165 \t AMARAVATI\t CHENNAI \n\n";
    }

    void BUS::Modification()
    {
        char ans1;
        int k=0;
        int choice;
        char name4[20][20];
        int seat4[10];
        char d1[3];
        cout<<"..................There will be 3 options..................\n"<<endl<<endl;
        cout<<"\t\t\t 1.  Change your name "<<endl<<endl;
        cout<<"\t\t\t 2.  Change your seat "<<endl<<endl;
        cout<<"\t\t\t 3.  Or Both          "<<endl<<endl;
        cout<<"\t\t\t YOU CAN CHOSE ANY ONE OPTION FROM IT"<<endl<<endl;
        cout<<"\t\t\t Enter your choice\n\n\t\t\t ";
        scanf(" %[^\n]s",d1);
        while((strlen(d1)!=1) ||(!(d1[0]>='1' && d1[0]<='3')))
        {
			cout<<"\t\t\tRe_enter the option:"<<endl;
			cout<<"\t\t";
			scanf(" %[^\n]s",d1);
        }
		choice=atoi(d1);
		int j=0,i=0,l=0;
        do
        {
        cout<<"\n\n\t\t\t Enter your registered name\n\n\t\t\t";
        scanf(" %[^\n]s",name4[j]);
        validation(name4[j]);
        cout<<"\n\n\t\t\t Enter registered number : \n\n\t\t\t ";
        scanf(" %[^\n]s",d1);
        tick_valid(d1);
        seat4[j]=atoi(d1);
        cout<<"\n\n................. CHECKING WHETHER YOUR NAME PRESENT OR NOT....................\n\n"<<endl;
        Sleep(2000);

		switch(choice)
		{
		case 1:
            for(i=0;i<tickets;i++)
            {
                if(strcmp(name4[j],name1[i])==0)
                {
                    if(strcmp(seat_no[seat4[j]],name4[j])==0)
                    {
                    cout<<"\n\n\t\t\t MATCHED :"<<endl<<endl;
                    Sleep(2000);
                    cout<<"\n\n\t\t\t Enter new name to be replaced :"<<endl<<endl<<"\t\t\t ";
                    scanf(" %[^\n]s",name4[j]);
                    validation(name4[j]);
                    strcpy(seat_no[seat4[j]],name4[j]);
                    cout<<"\n\nTHE SEATS REGISTERED ARE :\n\n";
                    seat_alloted();
                    break;
                    }
                    else if(strcmp(seat_no[seat4[j]],name4[j])!=0)
                    {
                    l++;
                    }
                }
                else if(strcmp(name4[j],name1[i])!=0)
                {
                    k++;
                }
            }
            if(l==tickets)
            {
            cout<<"\n\n\t\t\t NOT MATCHED : YOU HAVE ENTERED WRONG DETAILS"<<endl<<endl;
			}
            if(k==tickets)
            {
                cout<<"\n\n\t\t\t NOT MATCHED : YOU HAVE ENTERED WRONG DETAILS"<<endl<<endl;
            }
            break;
        case 2:
            for(i=0;i<tickets;i++)
            {
                if(strcmp(name4[j],name1[i])==0)
                {
                    if(strcmp(seat_no[seat4[j]],name4[j])==0)
                    {
                        cout<<"\n\n\t\t\t MATCHED :"<<endl<<endl;
                        Sleep(2000);
                        seat_no[seat4[j]]="EMPTY";
						cout<<"\n\n\t\t\t Enter new seat number you like :"<<endl<<endl<<"\t\t\t ";
						scanf(" %[^\n]s",d1);
				        tick_valid(d1);
				        seat4[j]=atoi(d1);
						strcpy(name1[i],name4[j]);
						seat_no[seat4[j]]=name1[i];
                        cout<<"\n\nTHE SEATS REGISTERED ARE :\n\n";
                        seat_alloted();
                        break;
                    }
                    else
                    {
                        l++;
                    }
                }
                else
                {
                    k++;
                }
            }
            if(l==tickets)
            {
            cout<<"\n\n\t\t\t Not matched : you have entered wrong details !"<<endl<<endl;
			}
            if(k==tickets)
            {
                cout<<"\n\n\t\t\t Not matched : you have entered wrong details !"<<endl<<endl;
            }
            break;
        case 3:
            for(i=0;i<tickets;i++)
            {
                if(strcmp(name4[j],name1[i])==0)
                {
                    if(strcmp(seat_no[seat4[j]],name4[j])==0)
                    {
                        cout<<"\n\n\t\t\t MATCHED :\t"<<endl<<endl;
                        Sleep(2000);
                        seat_no[seat4[j]]="EMPTY";
                        cout<<"\n\n\t\t\t Enter alternative name :\n\n\t\t\t ";
                        scanf(" %[^\n]s",name4[j]);
                        validation(name4[j]);
                        cout<<"\n\n\t\t\t Enter alternative seat :\n\n\t\t\t ";
                        scanf(" %[^\n]s",d1);
				        tick_valid(d1);
				        seat4[j]=atoi(d1);
                        strcpy(name1[i],name4[j]);
						seat_no[seat4[j]]=name1[i];
                        cout<<"\n\nTHE SEATS REGISTERED ARE :\n\n";
                        seat_alloted();
                        break;
                    }
                    else
                        l++;
                }
                else if(strcmp(name4[j],name1[i])!=0)
                    k++;
            }
            if(l==tickets)
            {
                cout<<"\n\n\t\t\t NOT MATCHED : INVALID DETAILS"<<endl<<endl;
			}
            if(k==tickets)
                cout<<"\n\n\t\t\t NOT MATCHED : INVALID DETAILS"<<endl<<endl;
        	break;
        }

		cout<<"\n\n\t\t\t Do you want to modify any other one ? [Y | N]"<<endl<<endl;
        scanf(" %[^\n]s",d1);
        while((strlen(d1)!=1) ||(d1[0]!='Y' && d1[0]!='y'&&d1[0]!='N'&&d1[0]!='n'))
	{
		cout<<"Re_enter the option : "<<endl;
		scanf(" %[^\n]s",d1);
	}
	ans1=d1[0];
    }while(ans1=='y'||ans1=='Y');
}

   void BUS :: Capcan()
    {
        char ans;
        char name4[20][20];
        int seat4[10];
        char d1[3];
        cout<<"\n\n\t\t\t YOUR BOOKED TICKETS "<<endl<<endl;
        seat_alloted();
        do
        {
        int i=0,k=0,l=0;
        cout<<"\n\n\t\t\t Enter name of the person "<<endl<<endl;
        cout<<"\t\t\t ";
        scanf(" %[^\n]s",name4[i]);
        validation(name4[i]);
        cout<<"\n\n\t\t\t Enter seat number "<<endl<<endl;
        cout<<"\t\t\t ";
        scanf(" %[^\n]s",d1);
		tick_valid(d1);
		seat4[i]=atoi(d1);
        cout<<"\n................. CHECKING WHETHER YOUR NAME PRESENT OR NOT...................."<<endl;
        Sleep(2000);
        for(int j=0; j<tickets; j++)
        {
        if(strcmp(name4[i],name1[j])==0)
        {
            if(strcmp(seat_no[seat4[i]],name4[i])==0)
            {
            	count++;

                seat_no[seat4[i]]="EMPTY";
                cout<<"\n\n\t\t\t SEAT CANCELLED "<<endl<<endl;
                cout<<"\nAmount\t"<<rate+tax1<<" will be credited within 2 days\n\n";
                cout<<"\n\nTHE SEATS REGISTERED ARE :\n\n";
                seat_alloted();
            }
            else
                cout<<"\n\t\t\t NO SEAT ALLOTED FOR YOU"<<endl<<endl;
         }
        else
        {
            if(strcmp(name4[i],seat_no[seat4[i]])!=0)
                k++;
        }
       }

    if(k==tickets || l==tickets)
    {
    	cout<<"\n\n";
        cout<<"\t\t\t THERE IS NO SEATED ALLOTED TO YOU KINDLY CHECK THE DETAILS YOU GAVE"<<endl<<endl;
    }
    if(count==tickets)
    {
        break;
    }
        cout<<"\n\n\t\t\t Do you want to cancel another ticket ? [y || n]\n\n\t\t\t ";
        scanf(" %[^\n]s",d1);
        while((strlen(d1)!=1) ||(d1[0]!='Y' && d1[0]!='y'&&d1[0]!='N'&&d1[0]!='n'))
	{
		cout<<"Re_enter the option : "<<endl;
		scanf(" %[^\n]s",d1);
	}
	ans=d1[0];
    }while(ans=='y'|| ans=='Y');
}

void BUS::ratings()
{
    ofstream outfile;
    int ratings;
    outfile.open("RATINGS4.txt",ios::app);
    cout<<"HELLO "<<name<<"!!!!"<<endl;
    cout<<"\n\nPLEASE GIVE YOUR RATINGS ON OUR SERVICE"<<endl;
    cout<<"\n\nENTER THE RATINGS OUT OF 5:"<<endl;
    cin>>ratings;
    while(ratings>5 || ratings<0)
    {
     cout<<"\n\nENTER THE RATINGS OUT OF 5:"<<endl;
     cin>>ratings;
    }
    outfile<<name<<"\n";
    outfile<<ratings<<"\n";
    outfile.close();
}
void BUS::view_ratings()
   {
    string read_name;
   // char temp_read[40]={"NULL"};
    ifstream infile;
    int j=0;
    infile.open("RATINGS4.txt");
    cout<<"NAME OF THE PASSENGER\t\t\t\t\t"<<"\tRATINGS OF THE USERS"<<"\t\t\t\t\t\t\t\t"<<"STARS"<<endl;
    while(!infile.eof())
    {

    	getline(infile,read_name);
    	j++;
    	cout<<left
    	    <<setw(10)<<read_name;
    	//cout<<read_name;
    	cout<<"\t\t\t\t\t\t\t\t";
    	if(j%2==0)
    	{
    		int read_rat;
    		std::istringstream(read_name) >> read_rat;
    		for(int m=0;m<read_rat;m++)
    		{
    			cout<<"*";
			}
    		j=0;
    		cout<<endl;
		}
	}
	infile.close();
}
class AC_BUS : public BUS
{
public:
    void online_transaction()
    {
        BUS::online_transaction();
    }
};

class NON_AC : public BUS
{
public:
    void online_transaction()
    {
        BUS::online_transaction();
    }
};

class Sleeper_AC : public AC_BUS
{
public:
    void online_transaction()
    {
        rate = 700;
        tax=amtcalc(rate,0.05); //AC= int datatype for template
        AC_BUS::online_transaction();
    }
}ac_s;

class Sleeper_NON_AC : public NON_AC
{
public:
    void online_transaction()
    {
        rate = 550.50;
        tax=amtcalc(rate,0.04);
        NON_AC::online_transaction();
    }
}non_ac_s;

class Non_Sleeper_AC : public AC_BUS
{
public:
    void online_transaction()
    {
        rate = 600;
        tax=amtcalc(rate,0.05);  // float data type for Non_Sleeper
        AC_BUS::online_transaction();
    }
}ac_ns;

class Non_Sleeper_NON_AC : public NON_AC
{
public:
    void online_transaction()
    {
        rate = 475.50;
        tax=amtcalc(rate,0.04);
        NON_AC::online_transaction();
    }
}non_ac_ns;

void opt_valid(char d1[])
{
    while((strlen(d1)!=1) ||(d1[0]!='1' && d1[0]!='2'))
	{
		cout<<"\t\t\tRe_enter the option : "<<endl;
		cout<<"\t\t\t";
		scanf(" %[^\n]s",d1);
	}
}
void BUS::tick_valid(char d1[])
{
		while(1)
    {
    	if(strlen(d1)==1)
    	{
    	  if((d1[0]>='0' && d1[0]<='9')&&(atoi(d1)!=0))
    	  {
    	  	cout<<"\t\t\tTHE NUMBER IS ACCEPTED:"<<endl;
    	  	break;
		  }else
		  {
		  	cout<<"\t\t\tRE ENTER THE NUMBER:"<<endl;
		  	cout<<"\t\t\t";
		  	scanf(" %[^\n]s",d1);
		  }
	  }else if(strlen(d1)==2)
	       {
	       	if((d1[0]>='0' && d1[0]<='9') &&(d1[1]>='0' && d1[1]<='9') &&(atoi(d1)<=32) &&(atoi(d1)!=0))
	        {

	        	cout<<"\t\t\tTHE NUMBER IS ACCEPTED:"<<endl;
	        	break;
			}else
			{
				cout<<"\t\t\tRE_ENTER THE NUMBER:"<<endl;
				cout<<"\t\t\t";
				scanf(" %[^\n]s",d1);
			}
		   }else
		   {
		   	 cout<<"\t\t\tRE_ENTER THE NUMBER:"<<endl;
		   	 cout<<"\t\t\t";
		   	 scanf(" %[^\n]s",d1);
		   }
	}

}
int main()
{
    class BUS obj,*ob,*obr;
    int l,count=0;
    char c1,c2,yes,opt1;
    char d1[30];
    cout<<endl<<endl;
    system("color 1F");
    repeat('*');
    cout<<"\n\n\t\t\tWELCOME TO MAKE MY TRIP\n\n";
    repeat('*');
    cout<<"\n\n\n\t\t\t1.Login\n\n\t\t\t"<<"2.Forgot Password\n";
    cout<<"\n\n\t\t\tEnter your choice:-> ";
    scanf(" %[^\n]s",d1);
    opt_valid(d1);
	c1=d1[0];
    switch(c1)
    {
    case '1':
        Sleep(2000);
        cout<<"\n\n\n\t\t\t\t";
        l=obj.login();
        break;
    case '2':
        Sleep(2000);
        system("cls");
        system("color 3F");
        cout<<"\n\n\n\n\t\t\t1.Create new password\n\n\t\t\t2.Create both login id and password\n\n"<<"\n\n\nPress 3 to exit\n\n";
        scanf(" %[^\n]s",d1);
        while((strlen(d1)!=1) || (d1[0]!='1' && d1[0]!='2' && d1[0]!='3'))
        {
            cout<<"\t\t\tRe_enter the option : \n\t\t\t"<<endl;
            scanf(" %[^\n]s",d1);
        }
        if(d1[0]=='3')
                exit(1);
        c2=d1[0];
        l=obj.login(c2);
        break;
    default:
        exit(1);
    }

    if(l==1)
    {
    Sleep(2000);
    system("cls");
    system("color 8F");

            cout<<"\t\t\t Enter Bus type "<<endl<<endl;
            cout<<"\t\t\t 1.A / C Bus - Sleeper"<<endl<<endl;
            cout<<"\t\t\t 2.NON A/C Bus - Sleeper"<<endl<<endl;
            cout<<"\t\t\t 3.A / C Bus - No Sleeper"<<endl<<endl;
            cout<<"\t\t\t 4.NON A/C Bus - No Sleeper"<<endl<<endl;
            cout<<"\t\t\t 5.Exit"<<endl<<endl;
            cout<<"\t\t\t Enter your choice "<<endl<<endl;
            scanf(" %[^\n]s",d1);
             while((strlen(d1)!=1) ||(!(d1[0]>='1' && d1[0]<='5')))
	        {
				cout<<"\t\t\tRe_enter the option:"<<endl;
				scanf(" %[^\n]s",d1);
	        }

      	   yes=d1[0];
      	   system("cls");
      	   system("color 5F");
        switch(yes)
        {
            case '1':
                    ob=&ac_s;
                    ob->bus_routes();
                    ob->get_details();
                    Sleep(5000);
                    system("cls");
                    cout<<"\n\nTHE SEATS AVAILABLE ARE :\n\n";
                    ob->seat_alloted();
                    ob->Booking_Process();

                    cout<<"Do you want to modify any details?\n\n1) Yes\n\n2) No\n\n";
                    scanf(" %[^\n]s",d1);
                    opt_valid(d1);
                    opt1=d1[0];
                    if(opt1=='1')
                        ob->Modification();
                    Sleep(3000);
                    system("cls");
                    system("color 6F");
                    ob->online_transaction();
                    Sleep(3000);
                    system("cls");
                    system("color 3E");
                    ob->booked();
                    cout<<"Do you want to cancel any seats?\n\n1) Yes\n\n2) No\n\n";
                    scanf(" %[^\n]s",d1);
					opt_valid(d1);
						opt1=d1[0];
                    if(opt1=='1')
                        ob->Capcan();
                    cout<<"\n\t\t\t Thank you ! Have a good day !!\n\n\n";
                  break;

        case '2':
                     ob = &non_ac_s;
                     ob->bus_routes();
                     ob->get_details();
                     Sleep(5000);
                     system("cls");
                     cout<<"\n\nTHE SEATS AVAILABLE ARE :\n\n";
                     ob->seat_alloted();
                     ob->Booking_Process();
                     cout<<"\n\nDo you want to modify any details?\n\n1) Yes\n\n2) No\n\n";
                     scanf(" %[^\n]s",d1);
                     opt_valid(d1);
                     opt1=d1[0];
                    if(opt1=='1')
                        ob->Modification();
                    Sleep(3000);
                    system("cls");
                    system("color 6F");
                    ob->online_transaction();
                    Sleep(3000);
                    system("cls");
                    system("color 3E");
                    ob->booked();
                    cout<<"\nDo you want to cancel any seats?\n\n1) Yes\n\n2) No\n\n";
                    scanf(" %[^\n]s",d1);
                    opt_valid(d1);
                    opt1=d1[0];
                    if(opt1=='1')
                        ob->Capcan();
                    cout<<"\n\t\t\t Thank you ! Have a good day !!\n\n\n";
                break;

        case '3':
                    ob=&ac_ns;
                    ob->bus_routes();
                    ob->get_details();
                    Sleep(5000);
                    system("cls");
                    cout<<"\n\nTHE SEATS AVAILABLE ARE :\n\n";
                    ob->seat_alloted();
                    ob->Booking_Process();
                    cout<<"Do you want to modify any details?\n\n1) Yes\n\n2) No\n\n";
                    scanf(" %[^\n]s",d1);
                    opt_valid(d1);
                    opt1=d1[0];
                    if(opt1=='1')
                        ob->Modification();
                    Sleep(3000);
                    system("cls");
                    system("color 6F");
                    ob->online_transaction();
                    Sleep(3000);
                    system("cls");
                    system("color 3E");
                    ob->booked();
                    cout<<"Do you want to cancel any seats?\n\n1) Yes\n\n2) No\n\n";
                    scanf(" %[^\n]s",d1);
                    opt_valid(d1);
                    opt1=d1[0];
                    if(opt1=='1')
                        ob->Capcan();
                    cout<<"\n\t\t\t Thank you ! Have a good day !!\n\n\n";
                break;

        case '4':
                    ob=&non_ac_ns;
                    ob->bus_routes();
                    ob->get_details();
                    Sleep(5000);
                    system("cls");
                    cout<<"\n\nTHE SEATS AVAILABLE ARE :\n\n";
                    ob->seat_alloted();
                    ob->Booking_Process();

                    cout<<"Do you want to modify any details?\n\n1) Yes\n\n2) No\n\n";
                    scanf(" %[^\n]s",d1);
                    opt_valid(d1);
                    opt1=d1[0];
                    if(opt1=='1')
                        ob->Modification();
                    Sleep(3000);
                    system("cls");
                    system("color 6F");
                    ob->online_transaction();
                    Sleep(3000);
                    system("cls");
                    system("color 3E");
                    ob->booked();
                    cout<<"Do you want to cancel any seats?\n\n1) Yes\n\n2) No\n\n";
                    scanf(" %[^\n]s",d1);
                    opt_valid(d1);
                    opt1=d1[0];
                    if(opt1=='1')
                        ob->Capcan();
                    cout<<"\n\t\t\t Thank you ! Have a good day !!\n\n\n";
               break;

    case '5':
       exit(1);
    default:
        cout<<"Invalid input\n\n";
    }

     int x=5;
     ofstream os("RATE1.DAT",ios::out|ios::binary);
        if(!os)
            cout<<"Error in file opening.";
        else
            os.write((char*)ob, sizeof(BUS));
        try
        {
            if(!os.good())
                 throw x;
        }
        catch(int x)
        {
            cout<<"Error in writing to file.\n\n";
        }

    os.close();

        ifstream is("RATE1.DAT",ios::in|ios::binary);
        if(!is)
            cout<<"Error in file opening.";
        else
        {
            is.read((char*)obr, sizeof(BUS));
            Sleep(3000);
            system("cls");
            system("color 2E");
            repeat('*');
            cout<<"\n\n\t\t\t THE CONTENTS READ FROM THE FILE IS : \n\n";
            ob->booked();
        }

        try
        {
            if(!os.good())
                 throw x;
        }
        catch(int x)
        {
            cout<<"Error in writing to file.\n\n";
        }

        is.close();

    cout<<endl<<endl<<endl<<endl<<endl;
    int rat_op=0;

    cout<<"PLEASE FILL OUT THE RATINGS:"<<endl;
    ob->ratings();
    cout<<endl;
    cout<<"DO YOU WANT TO SEE OTHER'S RATINGS"<<endl;
    cout<<" 1 . Yes"<<endl;
    cout<<" 2.  NO"<<endl;
     scanf(" %[^\n]s",d1);
     opt_valid(d1);
     rat_op=d1[0];
    while(rat_op<'0')
    {
        cout<<"RE_ENTER THE OPTION:"<<endl;
        cin>>rat_op;
    }
    if(rat_op=='1')
    {
        ob->view_ratings();
    }
    else
    {
        exit(0);
    }
}

    else
        cout<<"\n\n\nExiting! Thank You !!!\n\n\n";
getch();

return 0;
}
