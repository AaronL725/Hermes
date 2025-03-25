

  * 

[Triangular Arbitrage](/thread/64423-triangular-arbitrage "Admin, Please Delete Thread.") 258 replies

[Triangular Arbitrage](/thread/62477-triangular-arbitrage "Is going  
long 1 lot of eur/usd + 
long 1 lot of usd/jpy = long 1 lot of eur/jpy ?  
\(is the ratio of the number of lots correct for a...") 16 replies

[Triangular Arbitrage and carry trade](/thread/71997-triangular-arbitrage-and-carry-trade "Is it possible for us retail traders to be able to make use of Tri Arb or carry trades?  
 
Any one know of retail brokers 
 
 
\(I'm...") 6 replies

[Triangular Arbitrage](/thread/367072-triangular-arbitrage "I've been reading about triangular arbing and was surprised to find that the cross of two majors doesn't always equal what the calculation...") 7 replies

[Question: Trade Mechanics of Triangular Arbitrage](/thread/225246-question-trade-mechanics-of-triangular-arbitrage "Before I even ask this question, please allow me to be very clear.... I have no intention of attempting a triangular arbitrage trade\(for...") 6 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/676132-simple-high-profit-low-drawdown-triangular-arbitrage/reply#reply)
  * Subscribe
  * [147](javascript:void\(0\);)

Attachments: Simple High Profit low Drawdown Triangular Arbitrage

Tags: Simple High Profit low Drawdown Triangular Arbitrage

#  [](/thread/676132-simple-high-profit-low-drawdown-triangular-arbitrage)Simple High Profit low Drawdown Triangular Arbitrage 

  * 

  * [#1](/thread/676132-simple-high-profit-low-drawdown-triangular-arbitrage "Post Permalink")

  * First Post: Edited Sep 28, 2017 5:04pm  Jun 17, 2017 5:12pm | Edited Sep 28, 2017 5:04pm 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

I will always update this POST #1 with the latest information.  
So if you do not want to read all the posts then just read this one.  
  
I will also keep the EAs up to date here.  
  
The rest of the posts are interesting and I love flame wars ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
  
  
*******************************  
Very basic summary  
*******************************  
1) Buy 1 unit GBPJPY  
2) Sell 1 unit GBPUSD  
3) Sell ?? units using the USD in point (2) in USDJPY to balance everything out  
  
Buy low and sell high.  
Rinse and repeat.  
  
Can this work or what is the pitfalls with this idea ?  
  
  
*******************************  
Detail  
*******************************  
OK I am still new in this, but must say triangular arbitrage looks interesting.  
I made an EA to trade GBPUSB, GBPJPY and USDJPY  
  
Basically  
1) Buy 1 unit GBPJPY  
2) Sell 1 unit GBPUSD  
3) Sell ?? units using the USD in point (2) in USDJPY to balance everything out  
  
This basically ZEROs your position minus spread, commission and swap.  
Just hold on to this until in profit.  
It will oscillate around the ZERO point.  
  
Once I make profit I swap the above 123 points to Sell, Buy, Buy.  
  
My entry can be random and then go from there, but since I started I changed it so that I calculate what the low and high is and use those calculations as entry points.  
  
Now sometimes you do accidentally get in at just the wrong time.  
Basically buying at the highest point and it never gets back to that point.  
  
In 2 years time I found it about 9 times.  
You can see these in the load spikes at the bottom of the chart.  
  
This problem is solved by a minor grid.  
Basically once you unluckily buy at the highest point then you will be stuck, but no worries, because it can only fall so far before coming back, but never past that point again so just wait a bit and let it fall and once it fell enough then Buy again the same amount and leave it for a guaranteed profit a bit more than half way back so just wait a bit.  
  
Now as I said My speciality is maths and programming, but I am new to the forex market.  
  
The demo EA I wrote I ran from 2015-06-23 till 2017-06-16.  
I started with $1000 and ended with $2,725,839.38  
Maximum drawdown during this time was 25% of the account.  
  
I did have a safety catch in the system to prevent losses from going beyond 25% which was hit 2 times during the 2 year run, which does not affect the EA seeing that it will adapt itself to the next balance as needed.  
The cause for the 25% drawdown spikes was weekend gaps on the Monday.  
I tried preventing Friday trades which caused the maximum drawdown to drop to 15%, but the ending profit also dropped to about $1,800,000.00  
  
Other things to note was that I was maxing out my Metatrader 5 back test lot size at 99 lots after the 1 year mark at about 2016-06-28 and from there it stopped growing exponentially and started a slower sequential growth.  
In the live environment you can split your account into multiple accounts long before it reaches the limit for even more profit.  
  
The 25% drawdown hits will probably also increase if you can keep the exponential growth growing from 2 hits to about 4 hits, maybe 5 at most, but the EA is designed for it and can handle about 20 times 25% hist before starting to show a loss, because the growth rate is about 100% every 2 months and at worst it hit the 25% drawdown 2 times in one year..  
  
I do not have funds to test this live, but demo testing seem quite good.  
  
Any advice will be great.  
  
I even found this to be profitable using a starting capitol of only $100, but at this price all 3 pairs will start at the same 0.01 lots, which is a bit off in balance seeing that the USDJPY can not be the same as the other, but once it breaks the $1000 profit mark it works good and the $10,000 mark is just rocket fuel for it.  
  
Ignore the upward spikes in the charts.  
The EA is told to start selling the highest profitable once first.  
What matters to me is the equity and how far it falls after opening a 3 pair group.  
  
The 2 pair 25% drawdown happened in the beginning of the chart and therefore is almost invisible when compared to the profit of the rest of the chart.  
  
  
*******************************************************************************  
RULE UPDATE : 2017-09-23  
*******************************************************************************  
Ok this is a MAJOR update.  
  
Rules changed a bit.  
Still triangular on the 3 symbols.  
  
But.  
I now calculate what the average profit would be if I did a BUY, SELL, SELL and also SELL,BUY,BUY.  
This gives me 2 lines.  
Call the higher line the ASK line and the lower line the BUY line.  
  
Between the 2 lines is the average line calculated over some time, which if mostly a straight line as the buy and sell lines basically cancels each other out there.  
  
Now from time to time you will notice the ASK line cross the average line and this is the time you must open a Buy(Sell, Buy, Buy) to profit from the inevitable up movement.  
Close the open buy once the SELL line cross the average line.  
Do the opposite for opening a sell(Buy,Sell,Sell).  
  
One more thing is that I do not just open when it crosses the middle average line, but I only open once it crosses the average line for some distance before opening.  
  
Ok there is a lot more checks and stuff I put in the EA, but that is the basics.  
  
I tested this on MyFxchoice with a leverage of 1:200 so try and keep to those settings.  
I might work on other settings and I did try and build in intelligence to adapt to other brokers, but I had limited time and it might not work properly.  
Backtest to make sure it works properly before a forward test.  
  
DO NOT USE ON LIVE ACCOUNT.  
  
Other things in the EA are :  
1) Do not trade weekend gaps for the Monday slippage can be big.  
2) Do not trade between midnight and 2 am for the same reason as (1).  
3) Move all display and log coding after the system calculations to increase trade calculation performance.  
4) Use only 50% of ac  
count for trading, which only mean that 50% of the account must be converted to used margin.  
Draw-down is about 5% then, but I can not increase it for fear of getting a margin call.  
20% might be better, but I will test it one day.  
  
5) Check for failed trades and kill them to start over.  
6) Check for weekend and inactive markets to prevent system failure.  
7) Check commission using single 0.01 lot trade.  
8) Massive amounts of logs and graph code to display what is happening.  
This uses a lot of memory so I must probably move it into another EA for display reasons only seeing that it is not needed to do trading with, but looks nice and you can see why the EA does what it does.  
Then there can be one EA to do trading with and another display EA which you can load somewhere else to show the workings, without the display EA affecting the trade processing.  
  
Problems:  
1) Slippage and trade delays.  
I am getting close to 500 milliseconds delay on opening 3 trades for the 3 symbols at a time.  
This can cause some major slippage, especially on the 3rd trade, but luckily I still make profit on most trades seeing that the EA does cater for some slippage.  
I'm still trying to find ways to decrease the time delay, but it seem to be a limitation on how metatrader works.  
  
1.1) I might be able to improve the trade speed using 4 metatrader terminals and I have already created programs to allow EAs communicate with the outside world within less than 1 millisecond, but there is still a delay of about 300 milliseconds for a single trade to start.  
  
On the bright side I have now developed a driver that can connect an EA to anything else from other EAs to other terminals or even outside programs like java and even to other PCs in other countries or any other device for that matter or even making a metatrader EA use things like the FIX api.  
The possibilities are big for this driver.  
  
1.2) Delayed trade starts seem to be caused by the terminal logging out if there is no trade action for some time and when a new trade is needed then the terminal for have to take some time to log back in before the trade can be opened or closed.  
I could not find a way to prevent logout, EXCEPT by sending dummy trades or impossible pending trades or trade modifications every 20 to 30 seconds.  
Problem with this might be that broker will not appreciate receiving so many trade signals.  
  
1.3) FIX API.  
I have been playing around with FIX api and it might be a solution to this trade delay, but I need to test it first and .... well... time is not on my side ![](https://resources.faireconomy.media/images/emojis/64/1f641.png?v=15.1)  
  
  
  
*******************************************************************************  
RUNNING THE EA  
*******************************************************************************  
Do not run on live account.  
  
Just attach the EA to a chart ....... That is it ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
  
Some more details.  
The EA is made to run with symbols GBPUSD, GBPJPY, USDJPY  
Exactly and it is case sensitive.  
If those symbols is not in your market watch or trade able then it will not work, UNLESS...  
  
There are a couple of parameters in the EA you can set.  
Mostly the trade symbols.  
Keep in mind the EA is only made for GBPUSD, GBPJPY, USDJPY  
BUT if your broker contains symbols like GBPUSD#e ex.. then you can use the parameters to change the EA to use your broker's symbols.  
Keep in mind it is case sensitive and therefore if your broker lists GBPUSD#e and you put in GBPUSD#E then the EA will not work.  
  
To view the chart drawn by the EA I suggest making the chart window background BLACK and zoom the chart out by dragging down on the right hand vertical price bar till u can see all the lines the EA draws on the chart.  
I'll even suggest making everything black as the chart price gives no useful information. 

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: TesterGraphReport2017.06.16 2.png
Size: 19 KB](/attachment/image/2359013/thumbnail?d=1497687153)](/attachment/image/2359013?d=1497687153)   
[![Click to Enlarge

Name: Screenshot from 2017-06-16 23-25-10.png
Size: 200 KB](/attachment/image/2359014/thumbnail?d=1497687165)](/attachment/image/2359014?d=1497687165)   
[![Click to Enlarge

Name: Screenshot from 2017-06-17 14-38-00.png
Size: 207 KB](/attachment/image/2359131/thumbnail?d=1497703194)](/attachment/image/2359131?d=1497703194)   

Attached File(s)

![File Type: ex5](https://assets.faireconomy.media/images/attach/ex5.gif) [2017-09-18 09h00 JVB Arbitrage Auto Profit16 backtest.ex5](/attachment/file/2493416?d=1506297348) 123 KB | 2,431 downloads | Uploaded Sep 25, 2017 8:55am 

![File Type: ex5](https://assets.faireconomy.media/images/attach/ex5.gif) [2017-09-18 09h00 JVB Arbitrage Auto Profit18.ex5](/attachment/file/2496591?d=1506459231) 126 KB | 2,032 downloads | Uploaded Sep 27, 2017 5:53am 

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [2017-09-18 09h00 JVB Arbitrage Auto Profit18.ex4](/attachment/file/2496592?d=1506459232) 68 KB | 3,357 downloads | Uploaded Sep 27, 2017 5:53am 

![File Type: ex5](https://assets.faireconomy.media/images/attach/ex5.gif) [2017-09-18 09h00 JVB Arbitrage Auto Profit19.ex5](/attachment/file/2499030?d=1506585858) 127 KB | 2,970 downloads | Uploaded Sep 28, 2017 5:04pm 

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [2017-09-18 09h00 JVB Arbitrage Auto Profit19.ex4](/attachment/file/2499032?d=1506585859) 68 KB | 6,041 downloads | Uploaded Sep 28, 2017 5:04pm 

  * [#2](/thread/post/9988602#post9988602 "Post Permalink")

  * Jun 17, 2017 6:33pm  Jun 17, 2017 6:33pm 

  * [ Waddah](waddah)

  * | Joined Aug 2015  | Status: Trader | [76 Posts](/search?do=process&provider=Member&searchuser=422745)

thanks for sharing your system , but haw u calculate USDJPY lot ? 

[1 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#3](/thread/post/9988643#post9988643 "Post Permalink")

  * Jun 17, 2017 6:59pm  Jun 17, 2017 6:59pm 

  * [ HurryK](hurryk)

  * | Joined Jan 2016  | Status: Trader | [26 Posts](/search?do=process&provider=Member&searchuser=443489)

looks impressive.  
one thing i can think of on real account are issues with execution times of your orders.  
In demo they execute instantly, on real accounts you may experience drawdowns due to the lag.  
I guess maybe forward test this strategy also on live demo account first? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#4](/thread/post/9988705#post9988705 "Post Permalink")

  * Jun 17, 2017 7:33pm  Jun 17, 2017 7:33pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar46777_5.gif) shiva](shiva)

  * Joined Aug 2007 | Status: Doing It In Dubai | [2,457 Posts](/search?do=process&provider=Member&searchuser=46777)

Hi Jacques, I can test it on a live account if you share the EA. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#5](/thread/post/9988789#post9988789 "Post Permalink")

  * Edited 9:07pm  Jun 17, 2017 8:35pm | Edited 9:07pm 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@Waddah  
I might calculate it wrong, but I do the following :  
GBPJPY = lotSize  
GBPUSD = lotSize  
USDJPY = lotSize * GBPUSD  
  
@HurryK  
I know yes and would love to test it.  
I am busy testing it on a demo account, but I have got a 400ms lag ![](https://resources.faireconomy.media/images/emojis/64/1f641.png?v=15.1)  
Still making a profit (just a bit less), but lots of requotes and slippage.  
I do have plans to cater for slippages and requotes, which should be simple programming, but my problem is time and funds to do the development an maybe get a VPS to get a better forex connection which will cost me about $40 a month ..... That is a lot of money in South African rands and beyond my financial abilities.  
Took me a few months to get it where it is now and to make it bomb proof probably another 2 months.  
  
@shiva AND @HurryK  
I have attached the EA to this message, BUT PLEASE DO NOT USE ON LIVE.  
Rather on a faster than mine demo account.  
Reasoning is the stuff I have not build into it yet.  
As stated by @HurryK there are things on a live account that is not in back tests.  
To list a few :  
1) Requotes.  
EA should will still make a profit, but with further development it will make a lot closer to back test profit if it knows to look for it and cater for it, which I know how to program.... Will just take some time.... and at the moment I can not afford taking more time of work.  
2) Slippage.  
EA should will still make a profit, but with further development it will make a lot closer to back test profit if it knows to look for it and cater for it, which I know how to program.... Will just take some time.... and at the moment I can not afford taking more time of work.  
3) CRASH  
At the moment the EA lives in a fantasy perfect word of perfect internet and perfect metatrader programs.  
Isn't that nice.  
3.1) At the moment the EA does not check for existing positions when it starts up and therefore if there are it will mess with its head and calculations.  
3.2) If Metatrader restarts then it will also not look for trades left open since last time it ran and therefore miscalculate the future.  
3.3) EA Freeze.  
I have not seen this, but it is a possibility for which I would like to build in a remote connection to my cellphone or email or something to notify me of any problems so I can jump in and save it from gremlins.  
3.4) Check for existing positions and process them or warn the user and stop if not part of the system.  
3.5) Check for multiple EAs which can interfere with it.  
3.6) A Metatrader 4 version of the EA.(Already done, but not tested.)  
3.7) I still need a way to extract profits, without affecting the EA.  
This can be done using a user settings that can be activated mid run to tell the EA to leave alone a user selected amount and then notify user once this amount is lose so she can extract it without affecting the EA.  
You can extract any amount at the moment in-between trades, basically if there is no open position, which is difficult seeing that the EA can immediately open another trade.  
3.8) Quite a few other possible problems also need to be looked into....  
  
All of these CRASH points are easily solved in the program.... Will just take some time.... and at the moment I can not afford taking more time of work.  
  
To run the EA.  
1) Make sure you have got no open positions on you WHOLE account.  
2) Attach it to a GBPUSB or GBPJPY or USDJPY chart.  
ONLY ONE CHART and not multiple charts.  
Any time frame.  
It just need to be active and receive tick signals from anywhere.  
You can actually attach it to any chart, but the tick signal timing will differ so a one of the top 3 pairs will probably work best.  
3) I suggest a starting account with $10,000, but it should work with less.  
As stated it even worked on a $100 account, but it is risky with whiskey seeing that the USDJPY pair is not balanced correctly then.  
4) Thats it.  
No settings or anything is needed.  
It does check [spreads](/brokers/spreads "View Live Spreads on the Broker Guide") and will not open trades if the spread is too high.  
I suggest a ENC/commission broker with low spreads.  
It will take about 6 months for it to average out and show real profits.  
Or sooner if you are lucky.  
It does some trades once every 3 days on average, but can do a few per minute if the maket moves a lot.  
Keep in mind that this version of the EA is set to EXTREMELY aggressive.  
I can set it to safer settings which will still make about 500% profit a year, but hey ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1) I'M A DAREDEVIL ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1) Or I was dropped on my head to much. 

Attached File(s)

![File Type: ex5](https://assets.faireconomy.media/images/attach/ex5.gif) [2017-06-12 09h00 JVB Arbitrage Auto Profit2.ex5](/attachment/file/2359117?d=1497699292) 89 KB | 1,816 downloads 

![File Type: ex5](https://assets.faireconomy.media/images/attach/ex5.gif) [2017-06-12 09h00 JVB Arbitrage Auto Profit2 Avoid Fridays and get Less Profit and drawdown.ex5](/attachment/file/2359126?d=1497700962) 89 KB | 1,543 downloads 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#6](/thread/post/9988836#post9988836 "Post Permalink")

  * Jun 17, 2017 9:12pm  Jun 17, 2017 9:12pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar492187_10.gif) mr.brown](mr.brown)

  * Joined Sep 2016 | Status: Its my biz to know what others dont | [1,280 Posts](/search?do=process&provider=Member&searchuser=492187)

if u r not adding or closing trade sizes during positions floating, then u basicly trading the price changes n this can go positive or negative.  
  
the initial lot size calculation seem correct so far but 4 the actual prices. when u open arbitrage trio n let it run 4 days or weeks then the pricing will change n so lot sizes should be fixed by adding or closing partially. if not then u basicly trading the distortion of price change n this can go as said positive or negative 

WBS Where are Buyers and Sellers

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#7](/thread/post/9988843#post9988843 "Post Permalink")

  * Jun 17, 2017 9:14pm  Jun 17, 2017 9:14pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar492187_10.gif) mr.brown](mr.brown)

  * Joined Sep 2016 | Status: Its my biz to know what others dont | [1,280 Posts](/search?do=process&provider=Member&searchuser=492187)

> [Quoting mr.brown](/thread/post/9988836#post9988836 "View Quoted Post")
> 
> Disliked
> 
> if u r not adding or closing trade sizes during positions floating, then u basicly trading the price changes n this can go positive or negative. the lot size calculations seem correct so far but 4 the actual prices. when u open arbitrage trio n let it run 4 days or weeks then the pricing will change n so lot sizes should be fixed by adding or closing partially. if not then u basicly trading the distortion of price change n this can go as said positive or negative
> 
> Ignored

n when trades floating swaps will kill, if u wanna test on real find a swap free account, just sayin ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

WBS Where are Buyers and Sellers

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#8](/thread/post/9988847#post9988847 "Post Permalink")

  * Edited 9:42pm  Jun 17, 2017 9:22pm | Edited 9:42pm 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@mr.brown  
Thanks for the input ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
Not sure I understand correctly, but here goes.  
  
I actually bargain on the price changes.  
If the price never changed then I would make no profit or loss for that matter, except for the spread, swap and commission.  
  
I call the point at which I open the 3 pair the ZERO point.  
The price normally oscillate up and down (profit and loss) around this price.  
BUT once in a while(once a year or something) the ZERO point moves.  
The ZERO point can not move to much or else the whole financial world system will fall apart, but still with leverage it can affect you.  
But for this instance I do have another catch.  
If I open a position and I see that this position stays open for more than 3 days then I will check for the lowest point over the last floating 3 days time and if this low point is hit again I will open another position in the same direction to counter the ZERO point move.  
This way the price only have to move half way back to get into profit and close the whole position.  
  
You will see this happening in the cart I added above on the bottom DEPOSIT LOAD.  
There are spikes where my position doubled.  
I never go more than 2 full positions in and if it does not recover by then then I have one final stop loss of 25%, which was hit 2 times in 2 years, which is more than acceptable with this growth rate.  
  
My tests include SWAP so it already caters for swap.  
Most of my trades happen to fast in one day to incur any swap.  
I will add an image above showing swap loss on some trades and the profit made even with swap.  
  
Does someone know how to get the full trade history in text format so that I can attach it to this forum in stead of screen prints. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot from 2017-06-17 14-38-00.png
Size: 207 KB](/attachment/image/2359134/thumbnail?d=1497703241)](/attachment/image/2359134?d=1497703241)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#9](/thread/post/9988861#post9988861 "Post Permalink")

  * Jun 17, 2017 9:40pm  Jun 17, 2017 9:40pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar492187_10.gif) mr.brown](mr.brown)

  * Joined Sep 2016 | Status: Its my biz to know what others dont | [1,280 Posts](/search?do=process&provider=Member&searchuser=492187)

> [Quoting jvbJacques](/thread/post/9988847#post9988847 "View Quoted Post")
> 
> Disliked
> 
> @mr.brown Thanks for the input ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1) Not sure I understand correctly, but here goes. I actually bargain on the price changes. If the price never changed then I would make no profit or loss for that matter, except for the spread, swap and commission. I call the point at which I open the 3 pair the ZERO point. The price normally oscillate up and down (profit and loss) around this price. BUT once in a while(once a year or something) the ZERO point moves. The ZERO point can not move to much or else the whole financial world system will fall apart,...
> 
> Ignored

if u use initial price in your lot size calculation which u r, "26.03" "26.03" n "37.01" then when price changes u should change the lot size too by partially closing or adding. clear ?  
  
PS : is weekly double triple swaps added into account ? 

WBS Where are Buyers and Sellers

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#10](/thread/post/9988865#post9988865 "Post Permalink")

  * Jun 17, 2017 9:44pm  Jun 17, 2017 9:44pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar492187_10.gif) mr.brown](mr.brown)

  * Joined Sep 2016 | Status: Its my biz to know what others dont | [1,280 Posts](/search?do=process&provider=Member&searchuser=492187)

> [Quoting mr.brown](/thread/post/9988861#post9988861 "View Quoted Post")
> 
> Disliked
> 
> {quote} if u use initial price in your lot size calculation which u r, "26.03" "26.03" n "37.01" then when price changes u should change the lot size too by partially closing or adding. clear ? PS : is weekly double triple swaps added into account ?
> 
> Ignored

btw, Am not offensive, have tried triangular arbitrage years ago ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
I can give u n advise, use dll n use 3 platforms. connect them by using shared dll while when same instance opens 3 trades at the same time it puts them in a queue, if u use 3 patforms connected to same broker server then 3 will be opened at the same time [milliseconds] ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)  
  
hire a vps from the mean broker data center so u can get < 2ms latency ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)   
good luck 

WBS Where are Buyers and Sellers

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#11](/thread/post/9988871#post9988871 "Post Permalink")

  * Jun 17, 2017 9:47pm  Jun 17, 2017 9:47pm 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@mr.brown  
Yes I suspect double and triple is included, but swap is a minor amount to the profit.  
  
As for the size calculation.  
I leave the calculation the same for the run of the position, but I do recalculate once a position is closed and a new one is opened up.  
  
The size calculation change very little over a long period of time and therefore it does not affect the profit much as seen over the 2 year run backtest and most positions are closed the same day or hour.  
  
I try to keep things as simple as possible so I keep away from position sizing as that might eat a little into the profit. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#12](/thread/post/9988874#post9988874 "Post Permalink")

  * Jun 17, 2017 9:49pm  Jun 17, 2017 9:49pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar492187_10.gif) mr.brown](mr.brown)

  * Joined Sep 2016 | Status: Its my biz to know what others dont | [1,280 Posts](/search?do=process&provider=Member&searchuser=492187)

> [Quoting mr.brown](/thread/post/9988865#post9988865 "View Quoted Post")
> 
> Disliked
> 
> {quote} btw, Am not offensive, have tried triangular arbitrage years ago ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1) I can give u n advise, use dll n use 3 platforms. connect them by using shared dll while when same instance opens 3 trades at the same time it puts them in a queue, if u use 3 patforms connected to same broker server then 3 will be opened at the same time [milliseconds] ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1) hire a vps from the mean broker data center so u can get < 2ms latency ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1) good luck
> 
> Ignored

n when u put all together code, vps, dll, deposit, time, when its time to withdrawal, when broker check ur accıount detail n finds u simply trading gbpusd gbpjpy usdjpy or any other triangular arbitrage, it will probably freeze ur account n u will forget the deposit 

WBS Where are Buyers and Sellers

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#13](/thread/post/9988879#post9988879 "Post Permalink")

  * Jun 17, 2017 9:51pm  Jun 17, 2017 9:51pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar492187_10.gif) mr.brown](mr.brown)

  * Joined Sep 2016 | Status: Its my biz to know what others dont | [1,280 Posts](/search?do=process&provider=Member&searchuser=492187)

> [Quoting jvbJacques](/thread/post/9988871#post9988871 "View Quoted Post")
> 
> Disliked
> 
> @mr.brown Yes I suspect double and triple is included, but swap is a minor amount to the profit. As for the size calculation. I leave the calculation the same for the run of the position, but I do recalculate once a position is closed and a new one is opened up. The size calculation change very little over a long period of time and therefore it does not affect the profit much as seen over the 2 year run backtest and most positions are closed the same day or hour. I try to keep things as simple as possible so I keep away from position sizing as that...
> 
> Ignored

during bt u have no latency n slippage, when u run it on demo it can make profit too, but when on real u will see the ugly truth  
good luck anyway 

WBS Where are Buyers and Sellers

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#14](/thread/post/9988881#post9988881 "Post Permalink")

  * Jun 17, 2017 9:52pm  Jun 17, 2017 9:52pm 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@mr.brown  
I really appreciate your input.  
  
I was thinking the same thing about 3 programs running the same time, but I will do that at a later stage seeing that there is a lot of other potential problem that need programming first.  
  
As for the VPS.  
Yes that is a dream of mine, but $40 a month is a bit beyond my financial means ![](https://resources.faireconomy.media/images/emojis/64/1f641.png?v=15.1)  
But if it ever goes live then a VPS is a must for the speed.  
  
At the moment my poor test server here at home has got a 400ms delay and all the problems that come with it, but still making profit ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
Basically I adjusted the profit take to take into account the worst possible slippage and still some extra profit.  
So maybe my poor test server is a good stress test. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#15](/thread/post/9988935#post9988935 "Post Permalink")

  * Jun 17, 2017 10:47pm  Jun 17, 2017 10:47pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar303372_1.gif) skg3007](skg3007)

  * | Commercial User  | Joined Oct 2012 | [100 Posts](/search?do=process&provider=Member&searchuser=303372)

> [Quoting jvbJacques](/thread/post/9988881#post9988881 "View Quoted Post")
> 
> Disliked
> 
> @mr.brown I really appreciate your input. I was thinking the same thing about 3 programs running the same time, but I will do that at a later stage seeing that there is a lot of other potential problem that need programming first. As for the VPS. Yes that is a dream of mine, but $40 a month is a bit beyond my financial means ![](https://resources.faireconomy.media/images/emojis/64/1f641.png?v=15.1) But if it ever goes live then a VPS is a must for the speed. At the moment my poor test server here at home has got a 400ms delay and all the problems that come with it, but still making profit ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1) Basically...
> 
> Ignored

Here is the cheapest VPS. I am using more then 5 years. Take a 1GB RAM, Metered Bandwidth Windows VPS for $10/month  
<https://goo.gl/wTLezS>

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#16](/thread/post/9988949#post9988949 "Post Permalink")

  * Jun 17, 2017 11:01pm  Jun 17, 2017 11:01pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar492187_10.gif) mr.brown](mr.brown)

  * Joined Sep 2016 | Status: Its my biz to know what others dont | [1,280 Posts](/search?do=process&provider=Member&searchuser=492187)

> [Quoting skg3007](/thread/post/9988935#post9988935 "View Quoted Post")
> 
> Disliked
> 
> {quote} Here is the cheapest VPS. I am using more then 5 years. Take a 1GB RAM, Metered Bandwidth Windows VPS for $10/month <https://goo.gl/wTLezS>
> 
> Ignored

vps should be placed at the same data center where mean broker servers located. random vps location wont work 

WBS Where are Buyers and Sellers

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#17](/thread/post/9988962#post9988962 "Post Permalink")

  * Jun 17, 2017 11:10pm  Jun 17, 2017 11:10pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar46777_5.gif) shiva](shiva)

  * Joined Aug 2007 | Status: Doing It In Dubai | [2,457 Posts](/search?do=process&provider=Member&searchuser=46777)

> [Quoting jvbJacques](/thread/post/9988789#post9988789 "View Quoted Post")
> 
> Disliked
> 
> @shiva AND @HurryK I have attached the EA to this message, BUT PLEASE DO NOT USE ON LIVE. Rather on a faster than mine demo account. Reasoning is the stuff I have not build into it yet. As stated by @HurryK there are things on a live account that is not in back tests. To list a few : 1) Requotes. EA should will still make a profit, but with further development it will make a lot closer to back test profit if it knows to look for it and cater for it, which I know how to program.... Will just take some time.... and at the moment I can not afford taking...
> 
> Ignored

Thanks Jacques, as you wisely sugsted I will test it on demo and will also place it on myfxbook so that all of us can monitor how this goes ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#18](/thread/post/9989192#post9989192 "Post Permalink")

  * Jun 18, 2017 1:49am  Jun 18, 2017 1:49am 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@skg3007  
Thanks for the advice, but @mr.brown is right in that you need a fast connection to the broker you use.  
I used to use a vps connected directly to myfxchoice and it was fantastic, but it bled me dry financially.($40)  
One day maybe I can do it again.  
  
@shiva  
This will sound stupid, but how do I also see the results of this myfxbook ?  
Is it edible ?  
  
I'm a master builder, programmer, hardware and software automation in high security mining, tagging, gas, vehicle automation, camera body and facial recognition, architectural automatic build fenestration scanning and calculation automation, lamp room controls, and bla bla bla bla , BUT I know very little about forex.  
I do love mathematics and after a few months of dabbling in the forex I started seeing some patterns like this and applied what I know about A.I and automation and it seem to work.  
But how fxbook works is still beyond me ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
  
Monitor this forum or mail me from time to time and I will give you updates to the EA.  
Keep in mind what I said about the shortfalls of the EA.  
If you want to stop and start it then it must be done inbetween trades, so be quick or take the knock on a new trade and just close it after closing the EA.  
Do not start the EA on a account with already open position as it will not know about them and it will mess things up.  
Even trades opened by this EA itself...  
  
I will insert an update to stop more gracefully and do take profit better.  
One day.....  
  
I mostly tested this using a ENC broker account.  
I did test a normal non commission account also and it did make profit, but less.  
I tested the metatrader 4 version even less, but it worked thus far. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#19](/thread/post/9989252#post9989252 "Post Permalink")

  * Jun 18, 2017 2:23am  Jun 18, 2017 2:23am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar349524_1.gif) SubheadSeven](subheadseven)

  * | Joined Sep 2013  | Status: Trader | [96 Posts](/search?do=process&provider=Member&searchuser=349524)

Hi Jacques, Thanks for sharing. one question, this system is not suitable on Friday? 

SVT refer to mql5 link

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#20](/thread/post/9989258#post9989258 "Post Permalink")

  * Jun 18, 2017 2:29am  Jun 18, 2017 2:29am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar46777_5.gif) shiva](shiva)

  * Joined Aug 2007 | Status: Doing It In Dubai | [2,457 Posts](/search?do=process&provider=Member&searchuser=46777)

> [Quoting jvbJacques](/thread/post/9989192#post9989192 "View Quoted Post")
> 
> Disliked
> 
> @skg3007 Thanks for the advice, but @mr.brown is right in that you need a fast connection to the broker you use. I used to use a vps connected directly to myfxchoice and it was fantastic, but it bled me dry financially.($40) One day maybe I can do it again. @shiva This will sound stupid, but how do I also see the results of this myfxbook ? Is it edible ? I'm a master builder, programmer, hardware and software automation in high security mining, tagging, gas, vehicle automation, camera body and facial recognition, architectural automatic build fenestration...
> 
> Ignored

Hi Jacques, Myfxbook.com is a website to publish trading results. Just like forexfactory's trade explorer.  
Since your EA is MT5 and not MT4, I chose to use myfxbook instead of forexfactory explorer. Unfortunately forexfactory does not have a provision for publishing MT5 explorers yet.   
I will post the link here for all to see. It updates in real time. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Simple High Profit low Drawdown Triangular Arbitrage
  *   * [ **Reply to Thread** ](/thread/676132-simple-high-profit-low-drawdown-triangular-arbitrage/reply#reply)

  * More

[](https://www.forexfactory.com "Homepage")

  * [Forums](forums)
  * [Trades](trades)
  * [Calendar](calendar)
  * [News](news)
  * [Market](market)
  * [Brokers](brokers)

****

[](https://www.faireconomy.com/)

  * 

[Triangular Arbitrage](/thread/64423-triangular-arbitrage "Admin, Please Delete Thread.") 258 replies

[Triangular Arbitrage](/thread/62477-triangular-arbitrage "Is going  
long 1 lot of eur/usd + 
long 1 lot of usd/jpy = long 1 lot of eur/jpy ?  
\(is the ratio of the number of lots correct for a...") 16 replies

[Triangular Arbitrage and carry trade](/thread/71997-triangular-arbitrage-and-carry-trade "Is it possible for us retail traders to be able to make use of Tri Arb or carry trades?  
 
Any one know of retail brokers 
 
 
\(I'm...") 6 replies

[Triangular Arbitrage](/thread/367072-triangular-arbitrage "I've been reading about triangular arbing and was surprised to find that the cross of two majors doesn't always equal what the calculation...") 7 replies

[Question: Trade Mechanics of Triangular Arbitrage](/thread/225246-question-trade-mechanics-of-triangular-arbitrage "Before I even ask this question, please allow me to be very clear.... I have no intention of attempting a triangular arbitrage trade\(for...") 6 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/676132-simple-high-profit-low-drawdown-triangular-arbitrage/reply#reply)
  * Subscribe
  * [147](javascript:void\(0\);)

Attachments: Simple High Profit low Drawdown Triangular Arbitrage

Tags: Simple High Profit low Drawdown Triangular Arbitrage

#  [](/thread/676132-simple-high-profit-low-drawdown-triangular-arbitrage)Simple High Profit low Drawdown Triangular Arbitrage 

  * 

  * [#21](/thread/post/9989264#post9989264 "Post Permalink")

  * Jun 18, 2017 2:44am  Jun 18, 2017 2:44am 

  * [ mbes](mbes)

  * | Joined Aug 2009  | Status: Trader | [20 Posts](/search?do=process&provider=Member&searchuser=111011)

Close in profit? What does that mean? How much profit - 1 pip, 100 pips?

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#22](/thread/post/9989277#post9989277 "Post Permalink")

  * Jun 18, 2017 2:50am  Jun 18, 2017 2:50am 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@subheadseven  
What do you mean "not suitable on Friday"?  
This system works well on Friday, but is bad for your health if there is a big weekend gap and a weekend gap in the wrong direction can cause you to hit the 25% stop loss, BUT as said it is not a big problem seeing that trading Fridays does produce a lot more profit.  
Just use the EA you are most comfratable with.  
Or both.  
Do a backtest and pick the one you like most.  
Remember you need to run it at least 6 months to see balanced results.  
  
  
@shiva  
Thanks Shiva.  
I just added the metatrader 4 version for you.  
  
One more thing.  
My code is using a maximum spread limit of :  
GBPJPY=0.040  
GBPUSD=0.00030  
USDJPY=0.070  
  
Anything bigger and it will not open a trade.  
Therefore a commission account is better.  
  
I will later adapt it to use a bigger spread for non commission brokers or for whatever reason.  
  
  
@mbes  
At the moment I close when the profit equals the starting loss (spread+commission loss) PLUS ($0.5 per 0.01 lot on the GBPUSD symbol).  
Profit is seen as anything above what the equity was before I opened the first position(remember I can open 2 position groups at most.).  
I found this to cover whatever spread and commission and even some big slippages seeing that I have got a 400ms slow server to test on. 

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [2017-06-12 09h00 JVB Arbitrage Auto Profit2.ex4](/attachment/file/2359255?d=1497721708) 32 KB | 1,194 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#23](/thread/post/9989314#post9989314 "Post Permalink")

  * Jun 18, 2017 3:24am  Jun 18, 2017 3:24am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar349524_1.gif) SubheadSeven](subheadseven)

  * | Joined Sep 2013  | Status: Trader | [96 Posts](/search?do=process&provider=Member&searchuser=349524)

[quote=jvbJacques;9989277]@subheadseven What do you mean "not suitable on Friday"? This system works well on Friday, but is bad for your health if there is a big weekend gap and a weekend gap in the wrong direction can cause you to hit the 25% stop loss, BUT as said it is not a big problem seeing that trading Fridays does produce a lot more profit. Just use the EA you are most comfratable with. Or both. Do a backtest and pick the one you like most. Remember you need to run it at least 6 months to see balanced results.  
  
Thanks. if so then is ok. i saw your EA named as avoid Friday, so i thought not to trade on Friday. i will have a try, may be on [tickmill](/brokers/tickmill "View Tickmill Broker Profile")'s demo. 

SVT refer to mql5 link

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#24](/thread/post/9989322#post9989322 "Post Permalink")

  * Edited 3:45am  Jun 18, 2017 3:32am | Edited 3:45am 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@subheadSeven  
There are 2 EA groups.  
  
The one that says "avoid Fridays" will not open trades on Fridays.  
Otherwise they are the same.  
The EA that avoid Fridays will have a smaller drawdown of about 18% at worst, while the other one will get stopped out at 25% from time to time (2 time in 2 years), but trading on Fridays does produce a massive amount of extra profit.  
  
Still not nice to see your account drop 25% at once, even though you know it will rise 100% the next 3 months.  
Your heart remembers the losses more than the wins.  
  
WOW and thanks for the tickmill link.  
One thing my strategy use a lot of is a high leverage.  
I only tested it on 200:1, but even with that the profit/loss is extremely small.  
The high amount of trades is what brings in the profit.  
A higher leverage will increase the profit by an order of magnitude.  
  
BEWARE. My EA is hard coded to use a 200:1 leverage.  
Do not use it with a lower leverage else the calculations will cause you to get stopped out or margin called.  
Can use it with a higher leverage, but it will be wasted on this EA.  
I will look into teaching it to detect the leverage and adapting to it.  
Wow a lot of work....I need time ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
  
  
  
@SHIVA and everyone else wanting to use the EA  
Read post one for limitations.  
Especially that the leverage must be 200:1 or higher.  
It is made for 200:1 so the best is exactly 200:1 until I can get around to teaching the EA to detect and adapt to different leverages. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#25](/thread/post/9989334#post9989334 "Post Permalink")

  * Jun 18, 2017 3:55am  Jun 18, 2017 3:55am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar349524_1.gif) SubheadSeven](subheadseven)

  * | Joined Sep 2013  | Status: Trader | [96 Posts](/search?do=process&provider=Member&searchuser=349524)

> [Quoting jvbJacques](/thread/post/9989322#post9989322 "View Quoted Post")
> 
> Disliked
> 
> @subheadSeven There are 2 EA groups. The one that says "avoid Fridays" will not open trades on Fridays. Otherwise they are the same. The EA that avoid Fridays will have a smaller drawdown of about 18% at worst, while the other one will get stopped out at 25% from time to time (2 time in 2 years), but trading on Fridays does produce a massive amount of extra profit. Still not nice to see your account drop 25% at once, even though you know it will rise 100% the next 3 months. Your heart remembers the losses more than the wins. WOW and thanks for the...
> 
> Ignored

Thanks for your clarification and no problem for the tickmill link. Broker claim their demo is almost as same as live. i have both demo and live. They have slightly different and i believe is due to latency. 

SVT refer to mql5 link

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#26](/thread/post/9989337#post9989337 "Post Permalink")

  * Jun 18, 2017 3:56am  Jun 18, 2017 3:56am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar46777_5.gif) shiva](shiva)

  * Joined Aug 2007 | Status: Doing It In Dubai | [2,457 Posts](/search?do=process&provider=Member&searchuser=46777)

> [Quoting jvbJacques](/thread/post/9989277#post9989277 "View Quoted Post")
> 
> Disliked
> 
> @shiva Thanks Shiva. I just added the metatrader 4 version for you. One more thing. My code is using a maximum spread limit of : GBPJPY=0.040 GBPUSD=0.00030 USDJPY=0.070 Anything bigger and it will not open a trade. Therefore a commission account is better. I will later adapt it to use a bigger spread for non commission brokers or for whatever reason. . {file}
> 
> Ignored

Thanks! Like you said, it would be great if you can make the maximum spread as an user input. I am still trying to find one where all three pairs are within the spread-range you mention. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#27](/thread/post/9989346#post9989346 "Post Permalink")

  * Jun 18, 2017 4:02am  Jun 18, 2017 4:02am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar325446_4.gif) kosmo](kosmo)

  * Joined Feb 2013 | Status: constructively provocative | [1,505 Posts](/search?do=process&provider=Member&searchuser=325446)

> [Quoting jvbJacques](/thread/post/9988492#post9988492 "View Quoted Post")
> 
> Disliked
> 
> I do not have funds to test this live, but demo testing seem quite good.
> 
> Ignored

You could start your live journey with as little as $10 (equivalent to $1000 on a standard account) on a **micro** account. Good luck! ![](https://resources.faireconomy.media/images/emojis/64/1f340.png?v=15.1)

mind over matter

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#28](/thread/post/9989349#post9989349 "Post Permalink")

  * Jun 18, 2017 4:03am  Jun 18, 2017 4:03am 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@shiva  
I just removed the leverage limitation, but keep to 200:1 until I can test it with another broker also.  
Will work on the user [spreads](/brokers/spreads "View Live Spreads on the Broker Guide").  
  
What is good spreads for those 3 pairs ?  
  
I used myfxchoive's pro account.  
It is an ENC commission account and the spreads are normally below those values, but I did notice their non commission account does go above them.  
  
I would like to know some suggestions of good brokers for a poor South African like mini me.  
  
@shiva  
I just removed the leverage limitation, but keep to 200:1 until I can test it with another broker also.  
Will work on the user spreads.  
  
What is good spreads for those 3 pairs ?  
  
I used myfxchoive's pro account.  
It is an ENC commission account and the spreads are normally below those values, but I did notice their non commission account does go above them.  
  
I would like to know some suggestions of good brokers for a poor South African like mini me.  
  
@kosmo.  
Thanks, but this strategy is not very effective below $1000 on a 200:1 leverage.  
I suggest $10,000.  
Might be better on a higher leverage so I will find another higher leverage broker to test it later.  
Still. $10 + $40 per month for VPS. Is a lot for me.  
Does not mean I will not stop pondering this strategy and EA , even if I do not have the funds to actually use it ![](https://resources.faireconomy.media/images/emojis/64/1f641.png?v=15.1)  
Maybe someone could find a use for it ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1) Pay it forward ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#29](/thread/post/9989350#post9989350 "Post Permalink")

  * Jun 18, 2017 4:07am  Jun 18, 2017 4:07am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar349524_1.gif) SubheadSeven](subheadseven)

  * | Joined Sep 2013  | Status: Trader | [96 Posts](/search?do=process&provider=Member&searchuser=349524)

> [Quoting kosmo](/thread/post/9989346#post9989346 "View Quoted Post")
> 
> Disliked
> 
> {quote} You could start your live journey with as little as $10 (equivalent to $1000 on a standard account) on a micro account. Good luck! ![](https://resources.faireconomy.media/images/emojis/64/1f340.png?v=15.1)
> 
> Ignored

An excellent idea. 

SVT refer to mql5 link

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#30](/thread/post/9989355#post9989355 "Post Permalink")

  * Jun 18, 2017 4:14am  Jun 18, 2017 4:14am 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@kosmo.  
Thanks, but this strategy is not very effective below $1000 on a 200:1 leverage.  
I suggest $10,000.  
Might be better on a higher leverage so I will find another higher leverage broker to test it later.  
Still. $10 + $40 per month for VPS. Is a lot for me.  
Does not mean I will not stop pondering this strategy and EA , even if I do not have the funds to actually use it ![](https://resources.faireconomy.media/images/emojis/64/1f641.png?v=15.1)  
Maybe someone could find a use for it ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1) Pay it forward ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
  
  
@kosmo and subheadseven  
Even though you can use this strategy with $100 or even $10.  
This will cause all lots to bottom out at 0.01 lots.  
The USDJPY need to be calculated from GBPUSD and therefore if all is the same then they are not balanced and therefore the ZERO point will move a lot and become random and float.  
In backtests $100 works, but in theory I deem it a bit risky.  
  
At $10,000 you can see that USDJPY differs quite a bit from the other pairs, which is good seeing as it causes the ZERO point to be very stable and tradable, even over many months or years.  
This is the main reason this strategy is so low risk, because there is a small limit to what you can lose and this limit is quite fixed, compared to normal forex trading were bottoms can always be broken. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#31](/thread/post/9989359#post9989359 "Post Permalink")

  * Jun 18, 2017 4:18am  Jun 18, 2017 4:18am 

  * [ jacktrader1](jacktrader1)

  * | Joined May 2012  | Status: Trader | [155 Posts](/search?do=process&provider=Member&searchuser=251953)

hey nice strategy. thanks for sharing.  
  
how do you backtest this with mt4?   
  
i keep getting these errors...  
  
2017.06.18 03:14:12.812 2017.05.01 00:00:00 2017-06-12 09h00 JVB Arbitrage Auto Profit3 GBPJPY,H1: **** ERROR1=lastError=**** ERROR at=Time=2017-5-1 0:0 newError=4106 in_Str=GotFxError lastStr=Start1  
2017.06.18 03:14:12.812 2017.05.01 00:00:00 2017-06-12 09h00 JVB Arbitrage Auto Profit3 GBPJPY,H1: *****=maxDrawDown3=0 maxMargin=0 minMarginFreePers=1 maxAccountBalance=200 ERROR=  
2017.06.18 03:14:12.812 2017.05.01 00:00:00 2017-06-12 09h00 JVB Arbitrage Auto Profit3 GBPJPY,H1: **** INIT=AccountLeverage=500 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#32](/thread/post/9989366#post9989366 "Post Permalink")

  * Jun 18, 2017 4:23am  Jun 18, 2017 4:23am 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@jacktrader1  
WOW you have got a 500:1 leverage. NICE ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
  
Unfortunately metatrader 4 does not have the ability to test multiple currency pairs at once.  
Therefore I only backtest using metatrader 5 and then convert the MT5 exclusive coding using my hogwarts training to metatrader 4.  
But I can not test it, except that I do run it using my demo account on live data, but no back tests sorry for metatrader 4. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#33](/thread/post/9989367#post9989367 "Post Permalink")

  * Jun 18, 2017 4:23am  Jun 18, 2017 4:23am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar3609_19.gif) tunera](tunera)

  * | Commercial User  | Joined Sep 2005 | [2,784 Posts](/search?do=process&provider=Member&searchuser=3609)

let me tell you, the only way to have any sort of profit or loss during a triangular arbitrage is when the lotsizes of the 3 trades are not perfectly calculated (you are more exposed on some currencies than the other), thus your profits/losses comes from the fluctuation of such currencs.  
  
Basically you are buying and selling randomly and taking many small profits, what can ever go wrong?  
  
![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#34](/thread/post/9989368#post9989368 "Post Permalink")

  * Jun 18, 2017 4:24am  Jun 18, 2017 4:24am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar325446_4.gif) kosmo](kosmo)

  * Joined Feb 2013 | Status: constructively provocative | [1,505 Posts](/search?do=process&provider=Member&searchuser=325446)

> [Quoting jvbJacques](/thread/post/9989349#post9989349 "View Quoted Post")
> 
> Disliked
> 
> @kosmo. Thanks, but this strategy is not very effective below $1000 on a 200:1 leverage. I suggest $10,000. Might be better on a higher leverage so I will find another higher leverage broker to test it later. Still. $10 + $40 per month for VPS. Is a lot for me. Does not mean I will not stop pondering this strategy and EA , even if I do not have the funds to actually use it ![](https://resources.faireconomy.media/images/emojis/64/1f641.png?v=15.1) Maybe someone could find a use for it ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1) Pay it forward ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)
> 
> Ignored

micro 0.01 equals 0.001 on standard  
$10,000 equals $100 on a micro account, and you can easily get one with a 500:1.  
for a free VPS check out amazon web services  
  
still no good? ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)

mind over matter

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#35](/thread/post/9989380#post9989380 "Post Permalink")

  * Jun 18, 2017 4:33am  Jun 18, 2017 4:33am 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@tunera  
You are correct. Or at least I also think so so I taught the EA to also thinks so.  
  
@kosmo  
Thanks kosmo.  
You are right ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
Just do not try it using this EA as it is hardcoded for 0.01 lots.  
  
But I would love to try it.  
What broker do you suggest that is trustworthy with 500:1 and 0.001 lot size ?  
  
That will still only take it down from $10,000 to $1000, but still a massive improvement.  
  
I was looking at [oanda](/brokers/oanda "View OANDA Broker Profile") some time ago, but their charge $ to use their custom API ![](https://resources.faireconomy.media/images/emojis/64/1f641.png?v=15.1)  
I also do not know if oanda is trustworthy so far.  
But wow they do have the lowest lot sizes.  
  
As for the free amazon web services.  
Could work, but then again they are not directly connected to forex brokers and that in itself will cause lag in trades, which leads to slippage and missed trades. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#36](/thread/post/9989382#post9989382 "Post Permalink")

  * Jun 18, 2017 4:33am  Jun 18, 2017 4:33am 

  * [ jacktrader1](jacktrader1)

  * | Joined May 2012  | Status: Trader | [155 Posts](/search?do=process&provider=Member&searchuser=251953)

thanks for explaining. guess i will know how it runs on monday. btw many brokers offer 1:500, just you need to find one you trust. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#37](/thread/post/9989383#post9989383 "Post Permalink")

  * Jun 18, 2017 4:34am  Jun 18, 2017 4:34am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar349524_1.gif) SubheadSeven](subheadseven)

  * | Joined Sep 2013  | Status: Trader | [96 Posts](/search?do=process&provider=Member&searchuser=349524)

@kosmo and subheadseven Even though you can use this strategy with $100 or even $10. This will cause all lots to bottom out at 0.01 lots. The USDJPY need to be calculated from GBPUSD and therefore if all is the same then they are not balanced and therefore the ZERO point will move a lot and become random and float. In backtests $100 works, but in theory I deem it a bit risky. At $10,000 you can see that USDJPY differs quite a bit from the other pairs, which is good seeing as it causes the ZERO point to be very stable and tradable, even over many months or years. This is the main reason this strategy is so low risk, because there is a small limit to what you can lose and this limit is quite fixed, compared to normal forex trading were bottoms can always be broken.[/quote]  
  
Just my thought. as you said, in backtests $100 works, but in theory you deem it a bit risky. if so, you can go on live, who know you can make 1k or more from 100. if lost, the most is around 80 after margin call. 

SVT refer to mql5 link

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#38](/thread/post/9989388#post9989388 "Post Permalink")

  * Edited 4:55am  Jun 18, 2017 4:42am | Edited 4:55am 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@subheadseven  
You do have a point there.  
$100 will be about $1000 in one year if all goes well.  
$40 x 12 for the vps=$480  
Therefore I need $580 at least to do this for one year and it still need to run another 8 months to get to the $10,000 stable mark.  
Therefore about $900.  
  
The myfxchoice vps becomes free if your trade volume is enough so at $1000 you might get a big enough trade volume to get a free fast vps.  
  
Still.  
$900 = about R15,300 for me.  
Which is beyond my means.  
I did think about it ![](https://resources.faireconomy.media/images/emojis/64/1f641.png?v=15.1) Im a math geek you know ![](https://resources.faireconomy.media/images/emojis/64/1f641.png?v=15.1)  
Still. maybe one day 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#39](/thread/post/9989408#post9989408 "Post Permalink")

  * Jun 18, 2017 5:02am  Jun 18, 2017 5:02am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar349524_1.gif) SubheadSeven](subheadseven)

  * | Joined Sep 2013  | Status: Trader | [96 Posts](/search?do=process&provider=Member&searchuser=349524)

> [Quoting jvbJacques](/thread/post/9989388#post9989388 "View Quoted Post")
> 
> Disliked
> 
> @subheadseven You do have a point there. $100 will be about $1000 in one year if all goes well. $40 x 12 for the vps=$480 Therefore I need $580 at least to do this for one year and it still need to run another 8 months to get to the $10,000 stable mark. Therefore about $900. The myfxchoice vps becomes free if your trade volume is enough so at $1000 you might get a big enough trade volume to get a free fast vps. Still. $900 = about R15,300 for me. Which is beyond my means. I did think about it ![](https://resources.faireconomy.media/images/emojis/64/1f641.png?v=15.1) Im a math geek you know ![](https://resources.faireconomy.media/images/emojis/64/1f641.png?v=15.1)...
> 
> Ignored

May be you can try linkuphost VPS service. is a monthly paid service at $22/mth. so you can start with 122 to go live. 

SVT refer to mql5 link

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#40](/thread/post/9989414#post9989414 "Post Permalink")

  * Jun 18, 2017 5:17am  Jun 18, 2017 5:17am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar325446_4.gif) kosmo](kosmo)

  * Joined Feb 2013 | Status: constructively provocative | [1,505 Posts](/search?do=process&provider=Member&searchuser=325446)

> [Quoting jvbJacques](/thread/post/9989380#post9989380 "View Quoted Post")
> 
> Disliked
> 
> @kosmo Thanks kosmo. You are right ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1) Just do not try it using this EA as it is hardcoded for 0.01 lots. But I would love to try it. What broker do you suggest that is trustworthy with 500:1 and 0.001 lot size ? That will still only take it down from $10,000 to $1000, but still a massive improvement. I was looking at oanda some time ago, but their charge $ to use their custom API ![](https://resources.faireconomy.media/images/emojis/64/1f641.png?v=15.1) I also do not know if oanda is trustworthy so far. But wow they do have the lowest lot sizes. As for the free amazon web services. Could work, but...
> 
> Ignored

Jacques, to make it clear about the micro lots:  
  
0.01 on standard = $0.10 per pip;  
0.01 on micro = $0.010 per pip, so you can still trade your hardcoded 0.01; it will simply be less money per pip;  
hence $100 on micro equals $10,000 on standard, and hence my suggestion in the first place.  
  
Not meaning to be rude, but I'm not interested in your EA, just lending a hand here... 

mind over matter

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Simple High Profit low Drawdown Triangular Arbitrage
  *   * [ **Reply to Thread** ](/thread/676132-simple-high-profit-low-drawdown-triangular-arbitrage/reply#reply)

  * More

[](https://www.forexfactory.com "Homepage")

  * [Forums](forums)
  * [Trades](trades)
  * [Calendar](calendar)
  * [News](news)
  * [Market](market)
  * [Brokers](brokers)

****

[](https://www.faireconomy.com/)

  * 

[Triangular Arbitrage](/thread/64423-triangular-arbitrage "Admin, Please Delete Thread.") 258 replies

[Triangular Arbitrage](/thread/62477-triangular-arbitrage "Is going  
long 1 lot of eur/usd + 
long 1 lot of usd/jpy = long 1 lot of eur/jpy ?  
\(is the ratio of the number of lots correct for a...") 16 replies

[Triangular Arbitrage and carry trade](/thread/71997-triangular-arbitrage-and-carry-trade "Is it possible for us retail traders to be able to make use of Tri Arb or carry trades?  
 
Any one know of retail brokers 
 
 
\(I'm...") 6 replies

[Triangular Arbitrage](/thread/367072-triangular-arbitrage "I've been reading about triangular arbing and was surprised to find that the cross of two majors doesn't always equal what the calculation...") 7 replies

[Question: Trade Mechanics of Triangular Arbitrage](/thread/225246-question-trade-mechanics-of-triangular-arbitrage "Before I even ask this question, please allow me to be very clear.... I have no intention of attempting a triangular arbitrage trade\(for...") 6 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/676132-simple-high-profit-low-drawdown-triangular-arbitrage/reply#reply)
  * Subscribe
  * [147](javascript:void\(0\);)

Attachments: Simple High Profit low Drawdown Triangular Arbitrage

Tags: Simple High Profit low Drawdown Triangular Arbitrage

#  [](/thread/676132-simple-high-profit-low-drawdown-triangular-arbitrage)Simple High Profit low Drawdown Triangular Arbitrage 

  * 

  * [#41](/thread/post/9989419#post9989419 "Post Permalink")

  * Jun 18, 2017 5:23am  Jun 18, 2017 5:23am 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@kosmo  
I understand. thanks. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#42](/thread/post/9989563#post9989563 "Post Permalink")

  * Jun 18, 2017 8:40am  Jun 18, 2017 8:40am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar492187_10.gif) mr.brown](mr.brown)

  * Joined Sep 2016 | Status: Its my biz to know what others dont | [1,280 Posts](/search?do=process&provider=Member&searchuser=492187)

> [Quoting tunera](/thread/post/9989367#post9989367 "View Quoted Post")
> 
> Disliked
> 
> let me tell you, the only way to have any sort of profit or loss during a triangular arbitrage is when the lotsizes of the 3 trades are not perfectly calculated (you are more exposed on some currencies than the other), thus your profits/losses comes from the fluctuation of such currencs. Basically you are buying and selling randomly and taking many small profits, what can ever go wrong? ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)
> 
> Ignored

then open only the difference, simple math, n dont pay truck load of spread comission slippage swap for rest of the entries  
that will take u single entry conventional trading 

WBS Where are Buyers and Sellers

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#43](/thread/post/9989887#post9989887 "Post Permalink")

  * Edited Jun 19, 2017 4:02am  Jun 18, 2017 4:45pm | Edited Jun 19, 2017 4:02am 

  * [ rogelio11](rogelio11)

  * | Joined Sep 2014  | Status: Trader | [63 Posts](/search?do=process&provider=Member&searchuser=383011)

I'm subscribing this thread. this is something i want to try out in and demo account. this strategy can be useful.  
there is a broker named TradersWay offer 1:1000 leverage. i don't work or have any affiliation with them. I only found the info from forex broker reviewers and doing google searching. Also got a account with them as a regular ecn account.  
  
hopefully this EA can work on smaller accounts and somehow try to upscale the account balance equity by doing smaller lots or so. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#44](/thread/post/9990008#post9990008 "Post Permalink")

  * Jun 18, 2017 6:28pm  Jun 18, 2017 6:28pm 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@mr.brown  
simple math yes ...  
Starting to get complicated to build it into an EA, but still a lot of fun ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
  
@rogelio11  
Thanks for the broker roge.  
Keep in mind I build this EA just as a test and testing exclusively using a broker called myfxchoice using a leverage of 200:1.  
Anything else might mess with its head.  
I plan to put a lot more work into it to make it compatible with any flavour of broker settings out there, but it will take time.  
But still ... 1000:1 looks very good.  
I think I'm going to test it a bit.  
  
My other big problem is metatrader 4.  
Yes I did convert it to 4, but I have got no way of testing it, because mt4 can not test multiple currencies at once, so problems can creep in.  
Honestly I actually prefer MT4.  
  
For everyone.  
Keep in mind the EA is unstable.  
I already tested it on another broker and it failed to pick up some settings like swap for some reason.  
If you discover other problems let me know.  
  
As for the theory.  
It still hold firm and true.  
I just need the EA to be smart enough to cater for the technical problems and feed it into the theory.  
  
Almost time for me to go back to work so the updates might slow down until next weekend.  
Im trying to find alternatives to help me continue on this and will let you know as things progress. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#45](/thread/post/9990019#post9990019 "Post Permalink")

  * Jun 18, 2017 6:42pm  Jun 18, 2017 6:42pm 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

Ok this is risky, but I need advice.  
I opened an indiegogo page to help me fund some of the development of this EA seeing that I am received requests and PMs from everywhere for a lot of setting changes and enhancements.  
I appreciate it, but it is a lot of work. ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
I wont paste the link here just yet seeing that I do not know if it is allowed here.  
That is my question.  
Can I or can't I post a link ?  
This EA will be free once done and even before as you can see now in any case, but I need some way of helping or just to speed up the development. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#46](/thread/post/9990102#post9990102 "Post Permalink")

  * Jun 18, 2017 7:51pm  Jun 18, 2017 7:51pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar46777_5.gif) shiva](shiva)

  * Joined Aug 2007 | Status: Doing It In Dubai | [2,457 Posts](/search?do=process&provider=Member&searchuser=46777)

> [Quoting jvbJacques](/thread/post/9990019#post9990019 "View Quoted Post")
> 
> Disliked
> 
> Ok this is risky, but I need advice. I opened an indiegogo page to help me fund some of the development of this EA seeing that I am received requests and PMs from everywhere for a lot of setting changes and enhancements. I appreciate it, but it is a lot of work. ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1) I wont paste the link here just yet seeing that I do not know if it is allowed here. That is my question. Can I or can't I post a link ? This EA will be free once done and even before as you can see now in any case, but I need some way of helping or just to speed up the development....
> 
> Ignored

Jacques, I suggest you message twee and check with him. Any link leading towards fundraising will/may turn your thread in to commercial. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#47](/thread/post/9990109#post9990109 "Post Permalink")

  * Edited 8:29pm  Jun 18, 2017 7:56pm | Edited 8:29pm 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@shiva  
Thanks shiva. I will rather then not include any links.  
My goal is in any-case for everyone to benefit from this and I must say I have seen a lot of shortcomings in the EA which I must look into thanks to this thread.  
Still. The theory remains unchanged, which is a good thing as it shows this is working as expected. So far.  
  
Wow to [spreads](/brokers/spreads "View Live Spreads on the Broker Guide")  
I see now what you mean about so few brokers offering spreads in range of the EA maximum spread limits.  
I have been using fxchoice's enc account and these spreads are quite normal for them, probably making up some of the difference using their commission, which I really do not mind paying anymore seeing the massive spreads of other brokers, even other enc commission brokers.  
  
This is something I need to look into and I will.  
The program need to take into account the different spreads and cater for it in the profit, without moving the ZERO point down, which is happening at the moment.  
Using the myfxchoice spread the ZERO point does not move down much and therefore no need to adjust the EA for it.  
But on other brokers the movement is bigger and sometime so big that the amount of profit that must be made is more than the entry point.  
I should be able to cater for this and have opened an account with [fxpro](/brokers/fxpro "View FxPro Broker Profile") enc, which have got a crazy big spread compared to fxchoice, but a lower commission.  
I will let you know when I have adapted the EA for this seeing that if it can work between such different brokers then it should also work with a range of others.  
  
As for making the spread a user parameter.  
That should not be necessary, because the coding of the program can pick it up.  
At the moment there is no coding to cater for high spread so it just ignores it and just do not open a trade, but in future I will find a way to run even on high spreads by taking into account other factors like commission in the final profit, thereby allowing for higher spreads.  
Coding wise half of the commission is only added to the position once you close it, where spread in a sense is already mostly added once you open it, and the program need to be taught this so it does not calculate the ending profit incorrectly.  
Sorry. Lots of techo babble.  
  
Point is keep an eye on post #1.  
When an update comes I will update post #1.  
  
One thing to keep in mind with this strategy is that it is sensitive to spreads.  
It opens large lot positions and holds it for extremely small profit/loss targets.  
Therefore big spreads will hurt it a lot.  
Commission on the other hand does not affect it so much.  
So I rather go for low spread/high commission than the other way around.  
  
  
@EVERYONE  
Stupid question.  
I made a mistake and opened probably the wrong account on fxpro, but this is a good thing seeing that it revealed something I need to know.  
Comparing my fxchoice to fxpro accounts.  
fxchoice swap=about $30 over 2 years for a very small lot size, but $3 of commission.  
fxpro swap=about $754 over 2 years for ZERO commission.  
Poor EA was crying after this test so I need to teach it not to panic and cater for it.  
Can swap differ so much between brokers?  
I though it was a currency connected value, but it seem now to be broker/account specific.  
Am I correct ? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#48](/thread/post/9990142#post9990142 "Post Permalink")

  * Jun 18, 2017 8:33pm  Jun 18, 2017 8:33pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar46777_5.gif) shiva](shiva)

  * Joined Aug 2007 | Status: Doing It In Dubai | [2,457 Posts](/search?do=process&provider=Member&searchuser=46777)

> [Quoting jvbJacques](/thread/post/9990109#post9990109 "View Quoted Post")
> 
> Disliked
> 
> Poor EA was crying after this test so I need to teach it not to panic and cater for it. Can swap differ so much between brokers? I though it was a currency connected value, but it seem now to be broker/account specific. Am I correct ?
> 
> Ignored

How do you backtest on MT5? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#49](/thread/post/9990239#post9990239 "Post Permalink")

  * Jun 18, 2017 10:23pm  Jun 18, 2017 10:23pm 

  * [ rajandaas](rajandaas)

  * | Joined Jun 2011  | Status: Trader | [176 Posts](/search?do=process&provider=Member&searchuser=182339)

> [Quoting jvbJacques](/thread/post/9988492#post9988492 "View Quoted Post")
> 
> Disliked
> 
> ******************************* Very basic summary ******************************* 1) Buy 1 unit GBPJPY 2) Sell 1 unit GBPUSD 3) Sell ?? units using the USD in point (2) in USDJPY to balance everything out Do this randomly at any time if no open positions. Close in profit and open other direction (1) Sell (2) Buy (3) Buy Close in profit. Rinse and repeat. Can this work or what is the pitfalls with this idea ? ******************************* Detail ******************************* OK I am still new in this, but must say triangular arbitrage looks...
> 
> Ignored

  
  
Hi,  
  
If I buy 1 unit GBPJPY and sell 1 unit GBPUSD then how many units of USDJPY do I sell? Sorry for asking but I don't understand the "??" in para (3). Why can it not be used on a live account? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#50](/thread/post/9990259#post9990259 "Post Permalink")

  * Jun 18, 2017 10:38pm  Jun 18, 2017 10:38pm 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@shiva  
Attached is a picture of the tester.  
Open metatrader-->view-->strategy tester  
Pic the options the same as in the bottom tester part of the picture or make adjustments as you require.  
I also attached an EA I made to show the affect of triangular arbitrage.  
Basically it just opens up a 3 pair trade and never close it.  
This way you can see how it stays at the ZERO point, except for the swap that will bring it down a bit, depending on your broker.  
As stated myfxchoice have got a low swap where fxpro is high.  
Other brokers will also be different.  
Once the test start click on graph at the bottom to see you profit loss run up and down.  
Another window will also open up.  
At the top of this new window is pause and stop button and next to it a slider which you must pull all the way right to increase the test speed.  
Beware.  
Install and use the metatrader supplied by the broker you want to test seeing that I found sometimes that if you use the same metatrader between different brokers that the tester will use the settings for the owner broker on the others, which will give you incorrect results.  
  
@rajandaas  
GBPJPY == 1 lot  
GBPUSD == 1 lot  
USDJPY == 1 lot x GBPUSD(1.27778 lots)  
Think of the EA as a very successful race car that you know will win everything according to the specs on paper.  
And even during testing the race car is the best.  
BUT the engine parts of the race car is put together using duct tape and its weal nuts aren't tied down.  
So sooner or later it will fall apart.  
This was done so that I can quickly build the race car as a proof of concept and to test the theory, but I still have a LOT of work to remove the duct tape and properly fasten everything so that it can run on any broker without falling apart.  
Things like internet problems or metatraders crashes need to be catered for in the EA, which is not at the moment and the EA can not recover from it at the moment.  
Things a test run will not show, but I know about it and will insert it as I get time and funds in to do it.  
I will keep post #1 updated with updates and when it becomes stable enough for live environment I will also post it there for everyone to use.  
  
Not only this, but this EA is very basic and I have already seen multiple ways to increase the profit even further and decrease the drawdown more, which is not implemented yet seeing that I do not want to over complicate the EA at this stage until my original theory is running stable.  
  
So DO NOT USE ON LIVE ACCOUNT PLEASE. NOT YET 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot from 2017-06-18 15-19-57.png
Size: 118 KB](/attachment/image/2359574/thumbnail?d=1497793015)](/attachment/image/2359574?d=1497793015)   

Attached File(s)

![File Type: ex5](https://assets.faireconomy.media/images/attach/ex5.gif) [2017-06-12 09h00 JVB Arbitrage Auto Profit3 Single Trade Showing off triangular arbitrage.ex5](/attachment/file/2359578?d=1497793106) 90 KB | 544 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#51](/thread/post/9990304#post9990304 "Post Permalink")

  * Jun 18, 2017 11:20pm  Jun 18, 2017 11:20pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar159934_4.gif) spyderman](spyderman)

  * Joined Nov 2010 | Status: Snaggin' Some Pips | [2,159 Posts](/search?do=process&provider=Member&searchuser=159934)

> [Quoting jvbJacques](/thread/post/9990109#post9990109 "View Quoted Post")
> 
> Disliked
> 
> @shiva Can swap differ so much between brokers? I though it was a currency connected value, but it seem now to be broker/account specific. Am I correct ?
> 
> Ignored

Yes it can. Pairs involving currencies like Aud and Nzd will cost the trader more across all brokers due to the respective bank rates, but not all brokers pass that through the same. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#52](/thread/post/9990305#post9990305 "Post Permalink")

  * Jun 18, 2017 11:23pm  Jun 18, 2017 11:23pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar159934_4.gif) spyderman](spyderman)

  * Joined Nov 2010 | Status: Snaggin' Some Pips | [2,159 Posts](/search?do=process&provider=Member&searchuser=159934)

Jacques  
  
How do you calculate the base lot size. Lots per x$ of balance? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#53](/thread/post/9990343#post9990343 "Post Permalink")

  * Jun 18, 2017 11:40pm  Jun 18, 2017 11:40pm 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@spyderman  
Thanks.  
I will adapt my EA to detect swap and compensate.  
Should not be too difficult seeing swap make for an EXTREMELY small part of the profit.  
Just be aware that the current EA does not cater for high swaps and will DIE. ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
  
As for the base lot.  
That is a bit more involved.  
I calculate the margin required per lot size and then how how many levels deep I want to go, which at the moment is 2 level, but I am thinking of increasing it.  
Then calculate the amount of profit needed per trade using the amount of lots based on margin requirements and then using a simple loop decrease or increase the amounts to fit the 75% of the account balance.  
Once this is done I use the gap between the (margin for all lots / amount of levels) and the account balance as the stop loss level, which normally account for 25% of the account, but could be less.  
Then I use the difference of the equity before and after opening the trades and add $0.5 per 0.01 lot used for one symbol as the take profit point and also the next level down grid point.  
  
This is not all there is, but the rest of the details are very boring.  
Point is that I cater for failures in the calculation and try to use the whole account balance, while taking in account the maximum loss and profit and margin used.  
  
Now that was a mouth full wasn't it ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
I just love calculations.  
  
The theory might be basic, but implementing it not.  
But then again that is part of my nerd powers .... That and star trek reruns ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#54](/thread/post/9990362#post9990362 "Post Permalink")

  * Jun 18, 2017 11:55pm  Jun 18, 2017 11:55pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar458797_6.gif) EeZeeTrader](eezeetrader)

  * | Joined Apr 2016  | Status: Trader | [103 Posts](/search?do=process&provider=Member&searchuser=458797)

Sterkte met jou thread Jacques!  
  
Subscribed!!! 

Ask and you look stupid for 5 minutes. Don't ask and stay stupid forever.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#55](/thread/post/9990372#post9990372 "Post Permalink")

  * Jun 18, 2017 11:59pm  Jun 18, 2017 11:59pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar53444_2.gif) dagoods](dagoods)

  * Joined Nov 2007 | Status: Trader | [3,059 Posts](/search?do=process&provider=Member&searchuser=53444)

> [Quoting jvbJacques](/thread/post/9990343#post9990343 "View Quoted Post")
> 
> Disliked
> 
> @spyderman Thanks. I will adapt my EA to detect swap and compensate. Should not be too difficult seeing swap make for an EXTREMELY small part of the profit. Just be aware that the current EA does not cater for high swaps and will DIE. ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1) As for the base lot. That is a bit more involved. I calculate the margin required per lot size and then how how many levels deep I want to go, which at the moment is 2 level, but I am thinking of increasing it. Then calculate the amount of profit needed per trade using the amount of lots based on margin requirements...
> 
> Ignored

  

Inserted Video

![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#56](/thread/post/9990383#post9990383 "Post Permalink")

  * Jun 19, 2017 12:02am  Jun 19, 2017 12:02am 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@EeZeeTrader  
![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1) Wel Hallo daar.  
Nogals lekker om 'n ander Suid Afrikaner hier te sien ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
  
@dagoods  
I agree.  
The answer for anything complicated and boring ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#57](/thread/post/9990390#post9990390 "Post Permalink")

  * Jun 19, 2017 12:06am  Jun 19, 2017 12:06am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar458797_6.gif) EeZeeTrader](eezeetrader)

  * | Joined Apr 2016  | Status: Trader | [103 Posts](/search?do=process&provider=Member&searchuser=458797)

> [Quoting jvbJacques](/thread/post/9989380#post9989380 "View Quoted Post")
> 
> Disliked
> 
> What broker do you suggest that is trustworthy with 500:1 and 0.001 lot size ? That will still only take it down from $10,000 to $1000, but still a massive improvement.
> 
> Ignored

I'm using FXPro and have to say the service is good. Money deposits and withdrawals is quick and doesn't cost an arm and a leg.  
  
ACM Gold is locally based in Sandton JHB but their spreads are quite high but also gives you a 500:1 leverage.  
  
Regards  
  
EZ 

Ask and you look stupid for 5 minutes. Don't ask and stay stupid forever.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#58](/thread/post/9990418#post9990418 "Post Permalink")

  * Jun 19, 2017 12:18am  Jun 19, 2017 12:18am 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@EeZeeTrader  
For some reason is there no commission and very high spreads and very high swaps on the demo account I opened at FXPRO.  
This is compared to my fxchoice accounts.  
  
According to their website they do charge commission and have low spreads and swaps so I am confident if I take more time to find that demo account it will do better.  
I probably did something wrong and will check into it a bit later, but for now I am using it as a worst case scenario.  
  
I like to make sure my programs can work with it so that the better accounts can make even more profit.  
  
ACM Gold.... High spreads will hurt this strategy seeing that you open big lots and take very little profit.  
Therefore high spreads goes hand in hand with spreads.  
Meaning you start lower than normal and need to make more profit than other brokers.  
  
The very nature of triangular arbitrage is the small up and down movement and therefore if you start too low then you might never reach the profit point, seeing that unlike normal forex trading this have got a top and bottom level that changes very rarely and if so then very little so NONO to spreads.  
Rather go for commission and low spreads. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#59](/thread/post/9990491#post9990491 "Post Permalink")

  * Jun 19, 2017 12:59am  Jun 19, 2017 12:59am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar46777_5.gif) shiva](shiva)

  * Joined Aug 2007 | Status: Doing It In Dubai | [2,457 Posts](/search?do=process&provider=Member&searchuser=46777)

> [Quoting jvbJacques](/thread/post/9990418#post9990418 "View Quoted Post")
> 
> Disliked
> 
> @EeZeeTrader For some reason is there no commission and very high spreads and very high swaps on the demo account I opened at FXPRO. This is compared to my fxchoice accounts. According to their website they do charge commission and have low spreads and swaps so I am confident if I take more time to find that demo account it will do better. I probably did something wrong and will check into it a bit later, but for now I am using it as a worst case scenario. I like to make sure my programs can work with it so that the better accounts can make even...
> 
> Ignored

What if you open a cashback/rebate account where you get back a percentage of the spread returned to you? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#60](/thread/post/9990520#post9990520 "Post Permalink")

  * Jun 19, 2017 1:18am  Jun 19, 2017 1:18am 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@shiva  
Where can I find more information on these rebates ?  
  
Remember.  
My expertise lie in programming and mathematics.  
Not in forex.  
This strategy is just perfect for the math side of me and the EA for the programming side.  
  
OK I do have a few years of forex back ground, but that was more just dabbling in it until now.  
  
I do not know the inner workings of brokers. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Simple High Profit low Drawdown Triangular Arbitrage
  *   * [ **Reply to Thread** ](/thread/676132-simple-high-profit-low-drawdown-triangular-arbitrage/reply#reply)

  * More

[](https://www.forexfactory.com "Homepage")

  * [Forums](forums)
  * [Trades](trades)
  * [Calendar](calendar)
  * [News](news)
  * [Market](market)
  * [Brokers](brokers)

****

[](https://www.faireconomy.com/)

  * 

[Triangular Arbitrage](/thread/64423-triangular-arbitrage "Admin, Please Delete Thread.") 258 replies

[Triangular Arbitrage](/thread/62477-triangular-arbitrage "Is going  
long 1 lot of eur/usd + 
long 1 lot of usd/jpy = long 1 lot of eur/jpy ?  
\(is the ratio of the number of lots correct for a...") 16 replies

[Triangular Arbitrage and carry trade](/thread/71997-triangular-arbitrage-and-carry-trade "Is it possible for us retail traders to be able to make use of Tri Arb or carry trades?  
 
Any one know of retail brokers 
 
 
\(I'm...") 6 replies

[Triangular Arbitrage](/thread/367072-triangular-arbitrage "I've been reading about triangular arbing and was surprised to find that the cross of two majors doesn't always equal what the calculation...") 7 replies

[Question: Trade Mechanics of Triangular Arbitrage](/thread/225246-question-trade-mechanics-of-triangular-arbitrage "Before I even ask this question, please allow me to be very clear.... I have no intention of attempting a triangular arbitrage trade\(for...") 6 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/676132-simple-high-profit-low-drawdown-triangular-arbitrage/reply#reply)
  * Subscribe
  * [147](javascript:void\(0\);)

Attachments: Simple High Profit low Drawdown Triangular Arbitrage

Tags: Simple High Profit low Drawdown Triangular Arbitrage

#  [](/thread/676132-simple-high-profit-low-drawdown-triangular-arbitrage)Simple High Profit low Drawdown Triangular Arbitrage 

  * 

  * [#61](/thread/post/9990533#post9990533 "Post Permalink")

  * Jun 19, 2017 1:26am  Jun 19, 2017 1:26am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar53444_2.gif) dagoods](dagoods)

  * Joined Nov 2007 | Status: Trader | [3,059 Posts](/search?do=process&provider=Member&searchuser=53444)

> [Quoting jvbJacques](/thread/post/9990418#post9990418 "View Quoted Post")
> 
> Disliked
> 
> @EeZeeTrader For some reason is there no commission and very high spreads and very high swaps on the demo account I opened at FXPRO. This is compared to my fxchoice accounts. According to their website they do charge commission and have low spreads and swaps so I am confident if I take more time to find that demo account it will do better. I probably did something wrong and will check into it a bit later, but for now I am using it as a worst case scenario. I like to make sure my programs can work with it so that the better accounts can make even...
> 
> Ignored

  
how many pips is the typical profit? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#62](/thread/post/9990583#post9990583 "Post Permalink")

  * Jun 19, 2017 1:54am  Jun 19, 2017 1:54am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar458797_6.gif) EeZeeTrader](eezeetrader)

  * | Joined Apr 2016  | Status: Trader | [103 Posts](/search?do=process&provider=Member&searchuser=458797)

> [Quoting jvbJacques](/thread/post/9990418#post9990418 "View Quoted Post")
> 
> Disliked
> 
> The very nature of triangular arbitrage is the small up and down movement and therefore if you start too low then you might never reach the profit point, seeing that unlike normal forex trading this have got a top and bottom level that changes very rarely and if so then very little so NONO to spreads. Rather go for commission and low spreads.
> 
> Ignored

Agreed. My response was purely RE the 500:1 leverage. You definitely need a true ecn broker and NO dealing desk to make your strategy feasible. Will search around and PM you of my findings. 

Ask and you look stupid for 5 minutes. Don't ask and stay stupid forever.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#63](/thread/post/9990607#post9990607 "Post Permalink")

  * Jun 19, 2017 2:05am  Jun 19, 2017 2:05am 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@dagoods  
At the moment I close when the profit equals the starting loss (spread+commission loss) PLUS ($0.5 per 0.01 lot on the GBPUSD symbol).  
Profit is seen as anything above what the equity was before I opened the first position(remember I can open 2 position groups at most.).  
I found this to cover whatever spread and commission and even some big slippages seeing that I have got a 400ms slow server to test on.  
BUT this might change seeing that I found other ways to increase the profit even further, which I am testing now ....  
  
  
@EeZeeTrader  
Thanks.  
My tests on post #1 was with fxchoice and I have found that I can increase the spread quite a bit before it becomes a problem, it is just not build into this EA yet.  
I also found quite a few other brokers offering similar or even better [spreads](/brokers/spreads "View Live Spreads on the Broker Guide") than them, which I would like to test soon as I get time. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#64](/thread/post/9993117#post9993117 "Post Permalink")

  * Jun 19, 2017 8:32pm  Jun 19, 2017 8:32pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar150972_3.gif) !iii!](member.php?u=150972)

  * Joined Aug 2010 | Status: Trader | [146 Posts](/search?do=process&provider=Member&searchuser=150972)

Interesting findings, jvbJ, and hats off, if you get it to work.  
  
So far, I believe you are still in the Fata Morgana stage of backward testing a multiple currency pair spread dependent system. Even if you'd have tick feed for each currency pair, it still means nothing.  
  
I'd like to share some experiences, as I have been where you are now: I assume you are placing sequential market orders to get in and out.  
I once coded a TriArb EA combo with the master instance to be placed on the pair with the most frequent incoming ticks (e.g. GBPAUD) and searching for arb possibilities across all 28 pairs. I further set up 3 slave instances on one chart each (i.e. in total 4 charts open), which served nothing else than receiving calls from the master, as to when to enter and exit. This arrangement allowed me to achieve near synchronous order placement, which I forward tested via several ECN brokers and VPS providers co-located at LD4, LD5 and NY4. The best times I achieved were +/-1 ms for calculations, order placement and ping back/from the trading servers and then between 10-140ms (!) for the trading server itself. I reconfirmed those times with some of the brokers directly.  
  
Since MT4 doesn't cater to parallel order processing and the biggest lag and therefore risk actually derives from the brokers' execution, I gave up my HFT and hedging aspirations. The lags caused 2 major challenges with the usability of a chosen triangle: asynchronous filling (or no filling at all) of orders and slippage in all directions. In order to cover the commission, swap and slippages, you need to have 2 (!) very good execution cycles (in/out), which happens very rarely.  
  
Nevertheless, I'm always keen on hearing other people's experiences and success. 

Augmenting Intelligence

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#65](/thread/post/9993351#post9993351 "Post Permalink")

  * Jun 19, 2017 9:28pm  Jun 19, 2017 9:28pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar53444_2.gif) dagoods](dagoods)

  * Joined Nov 2007 | Status: Trader | [3,059 Posts](/search?do=process&provider=Member&searchuser=53444)

> [Quoting jvbJacques](/thread/post/9990607#post9990607 "View Quoted Post")
> 
> Disliked
> 
> @dagoods At the moment I close when the profit equals the starting loss (spread+commission loss) PLUS ($0.5 per 0.01 lot on the GBPUSD symbol). Profit is seen as anything above what the equity was before I opened the first position(remember I can open 2 position groups at most.). I found this to cover whatever spread and commission and even some big slippages seeing that I have got a 400ms slow server to test on. BUT this might change seeing that I found other ways to increase the profit even further, which I am testing now .... @EeZeeTrader Thanks....
> 
> Ignored

So the bigger the "starting loss" the better, then right  
Why or why not use 10 pips to start with  
  
  
"At the moment I close when the profit equals the starting loss (spread+commission loss) PLUS ($0.5 per 0.01 lot on the GBPUSD symbol)." 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#66](/thread/post/9993429#post9993429 "Post Permalink")

  * Edited 10:00pm  Jun 19, 2017 9:45pm | Edited 10:00pm 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@!iii!  
You are correct and I have a lot more testing and work to do to get this to work.  
One thing I build into the system is that it must be about to handle large slippages.  
Problem is if the slippage/delay happen during the closure of the 3 pairs, but even there I have put in slippage calculations and buffers to cater for it, but further testing is needed.  
As you said. Fata Morgana stage.  
I have a long rode ahead, especially with normal life and working for food coming in the way. Sleep is already a strange word for me, but this is fun so far ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
  
  
  
@dagoods  
No. Bigger starting losses is bad.  
The market does not move much from the ZERO point and if the starting loss is too big then there is a chance it might never move far enough back up to get into profit.  
Unlike the normal forex market movement where a top and bottom can always be broken an arbitrage like this can not, which is what allows for these profits, but also suffers when spreads/starting losses are too big.  
  
Also big starting losses will take longer to move into profit by an order of magnitude from small starting losses.  
This strategy benefits from low profit, high frequency trading.  
Even though the profit per 3 pair trade is extremely low it adds up in the end and it has the added bonus of a predictable low drawdown, except during weekend gaps, which is still low, but higher than normal.  
  
Also my profit calculation is working, but ultimately is not even close to the best option and just a placeholder for something better later.  
As stated earlier this is one of those duct tape strips that need to be removed and replaced with something better, but it is serving its purpose for now.  
  
I tried to stay away from pips and focus on actual USD profit.  
This way I do not have to care about pip this or pop that and can ultimately make this EA broker independent.  
I already made some major improvements in the EA (will post it later) to automatically calculate average spread and monitor and recover from spikes in the market.  
  
I grew tired of all the "MONEY MAKING" EAs out there that promise the world, but fail miserably and then blame the user settings.  
Also.  
I understand wanting money for development, but once your EA is working for a few years then why do you still charge for it seeing that you must be rich already if it works the way you say it does.  
My goal is ultimately to release this EA for free, but also it must have NO USER PARAMETERS if possible.  
It must detect everything automatically.  
Just place on chart and it will work. NOT THERE YET ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#67](/thread/post/9993496#post9993496 "Post Permalink")

  * Jun 19, 2017 9:56pm  Jun 19, 2017 9:56pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar53444_2.gif) dagoods](dagoods)

  * Joined Nov 2007 | Status: Trader | [3,059 Posts](/search?do=process&provider=Member&searchuser=53444)

> [Quoting jvbJacques](/thread/post/9993429#post9993429 "View Quoted Post")
> 
> Disliked
> 
> @!iii! You are correct and I have a lot more testing and work to do to get this to work. One thing I build into the system is that it must be about to handle large slippages. Problem is if the slippage/delay happen during the closure of the 3 pairs, but even there I have put in slippage calculations and buffers to cater for it, but further testing is needed. As you said. Fata Morgana stage. I have a long rode ahead, especially with normal life and working for food coming in the way. Sleep is already a strange word for me, but this is fun so far...
> 
> Ignored

  
TY JV. Please lets consider carefully before we reject any idea. Humor me. I'm trying to picture in my mind what would happen if you purposefully allow the starting loss to be 10 pips.... what happens? In my dream mind, it still hovers around zero, but it goes up much further and down much further, than your current settings, allowing you to take profits much easier. I could be wrong, just using my imaginations. yes? no?  
  
also, curious what happens if you start with EJ rather than GU? Just throwing some ideas that come to mind, possibly will spark imagination for betterment.   
  
I'm so glad you want to share with the world. I always try to share freely as well. If you do release the EA I'd appreciate a copy of the source code. TY again. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#68](/thread/post/9993536#post9993536 "Post Permalink")

  * Jun 19, 2017 10:06pm  Jun 19, 2017 10:06pm 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@dagoods  
Not sure what EJ and GU is.  
  
Problem is that you never know ahead of time exactly what the start loss is as there is slippage involved.  
Sometimes it is below 10 pips and others above.  
The reason I include it in the profit calculation is just a placeholder until I find a way to automatically deduce the commission from the current open orders and to have room for slippage.  
That is coming, but I only have 2 hands and time is my enemy ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
But it is coming.  
  
Later I also want to adapt the EA to work on triangles from other currency pairs and then 10 pips will have a different meaning so there again I try to stay away from it.  
  
In the mean time I am trying to gather enough funds to sponsor this project so I can focus more on it and speed up development.  
Go slow is the word at the moment, but my slow is not that slow ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#69](/thread/post/9993566#post9993566 "Post Permalink")

  * Jun 19, 2017 10:14pm  Jun 19, 2017 10:14pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar150972_3.gif) !iii!](member.php?u=150972)

  * Joined Aug 2010 | Status: Trader | [146 Posts](/search?do=process&provider=Member&searchuser=150972)

I theorized once a slightly different approach, maybe it helps you:  
  
1) You wait until each one of your chosen pairs runs a very low spot spread+commission (=most liquid pair at that point in time) and enter with a long and short order in order to "stock" that pair at a good price (from spread perspective).  
2) Now you wait for the whole ring (USDJPY, EURUSD, EURJPY) to invert (spread compression) and exit with the "stocked" pairs in the direction of the profit.  
3) The remaining stocked orders are still canceling each other out and you can either restart with step 1) or wait for them to run a profit.  
  
The above makes use of liquid positions to pile in, while profiting from liquidity imbalances. 

Augmenting Intelligence

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#70](/thread/post/9993576#post9993576 "Post Permalink")

  * Jun 19, 2017 10:16pm  Jun 19, 2017 10:16pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar159934_4.gif) spyderman](spyderman)

  * Joined Nov 2010 | Status: Snaggin' Some Pips | [2,159 Posts](/search?do=process&provider=Member&searchuser=159934)

> [Quoting jvbJacques](/thread/post/9993536#post9993536 "View Quoted Post")
> 
> Disliked
> 
> Not sure what EJ and GU is. ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)
> 
> Ignored

EJ - EurJpy  
GU - GbpUsd 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#71](/thread/post/9993616#post9993616 "Post Permalink")

  * Jun 19, 2017 10:21pm  Jun 19, 2017 10:21pm 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@spyderman  
Thanks spyderman.  
My ForexFu is weak ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
  
  
  
@!iii!  
1) I am already doing that to a point.  
I am more just calculating the average spread over time and get in if below average.  
  
2) If I understand correctly then I am already doing that along with a mass of other calculations and buffers and stuff I experimented with in my other 225 EAs that worked.  
Call this the frankenstein EA build from parts of all my other 225 EAs.  
  
3) Not sure I understand, but then again I might be reading points 1 and 2 also wrong, but I do appreciate the input ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#72](/thread/post/9993754#post9993754 "Post Permalink")

  * Jun 19, 2017 10:49pm  Jun 19, 2017 10:49pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar150972_3.gif) !iii!](member.php?u=150972)

  * Joined Aug 2010 | Status: Trader | [146 Posts](/search?do=process&provider=Member&searchuser=150972)

Looking at your statements you are _not_ doing what I am referring to.  
  
I am saying to build hedged positions on a pair during its most liquid times - e.g. when the spread on EU is zero - and, when you have a fully stocked triangle - i.e. long & short EU, long & short EJ, long & short UJ - to exit the side (e.g. long EU, long UJ, short EJ) that is in profit due to a momentary imbalance.  
  
Betting on imbalances twice - i.e. getting into a ring and out of it - is playing with fire during "real" (not demo) conditions. 

Augmenting Intelligence

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#73](/thread/post/9993894#post9993894 "Post Permalink")

  * Jun 19, 2017 11:13pm  Jun 19, 2017 11:13pm 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@!iii!  
I will look into it later once this strategy is implemented fully and the EA is stable.  
Thanks for the advice.  
  
I'm only betting on imbalances once to exit in profit, and my EA does cater for the times is does not happen to exit with as little loss as possible.  
The entry is plain and simple random (So long as the spreads are below average).  
  
For those monitoring this thread think about helping out a bit in advice and other means if possible. ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
  
Then for everyone.  
I updated the EA like crazy the past few hours.  
Many thanks for everyone pointing out problems.  
I also added more functionality :  
1) Calculate average spread over time and only get into position if below average spread.  
  
2) Remove the 2 level grid entry to recover from drawdown and keep to just one entry, but scale it down for a small loss over time.  
So no more grid system at stoploss.  
Main reason is to prevent margin call during spikes.  
  
3) Time delay stoploss to cater for weekend gaps and downward spikes and potentially recover.  
This completely removed the weekend gap problem over 2 years, but increased maximum drawdown seen during major market instability to 37%, but the adaptive system can cater for this drawdown easily.  
  
The attached chart starts at $1000 at 2015-06-23 ending 2017-06-19 with net profit of 2,550,930.53.  
Profit can be magnitudes more if split into different accounts seeing that the tester tops out at 99lots by 2016-04-28.  
Before 2016-04-28 it grew exponentially and after 2016-04-28 is grew much slower sequentially seeing that it could not grow the lots size further than 99lots. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: TesterGraphReport2017.06.19.png
Size: 18 KB](/attachment/image/2360916/thumbnail?d=1497881567)](/attachment/image/2360916?d=1497881567)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#74](/thread/post/9994007#post9994007 "Post Permalink")

  * Jun 19, 2017 11:34pm  Jun 19, 2017 11:34pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar150972_3.gif) !iii!](member.php?u=150972)

  * Joined Aug 2010 | Status: Trader | [146 Posts](/search?do=process&provider=Member&searchuser=150972)

I had triangles and whole baskets running live while tracking every tick of equity change over many days. Neither bars nor ticks are truly synchronized in MT4 or MT5, so backtests are meaningless. Again, I don't want to put a negative spin on your efforts but direct your attention to what really matters: real execution during liquidity imbalances. I ran the previously described system parallel on 3 brokers (1 STP with 2+ large liquidity providers and 2 well-known ECN) and while it worked occasionally on the STP, it eventually stopped doing so on all 3....due to increasing slippages / execution lags.  
  
I'll keep watching but mostly when people start putting it on real accounts. Demo is useless. 

Augmenting Intelligence

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#75](/thread/post/9994500#post9994500 "Post Permalink")

  * Jun 20, 2017 1:15am  Jun 20, 2017 1:15am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar429039_1.gif) sajib0189](sajib0189)

  * | Membership Revoked  | Joined Oct 2015 | [164 Posts](/search?do=process&provider=Member&searchuser=429039)

why the EA either profit 2 or 3 not working in my acc? where the setting? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#76](/thread/post/9994959#post9994959 "Post Permalink")

  * Jun 20, 2017 3:35am  Jun 20, 2017 3:35am 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@!iii!  
It will be sorry if this do not work, but here's hoping.  
I'm like a dog with a bone and this bones tastes juicy ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)   
If it turns out to be a plastic bone I will still have fun.  
  
I have now tested using 2 brokers and both make profit, all be it a massive difference in profit.  
myfxchoice = 2,700,000 and [fxpro](/brokers/fxpro "View FxPro Broker Profile") = 300,000 on a $1000 account.  
So far it looks like the massive amount of spread difference between the 2 accounts and indirectly because this causes less trades on fxpro.  
I have seen other broker like yforex ,but they are only metatrader 4 compatible so I can do no backtesting there.  
Demo forward testing will take a long time seeing that anything less than 3 months does not conform to my standards of testing.  
I do have demo forward tests running, but it like watching paint dry and still on a old version of the EA which I need to replace and start over ![](https://resources.faireconomy.media/images/emojis/64/1f641.png?v=15.1)  
  
I have got a limited amount of time so as I get more time I will test more.  
  
I do agree that large fluctuations in the triangle does not happen a lot, but this strategy can make use of minute fluctuation, although the big ones do help.  
Sometimes I get one trade every 5 days, but that is fine, so long as the cumulative profits is there in the end.  
Other times I get 5 trades in a minute.  
  
I'm hopeful this will work, but beacktesting is the best place to develop and it speeds up development a lot.  
Once that is done then the demo/live testing starts.  
  
The theory still hold true for me, and since the beginning of this venture the theory has not changed a bit, which to me is a good sign.  
The EA is another monster and needs a lot of work.  
  
  
  
@sajib0189  
The EA has got limitation on the maximum spread allowed per symbol pair.  
If your spread is bigger then it will not trade it.  
  
I have got a new version that will work out the average spread and use that rather.  
You can add the logs for me to look at.  
  
But please note the EA is UNSTABLE at this stage.  
Made on myfxchoice with 200:1 leverage and strict spreads.  
Anything else is just luck if it works.  
  
I want this EA to work without options and it takes time to look at everything. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#77](/thread/post/9995450#post9995450 "Post Permalink")

  * Jun 20, 2017 6:30am  Jun 20, 2017 6:30am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar444411_1.gif) savanhws](savanhws)

  * | Joined Jan 2016  | Status: Trader | [38 Posts](/search?do=process&provider=Member&searchuser=444411)

> [Quoting jvbJacques](/thread/post/9988847#post9988847 "View Quoted Post")
> 
> Disliked
> 
> But for this instance I do have another catch. If I open a position and I see that this position stays open for more than 3 days then I will check for the lowest point over the last floating 3 days time and if this low point is hit again I will open another position in the same direction to counter the ZERO point move. This way the price only have to move half way back to get into profit and close the whole position. You will see this happening in the cart I added above on the bottom DEPOSIT LOAD.{image}
> 
> Ignored

Hey Jacques, can you explain in details what do you do to your position after after the 3 days of "non-profit" because  
I would like to use your strategy manually. ("Deposit Load")  
So for example; GBPJPY sell @ 1 lot  
GBPUSD buy @ 1 lot  
USDJPY buy @ 1.43 lot  
how would I do it manually for it to go back half way to be in profit and on which pair? (Your recover strategy)  
thx dude 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#78](/thread/post/9995498#post9995498 "Post Permalink")

  * Jun 20, 2017 6:49am  Jun 20, 2017 6:49am 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@savanhws  
Before I open an position I save the current equity/balance.  
Called EQUITYSTART.  
  
I then hold the position until in profit.  
  
If not profit for 5 days then I check what the lowest point was during these 5 days.  
The is a running 5 days so I only check 5 days back.  
For example if the position was open for 7 days then I just check for the lowest point 5 days back, not 7.  
Call this low point LOW5.  
  
Now I wait again until the price hits or goes below LOW5.  
At this point I use to then open another triangle same as previous one and wait 5 days again and if in the next 5 days it is still not in profit then I stopLoss and close all positions.  
I changed this part now for a lot more profit.  
  
Now once LOW5 is hit or price goes below it then I just set the EQUITYSTART TO this LOW5 point and let it run for 5 days again and again and again.  
The system will then calculate profit from this new EQUITYSTART value, which normally mean a small loss.  
So far in my testing I have only hit LOW5 about 8 times in 2 years time.  
  
Use to happen mainly with weekend gaps, but I have a solution for that in that I see it as a spike and ignore it for 1 hour after weekend and normally the price recovers.  
  
I do the 5 day wait because most of the time the drop is just a spike and I do not want to be stopped out on a spike.  
If for some reason the spike is massive then I have got a global stopLoss that will close everything at 25% drop, but I have not seen that since my first EA...  
Then again I have about 10 other tricks in the system to cater for spikes and drops and slippages and to recover gracefully from them.  
  
I am already thinking of other recovery strategies I want to try and use, but that have to wait till I get time so that I can focus on stabilising the system a bit more.  
  
As for manual trading.  
Good luck. You must be fast.  
A lot of traders are done with gaps of a couple of days, but then you get those high movement days where the price moves within minutes or seconds.  
You got to glue yourself to the screen to catch those and those fast movers make a lot of profit.  
Does not happen often and months can go by without seeing that movement. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#79](/thread/post/9996107#post9996107 "Post Permalink")

  * Jun 20, 2017 11:41am  Jun 20, 2017 11:41am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar444411_1.gif) savanhws](savanhws)

  * | Joined Jan 2016  | Status: Trader | [38 Posts](/search?do=process&provider=Member&searchuser=444411)

Got it, thx 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#80](/thread/post/9996804#post9996804 "Post Permalink")

  * Jun 20, 2017 4:34pm  Jun 20, 2017 4:34pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar150972_3.gif) !iii!](member.php?u=150972)

  * Joined Aug 2010 | Status: Trader | [146 Posts](/search?do=process&provider=Member&searchuser=150972)

> [Quoting jvbJacques](/thread/post/9994959#post9994959 "View Quoted Post")
> 
> Disliked
> 
> @!iii!...Demo forward testing will take a long time seeing that anything less than 3 months does not conform to my standards of testing. I do have demo forward tests running, but it like watching paint dry and still on a old version of the EA which I need to replace and start over ![](https://resources.faireconomy.media/images/emojis/64/1f641.png?v=15.1) I have got a limited amount of time so as I get more time I will test more. I do agree that large fluctuations in the triangle does not happen a lot, but this strategy can make use of minute fluctuation, although the big ones do help. Sometimes I get one...
> 
> Ignored

The backward tests are good to iron out your bugs in the code, but that's about it.  
  
You can skip the demo forward test right away and go to live. Demo servers are sometimes reflecting the same feed like the live servers, but not necessarily. It depends on the broker. From a filling and execution point of view, demo servers are useless for what you are seeking. The times of liquidity imbalance when your signals shoot 5 times within a few seconds (= market confusion = chaotic volatility = broker confusion = platform freeze ) are a Fata Morgana - you'll get one entry at best and the lag from the first order will kill it for the rest. My personal record was entering and exiting a profitable arb (i.e. 6 transactions) in 50ms. That doesn't happen often - at all.  
  
The smaller the lot sizes, the less precise the hedging, obviously. So keep that in mind, when you go live.  
  
Good luck. 

Augmenting Intelligence

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Simple High Profit low Drawdown Triangular Arbitrage
  *   * [ **Reply to Thread** ](/thread/676132-simple-high-profit-low-drawdown-triangular-arbitrage/reply#reply)

  * More

[](https://www.forexfactory.com "Homepage")

  * [Forums](forums)
  * [Trades](trades)
  * [Calendar](calendar)
  * [News](news)
  * [Market](market)
  * [Brokers](brokers)

****

[](https://www.faireconomy.com/)

  * 

[Triangular Arbitrage](/thread/64423-triangular-arbitrage "Admin, Please Delete Thread.") 258 replies

[Triangular Arbitrage](/thread/62477-triangular-arbitrage "Is going  
long 1 lot of eur/usd + 
long 1 lot of usd/jpy = long 1 lot of eur/jpy ?  
\(is the ratio of the number of lots correct for a...") 16 replies

[Triangular Arbitrage and carry trade](/thread/71997-triangular-arbitrage-and-carry-trade "Is it possible for us retail traders to be able to make use of Tri Arb or carry trades?  
 
Any one know of retail brokers 
 
 
\(I'm...") 6 replies

[Triangular Arbitrage](/thread/367072-triangular-arbitrage "I've been reading about triangular arbing and was surprised to find that the cross of two majors doesn't always equal what the calculation...") 7 replies

[Question: Trade Mechanics of Triangular Arbitrage](/thread/225246-question-trade-mechanics-of-triangular-arbitrage "Before I even ask this question, please allow me to be very clear.... I have no intention of attempting a triangular arbitrage trade\(for...") 6 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/676132-simple-high-profit-low-drawdown-triangular-arbitrage/reply#reply)
  * Subscribe
  * [147](javascript:void\(0\);)

Attachments: Simple High Profit low Drawdown Triangular Arbitrage

Tags: Simple High Profit low Drawdown Triangular Arbitrage

#  [](/thread/676132-simple-high-profit-low-drawdown-triangular-arbitrage)Simple High Profit low Drawdown Triangular Arbitrage 

  * 

  * [#81](/thread/post/9997688#post9997688 "Post Permalink")

  * Edited 9:35pm  Jun 20, 2017 8:20pm | Edited 9:35pm 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@!iii!  
I realise there is lag and slippages, but I do not have funds to go live so my only options are backtesting and demo.  
  
Unluckily or luckily my demo account has got a 300 to 400ms delay, so at least that will test a bit of slippage.  
  
Lot sizes are important and I found anything below $1000 is risky. Another reason I can not go live. I can write the EA, but I can not use it.  
At least it is fun so far. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#82](/thread/post/9998239#post9998239 "Post Permalink")

  * Jun 20, 2017 10:28pm  Jun 20, 2017 10:28pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar150972_3.gif) !iii!](member.php?u=150972)

  * Joined Aug 2010 | Status: Trader | [146 Posts](/search?do=process&provider=Member&searchuser=150972)

It will remain theoretical then, unfortunately.  
  
Nevertheless, your thread brought me back to my own studies into identifying the currencies causing the imbalance and finding the pair(s) to trade it - ideally only one. Both the arb and accumulated spread calculations result in timeseries of stationary nature and it is just too tempting not to try do something with that...  
  
Again, good luck with your project. 

Augmenting Intelligence

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#83](/thread/post/9998310#post9998310 "Post Permalink")

  * Jun 20, 2017 10:38pm  Jun 20, 2017 10:38pm 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@!iii!  
Thanks and thank you for your input ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#84](/thread/post/9998387#post9998387 "Post Permalink")

  * Jun 20, 2017 10:50pm  Jun 20, 2017 10:50pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar150972_3.gif) !iii!](member.php?u=150972)

  * Joined Aug 2010 | Status: Trader | [146 Posts](/search?do=process&provider=Member&searchuser=150972)

Very last one: you mention your lag of 300-400ms. Your aim must be to get that down to zero. With the exception of your client receiving ticks, all your procedures in MT4 are sequential. You can get around the tick based refreshes by using a milliseconds based timer event in your EA - with the risk of using stale ticks also. In the time when the ticks and your orders travel from and to the trade server, prices change. No matter how close you are to the trade server, you are always seeing a broker digested past.  
  
Cheers. 

Augmenting Intelligence

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#85](/thread/post/9998452#post9998452 "Post Permalink")

  * Jun 20, 2017 10:58pm  Jun 20, 2017 10:58pm 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@!iii!  
I know, but as I said I see that 300ms - 400ms delay as a good thing for testing purposes.  
Similar to slippages.  
By the time the buy/sell order reach the broker the price has most definitely changed.  
Therefore I see this as worst case scenario.  
If I can make it work on a bad server like this then it will work even better on a good server later.  
  
I will never run a live test on this lag server, just tests.  
  
I always program for the worst, rather than the best and in this case I would sacrifice some of the profit if it make the program more stable and able to survive bad times.  
  
In any case.  
This is what I have to work with and even though it is slowing down development, it is better than nothing and I can make do. :| 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#86](/thread/post/9999724#post9999724 "Post Permalink")

  * Jun 21, 2017 3:46am  Jun 21, 2017 3:46am 

  * [ Greg0r](greg0r)

  * | Joined Mar 2015  | Status: Trader | [93 Posts](/search?do=process&provider=Member&searchuser=404070)

Thanks for sharing. I like your idea very march. Do you try to use another pairs for trading? For example : EURJPY EURUSD USDJPY. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#87](/thread/post/9999743#post9999743 "Post Permalink")

  * Jun 21, 2017 3:52am  Jun 21, 2017 3:52am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar446102_2.gif) dragonexpert](dragonexpert)

  * | Membership Revoked  | Joined Feb 2016 | [590 Posts](/search?do=process&provider=Member&searchuser=446102)

slippage and spread will kill us. i think worth to try 

Risk comes from not knowing what you're doing.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#88](/thread/post/9999986#post9999986 "Post Permalink")

  * Jun 21, 2017 5:04am  Jun 21, 2017 5:04am 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@GregOr  
I will try others later.  
I first want to get this program finished and stable by focusing on one triangle.  
  
The program is already compatible with EURJPY EURUSD USDJPY and any others, but I am already struggling to do all the coding inbetween other work to fund this project, so I would rather focus on a few things at time and once everything is stable then I will Add the option to do other triangles.  
My idea was to use the triangle that is part of the chart you attach it to, but that is something for another day.  
  
  
@dragonexpert  
Absolutely, mostly spread.  
So the lower the better.  
I am now busy building in some buffers to cater for higher [spreads](/brokers/spreads "View Live Spreads on the Broker Guide"), but that does affect the profit a bit, but worth it.  
Still months away from a final live EA at this rate. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#89](/thread/post/10000180#post10000180 "Post Permalink")

  * Jun 21, 2017 6:14am  Jun 21, 2017 6:14am 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

I had an itch to scratch.  
Some interesting findings.  
I tested the leverage affect.  
  
Keep in mind that this version of the program is a few versions newer than the one in post #1.  
I will add it or a better version a bit later.  
  
Unfortunately my account only go up to a 200:1 leverage.  
Starting with $1000.  
  
Time period tested between 2015.06.23 --> 2016-03-23  
  
Leverage 50:1  
End = $4013.61  
Max Lots = 0.43  
MaxoutDte =  
Draw Down = 09.087307875138648%  
  
Leverage 100:1  
End = $18,546,35  
Max Lots = 3.43  
MaxoutDte =  
Draw Down = 18.18960949917412%  
  
Leverage 200:1  
End = $107,431.65  
Max Lots = 38.53  
MaxoutDte =  
Draw Down = 37.456292074711% 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#90](/thread/post/10000296#post10000296 "Post Permalink")

  * Jun 21, 2017 7:18am  Jun 21, 2017 7:18am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar20956_6.gif) crashout](crashout)

  * | Joined Oct 2006  | Status: Trader | [373 Posts](/search?do=process&provider=Member&searchuser=20956)

Interesting work man, really good.  
  
Of course, higher leverage means higher profits, but bigger risks.  
  
Nonetheless, you realize you have here very good results, that all traders could only dream of.  
  
I think it worth a try, with spreads, etc ... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#91](/thread/post/10000356#post10000356 "Post Permalink")

  * Jun 21, 2017 7:55am  Jun 21, 2017 7:55am 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@crashout  
Thanks.  
I actual improved profit since previous post by 50% and draw down decreased by 5%.  
  
I still insist you NOT use the EA on a live account yet.  
  
I can monitor the EA and compensate for any unforeseen problems while the current EA is incapable of doing it herself.  
And unfortunately I have no funds to test it live at all and what I have is focused on the development of this project.  
  
Once ready I will tell all and you can use it freely, but that might take quite some time. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#92](/thread/post/10000362#post10000362 "Post Permalink")

  * Jun 21, 2017 7:59am  Jun 21, 2017 7:59am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar2942_8.gif) Nicholishen](nicholishen)

  * Joined Jul 2005 | Status: zzzzzzzzzzzzzzzzzzzzzzzzz zzzzzzzzzz | [1,261 Posts](/search?do=process&provider=Member&searchuser=2942)

OP,  
  
Well done on making a good EA...  
  
...however, (I hate to be the bearer of bad news) this has been tried many times on metatrader going back to '06, and it doesn't work. You might--maybe have a chance with MT5 asychronous orders on the best ECN broker in the universe, but even then you're competing with hedge funds with real big-boy HFT platforms running on colocated servers and full LP book access with sub-millisecond transaction times.   
  
A couple of things to note: 

  1. If there are any draw-downs (at all) then the lot sizes are miscalculated (all currency units aren't hedged) and _it's not arbitrage_. In this case you're better of trading those units straight up to free up margin and reduce swap.
  2. Trades are not entered into arbitrarily. The fractional product of inefficiency must first be calculated for bid and ask and then run through an algo that can determine whether the spreads and commissions can be covered by a relative swing in the opposite direction.
  3. The back-tester sucks at multi-currency (even MT5 which was designed for MC). In theory this is how arbitrage works, but with the back-tester it's garbage in garbage out. Backtester feeds in simulated ticks. You will never see these tick disparities IRL.

Back in the day we were using this system to arb swap by finding market neutral hedge rings with net positive swap, but those day are also long gone...   
  
Here is the OG thread that started the rush to this type of system... [https://www.kreslik.com/forums/neoti...ble-hedge-t307](https://www.kreslik.com/forums/neoticker-indicators/fpi-fractional-product-inefficiency-the-impeccable-hedge-t307)

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#93](/thread/post/10000399#post10000399 "Post Permalink")

  * Jun 21, 2017 8:23am  Jun 21, 2017 8:23am 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@Nicholishen  
Thanks for the information and I will definitely look into the material you supplied me.  
  
I am still not at the stage where I can go live, but I am almost at the stage where I can start running on demo accounts with hopefully realistic price feeds.  
The slippage and missed trades parts can only be tested on live accounts, but I have already build in buffers to cater for those.  
If the demos can prove the potential for market inefficiency, similar or maybe even less than the back tests then I will be happy.  
  
Still.  
I love calculations and coding so I will be pushing this until I hit a brick wall and have conclusively proven it can not be done or alternatively it can.  
In theory there must be inefficiencies in the live environment.  
That to me is not a question, but my question is if the inefficiencies are big enough to make a profit on.  
So far even bad spread demo back tests are making profits so I am hopeful the demo/live price feeds can reflect some of these profits.  
I'm still far away from finishing all my coding and tests seeing that it is very difficult for me to take of work during the week without funds to support me, so this is an after hours/weekend project, which will eventually be done.  
  
Let hope and see ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#94](/thread/post/10006519#post10006519 "Post Permalink")

  * Jun 22, 2017 6:04pm  Jun 22, 2017 6:04pm 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

Please everyone.  
  
I have received a LOT of PMs about how people want to run the EA on this and that and I am grateful you find it interesting, but please note that I am one person doing a lot of work and coding like crazy as I get time.  
For now the EA was developed on MYFXCHOICE's pro account on a 1:200 leverage and worst of all it ignores swap and some high spreads.  
This new version I have not uploaded yet takes these and more into account.  
  
Remember the theory is based on a perfect world without spread, swap or commission.  
Now for the amount of profit it generates those losses are small and should not interfere with the profit, but the EA does not know that and that is were all the coding time goes into is for the EA to realise that this is not a perfect world and to take it into account in its calculations or risk getting stuck or making bad choices.  
  
Note that the EA in post 1 is very unstable.  
I have spent all of 1 day working on it during the weekend.  
  
It might be good for back testing it on myfxchoice's pro demo account on MT5, but not much more.  
  
I have been working on it to the disappointment of my wife so I do have a much better version almost ready.  
  
I tested the EA on my [fxpro](/brokers/fxpro "View FxPro Broker Profile") account, which has got no commission, but bad swap and spreads.  
It kills the poor EA, which does not take swap into account seeing that fxchoice's swap is negligible.  
  
I just taught the EA to look at current swap loss and ignore it, and it runs much better and into profit, which the one in post 1 most certainly will not as it get stuck in a swap loss loop it knows nothing about.  
  
Problem is that triangle arbitrage profit/loss is very little and stable.  
Therefore if I do not take into account swap then it will go down bit by bit, but enough to prevent to open position to go back into profit.  
Now in the grand scheme of things swap is but a minor part of profit.  
So by ignoring it I lose a little profit on one ticket, but then the ticket can close as normal at a profit-swap(witch could be a small loss) and then allow for other tickets to be opened after it to pick up the slack and ultimately generate more profit.  
  
This strategy need lots of trades to profit.  
So being stuck because of swap is a NO NO, which I did not cater for.  
I'd rather close a long lived trade in loss than have it hold up other more profitable trades after it.  
  
Still a lot of stuff to do.  
Will update the forum once this EA it ready to be released.  
  
WARNING: DO NOT USE THE EA ON A LIVE ACCOUNT.  
It is just there to test the theory, but it is unstable.  
  
As I get time I will improve it, but I am still months away from a fully stable version so be patient or support me to speed up development.  
  
But never stop posting ideas.  
I need to get this theory bomb proof by putting it through the grinder to see if it can survive anything.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#95](/thread/post/10008063#post10008063 "Post Permalink")

  * Jun 22, 2017 11:36pm  Jun 22, 2017 11:36pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar53444_2.gif) dagoods](dagoods)

  * Joined Nov 2007 | Status: Trader | [3,059 Posts](/search?do=process&provider=Member&searchuser=53444)

wondering if we are better served with instead of triangular arbitrage...correlation arbitrage>>>>> <https://www.forexfactory.com/showthread.php?t=677100>

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#96](/thread/post/10008170#post10008170 "Post Permalink")

  * Jun 22, 2017 11:50pm  Jun 22, 2017 11:50pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar150972_3.gif) !iii!](member.php?u=150972)

  * Joined Aug 2010 | Status: Trader | [146 Posts](/search?do=process&provider=Member&searchuser=150972)

> [Quoting dagoods](/thread/post/10008063#post10008063 "View Quoted Post")
> 
> Disliked
> 
> wondering if we are better served with instead of triangular arbitrage...correlation arbitrage>>>>> <https://www.forexfactory.com/showthread.php?t=677100>
> 
> Ignored

Correlation in non-stationary timeseries is based on a faulty concept. Co-integration is a better approach for Statistical Arbitrage, but all the inherent challenges of choosing the right sample size, dealing with stochastic trends, etc remain and render it as useless.  
  
Check out the relevant posts of Codebreaker : [https://www.forexfactory.com/showthr...02#post1927002](https://www.forexfactory.com/showthread.php?p=1927002#post1927002)

Augmenting Intelligence

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#97](/thread/post/10008207#post10008207 "Post Permalink")

  * Jun 22, 2017 11:56pm  Jun 22, 2017 11:56pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar53444_2.gif) dagoods](dagoods)

  * Joined Nov 2007 | Status: Trader | [3,059 Posts](/search?do=process&provider=Member&searchuser=53444)

> [Quoting !iii!](/thread/post/10008170#post10008170 "View Quoted Post")
> 
> Disliked
> 
> {quote} Correlation in non-stationary timeseries is based on a faulty concept. Co-integration is a better approach for Statistical Arbitrage, but all the inherent challenges of choosing the right sample size, dealing with stochastic trends, etc remain and render it as useless. Check out the relevant posts of Codebreaker : [https://www.forexfactory.com/showthr...02#post1927002](https://www.forexfactory.com/showthread.php?p=1927002#post1927002)
> 
> Ignored

  
codebreaker is very smart...but i respectfully disagree that you need causality in order to profit from inefficiency. you do not IMO BTW the only casual predictive model in nature is synchronization.. for example...when you put 5 females in a house together you can predict with 100% certainty that their menstrual cycles will align lol. they can predict certain things about locusts and cows and such kinds of groups it's very interesting... the market is the same... it is a herd ... if you want causality that is probably your best bet... not seen it applied to markets yet however.... would be fun to predict the herd! lol 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#98](/thread/post/10008356#post10008356 "Post Permalink")

  * Jun 23, 2017 12:27am  Jun 23, 2017 12:27am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar150972_3.gif) !iii!](member.php?u=150972)

  * Joined Aug 2010 | Status: Trader | [146 Posts](/search?do=process&provider=Member&searchuser=150972)

How do you define inefficiency, when you don't know efficiency other than statistics occasionally lining up. I can create a non-forex "Synthetic" for USDCAD (btw given that any relative such as pair pricing becomes a spread why would adding more or comparing it with other spreads mean anything?) that lines up beautifully / correlates and then inverts. Does that mean it is now out-of-sync / inefficient and will mean-revert ? And at what weights measured from where ? I don't believe in the value-price concept being superior. Of course, exposure needs to be hedged in other markets but it is not consistently predictable. There is no objective inefficiency, there is only order flow, liquidity and spread.  
  
Let's not deviate from the topic of this thread being deterministic arbitrage. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: StatArb.png
Size: 53 KB](/attachment/image/2366369/thumbnail?d=1498145263)](/attachment/image/2366369?d=1498145263)   

Augmenting Intelligence

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#99](/thread/post/10008818#post10008818 "Post Permalink")

  * Edited 9:40pm  Jun 23, 2017 2:14am | Edited 9:40pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar53444_2.gif) dagoods](dagoods)

  * Joined Nov 2007 | Status: Trader | [3,059 Posts](/search?do=process&provider=Member&searchuser=53444)

yes. arbitrage is the thread's purpose... arbitrage of correlated pairs may be doable...[https://www.forexfactory.com/showthr...99#post8376599](https://www.forexfactory.com/showthread.php?p=8376599#post8376599) despite your objections, i've not heard any reason that makes me say "oh that's why it isn't doable"......i have OTOH seen many traders post, based on actual experience, many reasons why triangular arbitrage won't work in a live market... i simply offered an alternative approach, that may or may not be better...  
  
2 cents 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#100](/thread/post/10018624#post10018624 "Post Permalink")

  * Edited 9:27pm  Jun 26, 2017 9:09pm | Edited 9:27pm 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

Good news everybody...  
I just invented an ice cream toaster oven.  
  
On other news.  
I updated the EA with a mas amount of improvements.  
DO NOT USE ON LIVE ACCOUNT PLEASE.  
  
Keep in mind I tested this on my MyFxChoice MT5 account using 1:200 leverage.  
I also tested this on a FxPro account, but for some reason there is no commission and extremely high spreads on this fxpro account, which tells me I made a mistake in picking the wrong account there, but it still made a lot of profit so it is a good bad situation test.  
I also used $1000 starting balances for the tests.  
I do not suggest smaller.  
  
I did not have time to test on other brokers or see why my fxpro account is problematic.  
I also did not have time to convert to MT4 this time sorry, will do so much later as I get time.  
  
Some of the things I put into the EA:  
1) Base triangle strategy of buying at random, holding and selling at profit.  
  
2) Grid strategy to increase the position size 3 times as loss increase over specific time periods with special calculations to check for spikes and zero point movement.  
  
3) Stop loss at 25% drop during new stating position.  
  
4) Use opening start position loss (commission+spread+whatever costs) as profit take point and grid level loss points.  
  
5) Calculate average spread over a day and use spreads below as potential position opening points.  
Start at beginning with no history with current spread as average.  
  
6) Calculate equity low point since position start open over a 1 hour rolling period to calculate new grid entry points to be below it, else do not enter.  
Done to detect spikes and market stability.  
  
7) Calculate 4 grid full margin levels gap before opening a new position.  
Will only use 3, 4th is to ensure gap for stopLoss and to prevent margin call on 100% margin accounts.  
Also decreases drawdown to 7% and increases least free margin to 38% as seen over 2 years back test.  
  
8) Increased processing speed by removing some testing calculations and decreasing amount of logs from "you are nuts" to "are you sure you aren't nuts?".  
  
9) Take into account swap and ignore swap during profit take to stop swap bleed and take the knock during ultimate profit, which is minor.  
  
10) A lot more :  
I went through 10 versions since last week so a lot more was done, tested, removed, added.  
Some small some large.  
My coffee ran out so my brain stopped keeping track of all the changes ....  
But WOW it is working.  
  
6% growth forward test demo last week (5 days).  
80% growth since last month 5/23 back test.  
Then server crashed ![](https://resources.faireconomy.media/images/emojis/64/1f641.png?v=15.1) need new hard drive.  
Will see when I can fix it later.  
  
Sorry that the updates is taking so long.  
Sleep is getting in the way, and work, and running out of funds.  
Still not stopping ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
  
Good luck all, BUT DO NOT USE ON LIVE ACCOUNT.  
Still too unstable.  
My server crashed during forward test and it can not pick up where it left off YET.  
I still need to build those things in as I get time, but it will be devastating to a LIVE account.  
  
Still to do:  
Recover from crashes, internet problems and anything I can think of.  
1) Allow EA pause before opening new positions to allow for funds extract out of account, without affecting EA.  
2) Maybe not pause, but something to indicate the amount of fund it must keep aside and to notify you when the funds are available for extraction.  
3) Get history from broker history on new start and/or store history data in file that can survive crashes and other problems for a smooth restart and continuation of running period calculations.  
  
Do not tell my wife.  
If she know what I have been doing during my free time she will be extremely mad ![](https://resources.faireconomy.media/images/emojis/64/1f641.png?v=15.1)  
Im afraid ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1) lol 

Attached File(s)

![File Type: ex5](https://assets.faireconomy.media/images/attach/ex5.gif) [2017-06-12 09h00 JVB Arbitrage Auto Profit4.ex5](/attachment/file/2370471?d=1498478935) 81 KB | 545 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Simple High Profit low Drawdown Triangular Arbitrage
  *   * [ **Reply to Thread** ](/thread/676132-simple-high-profit-low-drawdown-triangular-arbitrage/reply#reply)

  * More

[](https://www.forexfactory.com "Homepage")

  * [Forums](forums)
  * [Trades](trades)
  * [Calendar](calendar)
  * [News](news)
  * [Market](market)
  * [Brokers](brokers)

****

[](https://www.faireconomy.com/)

  * 

[Triangular Arbitrage](/thread/64423-triangular-arbitrage "Admin, Please Delete Thread.") 258 replies

[Triangular Arbitrage](/thread/62477-triangular-arbitrage "Is going  
long 1 lot of eur/usd + 
long 1 lot of usd/jpy = long 1 lot of eur/jpy ?  
\(is the ratio of the number of lots correct for a...") 16 replies

[Triangular Arbitrage and carry trade](/thread/71997-triangular-arbitrage-and-carry-trade "Is it possible for us retail traders to be able to make use of Tri Arb or carry trades?  
 
Any one know of retail brokers 
 
 
\(I'm...") 6 replies

[Triangular Arbitrage](/thread/367072-triangular-arbitrage "I've been reading about triangular arbing and was surprised to find that the cross of two majors doesn't always equal what the calculation...") 7 replies

[Question: Trade Mechanics of Triangular Arbitrage](/thread/225246-question-trade-mechanics-of-triangular-arbitrage "Before I even ask this question, please allow me to be very clear.... I have no intention of attempting a triangular arbitrage trade\(for...") 6 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/676132-simple-high-profit-low-drawdown-triangular-arbitrage/reply#reply)
  * Subscribe
  * [147](javascript:void\(0\);)

Attachments: Simple High Profit low Drawdown Triangular Arbitrage

Tags: Simple High Profit low Drawdown Triangular Arbitrage

#  [](/thread/676132-simple-high-profit-low-drawdown-triangular-arbitrage)Simple High Profit low Drawdown Triangular Arbitrage 

  * 

  * [#101](/thread/post/10019219#post10019219 "Post Permalink")

  * Jun 26, 2017 11:14pm  Jun 26, 2017 11:14pm 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

Here is the Metatrader 4 version. 

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [2017-06-12 09h00 JVB Arbitrage Auto Profit4.ex4](/attachment/file/2370734?d=1498486465) 31 KB | 980 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#102](/thread/post/10019629#post10019629 "Post Permalink")

  * Jun 27, 2017 12:41am  Jun 27, 2017 12:41am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar46777_5.gif) shiva](shiva)

  * Joined Aug 2007 | Status: Doing It In Dubai | [2,457 Posts](/search?do=process&provider=Member&searchuser=46777)

> [Quoting jvbJacques](/thread/post/10019219#post10019219 "View Quoted Post")
> 
> Disliked
> 
> Here is the Metatrader 4 version. {file}
> 
> Ignored

Thanks Jaques. My explorer has beenrunning your idea but not the EA itselfasInoticed the lotsizes the EA took were 1)Too huge -like 40 lots and 2) Were not matiching what you had specified. It opened 48.97 lots each on GBPJPY(Sell) & GBPUSD(Buy), and 62.49lots sell on USDJPY as the first cycle. That is when I stoppped the EAand started using a script to place the orders. Result you can see in my explorer. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#103](/thread/post/10020226#post10020226 "Post Permalink")

  * Jun 27, 2017 3:25am  Jun 27, 2017 3:25am 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

The EA can have multiple days without movement.  
Sometimes a month can go bye, especially on the old EA.  
  
The new EA trades quicker, but having large lots does not mean it is not working seeing that they cancel each other out, although the new EA only reach 18 lots by the $100,000 mark.  
  
My server is broken at the moment.  
  
Once fixed I can start to do forward tests myself.  
  
How did you connect the results to your profile and can MT5 also do it ? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#104](/thread/post/10023259#post10023259 "Post Permalink")

  * Jun 27, 2017 7:33pm  Jun 27, 2017 7:33pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar268213_5.gif) kaczucha11](kaczucha11)

  * | Joined Jul 2012  | Status: Trader | [99 Posts](/search?do=process&provider=Member&searchuser=268213)

Hi Jacques,  
Thanks for sharing your system. will try it![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#105](/thread/post/10023321#post10023321 "Post Permalink")

  * Jun 27, 2017 7:44pm  Jun 27, 2017 7:44pm 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@kaczucha11  
More than welcome.  
The theory is sound, but the EA is unstable so please DO NOT USE ON LIVE accounts.  
Please read post 1 for more information and note that I mainly tested on myfxchoice.  
  
I already discovered a new potential improvement.  
At the moment the EA only opens up trades when the spread is below the average spread, unless the EA just started.  
Problem is that once the equity drops to a point where a new grid level is supposed to take over the spread most likely will increase significantly.  
Now normally you do not want to trade during high [spreads](/brokers/spreads "View Live Spreads on the Broker Guide"), but if the value of all these high spreads, subtracted from the low equity grid entry point then it might be a good idea to enter the grid level seeing that this is a large spike that must return to ZERO point and therefore is trade-able.  
  
Even if this causes the ultimate profit to be lower than if you only trade during low spread times, it will ultimately release the position run so that other positions can be opened up more frequently and therefore generate more profit by having more low profit trades rather than a few high profit ones.  
  
Will test it in time when my server is fixed one day.  
Just an idea so far. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#106](/thread/post/10023569#post10023569 "Post Permalink")

  * Jun 27, 2017 8:42pm  Jun 27, 2017 8:42pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar268213_5.gif) kaczucha11](kaczucha11)

  * | Joined Jul 2012  | Status: Trader | [99 Posts](/search?do=process&provider=Member&searchuser=268213)

> [Quoting shiva](/thread/post/10019629#post10019629 "View Quoted Post")
> 
> Disliked
> 
> {quote} Thanks Jaques. My explorer has beenrunning your idea but not the EA itselfasInoticed the lotsizes the EA took were 1)Too huge -like 40 lots and 2) Were not matiching what you had specified. It opened 48.97 lots each on GBPJPY(Sell) & GBPUSD(Buy), and 62.49lots sell on USDJPY as the first cycle. That is when I stoppped the EAand started using a script to place the orders. Result you can see in my explorer.
> 
> Ignored

  
Hi Shiva.  
Any chance share a script to place the orders?. Would like to play a little manualy. Thanks 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#107](/thread/post/10023706#post10023706 "Post Permalink")

  * Jun 27, 2017 9:14pm  Jun 27, 2017 9:14pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar46777_5.gif) shiva](shiva)

  * Joined Aug 2007 | Status: Doing It In Dubai | [2,457 Posts](/search?do=process&provider=Member&searchuser=46777)

Sure. 

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [TAT 1.ex4](/attachment/file/2372478?d=1498565635) 9 KB | 674 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#108](/thread/post/10023718#post10023718 "Post Permalink")

  * Jun 27, 2017 9:17pm  Jun 27, 2017 9:17pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar46777_5.gif) shiva](shiva)

  * Joined Aug 2007 | Status: Doing It In Dubai | [2,457 Posts](/search?do=process&provider=Member&searchuser=46777)

> [Quoting jvbJacques](/thread/post/10020226#post10020226 "View Quoted Post")
> 
> Disliked
> 
> The EA can have multiple days without movement. Sometimes a month can go bye, especially on the old EA. The new EA trades quicker, but having large lots does not mean it is not working seeing that they cancel each other out, although the new EA only reach 18 lots by the $100,000 mark. My server is broken at the moment. Once fixed I can start to do forward tests myself. How did you connect the results to your profile and can MT5 also do it ?
> 
> Ignored

Hi Jacques, it's easy.

  1. Go to your profile page (this is your profile [link)](https://www.forexfactory.com/jvbjacques)
  2. Select Create a new explorer

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#109](/thread/post/10023894#post10023894 "Post Permalink")

  * Jun 27, 2017 9:48pm  Jun 27, 2017 9:48pm 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

Thanks Shiva 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#110](/thread/post/10024002#post10024002 "Post Permalink")

  * Jun 27, 2017 10:03pm  Jun 27, 2017 10:03pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar268213_5.gif) kaczucha11](kaczucha11)

  * | Joined Jul 2012  | Status: Trader | [99 Posts](/search?do=process&provider=Member&searchuser=268213)

> [Quoting shiva](/thread/post/10023706#post10023706 "View Quoted Post")
> 
> Disliked
> 
> Sure. {file}
> 
> Ignored

Thanks 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#111](/thread/post/10024368#post10024368 "Post Permalink")

  * Jun 27, 2017 10:59pm  Jun 27, 2017 10:59pm 

  * [ koroshfx](koroshfx)

  * | Joined May 2017  | Status: Trader | [49 Posts](/search?do=process&provider=Member&searchuser=583679)

after 7 days on vps nothing happened. just negative swap and commission.  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: MT4.png
Size: 39 KB](/attachment/image/2372686/thumbnail?d=1498571823)](/attachment/image/2372686?d=1498571823)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#112](/thread/post/10026674#post10026674 "Post Permalink")

  * Jun 28, 2017 7:11am  Jun 28, 2017 7:11am 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@koroshfx  
That sounds about right.  
The first EA did not take swap into account.  
Also.  
The history the EA gathers on the first EA only reach saturation after 5 day and therefore trades opened up before that time is based on inaccurate rolling averages or just the starting values.  
  
Other than that.  
A month can go bye on some trades with no movement.  
  
At the moment I am sitting with pc problems and can not afford to fix it, at the moment.  
Once I saved enough I will get back to work on the EA.  
  
The important part is the theory.  
I have not looked at the EA Shiva made, but it might shed some more light into the workings of the theory.  
I also created a single trade EA in post 50, which you can run to see how the triangle works and the opportunities it presents.  
It only opens 3 trades and leaves them open so you can see the ZERO point clearly and how it moves around it.  
Based on this you can then abuse the rule with multiple strategies like grids and more to take profit.  
This is what I am planning for the full EA once done.  
  
You can also run the latest EA on a back test with myfxchoice or another broker and then look at the trades made and how large the time span can be between trades, which range from within seconds to weeks or more.  
  
I will work on the EA once I get the tools to do it, just wait a bit or jump in and write an EA based on the theory yourself so other can test it with you in the mean time. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#113](/thread/post/10202271#post10202271 "Post Permalink")

  * Aug 18, 2017 4:41am  Aug 18, 2017 4:41am 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

OK Here goes something.  
At last I gathered the funds to fix my server and along with it I made a massive amount of enhancements to the EA.  
Thing is.  
I did not have time to convert it to MT4 yet and with all of the enhancements most of the calculations are hard-coded into the EA so if you want to test it you need the following:  
Leverage of 200:1 ... Should work on other leverages, but I have not tested it long enough to ensure the draw-down and margin calculations are correct, but try it.  
Symbols GBPUSD, GBPJPY and USDJPY must be available for use.  
I found brokers with special symbols like GBPUSD. with a (dot) at the end.  
And others with even weirder symbols.  
One day I will make the EA compatible with other symbols but for now it will not work on others for it will not find them.  
Minimum lot size of at least 0.01  
Must be able to handle at least a maximum lot size of 50.0 lots.  
O and this is a MT5 EA.  
Will convert it to MT4 one day.  
  
To install the EA :  
Create the following folders in your metatrader installation folder :  
MQL5\Experts\0ForexEA\ForexEA  
MQL5\Indicators\0ForexEA\ForexEA  
Then copy the following files into the above folders :  
2017-06-13 20h00 JVB OnTick Spy.ex5  
2017-06-14 09h00 JVB Arbitrage Auto Profit11 FXChoice.ex5  
  
Now start or restart your metatrader 5 and run a backtest on GBPUSD for a year or so to ensure everything is working, keeping in mind the settings above.  
To run on DEMO account just open a GBPUSD chart and drag the "2017-06-14 09h00 JVB Arbitrage Auto Profit11 FXChoice.ex5" ea onto the chart.  
O and make sure your metatrader can run EAs.  
The "2017-06-13 20h00 JVB OnTick Spy.ex5" EA is automatically used by the other to monitor the 3 symbols in the background and therefore need to be in the exact folders as stated above to work.  
  
Check the logs for errors and just wait.  
  
The EA will take 1 hour to gather information before starting.  
It will draw multiple lines on the chart.  
Think of the top 2 lines as the ASK and BID prices Highs and Lows.  
If they cross then you have an arbitrage opportunity, but they must cross far enough to cover commission, spread and some profit costs.  
This actually happens often.  
The blue line is only useful to see the profit of an open position, of which there will only be one for each symbol at a time or none.  
  
The logs contains a MASSIVE amount of noisy information.  
Some interesting things are when a ticket is opened and closed.  
Then the log will compare the ASK and BID prices before and after the OPEN and CLOSE operations.  
What is shocking is that I have tested it on multiple brokers and it is working, but during demo forward testing I found that some brokers like [XM](/brokers/xm "View XM Broker Profile") have got MASSIVE slippages in the range of 60 or more pip spread over the 3 symbols on EVERY trade.  
Therefore making this and probably any other fast moving strategy unusable.  
Funny how slippage on some broker are always negative and never positive ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
Maybe it is just my poor server that has got a 300ms lag to their server, but then again I can not afford a VPS to get a better connection and FXCHOICE on the same slow server is running well.  
The EA has a build in buffer to cater for some reasonable slippage and even for the occasional massive slippage to a losing ticket, so long as it does not happen every single time.  
So far MyFXChoice have not shown big slippages and looks good.  
For the most profit this EA needs low spreads and even lower commission.  
Please list a few trustworthy broker that have got low spreads and commission for me to test with that also supports MT5.  
  
Too keep things simple:  
Open a ENC Pro Metatrader 5 demo account with MyFxChoice and run the EA on it.  
It was build and tested on it so all settings are already ready for it.  
  
I can cater for other brokers, but at the moment I can not afford the time and cost of modifying for each flavour of broker.  
I will try if I find one that look good, but I fear my old server is just not fast enough to properly test with it's slow ping.  
  
O and the EA will stop once it reaches 50 lot size.  
So if you backtest and you see your account profit goes horizontal then you maxed out the lot sizes.  
I found that to increase the lot size I have to split the trades into multiple trades, which in turn slows down the execution time and causes slippages.  
So in a live account in future I would suggest opening another account and split the funds between them.  
  
Also it shows brilliant profit using "every tick" during back tests.  
Do not be fooled.  
"Every tick" is extremely inaccurate and the EA is made to profit from market instability or inaccuracy.  
Rather use the slower "Real Tick" option.  
That will be closer to actual live data seeing that their time and dates for the different symbols are synchronised.  
Still some good profit.  
  
I hope to have some funds some day to complete this project and may test it using a VPS or even live.  
If that day comes I will let you all know the results and final EA.  
  
Please let me know if there is any broker with lower spreads and commission than MyFXChoice and I will test them.  
I found some, but none that I can trust so far or that slipped everything I traded with them.  
So far MyFXChoice seem to be one of the better brokers out there.  
Something for others to aspire to. ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

Attached File(s)

![File Type: ex5](https://assets.faireconomy.media/images/attach/ex5.gif) [2017-06-14 09h00 JVB Arbitrage Auto Profit11 FXChoice.ex5](/attachment/file/2444746?d=1502998865) 128 KB | 493 downloads 

![File Type: ex5](https://assets.faireconomy.media/images/attach/ex5.gif) [2017-06-13 20h00 JVB OnTick Spy.ex5](/attachment/file/2444749?d=1502998865) 7 KB | 472 downloads 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#114](/thread/post/10203395#post10203395 "Post Permalink")

  * Aug 18, 2017 3:21pm  Aug 18, 2017 3:21pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar573255_2.gif) kb77](kb77)

  * | Joined Apr 2017  | Status: Trader | [31 Posts](/search?do=process&provider=Member&searchuser=573255)

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screen Shot 2017-08-18 at 08.19.15.png
Size: 42 KB](/attachment/image/2445343/thumbnail?d=1503037252)](/attachment/image/2445343?d=1503037252)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#115](/thread/post/10203451#post10203451 "Post Permalink")

  * Aug 18, 2017 3:44pm  Aug 18, 2017 3:44pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar573255_2.gif) kb77](kb77)

  * | Joined Apr 2017  | Status: Trader | [31 Posts](/search?do=process&provider=Member&searchuser=573255)

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screen Shot 2017-08-18 at 08.43.24.png
Size: 28 KB](/attachment/image/2445366/thumbnail?d=1503038660)](/attachment/image/2445366?d=1503038660)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#116](/thread/post/10203595#post10203595 "Post Permalink")

  * Edited 4:53pm  Aug 18, 2017 4:30pm | Edited 4:53pm 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@EVERYONE  
@WARNING  
@PLEASE DO NOT DRINK AND DRIVE  
I received a couple of PMs where people want to run it on live accounts.  
DO NOT RUN ON LIVE ACCOUNT.  
IT WILL EAT YOUR CHILDREN.  
  
But really.  
It is way too unstable to run on live account.  
Read post 1.  
There are a lot of work before it can go live.  
It will get there, but not soon as I ran out of funds long ago, but it will get there, just not now.  
  
Run on DEMO or back test.  
This is still just a proof of concept.  
  
  
@kb77  
Post 114  
That is perfectly fine.  
ERROR= "blank" is perfect and the EA is running.  
Spies ok  
Is also a good message, because it is saying that it connected to the 3 symbols and are waiting for ticks from them.  
  
Post 115  
I never had this problem, but then again I am running it on my server and not a VPS.  
I assume you have got access to a nice VPS.  
  
This is a message from metatrader indicating the EA is too slow ... duh ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
  
Well. That is very true.  
Even though the EA is saying 11 it is actually version 132 or something like that and contains thousands of lines of code .... 70% of which are old stuff that are now useless and just slowing things down, but mostly the visual side of the EA I think are the big problem.  
  
It draws on average 500,000 lines on the screen to show the inner workings of the EA.  
Also looks cool ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
But uses a couple of gigs of memory and obviously very slow.  
  
Please see attached EA for a faster version using less memory, but no lines.  
Just add this EA to your chart instead of the other.  
  
Use the other one on a faster computer to see how the EA works on the chart.  
It is sometimes nice to see how Arbitrage looks than just the theory, but not needed if you are forward testing. 

Attached File(s)

![File Type: ex5](https://assets.faireconomy.media/images/attach/ex5.gif) [2017-06-14 09h00 JVB Arbitrage Auto Profit11 FAST No Graphics.ex5](/attachment/file/2445452?d=1503041422) 113 KB | 467 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#117](/thread/post/10203854#post10203854 "Post Permalink")

  * Aug 18, 2017 6:07pm  Aug 18, 2017 6:07pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar440253_2.gif) badeel](badeel)

  * Joined Dec 2015 | Status: Trader | [257 Posts](/search?do=process&provider=Member&searchuser=440253)

thanks downloaded on my vps and working fine lets see how it goes will update soon 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#118](/thread/post/10203879#post10203879 "Post Permalink")

  * Edited 6:34pm  Aug 18, 2017 6:11pm | Edited 6:34pm 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@badeel  
  
I wish I was you ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
  
Just remember it can not pick up already open trades.  
Not yet.  
So if you restart metatrader then only do it when there are no trades.  
  
  
@EVERYONE  
I forgot to mention.  
  
If you want to look at the inner workings of the EA and you are using the EA with the lines then keep in mind the lines are HUGE.  
So zoom the chart they are drawn on out until you can see all the lines.  
  
You can zoom the chart by left click dragging down on the right hand side of the chart on the currency values displayed for each horizontal line on the chart.  
Keep zooming out until you can see the full picture.  
  
The currency line means nothing.  
The lines the EA draws are what is actually happening in the back ground.  
  
Also change the chart color to black to that the lines are more visible. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#119](/thread/post/10205374#post10205374 "Post Permalink")

  * Aug 19, 2017 12:12am  Aug 19, 2017 12:12am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar440253_2.gif) badeel](badeel)

  * Joined Dec 2015 | Status: Trader | [257 Posts](/search?do=process&provider=Member&searchuser=440253)

here screen shot of my pc  
sir let me know if anything wrong also check expert message is it alright or some problem.  
thanks for your time 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: arbitrage image.PNG
Size: 97 KB](/attachment/image/2446153/thumbnail?d=1503069082)](/attachment/image/2446153?d=1503069082)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#120](/thread/post/10205439#post10205439 "Post Permalink")

  * Aug 19, 2017 12:24am  Aug 19, 2017 12:24am 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@badeel  
Yes that look good from what I see.  
  
It connected to all 3 symbols according to the logs and is running.  
  
You need to change the colors of your chart and zoom the chart out to see the rest of the lines.  
Make the background black and the price lines white.  
  
Then you can see how the ASK/BID spread and instabilities play with each other.  
as with this :  
[https://www.mql5.com/en/charts/75036...choice-limited](https://www.mql5.com/en/charts/7503648/gbpusd-m1-fx-choice-limited)  
  
You can zoom out by dragging down on the right side of the chart on the horizontal bar prices.  
Zoom a couple of times until you see all the lines.  
  
It does not look like the EA has started monitoring yet, but I can not see the whole chart so I do not know and it only start 1 hour after activation. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Simple High Profit low Drawdown Triangular Arbitrage
  *   * [ **Reply to Thread** ](/thread/676132-simple-high-profit-low-drawdown-triangular-arbitrage/reply#reply)

  * More

[](https://www.forexfactory.com "Homepage")

  * [Forums](forums)
  * [Trades](trades)
  * [Calendar](calendar)
  * [News](news)
  * [Market](market)
  * [Brokers](brokers)

****

[](https://www.faireconomy.com/)

  * 

[Triangular Arbitrage](/thread/64423-triangular-arbitrage "Admin, Please Delete Thread.") 258 replies

[Triangular Arbitrage](/thread/62477-triangular-arbitrage "Is going  
long 1 lot of eur/usd + 
long 1 lot of usd/jpy = long 1 lot of eur/jpy ?  
\(is the ratio of the number of lots correct for a...") 16 replies

[Triangular Arbitrage and carry trade](/thread/71997-triangular-arbitrage-and-carry-trade "Is it possible for us retail traders to be able to make use of Tri Arb or carry trades?  
 
Any one know of retail brokers 
 
 
\(I'm...") 6 replies

[Triangular Arbitrage](/thread/367072-triangular-arbitrage "I've been reading about triangular arbing and was surprised to find that the cross of two majors doesn't always equal what the calculation...") 7 replies

[Question: Trade Mechanics of Triangular Arbitrage](/thread/225246-question-trade-mechanics-of-triangular-arbitrage "Before I even ask this question, please allow me to be very clear.... I have no intention of attempting a triangular arbitrage trade\(for...") 6 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/676132-simple-high-profit-low-drawdown-triangular-arbitrage/reply#reply)
  * Subscribe
  * [147](javascript:void\(0\);)

Attachments: Simple High Profit low Drawdown Triangular Arbitrage

Tags: Simple High Profit low Drawdown Triangular Arbitrage

#  [](/thread/676132-simple-high-profit-low-drawdown-triangular-arbitrage)Simple High Profit low Drawdown Triangular Arbitrage 

  * 

  * [#121](/thread/post/10205831#post10205831 "Post Permalink")

  * Aug 19, 2017 1:41am  Aug 19, 2017 1:41am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar440253_2.gif) badeel](badeel)

  * Joined Dec 2015 | Status: Trader | [257 Posts](/search?do=process&provider=Member&searchuser=440253)

after zoom and modification looks like 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: arbitrage image.PNG
Size: 54 KB](/attachment/image/2446306/thumbnail?d=1503074490)](/attachment/image/2446306?d=1503074490)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#122](/thread/post/10205978#post10205978 "Post Permalink")

  * Edited 2:22am  Aug 19, 2017 2:11am | Edited 2:22am 

  * [ dukas_trader](dukas_trader)

  * | Membership Revoked  | Joined Mar 2010 | [2,525 Posts](/search?do=process&provider=Member&searchuser=136341)

> [Quoting jvbJacques](/thread/post/10202271#post10202271 "View Quoted Post")
> 
> Disliked
> 
> OK Here goes something. At last I gathered the funds to fix my server and along with it I made a massive amount of enhancements to the EA. Thing is. I did not have time to convert it to MT4 yet and with all of the enhancements most of the calculations are hard-coded into the EA so if you want to test it you need the following: Leverage of 200:1 ... Should work on other leverages, but I have not tested it long enough to ensure the draw-down and margin calculations are correct, but try it. Symbols GBPUSD, GBPJPY and USDJPY must be available for use....
> 
> Ignored

ok just for helping you and save you time:  
  
\- never ever test this 3 currency hedge arbitrage with an demoaccount --> in demo account you will get always wins, thats stupid, really stupid. its like with all arbitrage models, you win in demo near always, in real accounts you dont.  
\- do it in real account in small or dont test it.  
  
just to help you, you dont need to believe me. but demo trading is complete useless time, only testing your program is ok for prgramming errors, but not testing for any win. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#123](/thread/post/10206391#post10206391 "Post Permalink")

  * Aug 19, 2017 5:16am  Aug 19, 2017 5:16am 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

> [Quoting badeel](/thread/post/10205831#post10205831 "View Quoted Post")
> 
> Disliked
> 
> after zoom and modification looks like {image}
> 
> Ignored

@badeel  
The modifications on the chart does not change the EA and it is still running fine as before.  
It is just better visible for you now.  
  
You might want to change the currency line colors to white so you can also see the currency line.  
  
  
@dukas_trader  
I know, but have got no funds to test on live account.  
Need at least $1000 for proper test.  
I'm struggling to get by month to month so that is not an option for me.  
At least I am enjoying the math behind it and I have programmed a lot of AI programs for safety and security and the mining industries and multiple others.  
And most of my programs have been taken from me by bigger companies for their own profit leaving me with scraps.  
I'm a programmer. Not a lawyer or salesman and they know it.  
  
So why not use what I know with what I enjoy doing, even if I ultimately can not benifit from it then at least others can.  
  
Demo at least show some slippage problems.  
I already found some brokers that seem to slip even demo accounts, which at least tell me to avoid them.  
  
Demo is also more accurate than back testing.  
  
The major difference between demo and live is slippage and one day I hope to test it.  
I did build slip protection into the ea to hopefully take some slip hits. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#124](/thread/post/10206433#post10206433 "Post Permalink")

  * Aug 19, 2017 5:48am  Aug 19, 2017 5:48am 

  * [ dukas_trader](dukas_trader)

  * | Membership Revoked  | Joined Mar 2010 | [2,525 Posts](/search?do=process&provider=Member&searchuser=136341)

> [Quoting jvbJacques](/thread/post/10206391#post10206391 "View Quoted Post")
> 
> Disliked
> 
> {quote} @badeel The modifications on the chart does not change the EA and it is still running fine as before. It is just better visible for you now. You might want to change the currency line colors to white so you can also see the currency line. @dukas_trader I know, but have got no funds to test on live account. Need at least $1000 for proper test. I'm struggling to get by month to month so that is not an option for me. At least I am enjoying the math behind it and I have programmed a lot of AI programs for safety and security and the mining industries...
> 
> Ignored

i dont get this point.  
you can test with very small amounts or even cent accounts in live trading. with higher amounts it get more difficult (not that it is not from beginning) because higer slippage, higher spread, not enough volume in all 3 currencies same time.....!  
  
the difference between live and demo account are:  
\- slippage  
\- spread  
\- offquotes , unable to do trades to this prices for this amount  
\- to less amounts possible to trade  
\- different fill time, platform connections,responses ...  
\- sometimes different rollover fees  
.....  
  
you can program inside an ea what ever you want, until you test it in real account its complete wasted time, if you trade arbitrage trading, because arbitrage is in 99,99% of the time extrem wasted time, if you dont have special hardware/software advantage, its business of many people with all this, many competition for exact same trades.... and we dont speak about this cam software from all who offer arbitrage mt4 software! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#125](/thread/post/10206444#post10206444 "Post Permalink")

  * Aug 19, 2017 5:55am  Aug 19, 2017 5:55am 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

> [Quoting dukas_trader](/thread/post/10206433#post10206433 "View Quoted Post")
> 
> Disliked
> 
> {quote} i dont get this point. you can test with very small amounts or even cent accounts in live trading. with higher amounts it get more difficult (not that it is not from beginning) because higer slippage, higher spread, not enough volume in all 3 currencies same time.....!
> 
> Ignored

  
@dukas_trader  
Very simple.   
Read the theory in post 1.  
USDJPY lot size is a calculation based on the lot size of Gbpjpy.   
  
If the account size is too small then the lot size difference of USDJPY from the other 2 is nothing or too small to make a difference and to balance out the triangle.   
  
You can trade with $100, but then it is more luck than calculations.   
  
Best is $10,000 but $1000 will do 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#126](/thread/post/10206480#post10206480 "Post Permalink")

  * Aug 19, 2017 6:25am  Aug 19, 2017 6:25am 

  * [ dukas_trader](dukas_trader)

  * | Membership Revoked  | Joined Mar 2010 | [2,525 Posts](/search?do=process&provider=Member&searchuser=136341)

> [Quoting jvbJacques](/thread/post/10206444#post10206444 "View Quoted Post")
> 
> Disliked
> 
> {quote} @dukas_trader Very simple. Read the theory in post 1. USDJPY lot size is a calculation based on the lot size of Gbpjpy. If the account size is too small then the lot size difference of USDJPY from the other 2 is nothing or too small to make a difference and to balance out the triangle. You can trade with $100, but then it is more luck than calculations. Best is $10,000 but $1000 will do
> 
> Ignored

and when you use a cent account?? a cent is in this accounts faked a dollar, so you have 100 times more in balance then its worth. but perfect for your situation.  
so 100 usd is 10000 "account balance dollar" already to trade. this is not enough?  
  
and so you get with small money much much more accurate results. demo will not help a little. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#127](/thread/post/10206490#post10206490 "Post Permalink")

  * Aug 19, 2017 6:37am  Aug 19, 2017 6:37am 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

> [Quoting dukas_trader](/thread/post/10206480#post10206480 "View Quoted Post")
> 
> Disliked
> 
> {quote} and when you use a cent account?? so 100 usd is 10000 "account balance dollar" already to trade. this is not enough?
> 
> Ignored

@dukas_trader  
That actually might work.   
What broker offers this with mt5?   
  
Also what is the average spread you get with the 3 symbols on this kind of account?  
What commission.   
Sounds good.   
  
As for the differences between demo and live and all the parts that can differ.   
I see all of it as slippage.   
The meaning of slippage to me is if you do not get the exact currency value that you opened on, whether it is because of currency changes, lag, spread or pink butterflies.   
The point is that you picked a price point and did not get it.   
  
Now I do realise there is always some slippage and I cater for it in my ea and then some, but some brokers do push it a bit.   
  
My problem at the moment is lag, because I do not have a vps, but funds....   
  
You might think $100 is cheap, but for some people like me that is a lot.   
My cercumstances is of the sort that I live month to month and $10 here and there ads up for me.   
I can not remember when last I had takeaway.   
  
No coffee for me, unless I make it myself.   
And I do love my coffee 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#128](/thread/post/10206499#post10206499 "Post Permalink")

  * Aug 19, 2017 6:46am  Aug 19, 2017 6:46am 

  * [ dukas_trader](dukas_trader)

  * | Membership Revoked  | Joined Mar 2010 | [2,525 Posts](/search?do=process&provider=Member&searchuser=136341)

> [Quoting jvbJacques](/thread/post/10206490#post10206490 "View Quoted Post")
> 
> Disliked
> 
> {quote} @dukas_trader That actually might work. What broker offers this with mt5? Also what is the average spread you get with the 3 symbols on this kind of account? What commission. Sounds good. As for the differences between demo and live and all the parts that can differ. I see all of it as slippage. The meaning of slippage to me is if you do not get the exact currency value that you opened on, whether it is because of currency changes, lag, spread or pink butterflies. The point is that you picked a price point and did not get it. Now I do realise...
> 
> Ignored

slippage is only the best case you get, the worst case in real account is :  
\- offquotes: no trade possible because of connection, no quotes, or not this quotes for this amount you want trade  
\- order fill time is much slower...  
\- higher [spreads](/brokers/spreads "View Live Spreads on the Broker Guide")  
\- much faster new pricequotes/refreshes  
  
i dont use cent accounts, you have to look by your own to all brokers who offers this and check for all points you are interested in and make a table to compare, or open some with some brokers and take the best later..... (first demo to test ofcourse for some hours to filter what you dont like at all) 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#129](/thread/post/10206537#post10206537 "Post Permalink")

  * Aug 19, 2017 7:41am  Aug 19, 2017 7:41am 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@dukas_trader  
  
\- offquotes: no trade possible because of connection, no quotes  
This is bad, but an immediate close can solve this if all 3 symbols could not be traded.  
\- offquotes: or not this quotes for this amount you want trade  
Slippage  
\- order fill time is much slower...  
Slippage  
\- higher [spreads](https://www.forexfactory.com/brokers.php#spreads) than displayed when opened  
Slippage  
\- much faster new pricequotes/refreshes/lag  
Slippage  
  
Slippage to me is a blanket term that states you did not get what you paid for for whatever reason.  
You expect to get the amount at the time the order is placed, but I know there is some slippage.  
Slippage can be broken up into multiple sub categories, but I do not care about that detail when the end result is the same.  
The problem comes in when there is 20 to 50 pips slippage every time.  
Once in a while will not hurt that much, but still a red flag against the broker if you have no lag on your VPS.  
  
I checked a couple of cent accounts and although the idea is nice, their spreads are crazy high.  
Spreads are important to this strategy, along with commission.  
If I can get a cent account with spreads equal or better than MyFxChoice's ENC Pro account then that will be something to talk about.  
MX looks nice, but I need a VPS to test it because on my server I get about 60pip slippage on basically every trade, which is far too big, but might be caused by my 280millisecond lag to them, where myfxchoice with a 250millisecond lag slips much less and therefore stays in profit, even with higher spreads. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#130](/thread/post/10206564#post10206564 "Post Permalink")

  * Edited 9:00am  Aug 19, 2017 8:14am | Edited 9:00am 

  * [ dukas_trader](dukas_trader)

  * | Membership Revoked  | Joined Mar 2010 | [2,525 Posts](/search?do=process&provider=Member&searchuser=136341)

> [Quoting jvbJacques](/thread/post/10206537#post10206537 "View Quoted Post")
> 
> Disliked
> 
> @dukas_trader - offquotes: no trade possible because of connection, no quotes This is bad, but an immediate close can solve this if all 3 symbols could not be traded. - offquotes: or not this quotes for this amount you want trade Slippage - order fill time is much slower... Slippage - higher [spreads](https://www.forexfactory.com/brokers.php#spreads) than displayed when opened Slippage - much faster new pricequotes/refreshes/lag Slippage Slippage to me is a blanket term that states you did not get what you paid for for whatever reason....
> 
> Ignored

you play against big people with much money, big hardware and software.  
arbitrage trading is what biggest do with biggest possible amount of competition.  
many big firms win only from this (because most easy ,you dont need any trading plan or experience) and hide doing this by this. but the competition makes wins much smaller then with real trading, and for 99,99% of this trying even no wins at all.  
  
its really only a extrem small chance that you can much from the table, if you have to trade with such small brokers.  
try it, but dont put in to much hope.  
arbitrage is fine in theory, but because its biggest competition, any tome advantage, any software advantage, any contact advantage, any hardware advantage from other kill you system in real trading. in demo trading you cant see this. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#131](/thread/post/10208048#post10208048 "Post Permalink")

  * Aug 20, 2017 12:53pm  Aug 20, 2017 12:53pm 

  * [ yan7181](yan7181)

  * | Joined Aug 2009  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=111605)

Interesting stuff u have, will test it on Icmarket demo. By the way, there see cents account broker that u can trade for live. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#132](/thread/post/10210586#post10210586 "Post Permalink")

  * Aug 21, 2017 7:27pm  Aug 21, 2017 7:27pm 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@EVERYONE  
  
Bug detected.  
The market start to move on Sundays for some symbols.  
The EA then tries to trade when the market starts moving and fails seen that the market is not open for all the symbols yet.  
This then messes with the calculations as partial and incorrect trades are then opened when the market opens and the EA crash.  
  
Attached is a new EA that does not trade on Sundays and if trade failure is detected then close everything and try again.  
Still looking for a better solution to detect if the market is open for all the symbols.  
In MQ4 I can use the function MarketInfo, but this does not work in MQ5.  
any help here would be appreciated. 

Attached File(s)

![File Type: ex5](https://assets.faireconomy.media/images/attach/ex5.gif) [2017-06-14 09h00 JVB Arbitrage Auto Profit12 FXChoice.ex5](/attachment/file/2448492?d=1503311238) 129 KB | 340 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#133](/thread/post/10210699#post10210699 "Post Permalink")

  * Aug 21, 2017 8:09pm  Aug 21, 2017 8:09pm 

  * [ dukas_trader](dukas_trader)

  * | Membership Revoked  | Joined Mar 2010 | [2,525 Posts](/search?do=process&provider=Member&searchuser=136341)

> [Quoting jvbJacques](/thread/post/10210586#post10210586 "View Quoted Post")
> 
> Disliked
> 
> @EVERYONE Bug detected. The market start to move on Sundays for some symbols. The EA then tries to trade when the market starts moving and fails seen that the market is not open for all the symbols yet. This then messes with the calculations as partial and incorrect trades are then opened when the market opens and the EA crash. Attached is a new EA that does not trade on Sundays and if trade failure is detected then close everything and try again. Still looking for a better solution to detect if the market is open for all the symbols. In MQ4 I can...
> 
> Ignored

simple check the last time for the 1 min timeframe. trade only when all 3 currencies have a time difference not more then 2 mins to actuell time or what ever time you want. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#134](/thread/post/10210748#post10210748 "Post Permalink")

  * Aug 21, 2017 8:26pm  Aug 21, 2017 8:26pm 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@dukas_trader  
I was thinking the same thing, but I have read that there can be multiple reasons for the trading to stop or have gaps of multiple seconds or even a minute.  
So this can be inaccurate.  
  
But thanks.  
I will build it in as another check.  
The more the better, especially ones like these that does not influence the processing speed. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#135](/thread/post/10214912#post10214912 "Post Permalink")

  * Aug 22, 2017 10:28pm  Aug 22, 2017 10:28pm 

  * [ Kman](kman)

  * | Joined Apr 2012  | Status: Trader | [17 Posts](/search?do=process&provider=Member&searchuser=250634)

It seems like this strategy must have been tried by big players. Is there any indication that it is used by banks? My guess is that the market is not that simple. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#136](/thread/post/10215103#post10215103 "Post Permalink")

  * Aug 22, 2017 11:06pm  Aug 22, 2017 11:06pm 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@Kman  
I also think the big player must be using this, especially the banks.  
If you run the EA during back testing with the graph then ignore the profit and trades and zoom the chart out.  
You will see that I draw 2 graphs and an average line between them.  
  
The top graph shows what the actual account value is if you bought into the 3 symbols using the arbitrage calculation at the start of the run with and you do a SELL, BUY, BUY at that moment.  
The bottom one is the same, but a BUY, SELL, SELL.  
  
As you can see that no matter how long the period that the graphs are rock solid with minor fluctuations.  
These fluctuations are what you can profit on, but they need to be big enough to not only cross each other, but to cover spread, commission and a bit of profit.  
As you can see.  
The big fluctuations are rare.  
  
The advantage to the banks are that they have access you a fast price actions and EXTREMELY low spread with no commission.  
What I would not do for spreads like that.  
In stead of just making profits once in a while you can then make profits every few minutes or even seconds.  
  
A good example is the broker [XM](/brokers/xm "View XM Broker Profile").  
They have extremely low spreads and crosses happen quite often.  
Unfortunately their commission is very big and a cross need to be very big to cover the commission.  
That and the fact that my poor server's internet connection is too slow and therefore receives a lot of slippage because of the execution speed.  
  
If anyone can show me a broker with extremely low spreads and commission with very little slippage then please pm me, but then again without a good vps to that broker it probably will not help ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
  
I have been searching for a profitable forex strategy for many years now and have written hundreds of EAs based on advanced and simple strategies.  
One thing I noticed is that the simple strategies seem to be more profitable than the advanced once in the long run.  
This strategy is very difficult to implement in an EA, but the theory behind it is one of the simplest I found yet.  
  
I have got other strategies that also show good profit and share one thing in common and that is they are extremely simple to understand.  
  
Now some might disagree and I saw a lot of people saying this massive strategy and that is the best, but none can show proof of it and no one will share the detail of the strategy for others to test.  
This is why in post 1 I shared everything.  
I myself is dumbfounded that a strategy this simple can be so profitable.  
Or at least I hope so.  
I have got a massive amount of development ahead to test everything in the EA, but I am getting there slowly. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#137](/thread/post/10215481#post10215481 "Post Permalink")

  * Aug 23, 2017 12:12am  Aug 23, 2017 12:12am 

  * [ Kman](kman)

  * | Joined Apr 2012  | Status: Trader | [17 Posts](/search?do=process&provider=Member&searchuser=250634)

It seems like you would need a very large acount to make this worthwhile and the time to stare at your screen all day. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#138](/thread/post/10215553#post10215553 "Post Permalink")

  * Aug 23, 2017 12:38am  Aug 23, 2017 12:38am 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@Kman  
Surprisingly no to both.  
  
Test my EA with backtesting to see the results.  
  
Account size.  
I found that it can be profitable even on a $100 account, but I would not suggest that, because at that account level the calculations do not have enough room to work and therefore it is VERY risky and has the potential to not be a good hedge and blow your account, even though I could not do that during back testing it did come close a couple of times.  
  
I'd say the minimum account size with a 1:200 leverage is $500.  
Good = $1000  
Best = $10000 or better.  
  
As for time staring at the screen.  
That is what I am teaching my EA to do for me.  
The big trades are few and happen fast at any time (normally while you are on the toilet), but the EA can pick them out and you do not have to stay awake at all.  
  
I still have a long way to go, but it does look extremely good with about 1000% profit in 6 months based on "real ticks" and crazy amounts going back further, but that is more to do with the inaccuracy of the data I use in that I only have real tick data dating back for about 1 year and no more.  
  
I only now started forward testing, but my server is a bit slow (400 millisecond delay) to really do justice to the trades, but it hit 3 very good opportunities last week since Tuesday. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#139](/thread/post/10215708#post10215708 "Post Permalink")

  * Edited 1:31am  Aug 23, 2017 1:09am | Edited 1:31am 

  * [ dukas_trader](dukas_trader)

  * | Membership Revoked  | Joined Mar 2010 | [2,525 Posts](/search?do=process&provider=Member&searchuser=136341)

> [Quoting jvbJacques](/thread/post/10215553#post10215553 "View Quoted Post")
> 
> Disliked
> 
> @Kman Surprisingly no to both. Test my EA with backtesting to see the results. Account size. I found that it can be profitable even on a $100 account, but I would not suggest that, because at that account level the calculations do not have enough room to work and therefore it is VERY risky and has the potential to not be a good hedge and blow your account, even though I could not do that during back testing it did come close a couple of times. I'd say the minimum account size with a 1:200 leverage is $500. Good = $1000 Best = $10000 or better. As...
> 
> Ignored

you still count demo wins, so you count nothing. dont even think about this win will happen in real account until you used real account. you really cant invest time in demotrade with arbitrage systems, its 100% wasted time until you test it in real accounts.  
  
some strategies you can really count in demo account and compensate against real account with some pips or some intern recalculation, but with arbitrage really all you do in demo account is like you do nothing at all. any result is 100% useless and not this like in reality.  
  
in all your time, you already invested in this demo trading part, you could invent a normal trading model what you can start with very less money.  
i know, reality is hard, but basic in trading forex you cant go around, thats why no goo dtrader would any other beginner say "hey start with demo account". demo account is for lets know the platform and for test programs for coding problems. but for testing trading always you need a good real account, even its very very small its 1000% better then any demo account can even be. you learn also to grwo slowly and dont be greedy.  
  
i know you dont want to hear this, i dont will say it you again. but you cant lose so much time with worthless things. first learn basics whats possible, whats not and how its possible to do same thing, then doing. wasting time is not best way, because time is often really money in this business. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#140](/thread/post/10215825#post10215825 "Post Permalink")

  * Aug 23, 2017 1:30am  Aug 23, 2017 1:30am 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@dukas_trader  
I have got a different view of things.  
  
You seem to think that if you do not try then you can not lose.  
I'm more of the thinking of that if you do not try then you can not win.  
  
I can not go to a live account without first developing the strategy and testing it using backtesting, then demo then live.  
If I jumped to live using the first iteration of the EA then I would have lost everything.  
Not because of the strategy, but because of EA bugs and the wrong implementation of the strategy.  
  
It is easy to talk about the strategy, but difficult to tell a computer EA to do what you think.  
  
I count nothing as wins, but I do see the potential and potential is all I see until I use a real account at the end of the development.  
I know monopoly money is worth nothing in the bank, but it is fantastic to test with.  
  
If you build a racing car for the first time in your life you do not go to a live race.  
You will break the car, crash and die or kill someone.  
You first go to a demo track with the perfect conditions and ensure everything is working there.  
Then you start to through rocks at it and simulate problems to break it so you can fix it and make it better.  
Then after some time of development you go to a small race a couple of times and do the last small adjustments before going to the big live account.  
  
I think demos are fantastic for testing.  
No need to kill an idea before it can be fully realized.  
An if it does not work in a real account as you say then so be it.  
  
If we stopped development every time something is difficult then we probably would still live in caves or worse.  
  
It costs you nothing and I'm going bankrupt while doing this(Not because of this).  
So if it work then good for everyone and if not then I'm the only one that risked anything.  
But if it works then I want everyone to benefit from it. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Simple High Profit low Drawdown Triangular Arbitrage
  *   * [ **Reply to Thread** ](/thread/676132-simple-high-profit-low-drawdown-triangular-arbitrage/reply#reply)

  * More

[](https://www.forexfactory.com "Homepage")

  * [Forums](forums)
  * [Trades](trades)
  * [Calendar](calendar)
  * [News](news)
  * [Market](market)
  * [Brokers](brokers)

****

[](https://www.faireconomy.com/)

  * 

[Triangular Arbitrage](/thread/64423-triangular-arbitrage "Admin, Please Delete Thread.") 258 replies

[Triangular Arbitrage](/thread/62477-triangular-arbitrage "Is going  
long 1 lot of eur/usd + 
long 1 lot of usd/jpy = long 1 lot of eur/jpy ?  
\(is the ratio of the number of lots correct for a...") 16 replies

[Triangular Arbitrage and carry trade](/thread/71997-triangular-arbitrage-and-carry-trade "Is it possible for us retail traders to be able to make use of Tri Arb or carry trades?  
 
Any one know of retail brokers 
 
 
\(I'm...") 6 replies

[Triangular Arbitrage](/thread/367072-triangular-arbitrage "I've been reading about triangular arbing and was surprised to find that the cross of two majors doesn't always equal what the calculation...") 7 replies

[Question: Trade Mechanics of Triangular Arbitrage](/thread/225246-question-trade-mechanics-of-triangular-arbitrage "Before I even ask this question, please allow me to be very clear.... I have no intention of attempting a triangular arbitrage trade\(for...") 6 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/676132-simple-high-profit-low-drawdown-triangular-arbitrage/reply#reply)
  * Subscribe
  * [147](javascript:void\(0\);)

Attachments: Simple High Profit low Drawdown Triangular Arbitrage

Tags: Simple High Profit low Drawdown Triangular Arbitrage

#  [](/thread/676132-simple-high-profit-low-drawdown-triangular-arbitrage)Simple High Profit low Drawdown Triangular Arbitrage 

  * 

  * [#141](/thread/post/10215842#post10215842 "Post Permalink")

  * Aug 23, 2017 1:41am  Aug 23, 2017 1:41am 

  * [ dukas_trader](dukas_trader)

  * | Membership Revoked  | Joined Mar 2010 | [2,525 Posts](/search?do=process&provider=Member&searchuser=136341)

> [Quoting jvbJacques](/thread/post/10215825#post10215825 "View Quoted Post")
> 
> Disliked
> 
> @dukas_trader I have got a different view of things. You seem to think that if you do not try then you can not lose. I'm more of the thinking of that if you do not try then you can not win. I can not go to a live account without first developing the strategy and testing it using backtesting, then demo then live. If I jumped to live using the first iteration of the EA then I would have lost everything. Not because of the strategy, but because of EA bugs and the wrong implementation of the strategy. It is easy to talk about the strategy, but difficult...
> 
> Ignored

you have a bigger problem to solve:  
  
\- you dont trade a normal trading strategy, its only arbitrage!!, thats not really trading, its a step before. in real trading all counterparts have same informations at the same time, price and news, and so same chance to win. in arbitrage you have a time or information difference between both counterparts.  
\- your arbitrage is not testable in demo account for wins. you can calculate you to the richest person on earth, but will not happen in real accounts. you simple waste your time by any demo backtest and demotrading. i dont say you cant win maybe (dont know your chances), but you cant win any information with demoaccount backtest or forward test, thats for sure. you only can see if your arbitrage ea is working like its programmed.  
\- i dont tell you its difficult to develop this system, i tell you its impossible(!) to develop this system in demo account!  
\- "But if it works then I want everyone to benefit from it"- you are crazy , forget this point. if arbitrage would worh, there are so small amounts there to trade, you really believe when many will trade this same time some will get some amounts? you really have to learn some of the basics of this markets, there is no very high amounts all the time, its more easy if you read about basics by your own, it needs to much time to teach about this topic.  
\- i tried only to help you and save you many many time. if you will see it not as help, then ok. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#142](/thread/post/10215870#post10215870 "Post Permalink")

  * Aug 23, 2017 1:54am  Aug 23, 2017 1:54am 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@dukas_trader  
I'm glad you have money to test unstable EAs on real accounts.  
I'm also glad you think $10 is very little money to lose during testing of something you know will not work just to learn a valuable lessen.  
To me $10 is a lot of money.  
  
Time wise I only do this in my free time, otherwise I would have been done months ago.  
Very little business can be done after midnight when I do most of my development on this and it helps to relax me before bed so it is fun.  
  
You are talking in circles for I do not know what reason as I already stated that I agree with you that a proper test can only be done on live account.  
I just want to delay it for as long as possible until I am sure everything programatically is stable, which it surely is not at yet.  
  
I work in health and safety in the mining industry controlling gas monitor instruments, battery management, tag tracking, gate controls and multiple other hardware devices and then I apply all that and more to control employee movement, health, safety and during worst case scenarios rescues.  
I have to have this system working on the deepest mine in the world Mponeng and multiple others.  
I can not afford to do testing on site and risk peoples lives by small potential bugs just because it is faster to do it in the live environment.  
  
I apply this kind of development to all my programs.  
It need to be bomb proof before going live.  
Then I will tweak it.  
And if proven there that it does not work then so be it.  
  
I appreciate any helpful information.  
Do not think by repeating yourself I have not heard it the first time.  
I'm not trying to hurt you with this EA.  
Use it or don't.  
  
I'm actually enjoying these to and through quite a bit ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
I'm weird ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#143](/thread/post/10215890#post10215890 "Post Permalink")

  * Edited 2:22am  Aug 23, 2017 1:58am | Edited 2:22am 

  * [ dukas_trader](dukas_trader)

  * | Membership Revoked  | Joined Mar 2010 | [2,525 Posts](/search?do=process&provider=Member&searchuser=136341)

> [Quoting jvbJacques](/thread/post/10215870#post10215870 "View Quoted Post")
> 
> Disliked
> 
> @dukas_trader I'm glad you have money to test unstable EAs on real accounts. I'm also glad you think $10 is very little money to lose during testing of something you know will not work just to learn a valuable lessen. To me $10 is a lot of money. Time wise I only do this in my free time, otherwise I would have been done months ago. Very little business can be done after midnight when I do most of my development on this and it helps to relax me before bed so it is fun. You are talking in circles for I do not know what reason as I already stated that...
> 
> Ignored

i see your point, but you are wrong in one thing:  
  
you dont develop a trading EA, its "only " an arbitrage EA. there are other rules for it.  
you can test programm problems in demo, but any backtest in demo, any forward test to see if there are wins, thats complete useless and even wasted time. thats my point. dont calculate any wins or what ever is in demo, never ever. real improvements can only be done in live accounts, in demo all is running different. if you want to do your steps in demo account, develop a trading EA, not an arbitrage EA! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#144](/thread/post/10216221#post10216221 "Post Permalink")

  * Aug 23, 2017 3:43am  Aug 23, 2017 3:43am 

  * [ Kman](kman)

  * | Joined Apr 2012  | Status: Trader | [17 Posts](/search?do=process&provider=Member&searchuser=250634)

Low risk trading this live because your hedged. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#145](/thread/post/10216423#post10216423 "Post Permalink")

  * Aug 23, 2017 5:14am  Aug 23, 2017 5:14am 

  * [ Forex-Loser](forex-loser)

  * | Joined Aug 2017  | Status: Trader | [6 Posts](/search?do=process&provider=Member&searchuser=605222)

Hello everyone.  
  
I have read with great care the whole thread, uploaded the right files in the right directories and for some obscur reasons, backtesting is always washing up the account slowly. Usually around 1 montth of test.  
  
I have tried different time frames, but if i understand it right it does not have any importance since the EA uses ticks so... price action.  
  
My broker is ICMarkets I have an ECN account 1:500 started with $3,000 (which reflect the reality of one of my accounts).  
  
I do not understand what i do not understrand (It's like not remembering what you forgot sort of syndrome ).  
  
I presume my setup has something wrong since everyone seems to enjoy this EA or trading technique.  
  
Is there a magic wand somewhere that could make me understand ?  
  
Thanks 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#146](/thread/post/10216509#post10216509 "Post Permalink")

  * Aug 23, 2017 6:03am  Aug 23, 2017 6:03am 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@Forex-Loser  
Well yes.  
The EA is powered by you own personal time-turner, which should have been supplied to you after your 4th year at Hogwarts.  
If for some reason the time-turner is malfunctioning then you might have spoken the name that should not be spoken.  
In that case follow the following advise.  
  
I need to see the logs to see why it is not working as it should work with 1:500, although I normally do not test with that high a leverage.  
  
Do the backtest with a 1:200 leverage.  
Also.  
Attach the logs of the running EA so I can see if there are any problems and guide you from there.  
At the start of the logs there should be a line "Spies ok, waiting for events".  
Might by that one of my secret agents are not spying on one of the symbols.  
  
Does it open up a lot of trades or only one ?  
  
Something is throwing off the calculation and that tickles my fancy.  
Would like to see what caused it in the logs so I can cater for it in a future update, so please attached your logs. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#147](/thread/post/10261541#post10261541 "Post Permalink")

  * Sep 6, 2017 5:07am  Sep 6, 2017 5:07am 

  * [ Gene-K](gene-k)

  * | Joined Jun 2015  | Status: Trader | [5 Posts](/search?do=process&provider=Member&searchuser=414867)

Greetings, Jacques, and thank you for sharing your findings with us. I read the whole thread and the more I read the more questions I had. So, here we go:  
  
1) How do you get to take profit? As I understand, you close the orders in profit when it equals spread + commission cost + $0.50 per 0.01 of GBPUSD volume. For example, after you open orders on all the 3 currency pairs, your result floats around -$20 (that's what you call ZERO point, right?) and your GBPUSD order volume is 1.00 lot. Therefore, your triangle will close after the profit equals +$70 (20$ + 100*0.50). How is this possible for balanced position to fluctuate so much from the zero point? I opened 3 trades today on GBPJPY-USDJPY-GBPUSD, my zero point was -$30 and the best value I saw was -$20ish. And that leads to my second question.  
  
2) Are you sure your positions are balanced in terms of volume?  
  
3) Also I didn't quite understand this part:  
  
"Now sometimes you do accidentally get in at just the wrong time.  
Basically buying at the highest point and it never gets back to that point.  
In 2 years time I found it about 9 times.  
You can see these in the load spikes at the bottom of the chart.  
This problem is solved by a minor grid.  
Basically once you unluckily buy at the highest point then you will be stuck, but no worries, because it can only fall so far before coming back, but never past that point again so just wait a bit and let it fall and once it fell enough then Buy again the same amount and leave it for a guaranteed profit a bit more than half way back so just wait a bit."  
  
What do you mean by "wrong time"? If you open positions simultaneously, then how entering at the highest point affect anything? Can you provide an example of this situation and how the "minor grid" comes into play?  
  
By the way, you asked about a good ecn broker. Try alpari, I've worked with them for 2 years and ecn execution seems ok, even with my crappy internet speed. (Not affiliated with alpari, and this is not an advertisement). 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#148](/thread/post/10261744#post10261744 "Post Permalink")

  * Sep 6, 2017 6:29am  Sep 6, 2017 6:29am 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@Gene-K  
The version on post one is way out of date and contains a lot of bugs.  
Some of which I already fixed in later versions.  
  
I suggest you run the ea in post 1 containing the graph.  
  
Run it on myfxchoice where I did most of my development to see what it does.  
I ran it on multiple broker and found similar results everywhere.  
Ignore the trades it makes for now as I found some problems, but the theory is sound.  
  
One big change is that my trade entry point is not based on luck anymore and therefore I do not use a grid to get out of a wrong entry.  
  
1)  
Look at the chart being drawn.  
There are 2 lines.  
Think of the 2 lines the ask and bid prices, but in this case the Ask is a buy, sell, sell of the 3 currencies and the bid is the sell, buy, buy.  
Or the other way around.  
I cannot remember just now. ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
  
Each line is rather a channel representing the maximum and minimum of that line over the period.  
  
In the middle of the lines is a 3rd line showing the average between the 2 lines and as you can see it is rock solid for at least a 3 years.  
The limit of my tick data.  
  
The distance between the lines is basically the bid ask spread for the 3 currencies.   
  
The entry point of a position is when one of the lines crosses the middle line far enough to cover commission, a bit of profit, some extra for slippage and if you want swap, but I just ignore swap seeing that is so little.   
  
The position is then left open until the opposite line cross the middle line for profit.   
  
  
2)  
Already answered, but yes. Rock solid for as long back as I could test it. 3 years.   
And on multiple brokers.   
  
  
3)  
Forget the grid.   
No need anymore seeing that the entry and exit is now precisely calculated, but simple line crosses.   
By simple I mean months of code testing a simple theory.   
  
  
As I said.   
The ea is buggy, but the chart it draws are extremely useful to show what I mean and to see where the profit points are.   
  
Yes once open it can take a couple of seconds or days to exit, but still profitable.   
Same with open points.   
  
Also.   
These are spikes your trade.   
  
But the smaller the spread and commission the closer the lines and the more crosses you will be able to trade.   
  
I hit 4 trades on a demo last week before it crashed.   
The ea. Not the theory.   
It could not detect the market was closed and tried to close a poison and could only close one and left the other 2 to go into the red until their markets opened for a loss.   
Overall a profit of $110.  
Could have been $620 if the ea did not crash.   
  
Just do not run the ea with the chart line for actual trading, because it is quite resource heavy. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#149](/thread/post/10262784#post10262784 "Post Permalink")

  * Sep 6, 2017 5:11pm  Sep 6, 2017 5:11pm 

  * [ Gene-K](gene-k)

  * | Joined Jun 2015  | Status: Trader | [5 Posts](/search?do=process&provider=Member&searchuser=414867)

Thanks for your reply, Jacques. Ok, I'll check the ea out. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#150](/thread/post/10263238#post10263238 "Post Permalink")

  * Sep 6, 2017 7:39pm  Sep 6, 2017 7:39pm 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@Gene-K  
Good luck.  
  
Keep an eye out on the forum.  
I'm struggling to get time for this development, but I should have something new to put onto the forum in the next 2 weeks.  
Something more compatible to different types of brokers. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#151](/thread/post/10266503#post10266503 "Post Permalink")

  * Sep 7, 2017 1:53pm  Sep 7, 2017 1:53pm 

  * [ yan7181](yan7181)

  * | Joined Aug 2009  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=111605)

Use 2-3 brokers each enter different currency, will it do? For example, in ur chart, u hedge between nzdsgd, sgd jpy, nzdjpy. Trade with 3 brokers. Each enter one currency. Will it do? Though spread and price might differ 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#152](/thread/post/10266673#post10266673 "Post Permalink")

  * Sep 7, 2017 3:23pm  Sep 7, 2017 3:23pm 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@yan7181  
Yes that should work.  
  
I was planning to export the ea code to java to run it faster externally, which would mean it can then connect to anything from metatrader, jforex, fix and more and also to multiple brokers and combinations of it at the same time.  
  
Different [spreads](/brokers/spreads "View Live Spreads on the Broker Guide") will not matter, so long as the overall spread for all 3 is not too high, otherwise it will never trade for the arbitrage will not be big enough to cover the spread.  
  
But still a good idea.  
Brokers specialise in different currencies and therefore if you get a broker specialising in each currency with the lowest spread then it would be fantastic, just make sure the latency between all of them is extremely low to prevent slippage.  
Latency might be the biggest problem.  
  
But first I need to stabalise and test this ea, before enhancing it.  
  
Also another big problem that might prevent this is that you will need multiple accounts ballances at multiple brokers, which will be unbalanced and therefore one will increase in profit extremely fast just like the other will lose money just as fast.  
This account balance problem might be reason enough not to split it between different brokers. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#153](/thread/post/10321141#post10321141 "Post Permalink")

  * Edited 11:50pm  Sep 23, 2017 10:57pm | Edited 11:50pm 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

Hello everyone.  
  
My indigogo campain was a bust.  
I got hundreds of emails from people wanting the ea with no one wanting to contributing to the development ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
At least I tried.  
Still steaming away here and have got some nice updates to share with you all.  
  
Ok this is a MAJOR update.  
  
Rules changed a bit.  
Still triangular on the 3 symbols.  
  
But.  
I now calculate what the average profit would be if I did a BUY, SELL, SELL and also SELL,BUY,BUY.  
This gives me 2 lines.  
Call the higher line the ASK line and the lower line the BUY line.  
  
Between the 2 lines is the average line calculated over some time, which if mostly a straight line as the buy and sell lines basically cancels each other out there.  
  
Now from time to time you will notice the ASK line cross the average line and this is the time you must open a Buy(Sell, Buy, Buy) to profit from the inevitable up movement.  
Close the open buy once the SELL line cross the average line.  
Do the opposite for opening a sell(Buy,Sell,Sell).  
  
One more thing is that I do not just open when it crosses the middle average line, but I only open once it crosses the average line for some distance before opening.  
  
Ok there is a lot more checks and stuff I put in the EA, but that is the basics.  
  
I tested this on MyFxchoice with a leverage of 1:200 so try and keep to those settings.  
I might work on other settings and I did try and build in intelligence to adapt to other brokers, but I had limited time and it might not work properly.  
Backtest to make sure it works properly before a forward test.  
  
DO NOT USE ON LIVE ACCOUNT.  
  
Other things in the EA are :  
1) Do not trade weekend gaps for the Monday slippage can be big.  
2) Do not trade between midnight and 2 am for the same reason as (1).  
3) Move all display and log coding after the system calculations to increase trade calculation performance.  
4) Use only 50% of ac  
count for trading, which only mean that 50% of the account must be converted to used margin.  
Draw-down is about 5% then, but I can not increase it for fear of getting a margin call.  
20% might be better, but I will test it one day.  
  
5) Check for failed trades and kill them to start over.  
6) Check for weekend and inactive markets to prevent system failure.  
7) Check commission using single 0.01 lot trade.  
8) Massive amounts of logs and graph code to display what is happening.  
This uses a lot of memory so I must probably move it into another EA for display reasons only seeing that it is not needed to do trading with, but looks nice and you can see why the EA does what it does.  
Then there can be one EA to do trading with and another display EA which you can load somewhere else to show the workings, without the display EA affecting the trade processing.  
  
Problems:  
1) Slippage and trade delays.  
I am getting close to 500 milliseconds delay on opening 3 trades for the 3 symbols at a time.  
This can cause some major slippage, especially on the 3rd trade, but luckily I still make profit on most trades seeing that the EA does cater for some slippage.  
I'm still trying to find ways to decrease the time delay, but it seem to be a limitation on how metatrader works.  
  
1.1) I might be able to improve the trade speed using 4 metatrader terminals and I have already created programs to allow EAs communicate with the outside world within less than 1 millisecond, but there is still a delay of about 300 milliseconds for a single trade to start.  
  
On the bright side I have now developed a driver that can connect an EA to anything else from other EAs to other terminals or even outside programs like java and even to other PCs in other countries or any other device for that matter or even making a metatrader EA use things like the FIX api.  
The possibilities are big for this driver.  
  
1.2) Delayed trade starts seem to be caused by the terminal logging out if there is no trade action for some time and when a new trade is needed then the terminal for have to take some time to log back in before the trade can be opened or closed.  
I could not find a way to prevent logout, EXCEPT by sending dummy trades or impossible pending trades or trade modifications every 20 to 30 seconds.  
Problem with this might be that broker will not appreciate receiving so many trade signals.  
  
1.3) FIX API.  
I have been playing around with FIX api and it might be a solution to this trade delay, but I need to test it first and .... well... time is not on my side ![](https://resources.faireconomy.media/images/emojis/64/1f641.png?v=15.1)  
  
*******************************************************************************  
RUNNING THE EA  
*******************************************************************************  
Do not run on live account.  
  
Just attach the EA to a chart ....... That is it ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
  
Some more details.  
The EA is made to run with symbols GBPUSD, GBPJPY, USDJPY  
Exactly and it is case sensitive.  
If those symbols is not in your market watch or trade able then it will not work, UNLESS...  
  
There are a couple of parameters in the EA you can set.  
Mostly the trade symbols.  
Keep in mind the EA is only made for GBPUSD, GBPJPY, USDJPY  
BUT if your broker contains symbols like GBPUSD#e ex.. then you can use the parameters to change the EA to use your broker's symbols.  
Keep in mind it is case sensitive and therefore if your broker lists GBPUSD#e and you put in GBPUSD#E then the EA will not work.  
  
To view the chart drawn by the EA I suggest making the chart window background BLACK and zoom the chart out by dragging down on the right hand vertical price bar till u can see all the lines the EA draws on the chart.  
I'll even suggest making everything black as the chart price gives no useful information. 

Attached File(s)

![File Type: ex5](https://assets.faireconomy.media/images/attach/ex5.gif) [2017-09-18 09h00 JVB Arbitrage Auto Profit16.ex5](/attachment/file/2492558?d=1506175015) 123 KB | 365 downloads 

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [2017-09-18 09h00 JVB Arbitrage Auto Profit16.ex4](/attachment/file/2492559?d=1506175017) 67 KB | 481 downloads 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#154](/thread/post/10321337#post10321337 "Post Permalink")

  * Edited 3:07am  Sep 24, 2017 12:42am | Edited 3:07am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar53444_2.gif) dagoods](dagoods)

  * Joined Nov 2007 | Status: Trader | [3,059 Posts](/search?do=process&provider=Member&searchuser=53444)

> [Quoting jvbJacques](/thread/post/9988492#post9988492 "View Quoted Post")
> 
> Disliked
> 
> I will always update this POST #1 with the latest information. So if you do not want to read all the posts then just read this one. I will also keep the EAs up to date here. The rest of the posts are interesting and I love flame wars ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1) ******************************* Very basic summary ******************************* 1) Buy 1 unit GBPJPY 2) Sell 1 unit GBPUSD 3) Sell ?? units using the USD in point (2) in USDJPY to balance everything out Buy low and sell high. Rinse and repeat. Can this work or what is the pitfalls with this idea ? *******************************...
> 
> Ignored

  
what if......... you took it a bit deeper in order to overcome some realities....like spread and such.......... if the the concept is sound..... can we invent a method that does not rely on such small gains and losses so as to have the spread be a killer?  
  
for example: what if you took you initial trades or GJ and GU BUT you let them run for 24 hours or let it run until there was +100 or -100 dollars.............. Then you took a UJ trade or hedged it...... what would happen? your account would either be plus of minus but once you took your full triangle it would be locked in yes? hedged yes?  
  
IF you knew that price always retraces at least 20%, 98% of the time (or whatever variance you knew it did).... would this help you to figure out a way to make an eventual profit? for example if your hedge was -100 dollars it would fluctuate to -80 dollars eventually...... so for every loss your close it at -80 dollars but for every win you close it at +100 dollars  
  
of course those are hypothetical numbers, on average assumptions.  
  
<https://www.forexfactory.com/showthread.php?t=583322> <<< this concept (in first post, video)  
  
have no idea how to code so please don't ask...just throwing the idea over to you for your consideration  
i can already see the pitfall being a big trend and lots of losing days in a row..... maybe you can counter that somehow? maybe it won't matter?  
  
maybe you let the trade run only 10 minutes or 1 minute rather than one whole day.... just used 1 day to illustrate the idea  
  
That way, the profit is in the variance. The fluctuation of price = profits. But said fluctuation must be large enough to overcome spread.... the larger the range the better, no?  
  
think of cutting your losses(with 20/20 hindsight)...but not letting your profits run...but 100% banking your profits..... you still come out way ahead of the game, right?  
  
[https://www.forexfactory.com/showthr...1#post10321351](https://www.forexfactory.com/showthread.php?p=10321351#post10321351)  
  
anyhow, the basic concept is to take profit from the fluctuations.... the challenge is the fluctuations you have get eaten by the spread...the obvious solution is to increase the amount/size of fluctuation... yes? however that is accomplished. different kind of hedge besides triangle? multiple hedges, whatever....you can thank me later lol please share the source code if you accomplish it ![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)  
  
just musing  
  
Thanks ![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#155](/thread/post/10323107#post10323107 "Post Permalink")

  * Sep 25, 2017 4:37am  Sep 25, 2017 4:37am 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@Everyone  
I forgot to add an EA that you can back test with.  
The ones for forward testing are using an infinite loop and therefore will freeze a back-tester.  
This one I'm attaching now will just be activated during each tick of the chart.  
Therefore it will miss some opportunities, but still useful to see the back-test results.  
  
@dagoods  
Unfortunately leaving out one of the 3 legs of the triangle will destabilise it.  
Then the profit/loss will go fast into profit or loss with no limit.  
Once the 3rd leg is activated then yes you will lock in the profit or loss, but you will never regain the loss.  
  
As you said that if it is loss then once locked with 3rd leg then you can wait for some loss to be recovered, but not all and in this case you could just as well have started with 3 legs in the beginning and just waited for it to go into profit.  
  
In theory you should be able to make at most the same amount of profit this way as with starting with 3 legs, but the biggest problem is then sudden spikes or trends which will cause massive drawdowns.  
Therefore to go this way you have to use a much smaller amount of lots so that the drawdown does not kill your account.  
  
Also.  
Having only 2 legs will cause profit/loss with no limit, which is no different to the normal forex market where a top or bottom can always be broken, whereas with 3 legs the tops and bottoms are extremely stable and therefore you can bargain on them.  
  
The EA I have created already cater for any spreads or commissions.  
The smaller the spread/commission the more arbitrage opportunities.  
  
Run the backtest ea in a backtest to see how the 3 legs affect each other.  
  
Keep also in mind that at the moment I am only using GBPUSD,GBPJPY and USDJPY, but there are multiple other triangles that should also work. 

Attached File(s)

![File Type: ex5](https://assets.faireconomy.media/images/attach/ex5.gif) [2017-09-18 09h00 JVB Arbitrage Auto Profit16 backtest.ex5](/attachment/file/2493249?d=1506281841) 123 KB | 312 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#156](/thread/post/10323482#post10323482 "Post Permalink")

  * Sep 25, 2017 7:57am  Sep 25, 2017 7:57am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar53444_2.gif) dagoods](dagoods)

  * Joined Nov 2007 | Status: Trader | [3,059 Posts](/search?do=process&provider=Member&searchuser=53444)

> [Quoting jvbJacques](/thread/post/10323107#post10323107 "View Quoted Post")
> 
> Disliked
> 
> @Everyone I forgot to add an EA that you can back test with. The ones for forward testing are using an infinite loop and therefore will freeze a back-tester. This one I'm attaching now will just be activated during each tick of the chart. Therefore it will miss some opportunities, but still useful to see the back-test results. @dagoods Unfortunately leaving out one of the 3 legs of the triangle will destabilise it. Then the profit/loss will go fast into profit or loss with no limit. Once the 3rd leg is activated then yes you will lock in the profit...
> 
> Ignored

ok so set it for 100 dollars profit or loss which ever comes first, before locking in your hedge..... if the spread is 4 dollars... & the fluctuations are around 20% i.e, = 20 dollars...that should be doable, yes?  
  
each loss = -84 dollars and each win = +100 dollars  
  
  
if  
50 wins +5000 &  
50 losses -4200  
  
you net 800 dollars  
  
yes? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#157](/thread/post/10323597#post10323597 "Post Permalink")

  * Edited 9:05am  Sep 25, 2017 8:55am | Edited 9:05am 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@Everyone  
I did not include the modifiable parameters into the EAs.  
The newly attached ones contains the parameters so you can make sure the symbols match your broker's symbols.  
Keep in mind that the EAs is set to not use a lot of your account balance.  
If you back-test you will see the maximum draw-down is quite low.  
A 3rd parameter allows you to set the amount in % .. 0.5 = 50% of the account balance not to use.  
If you want to make it aggressive then try 0.1 or 0.2 on a leverage of 1:200.  
Problem is not that you will bottom out your account, but that you might hit a margin call if too aggressive.  
So even with a stop out your account will still survive, but you will take a loss so why risk it.  
Even at 50% where it stays far away from margin call it still makes good profit.  
Be careful for greed.  
  
  
@dagoods  
Unfortunately it will still not work.  
I tested it for fun and trading only 2 symbols makes the trading completely random or market dependant, which is random enough.  
So yes. Losses will be -$84 and profits $100, but the split will not be 50/50 and it might side with the losses more to 20/80 or worse.  
The 3 trades must be there from the beginning.  
  
As for the other grid thread you referenced.  
I tested the EAs they gave there and could not find one that made a good profit.  
Also they have massive draw-downs, which could kill accounts, but then again.  
Maybe I had the wrong settings.  
What I do not like about grids like that is that eventually during big trends they tend to cause big draw-downs, which will either kill your account or if you set the trading size very small then it will make very little profit.  
I have written quite a lot of grid EAs in the past and could not really find one that works.  
A grid might be useful to improve another already working strategy.  
  
I tried a grid strategy with this triangular EA, but although it improved the profit a bit it also increased the draw-down a lot so I decided to keep it simple (well sort of not really). 

Attached File(s)

![File Type: ex5](https://assets.faireconomy.media/images/attach/ex5.gif) [2017-09-18 09h00 JVB Arbitrage Auto Profit16 backtest.ex5](/attachment/file/2493408?d=1506297282) 123 KB | 309 downloads 

![File Type: ex5](https://assets.faireconomy.media/images/attach/ex5.gif) [2017-09-18 09h00 JVB Arbitrage Auto Profit16.ex5](/attachment/file/2493411?d=1506297290) 123 KB | 314 downloads 

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [2017-09-18 09h00 JVB Arbitrage Auto Profit16.ex4](/attachment/file/2493413?d=1506297294) 67 KB | 405 downloads 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#158](/thread/post/10325321#post10325321 "Post Permalink")

  * Sep 25, 2017 9:23pm  Sep 25, 2017 9:23pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar523703_1.gif) faryne](faryne)

  * | Joined Oct 2016  | Status: Trader | [93 Posts](/search?do=process&provider=Member&searchuser=523703)

How many trades by day the new system do? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#159](/thread/post/10325583#post10325583 "Post Permalink")

  * Sep 25, 2017 10:20pm  Sep 25, 2017 10:20pm 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@faryne  
It depends on a lot.  
  
But about one every 3 or so days.  
Sometimes on rare occasions a week can go by with no trades.  
Once open it closes normally within the same day.  
  
But more often than not.  
If there is arbitrage opportunities then there is normally multiple arbitrage opportunities the same day.  
  
So once every few days, but then multiple times that day.  
  
You can see it if you use very accurate real tick data on a back test for about a month back.  
I got about 4 hits last week, but the week before I only got 1, then again I only started it on that week on the Thursday.  
  
I am however struggling with trade lag.  
Because trades do not open so often then metatrader need to reconnect to the trade server every time a trade is made and this delays 3 trades by between 500ms and 1 seconds, which is a massive delay and causes slippage.  
I have seen this even on metatraders with a 7ms link.  
  
What is strange is that metatrader 5 seem to be much faster, closer to 200ms to 400 ms.  
Maybe mt5 have got a way to keep the connection open.  
  
I'm still looking for ways to decrease the trade execution speed to decrease slippage.  
I'm looking into using FIX api later to improve the speed.  
I have created a couple of drivers in the process of trying to improve the speed to connect and EA to external processes, which can include an application that can use the FIX api.  
I am planning to create a JAVA app to do the FIX trades using multiple threads and a way to monitor and keep open the trade server connection and the EA to just display the nice lines on the chart ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
  
Another way to to create dummy trades to keep the trade server connection open, but that will anger brokers, because it sounds like for this to work I have to send a trade once every 25 seconds. Not good for the broker. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#160](/thread/post/10326365#post10326365 "Post Permalink")

  * Sep 26, 2017 12:18am  Sep 26, 2017 12:18am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar523703_1.gif) faryne](faryne)

  * | Joined Oct 2016  | Status: Trader | [93 Posts](/search?do=process&provider=Member&searchuser=523703)

Thank you. I thought there was several each day.  
I just got a position, so it's actually working. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Simple High Profit low Drawdown Triangular Arbitrage
  *   * [ **Reply to Thread** ](/thread/676132-simple-high-profit-low-drawdown-triangular-arbitrage/reply#reply)

  * More

[](https://www.forexfactory.com "Homepage")

  * [Forums](forums)
  * [Trades](trades)
  * [Calendar](calendar)
  * [News](news)
  * [Market](market)
  * [Brokers](brokers)

****

[](https://www.faireconomy.com/)

  * 

[Triangular Arbitrage](/thread/64423-triangular-arbitrage "Admin, Please Delete Thread.") 258 replies

[Triangular Arbitrage](/thread/62477-triangular-arbitrage "Is going  
long 1 lot of eur/usd + 
long 1 lot of usd/jpy = long 1 lot of eur/jpy ?  
\(is the ratio of the number of lots correct for a...") 16 replies

[Triangular Arbitrage and carry trade](/thread/71997-triangular-arbitrage-and-carry-trade "Is it possible for us retail traders to be able to make use of Tri Arb or carry trades?  
 
Any one know of retail brokers 
 
 
\(I'm...") 6 replies

[Triangular Arbitrage](/thread/367072-triangular-arbitrage "I've been reading about triangular arbing and was surprised to find that the cross of two majors doesn't always equal what the calculation...") 7 replies

[Question: Trade Mechanics of Triangular Arbitrage](/thread/225246-question-trade-mechanics-of-triangular-arbitrage "Before I even ask this question, please allow me to be very clear.... I have no intention of attempting a triangular arbitrage trade\(for...") 6 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/676132-simple-high-profit-low-drawdown-triangular-arbitrage/reply#reply)
  * Subscribe
  * [147](javascript:void\(0\);)

Attachments: Simple High Profit low Drawdown Triangular Arbitrage

Tags: Simple High Profit low Drawdown Triangular Arbitrage

#  [](/thread/676132-simple-high-profit-low-drawdown-triangular-arbitrage)Simple High Profit low Drawdown Triangular Arbitrage 

  * 

  * [#161](/thread/post/10326458#post10326458 "Post Permalink")

  * Edited 12:39am  Sep 26, 2017 12:29am | Edited 12:39am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar53444_2.gif) dagoods](dagoods)

  * Joined Nov 2007 | Status: Trader | [3,059 Posts](/search?do=process&provider=Member&searchuser=53444)

> [Quoting jvbJacques](/thread/post/10323597#post10323597 "View Quoted Post")
> 
> Disliked
> 
> @Everyone I did not include the modifiable parameters into the EAs. The newly attached ones contains the parameters so you can make sure the symbols match your broker's symbols. Keep in mind that the EAs is set to not use a lot of your account balance. If you back-test you will see the maximum draw-down is quite low. A 3rd parameter allows you to set the amount in % .. 0.5 = 50% of the account balance not to use. If you want to make it aggressive then try 0.1 or 0.2 on a leverage of 1:200. Problem is not that you will bottom out your account, but...
> 
> Ignored

yes. it makes sense that it will be market dependant... that means you ought to come to a 50/50 (50% winning trades) eventually..... it is true and to be expected that you may possibly start with losses 20/80 or worse to begin with, Temporarily, and it is true also that it will eventually resolve itself. But i get it. it is not acceptable parameters for your brainy strategy. TY for testing it. So yeah it is a solution, just not one you particularly like. I still think it likely the only solution..... a solution that delivers a way to compensate for spread is going to have to do so with drawdown. I do not see any way around that. Could you not simply account for that with account size and money management? actually there is one way around that. a good strategy, that rarely loses many times in a row.... that way you decrease your probability of going 80/20 draw down n your eventual guaranteed profit.  
  
that interests me, because you are only looking for a strategy that wins a few loses a few without losing a bunch in a row, even if it is not a positive expectancy strategy....as opposed to a strategy that has + ev and an edge or profitability. your goal is to find a break even strategy that oscillates back n forth. that is kinda cool man. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#162](/thread/post/10326585#post10326585 "Post Permalink")

  * Edited 1:01am  Sep 26, 2017 12:51am | Edited 1:01am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar53444_2.gif) dagoods](dagoods)

  * Joined Nov 2007 | Status: Trader | [3,059 Posts](/search?do=process&provider=Member&searchuser=53444)

i'm not giving up just yet....lets go a little deeper...... lets do sets of ten trades, positive sets we bank but we also use the fluctuation to our advantage, negative sets we cut our losses as efficiently as possible.....  
  
  
e.g.  
take 10 trades hedged at +-100 dollars as discussed  
so if you get unlucky in your first set, 8 of them go negative and 2 positive  
then  
  
close the positive ones at +$120(as opposed to only +100 dollars) = +240  
  
close the negative ones at -84 = -672  
Net = -432  
  
then take the next set of 10 trades....... etc.  
  
you get the idea  
  
if this time you have 5 wins and 5 losses = 600-420= +180  
  
  
since your overall EV is +18% you will eventually make 18% in the long run....  
  
the question is one of practicality and efficiency to find the most efficient workable parameters, i.e money management, not the theory. no?  
  
obviously it isn't ideal, but it is a solution 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#163](/thread/post/10326719#post10326719 "Post Permalink")

  * Sep 26, 2017 1:09am  Sep 26, 2017 1:09am 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@faryne  
NOOOOOOOOOOOOOOOoooo  
I messed up by playing with my code and it opened the wrong trade on my side ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
Will teach me to not experiment to much with the code ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
Don't worry.  
The oops I did in the code is not in the EA on this forum.  
But for interest sake look at the expert log.  
You will see where it start opening the trades.  
  
Check from the log time of the log line just before the first trade and the log line just after the last trade to see the trade lag.  
This is a easy way to see the trade delay.  
You want that as short as possible.  
  
Also look for a line "OPEN3".  
The last one of those lines will show the amount of slippage because of the trade delay.  
  
  
  
@dagoods  
Brainy ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1) thanks. But I just like maths and programming so lets call it lucky ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
I really appreciate your input.  
I can see what you mean by leaving the one leg out and yes over a longer period of time it should level out to about 50/50 if you ignore the spread and commission.  
So your theory will work, but the problem is that it will increase the drawdown from the current say 10% to closer to 100%.  
To decrease the the drawdown you must then trade smaller amounts of lots, but this also decreases the amount of profit.  
So in theory ultimately it should balance out to about the same as the current strategy of using 3 legs.  
  
But as I am now typing I can start to see a glimmer of a possibility where it might make the affect of spread a bit less.  
  
The big problem is sudden movements.  
  
With 3 legs all balances out.  
So during a big market spike I have seen 2 symbols go negative -$20000 on a $10000 account, only for the 3rd symbol to be positive $20000 so balancing out to ZERO.  
  
Now if there where only 2 legs and you were unlucky to use the 2 losing symbols then your account would have been blown.  
  
OK OK this is a bit of an exaggeration. It is more like -$6000 on a $10000 account, but more than enough to hit your margin call and stop out levels.  
If you run the back test slow it down and watch the trades running.  
It is scary to see how big or low the profit goes for single symbols, only to be cancelled out by the others.  
  
Lets call the current 3 legs strategy the safe approach and the 2 leg one the risky profitable one.  
Still the safe strategy can still make 100% profit every 3 or so months during slow times and that to me is good for now and prevents heart attacks from crazy market movement ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
10% on my one account just last week. Was unexpected.  
  
Still it is food for thought and something I can test a bit more in future with some safeguards in place, but my main focus now is to decrease the execution time using FIX API or whatever else I can incorporate to decrease the slippage.  
  
  
  
I would love to get access to brokers with [spreads](/brokers/spreads "View Live Spreads on the Broker Guide") close to or even better than ENC broker with extremely low commission.  
Probably only available to banks, but just think how many hits the EA will get with an account like those.  
  
  
  
@dagoods 2nd post ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
That sounds like a grid system.  
Yes that should also work.  
  
Problem is that the current EA uses as much if not all of the available margin, minus a bit a profit/loss gap.  
So for each grid level you add you have to decrease your lot sizes by half.  
So 3 grid levels deep is 4 times less and 4 times is 8 times lot size less.  
  
I did have a grid system in the beginning and found that I get about the same amount of profit.  
For some strange wonderful reason if I use the 3 legs with a grid then decrease the lot size to cater for the extra grid levels then the extra grid levels cancels out the lot size decreases to give about the same amount of profit, maybe a bit less.  
  
But still I can see where you are going with the 2 leg strategy and I want to test it, but time management is my biggest problem at this time.  
I have barely enough time for this one EA, let alone all the variations on it and all the limitations of metatrader I had to overcome.  
I basically get a couple of hours maybe once every 3 or so days and that is if I sleep 3 hours a day, luckily I get 4 hours sleep a day ![](https://resources.faireconomy.media/images/emojis/64/1f641.png?v=15.1)  
I wish I could do this full time.  
Just think of the wonders I could develop.  
  
This EA already produces some mutations like a 1 leg latency arbitrage, drivers to connect outside of metatrader, fix api incorporation, multi-threaded MT4 and MT5 EA functionality, massive market watch speed improvement coding, and lots more...  
Time is not on my side ![](https://resources.faireconomy.media/images/emojis/64/1f641.png?v=15.1)  
  
But do not stop giving ideas, maybe one day.  
  
  
Now to go and fix my coding mistake on my running EA ![](https://resources.faireconomy.media/images/emojis/64/1f641.png?v=15.1)  
I like chatting too much ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#164](/thread/post/10329344#post10329344 "Post Permalink")

  * Sep 26, 2017 7:13pm  Sep 26, 2017 7:13pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar438576_2.gif) raffus](raffus)

  * | Joined Dec 2015  | Status: Member RFP | [57 Posts](/search?do=process&provider=Member&searchuser=438576)

hello @jvbJacques  
first of all i would like to thank you about your job.  
  
i have attached to GBPUSD chart your lastest ea to MT4 demo with €500  
first of all it opened & closed 1 position, losing some eurocents. (i don't know why but it is twice)  
  
After that it opened with maxDD set @0.3:

  1. GBPJPY = 0.50 lot
  2. GBPUSD = 0.50 lot
  3. USDJPY = 0.67 lot

  
currently the floating point is -15.13 euro  
my question is this: is correct different lost used? because USDJPY was 0.50 as the other 2 the floating point should be -6.13 euro  
  
thanks x all  
regards 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#165](/thread/post/10329470#post10329470 "Post Permalink")

  * Sep 26, 2017 7:44pm  Sep 26, 2017 7:44pm 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@raffus  
All seems correct.  
  
The first trade is to determine the commission.  
It opens one 0.01 lot trade and closes it immediately, only once and then look into the trade history to determine the commission.  
  
There is only one of those 0.01 lot trades, but I suspect you are using mt5, which to me has got a better trade response time than mt4.  
In MT5 one trade looks like 2, instead of 1, but it is only one.  
1 = an "IN" trade indicating a position was opened.  
2= an "OUT" trade indicating the above "IN" position was closed.  
But together they form one fully completed trade.  
  
As for USDJPY.  
It must not be the same amount of lots as the other 2 so it is correct.  
It need to be different to fully hedge/balance out the calculation.  
  
As for the profit/loss.  
Look at the lines drawn on the chart.  
I suggest making everything on the chart BLACK so that the lines the EA draws can stand out better, then zoom the chart out to see the lines.  
  
There are 2 line channels indicating a virtual ASK and BID lines.  
Then there are 2 blue lines indicating the open trade positions and finally the middle average line.  
If the ASK line crosses the bottom blue line then a trade opens.  
The trade will remain open until the BID line crosses the middle line.  
  
The amount of profit depends on the amount of slippage you have.  
So I suggest you must have a very good broker connection of about 50ms or less.  
  
But yes the profit/loss will float there forever until it crosses the middle line.  
  
I'm still looking into a way to improve the trade response speed to reduce slippage.  
I was thinking of creating a pending impossible trade and then updating that trade once every 25 second to keep the trade server connection connection so that there is no delay in waiting for metatrader to first sign on to the trade server every-time a trade need to be made.  
  
FIX is even better, but I have no demo FIX account to test it on so for now that must wait.  
  
I still suggest not to use this on a real account until fully tested and developed.  
Remember.  
I have not inserted code to pick up preexisting trades, so if metatrader restarts then you must first close all existing trades before restarting the EA.  
  
I will insert code later to pick up existing trades.  
  
Good luck. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#166](/thread/post/10329688#post10329688 "Post Permalink")

  * Sep 26, 2017 8:35pm  Sep 26, 2017 8:35pm 

  * [ eatrader75](eatrader75)

  * | Joined Aug 2017  | Status: Trader | [28 Posts](/search?do=process&provider=Member&searchuser=605097)

Hi Jacques,  
  
Thanks for the EA!  
On forward demo test (broker with ping 8.71ms) yesterday I've got trades with different lot sizes, as it should be. By mistake, the Metatrader restated so I had to close those trades manually. Today, however, the EA opened trades with the same lots. At the moment is in floating profit, waiting for the EA to close them by itself.  
  
Regards  
Attila 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: open and closed trades.jpg
Size: 143 KB](/attachment/image/2495655/thumbnail?d=1506424432)](/attachment/image/2495655?d=1506424432)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#167](/thread/post/10329723#post10329723 "Post Permalink")

  * Sep 26, 2017 8:49pm  Sep 26, 2017 8:49pm 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@eatrader75  
Sorry to hear about the restart.  
Will include the code to pick up lingering trades upon EA restart as I get time.  
Just keep in mind this is still a work in progress.  
  
Still a good example of what happens with the triangle.  
You can leave the trades for a long time and the floating profit loss will always return to the zero point. (If little to no slippage)  
So less stress.  
  
Nice commission.  
What spread do you get on the 3 symbols ?  
  
Also look into the expert logs to see what slippage you are getting.  
fx1=GBPJPY  
fx2=GBPUSD  
fx3=USDJPY  
  
So looking through the mess of logs you can see what symbol does what by looking for the 1,2,3.  
  
Good luck ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#168](/thread/post/10329836#post10329836 "Post Permalink")

  * Sep 26, 2017 9:08pm  Sep 26, 2017 9:08pm 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@Everyone and @eatrader75  
Looking at your screenshot I can see a problem.  
  
The buy,sell,sell is not balanced.  
Lot size of USDJPY need to be different.  
  
I do not know if some test code snuck in, but in either case.  
Please update your EAs with the new attached EAs. 

Attached File(s)

![File Type: ex5](https://assets.faireconomy.media/images/attach/ex5.gif) [2017-09-18 09h00 JVB Arbitrage Auto Profit17.ex5](/attachment/file/2495746?d=1506427729) 125 KB | 296 downloads 

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [2017-09-18 09h00 JVB Arbitrage Auto Profit17.ex4](/attachment/file/2495748?d=1506427731) 69 KB | 406 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#169](/thread/post/10329897#post10329897 "Post Permalink")

  * Sep 26, 2017 9:21pm  Sep 26, 2017 9:21pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar402047_21.gif) Fxentropy](fxentropy)

  * Joined Feb 2015 | Status: Who Dares Wins | [1,710 Posts](/search?do=process&provider=Member&searchuser=402047)

> [Quoting jvbJacques](/thread/post/10329836#post10329836 "View Quoted Post")
> 
> Disliked
> 
> @Everyone and @eatrader75 Looking at your screenshot I can see a problem. The buy,sell,sell is not balanced. Lot size of USDJPY need to be different. I do not know if some test code snuck in, but in either case. Please update your EAs with the new attached EAs. {file} {file}
> 
> Ignored

Uploaded V17 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: xJhur.png
Size: 76 KB](/attachment/image/2495780/thumbnail?d=1506428458)](/attachment/image/2495780?d=1506428458)   

"What would you attempt to do, if you knew your success was a certainty?"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#170](/thread/post/10329909#post10329909 "Post Permalink")

  * Sep 26, 2017 9:23pm  Sep 26, 2017 9:23pm 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@Fxentropy  
Looks correct.  
It will only start trading after 100 minutes so give it time for it to build up some history.  
  
@Everyone  
If you want to view the lines drawn by the EA correctly then attach the EA to a 1 minute chart.  
On a one hour or other time-frame it is a bit difficult to see the finer points of the chart.  
  
The time-frame of the chart does not affect the working of the EA.  
Just the display part. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot from 2017-09-26 14-28-02.png
Size: 110 KB](/attachment/image/2495796/thumbnail?d=1506428943)](/attachment/image/2495796?d=1506428943)   

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#171](/thread/post/10329952#post10329952 "Post Permalink")

  * Sep 26, 2017 9:34pm  Sep 26, 2017 9:34pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar402047_21.gif) Fxentropy](fxentropy)

  * Joined Feb 2015 | Status: Who Dares Wins | [1,710 Posts](/search?do=process&provider=Member&searchuser=402047)

> [Quoting jvbJacques](/thread/post/10329909#post10329909 "View Quoted Post")
> 
> Disliked
> 
> @Fxentropy Looks correct. It will only start trading after 100 minutes so give it time for it to build up some history. @Everyone If you want to view the lines drawn by the EA correctly then attach the EA to a 1 minute chart. On a one hour or other time-frame it is a bit difficult to see the finer points of the chart. The time-frame of the chart does not affect the working of the EA. Just the display part. {image}
> 
> Ignored

Done 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: xJhTt.png
Size: 73 KB](/attachment/image/2495809/thumbnail?d=1506429263)](/attachment/image/2495809?d=1506429263)   

"What would you attempt to do, if you knew your success was a certainty?"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#172](/thread/post/10329998#post10329998 "Post Permalink")

  * Sep 26, 2017 9:41pm  Sep 26, 2017 9:41pm 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@Fxentropy  
WOW  
The difference between the top white line and the bottom red line is basically your spread/commission.  
  
You have got a fantastic spread and commission.  
What is your commission and spread and where can I get an account like that ?  
  
Look at my screenshot of myfxchoice in post #170  
It is not even close ![](https://resources.faireconomy.media/images/emojis/64/1f641.png?v=15.1)  
  
The smaller the spread and commission the more arbitrage hits you will get.  
  
Again.  
What broker and account are you using and can a broke guy like me get an account like that or is it something special ? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#173](/thread/post/10330011#post10330011 "Post Permalink")

  * Sep 26, 2017 9:48pm  Sep 26, 2017 9:48pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar402047_21.gif) Fxentropy](fxentropy)

  * Joined Feb 2015 | Status: Who Dares Wins | [1,710 Posts](/search?do=process&provider=Member&searchuser=402047)

> [Quoting jvbJacques](/thread/post/10329998#post10329998 "View Quoted Post")
> 
> Disliked
> 
> @Fxentropy WOW The difference between the top white line and the bottom red line is basically your spread/commission. You have got a fantastic spread and commission. What is your commission and spread and where can I get an account like that ? Look at my screenshot of myfxchoice in post #170 It is not even close ![](https://resources.faireconomy.media/images/emojis/64/1f641.png?v=15.1) The smaller the spread and commission the more arbitrage hits you will get. Again. What broker and account are you using and can a broke guy like me get an account like that or is it something special ?
> 
> Ignored

This is a Darwinex account. (Leverage 200)  
  
But i think you can get one cheaper at [Pepperstone](/brokers/pepperstone "View Pepperstone Broker Profile") (Leverage 400). Also Onetrade (Leverage 100) is sharp too.  
  
All brokers can be funded with 100$ or even less... 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: xJijG.png
Size: 96 KB](/attachment/image/2495826/thumbnail?d=1506430097)](/attachment/image/2495826?d=1506430097)   

"What would you attempt to do, if you knew your success was a certainty?"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#174](/thread/post/10330073#post10330073 "Post Permalink")

  * Sep 26, 2017 10:04pm  Sep 26, 2017 10:04pm 

  * [ eatrader75](eatrader75)

  * | Joined Aug 2017  | Status: Trader | [28 Posts](/search?do=process&provider=Member&searchuser=605097)

> [Quoting jvbJacques](/thread/post/10329723#post10329723 "View Quoted Post")
> 
> Disliked
> 
> @eatrader75 Sorry to hear about the restart. Will include the code to pick up lingering trades upon EA restart as I get time. Just keep in mind this is still a work in progress. Still a good example of what happens with the triangle. You can leave the trades for a long time and the floating profit loss will always return to the zero point. (If little to no slippage) So less stress. Nice commission. What spread do you get on the 3 symbols ? Also look into the expert logs to see what slippage you are getting. fx1=GBPJPY fx2=GBPUSD fx3=USDJPY So looking...
> 
> Ignored

I get lost in the log so I think a screenshot is better... 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: slippage.jpg
Size: 456 KB](/attachment/image/2495856/thumbnail?d=1506431038)](/attachment/image/2495856?d=1506431038)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#175](/thread/post/10330427#post10330427 "Post Permalink")

  * Edited 11:32pm  Sep 26, 2017 11:04pm | Edited 11:32pm 

  * [ Forex-Loser](forex-loser)

  * | Joined Aug 2017  | Status: Trader | [6 Posts](/search?do=process&provider=Member&searchuser=605222)

Hi folks !  
  
Installed V17 on MT5, on my VPS for forward testing yesterday.  
  
Eveyone seems to have nice little colored bars... but me !  
  
Any reason? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#176](/thread/post/10330841#post10330841 "Post Permalink")

  * Sep 27, 2017 12:05am  Sep 27, 2017 12:05am 

  * [ eatrader75](eatrader75)

  * | Joined Aug 2017  | Status: Trader | [28 Posts](/search?do=process&provider=Member&searchuser=605097)

> [Quoting Forex-Loser](/thread/post/10330427#post10330427 "View Quoted Post")
> 
> Disliked
> 
> Hi folks ! Installed V17 on MT5, on my VPS for forward testing yesterday. Eveyone seems to have nice little colored bars... but me ! Any reason?
> 
> Ignored

Check the Market Watch on the left-hand side of the Metatrader. It has to show all the 3 currency pairs needed for this ea: GBPUSD, GBPJPY and USDJPY. If not, click to add. Then put back the ea on the chart 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#177](/thread/post/10331062#post10331062 "Post Permalink")

  * Sep 27, 2017 12:39am  Sep 27, 2017 12:39am 

  * [ Forex-Loser](forex-loser)

  * | Joined Aug 2017  | Status: Trader | [6 Posts](/search?do=process&provider=Member&searchuser=605222)

OK it works now after reinstalling the EA on a chart.  
  
Will post results here every friday afternoon.  
  
Thanks 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#178](/thread/post/10331220#post10331220 "Post Permalink")

  * Sep 27, 2017 1:10am  Sep 27, 2017 1:10am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar402047_21.gif) Fxentropy](fxentropy)

  * Joined Feb 2015 | Status: Who Dares Wins | [1,710 Posts](/search?do=process&provider=Member&searchuser=402047)

Anyone had a trade in last couple of hours?. I had not 

"What would you attempt to do, if you knew your success was a certainty?"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#179](/thread/post/10331237#post10331237 "Post Permalink")

  * Sep 27, 2017 1:17am  Sep 27, 2017 1:17am 

  * [ eatrader75](eatrader75)

  * | Joined Aug 2017  | Status: Trader | [28 Posts](/search?do=process&provider=Member&searchuser=605097)

> [Quoting Fxentropy](/thread/post/10331220#post10331220 "View Quoted Post")
> 
> Disliked
> 
> Anyone had a trade in last couple of hours?. I had not
> 
> Ignored

I had only one at London opening 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#180](/thread/post/10331437#post10331437 "Post Permalink")

  * Sep 27, 2017 1:55am  Sep 27, 2017 1:55am 

  * [ eatrader75](eatrader75)

  * | Joined Aug 2017  | Status: Trader | [28 Posts](/search?do=process&provider=Member&searchuser=605097)

Just missed an opportunity... 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot1.png
Size: 117 KB](/attachment/image/2496261/thumbnail?d=1506444847)](/attachment/image/2496261?d=1506444847)   

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Simple High Profit low Drawdown Triangular Arbitrage
  *   * [ **Reply to Thread** ](/thread/676132-simple-high-profit-low-drawdown-triangular-arbitrage/reply#reply)

  * More

[](https://www.forexfactory.com "Homepage")

  * [Forums](forums)
  * [Trades](trades)
  * [Calendar](calendar)
  * [News](news)
  * [Market](market)
  * [Brokers](brokers)

****

[](https://www.faireconomy.com/)

  * 

[Triangular Arbitrage](/thread/64423-triangular-arbitrage "Admin, Please Delete Thread.") 258 replies

[Triangular Arbitrage](/thread/62477-triangular-arbitrage "Is going  
long 1 lot of eur/usd + 
long 1 lot of usd/jpy = long 1 lot of eur/jpy ?  
\(is the ratio of the number of lots correct for a...") 16 replies

[Triangular Arbitrage and carry trade](/thread/71997-triangular-arbitrage-and-carry-trade "Is it possible for us retail traders to be able to make use of Tri Arb or carry trades?  
 
Any one know of retail brokers 
 
 
\(I'm...") 6 replies

[Triangular Arbitrage](/thread/367072-triangular-arbitrage "I've been reading about triangular arbing and was surprised to find that the cross of two majors doesn't always equal what the calculation...") 7 replies

[Question: Trade Mechanics of Triangular Arbitrage](/thread/225246-question-trade-mechanics-of-triangular-arbitrage "Before I even ask this question, please allow me to be very clear.... I have no intention of attempting a triangular arbitrage trade\(for...") 6 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/676132-simple-high-profit-low-drawdown-triangular-arbitrage/reply#reply)
  * Subscribe
  * [147](javascript:void\(0\);)

Attachments: Simple High Profit low Drawdown Triangular Arbitrage

Tags: Simple High Profit low Drawdown Triangular Arbitrage

#  [](/thread/676132-simple-high-profit-low-drawdown-triangular-arbitrage)Simple High Profit low Drawdown Triangular Arbitrage 

  * 

  * [#181](/thread/post/10332100#post10332100 "Post Permalink")

  * Edited 4:59am  Sep 27, 2017 4:31am | Edited 4:59am 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@EVERYONE  
WAIT FOR VERSION 18.  
I discovered a but in the MT4 version of the EA in that it does not calculate the SELL trades correctly.  
  
  
@eatrader75  
@Post #174  
The logs ..... ooooo ... the logs ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
I went log crazy ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
  
There is a lot of information.  
The stuff about the Illuminati, Bermuda triangle and JFK assassination you can ignore.  
  
Look at the "*** OPEN" and "*** CLOSE" lines.  
They contain what the 3 prices were before the tickets were opened and then after.  
Then it also contains the amount the price slipped "SLIP" after the trades were opened.  
I can see that GBPJPY slipped by 1.6 pips, GBPUSD by 1 pip and USDJPY did not slip, which is not to bad.  
  
You can also look at the actual opening of trades.  
Look at the first log line before the first trade opened and its timestamp.  
Then look at time of the last trade and you will see how long it took to open the 3 trades.  
In your case it took about 100ms to open a trade so 325ms to open all 3, which is not to bad from what I have seen, but compared to FIX API it is bad.  
  
I am still looking for a way to improve on the open and close time delays.  
One way is to communicate with the trade server every 25 seconds to prevent the connection from timing out so that there is no login delay before trades, but I do not think brokers will like 2880 signal per day that is not actually open or close trade signals, but other than that or the FIX api I am not sure how to speed it up ... YET.  
Suggestions are welcome.  
  
According to me the time to open/close a ticket should not be longer than 2 times your connection speed to the server.  
I have developed a multi threaded version of the EA, but it runs even worse, because each thread then need to sign on seeing that they run in seperate metatrader instances, where a single thread only signs on once.  
  
@Post #180  
Nooo...  
Why did you restart it ![](https://resources.faireconomy.media/images/emojis/64/1f641.png?v=15.1)  
Yes you missed it because of the 100 minute start delay.  
Too bad.  
Next time ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
You might want to look for a broker with a better spread and commission also.  
The distance between the top white channel and bottom red channel is a bit big.  
It will work, but only once in a while like mine ![](https://resources.faireconomy.media/images/emojis/64/1f641.png?v=15.1)  
  
@Post #174  
Looking at the logs I still see a problem in that the trades contains the same amount of lots.  
Is this version 17 of the EA ?  
That is wrong.  
I will look into it a bit.  
Found the bug.  
Will be fixed in version 18 

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#182](/thread/post/10332317#post10332317 "Post Permalink")

  * Sep 27, 2017 5:53am  Sep 27, 2017 5:53am 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

Fixed  
Attached is the new EA.  
  
Someone please tell me how to remove the trade delay on trades in metatrader.  
It is really frustrating.  
500ms is a long time to wait for a trade to go through, even 100ms is a long time if you have got a 6ms link to the server. 

Attached File(s)

![File Type: ex5](https://assets.faireconomy.media/images/attach/ex5.gif) [2017-09-18 09h00 JVB Arbitrage Auto Profit18.ex5](/attachment/file/2496587?d=1506459200) 126 KB | 323 downloads 

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [2017-09-18 09h00 JVB Arbitrage Auto Profit18.ex4](/attachment/file/2496590?d=1506459201) 68 KB | 445 downloads 

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#183](/thread/post/10332345#post10332345 "Post Permalink")

  * Sep 27, 2017 6:03am  Sep 27, 2017 6:03am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar402047_21.gif) Fxentropy](fxentropy)

  * Joined Feb 2015 | Status: Who Dares Wins | [1,710 Posts](/search?do=process&provider=Member&searchuser=402047)

> [Quoting jvbJacques](/thread/post/10332317#post10332317 "View Quoted Post")
> 
> Disliked
> 
> Fixed Attached is the new EA. Someone please tell me how to remove the trade delay on trades in metatrader. It is really frustrating. 500ms is a long time to wait for a trade to go through, even 100ms is a long time if you have got a 6ms link to the server. {file} {file}
> 
> Ignored

Lock and load  
  
"Someone please tell me how to remove the trade delay on trades in metatrader" _ you may want to ask XMESS7, he is **a really good guy and a awesome coder**!  
  
<https://www.forexfactory.com/xmess7> ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)

Attached Image (click to enlarge)

[![Click to Enlarge

Name: xJChW.png
Size: 165 KB](/attachment/image/2496599/thumbnail?d=1506459792)](/attachment/image/2496599?d=1506459792)   

"What would you attempt to do, if you knew your success was a certainty?"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#184](/thread/post/10332372#post10332372 "Post Permalink")

  * Sep 27, 2017 6:17am  Sep 27, 2017 6:17am 

  * [ eatrader75](eatrader75)

  * | Joined Aug 2017  | Status: Trader | [28 Posts](/search?do=process&provider=Member&searchuser=605097)

Jacques,  
  
@Post #174  
Thanks for help with the logs!  
I run 2 MT's: [FxPro](/brokers/fxpro "View FxPro Broker Profile") and Global Prime. FxPro is quicker (9ms) and has higher spread rate on these pairs: 1-3 pips or more. GP has less than 1 pip with 7$ commission per lot but the ping is 79ms and had no trade. Anyway, if we manage to go live with, will need a VPS. Maybe I'll try Darwinex too, suggested by Fxentropy.  
  
@Post #180  
The lots weren't well balanced (v16) so I just wanted to save the 38$ demo profit and try your v17. As you see the attachment in Post #166, the first set of trade was ok only the second set went wrong.  
  
I'll try multiple pairs with reduced account size so possibly will get more trades to analyse. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#185](/thread/post/10332378#post10332378 "Post Permalink")

  * Sep 27, 2017 6:21am  Sep 27, 2017 6:21am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar455078_1.gif) aszain02](aszain02)

  * | Joined Mar 2016  | Status: Mr Perfect | [74 Posts](/search?do=process&provider=Member&searchuser=455078)

> [Quoting jvbJacques](/thread/post/10332317#post10332317 "View Quoted Post")
> 
> Disliked
> 
> Fixed Attached is the new EA. Someone please tell me how to remove the trade delay on trades in metatrader. It is really frustrating. 500ms is a long time to wait for a trade to go through, even 100ms is a long time if you have got a 6ms link to the server. {file} {file}
> 
> Ignored

Use a good vps with good ms speed. There are a lot in market connecting less then 1 ms speed, first check ur forex mt4 location from ur broker.  
for example : USA, U.K. Eu, then buy the appropriate one. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#186](/thread/post/10332407#post10332407 "Post Permalink")

  * Sep 27, 2017 6:44am  Sep 27, 2017 6:44am 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@eatrader75  
Yes the bug was in the 2nd part of the coding also.  
There is no way to backtest the MT4 code to make sure it runs correctly so it only revealed itself during the forward test.  
Thanks for the log ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
  
MT5 I could backtest and it is running correctly since version 16 using the new coding.  
  
  
  
@aszain02  
I helped someone with a VPS which have got a 17ms connection to the MyFxChoice servers, but the trade delay is still about 500ms for 3 trades.  
Maybe there is something else in play here.  
Maybe 17ms is just to the MyFxChoice MT4 server and then it still need to go to the actual market from there, but that speed I can not test seeing that I do not know how they connect.  
Then again it is pure speculation.  
  
I just need to find a way to reduce the delay, because a lot can happen in a second.  
  
Then I helped someone else with a VPS connecting to another broker with a 3ms to 5ms connection that gets a trade delay of a WOPPING 2 seconds for opening 3 trades.  
That is crazy slow.  
So something else must happen in the background.  
Same metatrader version.  
  
Maybe it also depends on the broker themselves.  
Just not sure how to find out which broker is fast.  
  
I was thinking of testing on Dukascopy, but for that I need to convert the EA to java to run on JTrader, which I am planning to do seeing that Java is my speciality.  
From what I heard Dukascopy have got very fast order execution.  
  
Yet another theory is that the delay is done on purpose by the broker on demo accounts so as not to slow down live accounts.  
That is extremely difficult to test. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#187](/thread/post/10332544#post10332544 "Post Permalink")

  * Sep 27, 2017 8:05am  Sep 27, 2017 8:05am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar455078_1.gif) aszain02](aszain02)

  * | Joined Mar 2016  | Status: Mr Perfect | [74 Posts](/search?do=process&provider=Member&searchuser=455078)

> [Quoting jvbJacques](/thread/post/10332407#post10332407 "View Quoted Post")
> 
> Disliked
> 
> @eatrader75 Yes the bug was in the 2nd part of the coding also. There is no way to backtest the MT4 code to make sure it runs correctly so it only revealed itself during the forward test. Thanks for the log ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1) MT5 I could backtest and it is running correctly since version 16 using the new coding. @aszain02 I helped someone with a VPS which have got a 17ms connection to the MyFxChoice servers, but the trade delay is still about 500ms for 3 trades. Maybe there is something else in play here. Maybe 17ms is just to the MyFxChoice MT4 server and...
> 
> Ignored

can u plz give a try on other brokers :  
[tickmill](/brokers/tickmill "View Tickmill Broker Profile")  
jfd  
paternosters  
Regards 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#188](/thread/post/10333256#post10333256 "Post Permalink")

  * Sep 27, 2017 4:17pm  Sep 27, 2017 4:17pm 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@aszain02  
I live in South Africa.  
My ping to most brokers are about 600ms to 800ms.  
For me to test without a VPS close to each of those brokers is next to impossible.  
  
The VPS I did use is someone else's and I can not do with it what I like out of respect.  
  
I would love to test it. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#189](/thread/post/10333636#post10333636 "Post Permalink")

  * Sep 27, 2017 5:41pm  Sep 27, 2017 5:41pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar402047_21.gif) Fxentropy](fxentropy)

  * Joined Feb 2015 | Status: Who Dares Wins | [1,710 Posts](/search?do=process&provider=Member&searchuser=402047)

Still havent got one trade yet....its normal? 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: xK15J.png
Size: 99 KB](/attachment/image/2497212/thumbnail?d=1506501684)](/attachment/image/2497212?d=1506501684)   

"What would you attempt to do, if you knew your success was a certainty?"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#190](/thread/post/10333915#post10333915 "Post Permalink")

  * Sep 27, 2017 6:53pm  Sep 27, 2017 6:53pm 

  * [ eatrader75](eatrader75)

  * | Joined Aug 2017  | Status: Trader | [28 Posts](/search?do=process&provider=Member&searchuser=605097)

Jacques,  
  
I might be wrong trying with other pairs (e.g. EURJPY, EURCHF, CHFJPY) - I know, you've designed the ea for GBPJPY, GBPUSD, USDJPY. Simply, I wanted to see more trades on the forward test. I've got the same good results on MT5 backtest (V16 backtest) with these new pairs. It's true, no drawing. No drawing on forward test either. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot1.png
Size: 87 KB](/attachment/image/2497311/thumbnail?d=1506504949)](/attachment/image/2497311?d=1506504949)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#191](/thread/post/10334079#post10334079 "Post Permalink")

  * Sep 27, 2017 7:43pm  Sep 27, 2017 7:43pm 

  * [ love4kilo](love4kilo)

  * | Joined Apr 2017  | Status: Trader | [2 Posts](/search?do=process&provider=Member&searchuser=572431)

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot2.png
Size: 1.8 MB](/attachment/image/2497424/thumbnail?d=1506508986)](/attachment/image/2497424?d=1506508986)   

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot4.png
Size: 1.1 MB](/attachment/image/2497426/thumbnail?d=1506509007)](/attachment/image/2497426?d=1506509007)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#192](/thread/post/10334514#post10334514 "Post Permalink")

  * Sep 27, 2017 9:33pm  Sep 27, 2017 9:33pm 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@Fxentropy  
Yes that is normal.  
Days can go bye with no trade, but I found the past few days to contain a couple of hits.  
Just give it time.  
According to your chart there was no hit yet, but they did come close a couple of times.  
  
I am working on a new model to hopefully cater for more slippage and more profit in a shorter period of time.  
  
Also keep in mind that once the EA is stable then I will be adding all possible triangle as @eatrader75 already started to test ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
That should speed up the number of arbitrage hits exponentially, but it is easier to test and develop using one triangle for now until I know everything is working correctly rather than multiple triangles and then also trying to figure out in which triangle a bug is.  
This strategy is extremely expandable.  
  
  
  
@eatrader75  
My original idea was to run it on all possible triangles at the same time so that you get more hits.  
So yes it should work on other triangles like your pairs, but I did focus on GBP first until I can stabilise the EA.  
Once stable then I can incorporate the other pairs.  
  
The nice thing about this strategy is that you can add as many pairs as you want with no extra drawdown.  
Just more hits and profit, but only as long as the same EA handles all the pairs seeing that they can not be opened at the same time or risk hitting margin call.  
  
Just make sure when you backtest to use EVERY TICK BASED ON REAL DATA and not EVERY TICK.  
I suspect you used EVERY TICK.  
It is not as accurate, but it does look very good. ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
  
As for not seeing the chart.  
You must attach the EA to the 2nd symbol, which in this case is EURCHF.  
It is drawing the cart on EURJPY, but somewhere off screen close to Jupiter. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#193](/thread/post/10334967#post10334967 "Post Permalink")

  * Sep 27, 2017 10:55pm  Sep 27, 2017 10:55pm 

  * [ eatrader75](eatrader75)

  * | Joined Aug 2017  | Status: Trader | [28 Posts](/search?do=process&provider=Member&searchuser=605097)

I made the backtest now with "every tick based on real data", attached to EURCHF. I've got back the drawings. Just observed, there's an extra red line on top of the price. Only the V16 backtest works, the V17 and V18 don't.  
The results aren't so consistent as with "every tick" only.  
  
On forward demo I can run only 1 ea per MT4 at the same time. So I may need multiple MT's in different folders or you just code the option to change the magic number.  
  
Thanks  
Attila 

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: Screenshot1.png
Size: 88 KB](/attachment/image/2497746/thumbnail?d=1506518506)](/attachment/image/2497746?d=1506518506)   
[![Click to Enlarge

Name: Screenshot2.png
Size: 84 KB](/attachment/image/2497764/thumbnail?d=1506518759)](/attachment/image/2497764?d=1506518759)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#194](/thread/post/10335038#post10335038 "Post Permalink")

  * Edited 11:23pm  Sep 27, 2017 11:07pm | Edited 11:23pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar402047_21.gif) Fxentropy](fxentropy)

  * Joined Feb 2015 | Status: Who Dares Wins | [1,710 Posts](/search?do=process&provider=Member&searchuser=402047)

> [Quoting jvbJacques](/thread/post/10334514#post10334514 "View Quoted Post")
> 
> Disliked
> 
> @Fxentropy Yes that is normal. Days can go bye with no trade, but I found the past few days to contain a couple of hits. Just give it time. According to your chart there was no hit yet, but they did come close a couple of times. I am working on a new model to hopefully cater for more slippage and more profit in a shorter period of time. Also keep in mind that once the EA is stable then I will be adding all possible triangle as @eatrader75 already started to test ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1) That should speed up the number of arbitrage hits exponentially, but it is...
> 
> Ignored

  
ok, for the sake of testing....i added these pairs lol  
  
3 trades of 0.01 i had in the morning.... 

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: xKa8g.png
Size: 113 KB](/attachment/image/2497845/thumbnail?d=1506521246)](/attachment/image/2497845?d=1506521246)   
[![Click to Enlarge

Name: xKaaI.png
Size: 101 KB](/attachment/image/2497846/thumbnail?d=1506521272)](/attachment/image/2497846?d=1506521272)   

"What would you attempt to do, if you knew your success was a certainty?"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#195](/thread/post/10335754#post10335754 "Post Permalink")

  * Sep 28, 2017 1:41am  Sep 28, 2017 1:41am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar438576_2.gif) raffus](raffus)

  * | Joined Dec 2015  | Status: Member RFP | [57 Posts](/search?do=process&provider=Member&searchuser=438576)

> [Quoting jvbJacques](/thread/post/10333256#post10333256 "View Quoted Post")
> 
> Disliked
> 
> @aszain02 I live in South Africa. My ping to most brokers are about 600ms to 800ms. For me to test without a VPS close to each of those brokers is next to impossible. The VPS I did use is someone else's and I can not do with it what I like out of respect. I would love to test it.
> 
> Ignored

  
hello  
if you need to test something in my VPS, i also have same cent account with Justforex, FortFx and [XM](/brokers/xm "View XM Broker Profile").com  
  
  
we are here to support you  
Don't worry ask me if you need my help  
  
ciao 

Attached Image

![](/attachment/image/2498109?d=1506530428)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#196](/thread/post/10336115#post10336115 "Post Permalink")

  * Sep 28, 2017 3:37am  Sep 28, 2017 3:37am 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@eatrader75  
Strange that you can not run multiple EAs in your metatrader.  
I have no problem.  
  
But in any case.  
Do not run multiple copies of this EA on the same account, even if on different terminals.  
  
The EA uses a lot of margin and if 2 of these EAs opens positions at the same time then you are guaranteed a margin call and a failed trade.  
At the moment it uses almost 50% of the available margin so 2 EAs might work, but with just a tiny drawdown and you hit margin call.  
  
It need to be coded into the EA to handle this situation so that it does not open trades at the same time, but still use all triangles as faster entry points.  
  
  
@Fxentropy  
Read above message to eatrader75.  
  
This will not work.  
Well it might, but if it tries to open trades at the same time then it will crash seeing that it will hit margin call.  
I still need to build in the checks to prevent this situation, but this EA can only handle one triangle at a time.  
  
My focus at the moment is to decrease the slippage by decreasing the time it takes to open and close tickets.  
So far no reasonable solution.  
  
  
@raffus  
Thanks.  
I need all the help I can get and I have already some wonderful patrons that are lending me their VPS.  
Problem now is getting the time to do the actual development.  
Not cheap so I must lick boots to save up for free coding time ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
  
That server does look good, but I also have access to a 6ms server connection terminal, but even on that one the trade delay is upwards of 600ms.  
I need to solve this delay dilemma first before I can really make use of further vps tests.  
  
Thanks for my VPS providers seeing that I would not have found that problem without a vps.  
Now just to solve it.  
  
  
@dagoods  
I do not care for metatrader much.  
Especially after the delay problems.  
I know more than 25 different programming languages and learning more APIs unique to brokers like [oanda](/brokers/oanda "View OANDA Broker Profile") is no problem for me, especially if it can do better trade execution.  
I heard the same about JTrader on Dukascopy and the FIX api.  
Problem is getting a demo account to test on them.  
FIX normally require a live account.  
oanda last I checked also requires some sort of payment for using their API if you do not have a live account with them.  
  
Jtrader is free, but dukascopy only have got a 14 day demo account trial.  
Luckily Java is easy to program so I should be able to do it quickly .... well ... during my free time, which is limited.  
  
I does seem like the only option is to make use of the proprietary broker platform for speed.  
Metatrader seem to have fallen behind on development and is slow, even on a fast broker.  
  
Problem with metatrader is that even if you have a fast connection to the metatrader server it does not mean that metatrader have got a fast connection to the market.  
From what I heard is that what makes matters worse is that metatrader is a single threaded application, meaning it can only do one trade at a time and therefore if it becomes busy then it will slow to a crawl, relatively speaking. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#197](/thread/post/10336489#post10336489 "Post Permalink")

  * Sep 28, 2017 5:46am  Sep 28, 2017 5:46am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar402047_21.gif) Fxentropy](fxentropy)

  * Joined Feb 2015 | Status: Who Dares Wins | [1,710 Posts](/search?do=process&provider=Member&searchuser=402047)

Had first set of trades on GU GJ UJ 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: xKqaL.png
Size: 141 KB](/attachment/image/2498410/thumbnail?d=1506545177)](/attachment/image/2498410?d=1506545177)   

"What would you attempt to do, if you knew your success was a certainty?"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#198](/thread/post/10336518#post10336518 "Post Permalink")

  * Sep 28, 2017 6:01am  Sep 28, 2017 6:01am 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@Everyone  
Hang on.  
This slippage problem is killing this strategy.  
  
It can handle a couple of pips slip, but 5 or more pips will eat up the profit.  
  
I am working on an idea that just might kick the slip between the legs.  
Wait a bit for me to create and test it. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#199](/thread/post/10336628#post10336628 "Post Permalink")

  * Sep 28, 2017 6:54am  Sep 28, 2017 6:54am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar438576_2.gif) raffus](raffus)

  * | Joined Dec 2015  | Status: Member RFP | [57 Posts](/search?do=process&provider=Member&searchuser=438576)

watching the image of @Fxentropy and mine  
  
if the value of lot of USDJPY was the same of other 2 currencies, the trades will be closed with profit.  
  
Actually not  
  
i know u told me that is due just to balance/hedge the arbitrage but i see i many case .....this "issue" 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot1.png
Size: 148 KB](/attachment/image/2498482/thumbnail?d=1506549138)](/attachment/image/2498482?d=1506549138)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#200](/thread/post/10336641#post10336641 "Post Permalink")

  * Sep 28, 2017 7:00am  Sep 28, 2017 7:00am 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@raffus  
Not quite, but I am working on a theory where an unbalanced arbitrage where all lots are the same might help.  
Bigger draw down, but bigger profit and more trades.  
Still testing it.  
Requires quite a bit of changes.  
  
Hopefully will have something to test tomorrow.  
  
If it wasn't for slippage then the trades you saw would have been in profit.  
Metatrader is way too slow, a direct broker api will work better on this strategy, but I might have a solution that can work even with slippage.  
  
Look.  
Slippage is never good, but I might have a way to counter it. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Simple High Profit low Drawdown Triangular Arbitrage
  *   * [ **Reply to Thread** ](/thread/676132-simple-high-profit-low-drawdown-triangular-arbitrage/reply#reply)

  * More

[](https://www.forexfactory.com "Homepage")

  * [Forums](forums)
  * [Trades](trades)
  * [Calendar](calendar)
  * [News](news)
  * [Market](market)
  * [Brokers](brokers)

****

[](https://www.faireconomy.com/)

  * 

[Triangular Arbitrage](/thread/64423-triangular-arbitrage "Admin, Please Delete Thread.") 258 replies

[Triangular Arbitrage](/thread/62477-triangular-arbitrage "Is going  
long 1 lot of eur/usd + 
long 1 lot of usd/jpy = long 1 lot of eur/jpy ?  
\(is the ratio of the number of lots correct for a...") 16 replies

[Triangular Arbitrage and carry trade](/thread/71997-triangular-arbitrage-and-carry-trade "Is it possible for us retail traders to be able to make use of Tri Arb or carry trades?  
 
Any one know of retail brokers 
 
 
\(I'm...") 6 replies

[Triangular Arbitrage](/thread/367072-triangular-arbitrage "I've been reading about triangular arbing and was surprised to find that the cross of two majors doesn't always equal what the calculation...") 7 replies

[Question: Trade Mechanics of Triangular Arbitrage](/thread/225246-question-trade-mechanics-of-triangular-arbitrage "Before I even ask this question, please allow me to be very clear.... I have no intention of attempting a triangular arbitrage trade\(for...") 6 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/676132-simple-high-profit-low-drawdown-triangular-arbitrage/reply#reply)
  * Subscribe
  * [147](javascript:void\(0\);)

Attachments: Simple High Profit low Drawdown Triangular Arbitrage

Tags: Simple High Profit low Drawdown Triangular Arbitrage

#  [](/thread/676132-simple-high-profit-low-drawdown-triangular-arbitrage)Simple High Profit low Drawdown Triangular Arbitrage 

  * 

  * [#201](/thread/post/10337907#post10337907 "Post Permalink")

  * Sep 28, 2017 5:03pm  Sep 28, 2017 5:03pm 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@Everyone  
Try this one on for size.  
  
I got very busy the last time so I could not focus on this EA as I would like to, BUT I did manage to make some change.  
  
The attached EA does not look at the virtual ASK and BID lines anymore.  
Well it does for opening a trade, but not for closing it.  
  
Instead it monitors the account equity until it is in profit and then only closes it.  
  
I found that in a perfect world without massive slippage this EA will make a lot, but with slippage it is struggling to open at the correct place and close correctly too.  
So now I only look at the actual profit.  
  
This is still untested so be warned :0)  
  
O and you can back-test with this EA 19.  
I put a check into it for back-testing so that it disables the infinite loop. 

Attached File(s)

![File Type: ex5](https://assets.faireconomy.media/images/attach/ex5.gif) [2017-09-18 09h00 JVB Arbitrage Auto Profit19.ex5](/attachment/file/2499020?d=1506585806) 127 KB | 462 downloads 

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [2017-09-18 09h00 JVB Arbitrage Auto Profit19.ex4](/attachment/file/2499023?d=1506585807) 68 KB | 623 downloads 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#202](/thread/post/10338226#post10338226 "Post Permalink")

  * Sep 28, 2017 6:08pm  Sep 28, 2017 6:08pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar438576_2.gif) raffus](raffus)

  * | Joined Dec 2015  | Status: Member RFP | [57 Posts](/search?do=process&provider=Member&searchuser=438576)

> [Quoting jvbJacques](/thread/post/10336641#post10336641 "View Quoted Post")
> 
> Disliked
> 
> @raffus Not quite, but I am working on a theory where an unbalanced arbitrage where all lots are the same might help. Bigger draw down, but bigger profit and more trades. Still testing it. Requires quite a bit of changes. Hopefully will have something to test tomorrow. If it wasn't for slippage then the trades you saw would have been in profit. Metatrader is way too slow, a direct broker api will work better on this strategy, but I might have a solution that can work even with slippage. Look. Slippage is never good, but I might have a way to counter...
> 
> Ignored

My trades closed in loss due to swap commissions 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#203](/thread/post/10338301#post10338301 "Post Permalink")

  * Sep 28, 2017 6:25pm  Sep 28, 2017 6:25pm 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@raffus  
Unlikely.  
Look in the logs at the slippage for the open and close of those trades.  
  
The slippage is massive.  
Swap is so small that it does not even play a role.  
  
Also the EA does take into account commission.  
  
Problem is slippage on the open causes the trade to be opened at the wrong position, thereby throwing the calculations out that is only looking at the virtual ASK and BID lines, which contains no slippage.  
  
EA 19 I changed a few things in that it now checks for slippage after open and adapts the close calculations to that and also cater for some slippage during the close operation.  
Take into account that EA 19 was developed at 2am with a coffee induces frenzy so ..... untested ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
I also suspect the profit take on 19 is too high, but I need further testing. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#204](/thread/post/10338314#post10338314 "Post Permalink")

  * Sep 28, 2017 6:28pm  Sep 28, 2017 6:28pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar402047_21.gif) Fxentropy](fxentropy)

  * Joined Feb 2015 | Status: Who Dares Wins | [1,710 Posts](/search?do=process&provider=Member&searchuser=402047)

> [Quoting jvbJacques](/thread/post/10337907#post10337907 "View Quoted Post")
> 
> Disliked
> 
> @Everyone Try this one on for size. I got very busy the last time so I could not focus on this EA as I would like to, BUT I did manage to make some change. The attached EA does not look at the virtual ASK and BID lines anymore. Well it does for opening a trade, but not for closing it. Instead it monitors the account equity until it is in profit and then only closes it. I found that in a perfect world without massive slippage this EA will make a lot, but with slippage it is struggling to open at the correct place and close correctly too. So now I...
> 
> Ignored

It did the test, loaded and waiting now ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

Attached Image (click to enlarge)

[![Click to Enlarge

Name: xKQZ6.png
Size: 96 KB](/attachment/image/2499148/thumbnail?d=1506590921)](/attachment/image/2499148?d=1506590921)   

"What would you attempt to do, if you knew your success was a certainty?"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#205](/thread/post/10338335#post10338335 "Post Permalink")

  * Sep 28, 2017 6:33pm  Sep 28, 2017 6:33pm 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@Fxentropy  
I suggest closing and reopening the chart window before all those line strangle you ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
I blame my cat, because he likes lines.  
Otherwise maybe you like lines, in which case ... go for it ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
But you are talking about 20000 lines on screen, which might slow down a slow VPS, so less is better for speed.  
Check your task manager or TOP on linux to see if your CPU is taxed, but unlikely.  
  
I saw that the mt4 version creates some strange horizontal lines.  
I want to fix it, but time management suggest I rather focus on implementing the strategy in the EA rather than play around with strings ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
  
The mt5 version does not seem to have that problem. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#206](/thread/post/10338385#post10338385 "Post Permalink")

  * Sep 28, 2017 6:47pm  Sep 28, 2017 6:47pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar541172_2.gif) youngfxthug](youngfxthug)

  * | Joined Dec 2016  | Status: Trader | [7 Posts](/search?do=process&provider=Member&searchuser=541172)

thanks for MAs  
  
  
  
they look good for higher TFs 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#207](/thread/post/10338388#post10338388 "Post Permalink")

  * Sep 28, 2017 6:47pm  Sep 28, 2017 6:47pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar402047_21.gif) Fxentropy](fxentropy)

  * Joined Feb 2015 | Status: Who Dares Wins | [1,710 Posts](/search?do=process&provider=Member&searchuser=402047)

> [Quoting jvbJacques](/thread/post/10338335#post10338335 "View Quoted Post")
> 
> Disliked
> 
> @Fxentropy I suggest closing and reopening the chart window before all those line strangle you ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1) I blame my cat, because he likes lines. Otherwise maybe you like lines, in which case ... go for it ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1) But you are talking about 20000 lines on screen, which might slow down a slow VPS, so less is better for speed. Check your task manager or TOP on linux to see if your CPU is taxed, but unlikely. I saw that the mt4 version creates some strange horizontal lines. I want to fix it, but time management suggest I rather focus on implementing...
> 
> Ignored

Right, done 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: xKRrV.png
Size: 28 KB](/attachment/image/2499188/thumbnail?d=1506592068)](/attachment/image/2499188?d=1506592068)   

"What would you attempt to do, if you knew your success was a certainty?"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#208](/thread/post/10338437#post10338437 "Post Permalink")

  * Sep 28, 2017 7:06pm  Sep 28, 2017 7:06pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar440253_2.gif) badeel](badeel)

  * Joined Dec 2015 | Status: Trader | [257 Posts](/search?do=process&provider=Member&searchuser=440253)

we are very near to success excellent share going to use in live ECN account........  
thanks 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#209](/thread/post/10338473#post10338473 "Post Permalink")

  * Sep 28, 2017 7:17pm  Sep 28, 2017 7:17pm 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@badeel  
Wow ok.  
EA 19 is still untested.  
  
I would strongly suggest not to use on live account.  
  
I'm also working on some large changes to the EA, but it will take time.  
  
Just saying.  
Do not use on live.  
A lot of work still need to be done to negate the slippage problem.  
  
If you really want to throw money away then rather through it my way so I can pay for the development and spend more time on it.  
  
Really this EA is not live ready yet. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#210](/thread/post/10338539#post10338539 "Post Permalink")

  * Sep 28, 2017 7:39pm  Sep 28, 2017 7:39pm 

  * [ Forex-Loser](forex-loser)

  * | Joined Aug 2017  | Status: Trader | [6 Posts](/search?do=process&provider=Member&searchuser=605222)

If spread is a problem coucld your software work to get larger profit 20 or 200 pips? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#211](/thread/post/10338540#post10338540 "Post Permalink")

  * Edited 8:23pm  Sep 28, 2017 7:39pm | Edited 8:23pm 

  * [ mariushc](mariushc)

  * | Joined Sep 2017  | Status: Trader | [1 Post](/search?do=process&provider=Member&searchuser=615551)

Hi Jacques  
  
I've been trading / playing with strategies for over 2 years now and your idea seems very interesting ???  
  
Please send me some details regading you bot ???  
  
email me at { email address deleted by staff }  
we are neighbours i reside in jaohannesburg south africa. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#212](/thread/post/10338673#post10338673 "Post Permalink")

  * Sep 28, 2017 8:11pm  Sep 28, 2017 8:11pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar457690_1.gif) artico01](artico01)

  * Joined Apr 2016 | Status: Trader | [108 Posts](/search?do=process&provider=Member&searchuser=457690)

Hi, jvbJaque.  
  
I'm testing on demo, of course, the JVB Arbitrage Profit2 EA and Profit19.  
Profit2 trades directly with three lots depending on your equity or balance (I'm not sure).  
Profit19 draws lines on the GBP / USD chart, but does not trade. I do not know if it is looking for the right time to trade or is that it does not work on my platform.  
What is the difference between them?  
  
Thank you. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#213](/thread/post/10339084#post10339084 "Post Permalink")

  * Sep 28, 2017 9:57pm  Sep 28, 2017 9:57pm 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@Forex-Loser  
Spread is actually not a problem.  
Spread just determines how often an arbitrage opportunity it hit, but once hit then spread plays no role.  
  
So spread determines number of trades and therefore also the amount of profit.  
  
Increasing the profit take will not work seeing that arbitrage by its very nature does no deviate much from the ZERO line and therefore if you make the take profit too big then it will never hit it and never close the trades.  
  
But it need to be big enough to cover the unknown slippage amount and that is what I build into EA 19.  
EA 19 is just a rough test start and I will build on it to adapt to real world problems.  
  
  
  
@maruishc  
Hello neighbour ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
I must say I see your email address everywhere.  
I even tried to send to your address {email address deleted by staff}, but it keeps coming back in that it cannot find the staff email address.  
Must be lost at the post office ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
  
In any case. PM the address rather.  
  
But what do you want to know.  
  
It is not as if I am hiding anything about the EA.  
Post #1 contain most of the information and you are welcome to ask anything you do not know or wonder about.  
Like : Does it make coffe.  
... Yes, but you need a special driver for it.  
  
  
@artico01  
Not sure I understand the question, but let me try and answer.  
EA2 is VERY old and there has been a LOT of changes since then. Few thousand lines of code has gone through the EA and some of that new code have been discarded even in the later EAs.  
So only use the latest EA for it contains all the updates.  
  
EA 19 does trade, but is unstable.  
Look at the top White line and Bottom Red lines.  
They need to cross the opposite blue line before it opens any trades.  
It also takes 100 minutes from the start of the EA before it start too look for entry positions.  
  
The balance only comes into play once the EA tries to open a trade to determine the lot size.  
After that it normally ignored the equity and balance in the older EAs and only looked the lines crossing the middle for close signals, but EA19 now looks at the percentage profit based on equity and balance for a close signal.  
This was done because of slippage causing trades to be opened at the wrong positions and therefore closed at the wrong times.  
Hopefully EA 19 or a later version will counter this slippage problem. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#214](/thread/post/10339123#post10339123 "Post Permalink")

  * Sep 28, 2017 10:05pm  Sep 28, 2017 10:05pm 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@Everyone  
  
I love talking to everyone and try to answer everyone via forum, email, phone, whatsapp, pm,......  
But I am overwelmed sometimes with the amount of interest in this.  
  
![](https://resources.faireconomy.media/images/emojis/64/1f641.png?v=15.1) Just wish my indigogo campaign had that amount of interest to fund this project, then I could have finished this already and not have gone broke ![](https://resources.faireconomy.media/images/emojis/64/1f641.png?v=15.1)  
  
In any case.  
Do not stop talking and sending, you are not bothering me, but if I missed your message then please remind me later.  
I will not do it on purpose ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
Sometimes I miss stuff. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#215](/thread/post/10342471#post10342471 "Post Permalink")

  * Sep 29, 2017 6:39pm  Sep 29, 2017 6:39pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar457690_1.gif) artico01](artico01)

  * Joined Apr 2016 | Status: Trader | [108 Posts](/search?do=process&provider=Member&searchuser=457690)

EA in progress. [Spreads](/brokers/spreads "View Live Spreads on the Broker Guide"): UJ: 0.3 pips, GU: 0.2/0.3 pips. GJ: 0.9/1 pips. Time: 9:30 AM and 11:30 AM 

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: 09-27-17-9_30AM.jpg
Size: 259 KB](/attachment/image/2500526/thumbnail?d=1506677805)](/attachment/image/2500526?d=1506677805)   
[![Click to Enlarge

Name: 09-27-17-11_28AM.jpg
Size: 311 KB](/attachment/image/2500528/thumbnail?d=1506677806)](/attachment/image/2500528?d=1506677806)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#216](/thread/post/10343157#post10343157 "Post Permalink")

  * Sep 29, 2017 9:45pm  Sep 29, 2017 9:45pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar402047_21.gif) Fxentropy](fxentropy)

  * Joined Feb 2015 | Status: Who Dares Wins | [1,710 Posts](/search?do=process&provider=Member&searchuser=402047)

ehee 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: xLKDQ.png
Size: 11 KB](/attachment/image/2500809/thumbnail?d=1506689146)](/attachment/image/2500809?d=1506689146)   

"What would you attempt to do, if you knew your success was a certainty?"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#217](/thread/post/10343229#post10343229 "Post Permalink")

  * Sep 29, 2017 9:57pm  Sep 29, 2017 9:57pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar438576_2.gif) raffus](raffus)

  * | Joined Dec 2015  | Status: Member RFP | [57 Posts](/search?do=process&provider=Member&searchuser=438576)

> [Quoting artico01](/thread/post/10342471#post10342471 "View Quoted Post")
> 
> Disliked
> 
> EA in progress. Spreads: UJ: 0.3 pips, GU: 0.2/0.3 pips. GJ: 0.9/1 pips. Time: 9:30 AM and 11:30 AM {image} {image}
> 
> Ignored

Hello  
what broker are you using?  
It seems you have really good spreads  
  
Thanks 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#218](/thread/post/10343235#post10343235 "Post Permalink")

  * Sep 29, 2017 9:58pm  Sep 29, 2017 9:58pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar438576_2.gif) raffus](raffus)

  * | Joined Dec 2015  | Status: Member RFP | [57 Posts](/search?do=process&provider=Member&searchuser=438576)

> [Quoting Fxentropy](/thread/post/10343157#post10343157 "View Quoted Post")
> 
> Disliked
> 
> ehee {image}
> 
> Ignored

Nice goal 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#219](/thread/post/10343906#post10343906 "Post Permalink")

  * Sep 30, 2017 12:22am  Sep 30, 2017 12:22am 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@artico01  
That is fantastic spreads.  
  
What can I do to get an account like that ?  
  
I'm still working on the slippage problem.  
  
I found that slippage is extremely bad on MT4, but much better on MT5 so if you can use MT5 on that broker then I suggest rather use that.  
I think it might be the way MT4 handles multiple trades or something.  
  
But with an account like yours with those low spreads then I can increase the profit take a lot to cater for more slippage.  
Still. I'd rather find a way to decrease the time it takes to open trades.  
I also saw other low spread accounts with crazy high slippages/trade delays.  
Does not help if the profit target is $100 and the slippage is -$150.  
  
Also.  
EA version 18 and older does not cater for slippage.  
Rather use EA 19, which does extra calculations after opening a trade to counter some of the slippage.  
  
I would like to see your logs if possible so I can improve the system, even if it is the logs of EA 18.  
Just tell me what EA you are using.  
  
  
@Fxentropy  
That is very nice.  
Is that on MT4 or MT5 ?  
I'm still working on a massive update, but I ran out of time.  
I hope to have it done by Tuesday.  
  
Thanks to the "same lot bug" I actually discovered an interesting side-affect.  
Yes if all lots are the same then the profit/loss fluctuates a lot more than balanced and calculated lots sizes.  
BUT .... so far I have found that it still fluctuates around a ZERO point to some extend, just much more wildly and unstable than the balanced strategy.  
The good thing about this is that is generates a large amount of more hits and potentially much bigger profits, at the expense of a bigger drawdown.  
The drawdown can then be countered by decreased lot sizes and a small grid system.  
Still a lot of tests to go, but who knows. Might be on to something.  
  
  
@Everyone  
I am still working on the slippage problem, which is caused by slow execution of trades.  
More than 200ms per ticket some times, of which this strategy need to open 3 at a time, which causes massive slippage seeing that it takes up to 1.5 seconds to process 3 tickets at a time.  
  
This seem to affect MT4 far more than MT5.  
  
Maybe MT5 changes something, but even MT5 contains some slippage.  
  
Any suggestion on how to execute 3 trade at the same time extremely fast will be appreciated.  
  
I am looking into possible solutions, but so far I have not found a feasible pure metatrader solution yet and I started too look outside of metatrader, which unfortunately will exclude a lot of brokers that only supports metatrader.  
  
The only way so far I found was to open a way out pending order.  
Then modify that order once every 25 seconds to keep the trade server connection open, but that causes other problems such as overloading the trade server and angering the broker and getting your account blocked.  
  
Other options are to use multiple threads, but I found that that actually makes things a bit worse seeing that now instead of one thread having to wait for a sign on then now you have 3 or 4 threads, so no improvement there.  
  
This must be really bad for scalpers trading once every few minutes.  
If the solution is out there then I will find it.  
In the mean time there is wonderful JTrader and FIX and multiple other APIs.  
Problem is that then the EA need to be adapted to fit each broker's unique API.  
Not a problem, just takes time and I am working on a cross platform version of this EA to which you only add a small driver to connect it to your broker's API, but leave the base EA the same.  
This is still far off in coding time of which I can only afford after hours midnight free development time. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#220](/thread/post/10344060#post10344060 "Post Permalink")

  * Sep 30, 2017 12:54am  Sep 30, 2017 12:54am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar402047_21.gif) Fxentropy](fxentropy)

  * Joined Feb 2015 | Status: Who Dares Wins | [1,710 Posts](/search?do=process&provider=Member&searchuser=402047)

> [Quoting jvbJacques](/thread/post/10343906#post10343906 "View Quoted Post")
> 
> Disliked
> 
> @Fxentropy That is very nice. Is that on MT4 or MT5 ? I'm still working on a massive update, but I ran out of time. I hope to have it done by Tuesday. Thanks to the "same lot bug" I actually discovered an interesting side-affect. Yes if all lots are the same then the profit/loss fluctuates a lot more than balanced and calculated lots sizes. BUT .... so far I have found that it still fluctuates around a ZERO point to some extend, just much more wildly and unstable than the balanced strategy. The good thing about this is that is generates a large...
> 
> Ignored

  
Its MT4 Darwinex. Now running a second trade for today 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: xLRi5.png
Size: 14 KB](/attachment/image/2501085/thumbnail?d=1506700476)](/attachment/image/2501085?d=1506700476)   

"What would you attempt to do, if you knew your success was a certainty?"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Simple High Profit low Drawdown Triangular Arbitrage
  *   * [ **Reply to Thread** ](/thread/676132-simple-high-profit-low-drawdown-triangular-arbitrage/reply#reply)

  * More

[](https://www.forexfactory.com "Homepage")

  * [Forums](forums)
  * [Trades](trades)
  * [Calendar](calendar)
  * [News](news)
  * [Market](market)
  * [Brokers](brokers)

****

[](https://www.faireconomy.com/)

  * 

[Triangular Arbitrage](/thread/64423-triangular-arbitrage "Admin, Please Delete Thread.") 258 replies

[Triangular Arbitrage](/thread/62477-triangular-arbitrage "Is going  
long 1 lot of eur/usd + 
long 1 lot of usd/jpy = long 1 lot of eur/jpy ?  
\(is the ratio of the number of lots correct for a...") 16 replies

[Triangular Arbitrage and carry trade](/thread/71997-triangular-arbitrage-and-carry-trade "Is it possible for us retail traders to be able to make use of Tri Arb or carry trades?  
 
Any one know of retail brokers 
 
 
\(I'm...") 6 replies

[Triangular Arbitrage](/thread/367072-triangular-arbitrage "I've been reading about triangular arbing and was surprised to find that the cross of two majors doesn't always equal what the calculation...") 7 replies

[Question: Trade Mechanics of Triangular Arbitrage](/thread/225246-question-trade-mechanics-of-triangular-arbitrage "Before I even ask this question, please allow me to be very clear.... I have no intention of attempting a triangular arbitrage trade\(for...") 6 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/676132-simple-high-profit-low-drawdown-triangular-arbitrage/reply#reply)
  * Subscribe
  * [147](javascript:void\(0\);)

Attachments: Simple High Profit low Drawdown Triangular Arbitrage

Tags: Simple High Profit low Drawdown Triangular Arbitrage

#  [](/thread/676132-simple-high-profit-low-drawdown-triangular-arbitrage)Simple High Profit low Drawdown Triangular Arbitrage 

  * 

  * [#221](/thread/post/10344323#post10344323 "Post Permalink")

  * Sep 30, 2017 2:14am  Sep 30, 2017 2:14am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar457690_1.gif) artico01](artico01)

  * Joined Apr 2016 | Status: Trader | [108 Posts](/search?do=process&provider=Member&searchuser=457690)

@raffus @jvbJacques  
  
Broker: Solidary Markets NZ. Demo account. Leverage: 1:100 USD. Platform: MT4  
  
<https://solidarymarkets.com/accounts/trading_accounts>.  
  
Today's results with EA 19 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: 2017-09-29.png
Size: 67 KB](/attachment/image/2501173/thumbnail?d=1506705220)](/attachment/image/2501173?d=1506705220)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#222](/thread/post/10344486#post10344486 "Post Permalink")

  * Sep 30, 2017 3:31am  Sep 30, 2017 3:31am 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@artico01  
That looks very good.  
Once this EA can improve the slippage problem then you can make a killing with that broker.  
  
Which account is it ?  
Is it possible to send me the log of the EA ?  
I would like to analyse the results and maybe the slippages. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#223](/thread/post/10344511#post10344511 "Post Permalink")

  * Sep 30, 2017 3:55am  Sep 30, 2017 3:55am 

  * [ eatrader75](eatrader75)

  * | Joined Aug 2017  | Status: Trader | [28 Posts](/search?do=process&provider=Member&searchuser=605097)

Jacques,  
  
A possible way to speed up the order closing process by reversing the position, a thread by Nicholishen, here in FF. I guess you know it already, just thought to share it...  
<https://www.forexfactory.com/showthread.php?t=701784>

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#224](/thread/post/10344570#post10344570 "Post Permalink")

  * Sep 30, 2017 4:35am  Sep 30, 2017 4:35am 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@eatrader75  
Thanks, but it will not work for single trades or multiple symbols.  
  
It only allows you to close multiple tickets on the same symbol for the execution time cost of one reverse trade.  
  
In this case I open one ticket per symbol so closing one ticket in that way will not improve the speed unfortunately.  
But again thanks for the link.  
I'm still looking for something to speed things up and I will get there. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#225](/thread/post/10344652#post10344652 "Post Permalink")

  * Sep 30, 2017 5:38am  Sep 30, 2017 5:38am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar457690_1.gif) artico01](artico01)

  * Joined Apr 2016 | Status: Trader | [108 Posts](/search?do=process&provider=Member&searchuser=457690)

@jvbJacques  
  
I'm sorry but I lost the read-only password. I send the screens with the inputs and closures of the EA (only GBPJPY & GBPUSD. USDJPY no inputs)  
  
Maybe I can create another account to see how the EA19 works. That way I could give you read access.  
Amount: 10000 USD and leverage 1: 100? 

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: GBPJPY.png
Size: 52 KB](/attachment/image/2501310/thumbnail?d=1506717391)](/attachment/image/2501310?d=1506717391)   
[![Click to Enlarge

Name: GBPUSD.png
Size: 80 KB](/attachment/image/2501313/thumbnail?d=1506717392)](/attachment/image/2501313?d=1506717392)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#226](/thread/post/10344658#post10344658 "Post Permalink")

  * Sep 30, 2017 5:49am  Sep 30, 2017 5:49am 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@artico01  
I think there was a miscommunication.  
I do not need access to your account.  
  
I just wanted to see the logs of the EA.  
  
You can access the logs by clicking on the EXPERTS tab and it will display the logs.  
Then right click inside that tab on one of the log lines and select open.  
  
There you will find the log files of the expert sorted by date.  
  
If you want to you can send me that text file.  
It only contains the logs of the EA.  
  
I want to see what it did during the opening and closing of the trades.  
  
How fast is your connection to the metatrader server ?  
You can see that sometimes by clicking on the far right bottom part of metatrader.  
It will show you the server you are connected to and the speed in milliseconds between you and it. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#227](/thread/post/10344712#post10344712 "Post Permalink")

  * Sep 30, 2017 6:18am  Sep 30, 2017 6:18am 

  * [ Geges](geges)

  * | Joined Dec 2009  | Status: Trader | [139 Posts](/search?do=process&provider=Member&searchuser=127693)

Attached Image (click to enlarge)

[![Click to Enlarge

Name: FXChoice MetaTrader 5  triangular arbitrage 9-29-2017.png
Size: 141 KB](/attachment/image/2501346/thumbnail?d=1506719842)](/attachment/image/2501346?d=1506719842)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#228](/thread/post/10344715#post10344715 "Post Permalink")

  * Sep 30, 2017 6:23am  Sep 30, 2017 6:23am 

  * [ Geges](geges)

  * | Joined Dec 2009  | Status: Trader | [139 Posts](/search?do=process&provider=Member&searchuser=127693)

Hi Jacques,  
  
I must be getting old. Can't even submit a post correctly.lol.  
I tested this today and in the screen above it looked like the  
trade opened and closed in 1 second or less. Is that possible ?  
  
Also I'm testing in strategy tester right now. It's going slowly  
but looks really impressive. Thanks for trying this...I followed  
others in the past with similar ideas but end up failing long term.  
  
I put on my VPS for next week as well. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#229](/thread/post/10344737#post10344737 "Post Permalink")

  * Sep 30, 2017 6:43am  Sep 30, 2017 6:43am 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@Geges  
Yes it is possible to open and close so fast.  
  
If it wasn't for slippage then this strategy can easily work long term.  
You can see this in your strategy tester by just opening the 3 symbols and leaving to run for a couple of years.  
The profit/loss stays the same and forms a straight line, except for a minute amount of swap that almost does not register.  
  
Problem is it takes a long time (500ms to 2000ms) for metatrader 4 to open trades, even if your VPS have got a fast (5ms or better) connection to it's metatrader server.  
MT4 is old and I do not think it was intended for high frequency trading like this.  
  
MT5 seem to do better with trade execution speed, but still slow.  
  
As I get time I will start to test on other platforms like JTrader to see if it can deliver on what it promise of high speed trade execution.  
  
Did you attach the EA to your GBPUSD chart ?  
If so then look at that chart to see the lines the EA creates.  
Make the background of the chart black to see the lines better and zoom it out by dragging the right vertical price bar.  
  
While I am looking for a solution to high speed 3 trade execution I am working on a unbalanced triangular arbitrage to maybe increase profits and counter more of the slippage. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#230](/thread/post/10345498#post10345498 "Post Permalink")

  * Oct 1, 2017 2:29am  Oct 1, 2017 2:29am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar457690_1.gif) artico01](artico01)

  * Joined Apr 2016 | Status: Trader | [108 Posts](/search?do=process&provider=Member&searchuser=457690)

@jvbJacques  
I'm sorry for my error, but I am not a expert in metatrades forlder.  
It´s is my log file.  
  
Today with Market closed my conecction is 102 ms. Monday I will send the speed of my conecction  
If I open new account in this screen appear three servers with their respective pings  
  
Thanks 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Trading servers.png
Size: 69 KB](/attachment/image/2501738/thumbnail?d=1506792313)](/attachment/image/2501738?d=1506792313)   

Attached File(s)

![File Type: txt](https://assets.faireconomy.media/images/attach/txt.gif) [20170928.txt](/attachment/file/2501732?d=1506791632) 5 KB | 274 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#231](/thread/post/10348528#post10348528 "Post Permalink")

  * Oct 2, 2017 11:54pm  Oct 2, 2017 11:54pm 

  * [ eatrader75](eatrader75)

  * | Joined Aug 2017  | Status: Trader | [28 Posts](/search?do=process&provider=Member&searchuser=605097)

Jacques,  
  
Got some nice results today on Solidary Markets Demo 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot1.png
Size: 130 KB](/attachment/image/2502943/thumbnail?d=1506954938)](/attachment/image/2502943?d=1506954938)   

Attached File(s)

![File Type: txt](https://assets.faireconomy.media/images/attach/txt.gif) [Solidary Markets Demo.txt](/attachment/file/2502991?d=1506955948) 23 KB | 231 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#232](/thread/post/10348800#post10348800 "Post Permalink")

  * Oct 3, 2017 12:59am  Oct 3, 2017 12:59am 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@arico01 and @eatrader75  
Looks nice.  
Seems like you 2 have got different accounts seeing that the spread/commission on arico01 is way lower than eatrader75.  
  
What account types do you two have with Solitary Markets ? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#233](/thread/post/10348813#post10348813 "Post Permalink")

  * Oct 3, 2017 1:03am  Oct 3, 2017 1:03am 

  * [ eatrader75](eatrader75)

  * | Joined Aug 2017  | Status: Trader | [28 Posts](/search?do=process&provider=Member&searchuser=605097)

Got the same time on Global Prime another set of trades, but they're still in floating loss 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot1.png
Size: 120 KB](/attachment/image/2503107/thumbnail?d=1506960062)](/attachment/image/2503107?d=1506960062)   

Attached File(s)

![File Type: txt](https://assets.faireconomy.media/images/attach/txt.gif) [GP.txt](/attachment/file/2503111?d=1506960169) 8 KB | 216 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#234](/thread/post/10348860#post10348860 "Post Permalink")

  * Oct 3, 2017 1:16am  Oct 3, 2017 1:16am 

  * [ eatrader75](eatrader75)

  * | Joined Aug 2017  | Status: Trader | [28 Posts](/search?do=process&provider=Member&searchuser=605097)

> [Quoting jvbJacques](/thread/post/10348800#post10348800 "View Quoted Post")
> 
> Disliked
> 
> @arico01 and @eatrader75 Looks nice. Seems like you 2 have got different accounts seeing that the spread/commission on arico01 is way lower than eatrader75. What account types do you two have with Solitary Markets ?
> 
> Ignored

I guess I've chosen the "Elite" meanwhile artico01 the "Top" account. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#235](/thread/post/10348877#post10348877 "Post Permalink")

  * Edited 1:44am  Oct 3, 2017 1:26am | Edited 1:44am 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

As soon as I find a solution to the trade delay, which causes slippage then this will really be a killer.  
You are losing a lot of the profit just because of slippage.  
Easily more than 70% of the profit disappears to slippage.  
  
@Everyone  
I checked the logs of EATRADER75.  
Very good/(not so bad) slippage.  
500ms for all 3 trades.  
So it does look like slippage is very dependant on the broker and not always your connection.  
I had my hands on a 6ms broker connection on another broker and it had a 2000ms turn around time for 3 trades. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#236](/thread/post/10348959#post10348959 "Post Permalink")

  * Oct 3, 2017 1:52am  Oct 3, 2017 1:52am 

  * [ eatrader75](eatrader75)

  * | Joined Aug 2017  | Status: Trader | [28 Posts](/search?do=process&provider=Member&searchuser=605097)

Jacques,  
  
At the end of "My Own Broker Arbitrage" MetaCoder mentioned about his fast arbitrage EA. Maybe he found something useful or this is the same as your Fix Api idea.  
  

> [Quoting MetaCoder](/thread/post/10167395#post10167395 "View Quoted Post")
> 
> Disliked
> 
> Interesting thread, especially now that I developed my own fast broker arb EAs with two-way interprocess communication and NOT reliant on the OnTick function, which is far too slow for detecting and reacting to arb opportunities. Many say it can't be done successfully, and if somehow you are successful with it, the brokers will cripple your trading. Fair enough, noted.
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#237](/thread/post/10349065#post10349065 "Post Permalink")

  * Oct 3, 2017 2:31am  Oct 3, 2017 2:31am 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@eatrader75  
I also do not use OnTick.  
Too slow.  
I also know and have partially developed a 2 legged or latency arbitrage system, but problem with latency arbitrage is that brokers REALLY do not like it.  
It works, but they close your account or cancel your profits, stating that you are doing insider trading between a fast and slow broker, which it is not, but if you read the fine print then they can do what they want and you are out of luck.  
  
You can only make profit on the slow broker, but normally only the fast broker allows it so you are in trouble from the start.  
  
Plus it is also extremely reliant on no slippage seeing that the profit take is normally 1 pip to take advantage of the difference between the slow and fast broker.  
I have seen an EA like that actually working, until I did some investigation and found that the account it ran on had almost no spread and no commission, which was not available to anyone except the broker itself, which is very suspicious and without it the EA did not work seeing that the spread alone killed it.  
  
The advantage is that there normally is only one trade instead of 3 like the triangle and therefore 3 times faster, unless I can implement my mutli-threaded ea.  
  
The disadvantage is that ANY slippage and you lose all the profit seeing that 1 pip profit is killed by anything close to 1 pip slippage, which can happen on the open and close side.  
  
Also.  
If the broker locks your account or for some reason your EA does not catch the trade signal in time, then it will run far into negative, unlike the triangle that does not mind.  
  
BUT.  
I would love to be proved wrong and be pointed to a broker that will allow this for I have tried it and it looks good, but without a good VPS and good spread/commission it does not work from what I have seen. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#238](/thread/post/10349336#post10349336 "Post Permalink")

  * Oct 3, 2017 4:18am  Oct 3, 2017 4:18am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar457690_1.gif) artico01](artico01)

  * Joined Apr 2016 | Status: Trader | [108 Posts](/search?do=process&provider=Member&searchuser=457690)

@jvbJacques  
  
I opened demo account in November 2016. The SMFX conditions may have changed. Now it charges a commission of 2.9 per lot. [Spreads](/brokers/spreads "View Live Spreads on the Broker Guide") very low.  
  
<https://solidarymarkets.com/>

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#239](/thread/post/10349417#post10349417 "Post Permalink")

  * Edited 5:07am  Oct 3, 2017 4:48am | Edited 5:07am 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@artico01  
I have checked out the SMFX standard account and it looks fantastic.  
The spread/commission on the standard account is the lowest I have seen anywhere with multiple arbitrage crosses an hour.  
  
How trustworthy is this broker ?  
Have you done any trading with it and do they pay out profits, beyond what you deposit ? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#240](/thread/post/10349629#post10349629 "Post Permalink")

  * Oct 3, 2017 6:21am  Oct 3, 2017 6:21am 

  * [ eatrader75](eatrader75)

  * | Joined Aug 2017  | Status: Trader | [28 Posts](/search?do=process&provider=Member&searchuser=605097)

Jacques,  
  
To correct the slippage, we could add to the lots for scaling up or averaging down. But we need to reduce the original lots to have enough room for correction 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Simple High Profit low Drawdown Triangular Arbitrage
  *   * [ **Reply to Thread** ](/thread/676132-simple-high-profit-low-drawdown-triangular-arbitrage/reply#reply)

  * More

[](https://www.forexfactory.com "Homepage")

  * [Forums](forums)
  * [Trades](trades)
  * [Calendar](calendar)
  * [News](news)
  * [Market](market)
  * [Brokers](brokers)

****

[](https://www.faireconomy.com/)

  * 

[Triangular Arbitrage](/thread/64423-triangular-arbitrage "Admin, Please Delete Thread.") 258 replies

[Triangular Arbitrage](/thread/62477-triangular-arbitrage "Is going  
long 1 lot of eur/usd + 
long 1 lot of usd/jpy = long 1 lot of eur/jpy ?  
\(is the ratio of the number of lots correct for a...") 16 replies

[Triangular Arbitrage and carry trade](/thread/71997-triangular-arbitrage-and-carry-trade "Is it possible for us retail traders to be able to make use of Tri Arb or carry trades?  
 
Any one know of retail brokers 
 
 
\(I'm...") 6 replies

[Triangular Arbitrage](/thread/367072-triangular-arbitrage "I've been reading about triangular arbing and was surprised to find that the cross of two majors doesn't always equal what the calculation...") 7 replies

[Question: Trade Mechanics of Triangular Arbitrage](/thread/225246-question-trade-mechanics-of-triangular-arbitrage "Before I even ask this question, please allow me to be very clear.... I have no intention of attempting a triangular arbitrage trade\(for...") 6 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/676132-simple-high-profit-low-drawdown-triangular-arbitrage/reply#reply)
  * Subscribe
  * [147](javascript:void\(0\);)

Attachments: Simple High Profit low Drawdown Triangular Arbitrage

Tags: Simple High Profit low Drawdown Triangular Arbitrage

#  [](/thread/676132-simple-high-profit-low-drawdown-triangular-arbitrage)Simple High Profit low Drawdown Triangular Arbitrage 

  * 

  * [#241](/thread/post/10349651#post10349651 "Post Permalink")

  * Oct 3, 2017 6:31am  Oct 3, 2017 6:31am 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@eatrader75  
Not sure if it will work, because after you determined that the 3 trades you just opened opened at the wrong positions because of slippage you will then be at a even more unfavourable position to correct it using scaling.  
  
What I did in 19 is to ignore the fixed closed position, because that is based on a perfect no slippage calculation and rather just look at the profit take.  
What I still need to test one day is to keep more detailed price history and then recalculate all the virtual ASK, BID, average and close lines as they are drawn on the chart.  
Then use these new lines as the close position.  
EA 19 might get a big slip and buy at the extreme high position, meaning it might never return into profit so recalculating the virtual lines will add the functionality of a virtual stop loss to prevent extremely incorrectly places trades.  
Not an easy feat to insert into coding ... Well easy enough, but a LOT of coding so will take a long time.  
  
In the mean time I am playing with other ideas that might alleviate the problem, including unbalancing the triangle a bit to increase the profit and draw-down, but in the process make the profit big enough to counter slippage and also at the same time increase the number of arbitrage hits to counter the lower lot sizes.  
  
BUT again.  
This will take a long time and I am now at a point in my business where I can not stand off so much time to this EA anymore so development is going to slow down a lot, but it will not stop.  
Just be patient. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#242](/thread/post/10349833#post10349833 "Post Permalink")

  * Oct 3, 2017 8:06am  Oct 3, 2017 8:06am 

  * [ dev800](dev800)

  * | Joined Oct 2017  | Status: Trader | [1 Post](/search?do=process&provider=Member&searchuser=615998)

Interesting articles about the topic and slippage issue:  
  
<http://www.onestepremoved.com/triangular-arbitrage/>  
[https://www.mql5.com/en/docs/constan...rade_execution](https://www.mql5.com/en/docs/constants/environment_state/marketinfoconstants#enum_symbol_trade_execution)  
[https://sites.google.com/site/market...-arbitrage-101](https://sites.google.com/site/marketformula/articles/triangular-arbitrage-101)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#243](/thread/post/10349883#post10349883 "Post Permalink")

  * Oct 3, 2017 8:43am  Oct 3, 2017 8:43am 

  * [ cphcphcph](cphcphcph)

  * | Joined Oct 2009  | Status: Trader | [129 Posts](/search?do=process&provider=Member&searchuser=120768)

Hi Jac,  
Sharing out the EA log for your reference.  
May I know the meaning of timedlog here?   
Thank you 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot_2017-10-03-07-38-05-592_com.microsoft.rdc.android.png
Size: 539 KB](/attachment/image/2503530/thumbnail?d=1506987689)](/attachment/image/2503530?d=1506987689)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#244](/thread/post/10350905#post10350905 "Post Permalink")

  * Oct 3, 2017 6:00pm  Oct 3, 2017 6:00pm 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@dev800  
Thanks for the articles.  
I have read them before and agree with most what they say there.  
  
One good thing is that unlike latency arbitrage, most brokers do not have a problem with triangular arbitrage, because it does not affect them like with latency arbitrage, but it does affect delays between countries, which they do not care about.  
  
I do see that they also ran into the trade execution delay.  
I already made a connection to 4 trading platforms to try and decrease the delay a bit or at most by 3 times, but I keep coming back to the idea thaht if you really want speed then the only option is to use the broker's own API like Jtrader or FIX or whatever they offer.  
  
It will make the EA less transportable between broker, but who cares if you are making money, plus from what I heard is that Dukascopy and LMAX are some of the most trustworthy brokers out there and also have some of the best and fastest API out there so best of both worlds.... That is when I get time to implement it.  
  
  
@cphcphcph  
Timelog was just a log to see if there is any time delay between large calculation parts of the EA's coding, which there was not.  
So just a useless log. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#245](/thread/post/10350988#post10350988 "Post Permalink")

  * Oct 3, 2017 6:15pm  Oct 3, 2017 6:15pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar402047_21.gif) Fxentropy](fxentropy)

  * Joined Feb 2015 | Status: Who Dares Wins | [1,710 Posts](/search?do=process&provider=Member&searchuser=402047)

Updating , today got 2 trades  
  
Jacques, can you edit this 19 version to be able to set the percentage of account to be used? Right now its using the full capacity of equity  
  
thanks 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: xOTsx.png
Size: 28 KB](/attachment/image/2503951/thumbnail?d=1507022139)](/attachment/image/2503951?d=1507022139)   

"What would you attempt to do, if you knew your success was a certainty?"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#246](/thread/post/10351071#post10351071 "Post Permalink")

  * Oct 3, 2017 6:34pm  Oct 3, 2017 6:34pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar268213_5.gif) kaczucha11](kaczucha11)

  * | Joined Jul 2012  | Status: Trader | [99 Posts](/search?do=process&provider=Member&searchuser=268213)

> [Quoting Fxentropy](/thread/post/10350988#post10350988 "View Quoted Post")
> 
> Disliked
> 
> Updating , today got 2 trades Jacques, can you edit this 19 version to be able to set the percentage of account to be used? Right now its using the full capacity of equity thanks {image}
> 
> Ignored

That's very good point. I had margin call on Sunday when market open. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#247](/thread/post/10351091#post10351091 "Post Permalink")

  * Oct 3, 2017 6:40pm  Oct 3, 2017 6:40pm 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@Everyone  
This EA does use the whole account, but only about 10% drawdown at most.  
  
It does use up 80% of your margin so do not run anything else on you account with this EA or else you will get a margin call.  
  
I can see that something traded a 3.36lot trade while the EA was trading on @Fxentropy and that will cause a margin call seeing that there is not much margin left.  
  
I will make a parameter available in the next EA that will limit the amount of your account the EA must leave alone. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#248](/thread/post/10351113#post10351113 "Post Permalink")

  * Oct 3, 2017 6:42pm  Oct 3, 2017 6:42pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar402047_21.gif) Fxentropy](fxentropy)

  * Joined Feb 2015 | Status: Who Dares Wins | [1,710 Posts](/search?do=process&provider=Member&searchuser=402047)

> [Quoting jvbJacques](/thread/post/10351091#post10351091 "View Quoted Post")
> 
> Disliked
> 
> @Everyone This EA does use the whole account, but only about 10% drawdown at most. It does use up 80% of your margin so do not run anything else on you account with this EA or else you will get a margin call. I can see that something traded a 3.36lot trade while the EA was trading on @Fxentropy and that will cause a margin call seeing that there is not much margin left. I will make a parameter available in the next EA that will limit the amount of your account the EA must leave alone.
> 
> Ignored

  
That trade of 3.36lot ....i forgot an EA that take partial profit ON  
  
"I will make a parameter available in the next EA that will limit the amount of your account the EA must leave alone" =>**OK, thanks!!**

"What would you attempt to do, if you knew your success was a certainty?"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#249](/thread/post/10351137#post10351137 "Post Permalink")

  * Oct 3, 2017 6:48pm  Oct 3, 2017 6:48pm 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@Fxentropy  
I already have a parameter like that build in, but not by percentage, but telling the system to leave an amount alone to test on bigger accounts without using everything.  
  
You can see it in the logs called AccountDecrease, which I will make available.  
  
The EA is just pulled apart at the moment and I do not have time now to put it back together without removing the new updates and therefore I must push through until the new updates are done and then activate it.  
  
Might take a few days. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#250](/thread/post/10351161#post10351161 "Post Permalink")

  * Oct 3, 2017 6:53pm  Oct 3, 2017 6:53pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar402047_21.gif) Fxentropy](fxentropy)

  * Joined Feb 2015 | Status: Who Dares Wins | [1,710 Posts](/search?do=process&provider=Member&searchuser=402047)

> [Quoting jvbJacques](/thread/post/10351137#post10351137 "View Quoted Post")
> 
> Disliked
> 
> @Fxentropy I already have a parameter like that build in, but not by percentage, but telling the system to leave an amount alone to test on bigger accounts without using everything. You can see it in the logs called AccountDecrease, which I will make available. The EA is just pulled apart at the moment and I do not have time now to put it back together without removing the new updates and therefore I must push through until the new updates are done and then activate it. Might take a few days.
> 
> Ignored

take your time mate.  
  
no rush 

Attached Image

![](/attachment/image/2504047?d=1507024468)

"What would you attempt to do, if you knew your success was a certainty?"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#251](/thread/post/10351174#post10351174 "Post Permalink")

  * Oct 3, 2017 6:56pm  Oct 3, 2017 6:56pm 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@Fxentropy  
That is not right and down right illegal !!!!!  
  
Are you hacking my computer ?????  
  
Where did you get a picture of me ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#252](/thread/post/10351318#post10351318 "Post Permalink")

  * Oct 3, 2017 7:45pm  Oct 3, 2017 7:45pm 

  * [ cphcphcph](cphcphcph)

  * | Joined Oct 2009  | Status: Trader | [129 Posts](/search?do=process&provider=Member&searchuser=120768)

Dear Jac,  
  
Thank you for your response.  
  
One more question, I found some error in the EA log as attached. Appreciate your help again..thanks! 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot_2017-10-03-18-43-06-816_com.microsoft.rdc.android.png
Size: 663 KB](/attachment/image/2504110/thumbnail?d=1507027490)](/attachment/image/2504110?d=1507027490)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#253](/thread/post/10351382#post10351382 "Post Permalink")

  * Oct 3, 2017 8:04pm  Oct 3, 2017 8:04pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar64206_3.gif) ChicagoRob](chicagorob)

  * | Joined Mar 2008  | Status: Trader | [901 Posts](/search?do=process&provider=Member&searchuser=64206)

> [Quoting Fxentropy](/thread/post/10350988#post10350988 "View Quoted Post")
> 
> Disliked
> 
> Updating , today got 2 trades Jacques, can you edit this 19 version to be able to set the percentage of account to be used? Right now its using the full capacity of equity thanks {image}
> 
> Ignored

45 lots, eh? Go big or go home. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#254](/thread/post/10351441#post10351441 "Post Permalink")

  * Oct 3, 2017 8:26pm  Oct 3, 2017 8:26pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar402047_21.gif) Fxentropy](fxentropy)

  * Joined Feb 2015 | Status: Who Dares Wins | [1,710 Posts](/search?do=process&provider=Member&searchuser=402047)

> [Quoting ChicagoRob](/thread/post/10351382#post10351382 "View Quoted Post")
> 
> Disliked
> 
> {quote} 45 lots, eh? Go big or go home.
> 
> Ignored

Couldnt set the risk hence the big lots..but yes....go big or go home is what i like it. 

Attached Image

![](/attachment/image/2504192?d=1507030049)

"What would you attempt to do, if you knew your success was a certainty?"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#255](/thread/post/10351651#post10351651 "Post Permalink")

  * Oct 3, 2017 9:23pm  Oct 3, 2017 9:23pm 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@cphcphcph  
Your ea trading does not seem to be active in your metatrader options.  
Click.  
Tools--options--Expert Adviser and check attached pic.  
  
  
@Fxentropy  
If you make profit then your EA should stop pretty soon.  
It only trades till 50 lots at the moment. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot from 2017-10-03 14-20-44.png
Size: 122 KB](/attachment/image/2504307/thumbnail?d=1507033377)](/attachment/image/2504307?d=1507033377)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#256](/thread/post/10351708#post10351708 "Post Permalink")

  * Oct 3, 2017 9:35pm  Oct 3, 2017 9:35pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar402047_21.gif) Fxentropy](fxentropy)

  * Joined Feb 2015 | Status: Who Dares Wins | [1,710 Posts](/search?do=process&provider=Member&searchuser=402047)

> [Quoting jvbJacques](/thread/post/10351651#post10351651 "View Quoted Post")
> 
> Disliked
> 
> @cphcphcph Your ea trading does not seem to be active in your metatrader options. Click. Tools--options--Expert Adviser and check attached pic. @Fxentropy If you make profit then your EA should stop pretty soon. It only trades till 50 lots at the moment. {image}
> 
> Ignored

oh, ok, then will start a demo with less capital......thx  
  
or...i'll just wait your new version 

"What would you attempt to do, if you knew your success was a certainty?"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#257](/thread/post/10351736#post10351736 "Post Permalink")

  * Oct 3, 2017 9:43pm  Oct 3, 2017 9:43pm 

  * [ cphcphcph](cphcphcph)

  * | Joined Oct 2009  | Status: Trader | [129 Posts](/search?do=process&provider=Member&searchuser=120768)

> [Quoting jvbJacques](/thread/post/10351651#post10351651 "View Quoted Post")
> 
> Disliked
> 
> @cphcphcph Your ea trading does not seem to be active in your metatrader options. Click. Tools--options--Expert Adviser and check attached pic. {image}
> 
> Ignored

Hi Jac,  
  
Thank you for your response.  
  
How about the EA log as attached? Do you think it is working now?  
  
Thank you? 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: comment.JPG
Size: 225 KB](/attachment/image/2504324/thumbnail?d=1507034390)](/attachment/image/2504324?d=1507034390)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#258](/thread/post/10351750#post10351750 "Post Permalink")

  * Oct 3, 2017 9:46pm  Oct 3, 2017 9:46pm 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@Fxentropy  
You could be waiting a long time ![](https://resources.faireconomy.media/images/emojis/64/1f641.png?v=15.1)  
  
  
@cphcphcph  
All looks fine now.  
Next time right click on that log and select OPEN.  
Then attach that file to the forum.  
The image does not contain everything of the log. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#259](/thread/post/10352606#post10352606 "Post Permalink")

  * Oct 4, 2017 12:36am  Oct 4, 2017 12:36am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar457690_1.gif) artico01](artico01)

  * Joined Apr 2016 | Status: Trader | [108 Posts](/search?do=process&provider=Member&searchuser=457690)

@jvbJacques  
  
I do not know. I've only used it in demo account to test strategies.  
I searched for comments about the broker on the net but I did not find much. On the other hand the information is internet can be manipulated.  
The only option. Once adjusted the EA to try with money you do not fear losing. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#260](/thread/post/10353315#post10353315 "Post Permalink")

  * Oct 4, 2017 3:46am  Oct 4, 2017 3:46am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar53444_2.gif) dagoods](dagoods)

  * Joined Nov 2007 | Status: Trader | [3,059 Posts](/search?do=process&provider=Member&searchuser=53444)

[https://www.forexfactory.com/showthr...22#post9898722](https://www.forexfactory.com/showthread.php?p=9898722#post9898722)  
  
"Any hve looke this EA please Upload  
EURUSD USDJPY EURJPY  
Buy buy Sell  
After 10 pip open new inverse ordr  
Sell sell buy"  
  
  
  
solution? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Simple High Profit low Drawdown Triangular Arbitrage
  *   * [ **Reply to Thread** ](/thread/676132-simple-high-profit-low-drawdown-triangular-arbitrage/reply#reply)

  * More

[](https://www.forexfactory.com "Homepage")

  * [Forums](forums)
  * [Trades](trades)
  * [Calendar](calendar)
  * [News](news)
  * [Market](market)
  * [Brokers](brokers)

****

[](https://www.faireconomy.com/)

  * 

[Triangular Arbitrage](/thread/64423-triangular-arbitrage "Admin, Please Delete Thread.") 258 replies

[Triangular Arbitrage](/thread/62477-triangular-arbitrage "Is going  
long 1 lot of eur/usd + 
long 1 lot of usd/jpy = long 1 lot of eur/jpy ?  
\(is the ratio of the number of lots correct for a...") 16 replies

[Triangular Arbitrage and carry trade](/thread/71997-triangular-arbitrage-and-carry-trade "Is it possible for us retail traders to be able to make use of Tri Arb or carry trades?  
 
Any one know of retail brokers 
 
 
\(I'm...") 6 replies

[Triangular Arbitrage](/thread/367072-triangular-arbitrage "I've been reading about triangular arbing and was surprised to find that the cross of two majors doesn't always equal what the calculation...") 7 replies

[Question: Trade Mechanics of Triangular Arbitrage](/thread/225246-question-trade-mechanics-of-triangular-arbitrage "Before I even ask this question, please allow me to be very clear.... I have no intention of attempting a triangular arbitrage trade\(for...") 6 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/676132-simple-high-profit-low-drawdown-triangular-arbitrage/reply#reply)
  * Subscribe
  * [147](javascript:void\(0\);)

Attachments: Simple High Profit low Drawdown Triangular Arbitrage

Tags: Simple High Profit low Drawdown Triangular Arbitrage

#  [](/thread/676132-simple-high-profit-low-drawdown-triangular-arbitrage)Simple High Profit low Drawdown Triangular Arbitrage 

  * 

  * [#261](/thread/post/10353851#post10353851 "Post Permalink")

  * Oct 4, 2017 8:36am  Oct 4, 2017 8:36am 

  * [ cphcphcph](cphcphcph)

  * | Joined Oct 2009  | Status: Trader | [129 Posts](/search?do=process&provider=Member&searchuser=120768)

@jac  
  
The EA seems not working on my ECN broker.  
  
Attached herewith the log again.  
  
Thanks 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot_2017-10-04-07-30-38-294_com.microsoft.rdc.android.png
Size: 521 KB](/attachment/image/2505042/thumbnail?d=1507074001)](/attachment/image/2505042?d=1507074001)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#262](/thread/post/10354327#post10354327 "Post Permalink")

  * Oct 4, 2017 3:14pm  Oct 4, 2017 3:14pm 

  * [ quin2k](quin2k)

  * | Joined Jun 2008  | Status: Trader | [12 Posts](/search?do=process&provider=Member&searchuser=72631)

@jac  
  
Thank you for your interesting work.  
  

Do I have to install the EA on each of the three pairs or is having it on just one chart/pair sufficient?  
  
Many thanks. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#263](/thread/post/10354751#post10354751 "Post Permalink")

  * Oct 4, 2017 5:27pm  Oct 4, 2017 5:27pm 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@cphcphcph  
That is a screen print of the log.  
Please attach the log files itself, because the screen print excludes parts of the error message so I can not see what or where it went wrong.  
  
I suspect either your broker does not allow trades on GBPJPY or you did not show all 3 the symbols on market watch on the left side.  
  
  
@Jac  
I suggest loading it on the GBPUSD chart with a timeframe of 1 minute to see the chart it draws.  
It will work on other charts, but you will not see the lines it draws.  
  
Only load on one chart and make sure all 3 symbols are displayed in your market watch.  
  
  
Keep in mind EA 19 is very unstable still seeing that I am experimenting in ways to remove some of the slippage because of slow trades.  
  
Also MT5 is much faster than MT4 in trade execution. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#264](/thread/post/10354831#post10354831 "Post Permalink")

  * Oct 4, 2017 5:56pm  Oct 4, 2017 5:56pm 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@EVERYONE  
The reason I am so slow in development is because this project will take me about 3 months.  
I maybe have about a month left in full development time.  
  
Problem is I can only do this during my free time and I have to do 5 jobs just to support my monthly payments, which leaves me with about an hour or so worth of free time only some days.  
Therefore splitting a month of development into chunks of 1 hour increments make it extremely slow so just be patient.  
  
The EA is already about 1700 lines of code and beyond that I already discarded and coded 30 times that to test different things.  
It is getting there.  
  
If you really want to support the development, just not financially then you can find out if you can get me vendor numbers at any and all mining industries in South Africa or globally.  
I need a vendor number to get paid for work I do on mines here in South Africa, otherwise I work for nothing or the companies that lend me their vendor number takes most of the profit.  
  
My speciality is safety, security and hardware/software automation.  
More specifically I specialise in mining lamp rooms and all hardware tracking and linking and human/hardware traffic control.  
  
Most mining industries in South Africa and in other countries already run my lamp room systems, but through other companies that have got a vendor number and sell the system as their own.  
  
I do not need funds.  
I just need vendor numbers or interested contacts at any mine across the globe seeing that there is a good chance they are already running my system without them knowing it.  
A vendor number is nothing more than a VIP list of companies allowed to do business with mines and is there to prevent competition by smaller competitors and a way for bigger companies to make money by loaning their vendor number out without them actually having to do anything.  
  
All I want is a vendor number to get paid for what I already do and at the same time give massive discounts to the mines that then do not need to pay a loaded price to the current vendor company for work I do in any case through them.  
  
Keep in mind my system can run globally on any mine and can be made to link into and control any type of hardware or other software devices with full after sales support.  
PM me with any information.  
A vendor number is free and only allows me to tender for work and get paid if they want the system or nothing if they don't.  
  
I can even give live running examples in some of the biggest mines in the world like Mponeng, Moab Kotsong, multiple Beatrix, Kloof, platinum, Modikwa, and many more.....  
The system have proven itself time and again for decades.  
  
There is the old saying that it is not what you know, but who you know.  
And when it comes to vendor numbers it is so true.  
Problem is I know what and how to do the work, but I do not know the who.  
The question the mine need to ask is do they want the company that are good sales people or the one that actually produces results, especially when it comes to safety and security of their personnel and indirectly their bottom line. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#265](/thread/post/10354875#post10354875 "Post Permalink")

  * Oct 4, 2017 6:11pm  Oct 4, 2017 6:11pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar339236_1.gif) paul72](paul72)

  * | Joined Jun 2013  | Status: Trader | [138 Posts](/search?do=process&provider=Member&searchuser=339236)

hi there jacques.  
  
turn this EA into a job.  
  
go commercial and guys shall pay for production of this EA.? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#266](/thread/post/10354883#post10354883 "Post Permalink")

  * Oct 4, 2017 6:14pm  Oct 4, 2017 6:14pm 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@paul72  
I tried that with an indigogo campaign and nothing.  
I'm not a good sales person you see ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
  
Would love to make this kind of programming a job, if I can find a way of getting paid for it.  
  
My dream is still to finish this and once profitable to make it available for free.  
Once profitable I see no reason to make it free seeing that then I can also profit.  
  
My problem is that I skilled myself up to the extreme in programming to the point where I can basically program in anything.  
25 distinct and some obscure programming languages, but no sales training.  
Doing the job does not mean you get paid for the job.  
  
Do you think Bill Gates or Steve Jobs can program or develop all those cool stuff or do they call on their team of developers to do the job for them ?!  
That does not make them bad people, just good salesmen that know what they are talking about and are the face of the company because of that reason.  
Watch "pirates of silicon valley". I have got a lot of respect for Mr Gates, even though I do not like or use windows ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#267](/thread/post/10354918#post10354918 "Post Permalink")

  * Oct 4, 2017 6:30pm  Oct 4, 2017 6:30pm 

  * [ eatrader75](eatrader75)

  * | Joined Aug 2017  | Status: Trader | [28 Posts](/search?do=process&provider=Member&searchuser=605097)

Jacques,  
  
I opened the Standard Demo account with SMFX, looks good for now... 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot1.png
Size: 135 KB](/attachment/image/2505496/thumbnail?d=1507108892)](/attachment/image/2505496?d=1507108892)   

Attached File(s)

![File Type: txt](https://assets.faireconomy.media/images/attach/txt.gif) [SMFX Standard.txt](/attachment/file/2505522?d=1507109391) 10 KB | 286 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#268](/thread/post/10354973#post10354973 "Post Permalink")

  * Oct 4, 2017 6:48pm  Oct 4, 2017 6:48pm 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@eatrader75  
Those lines does look very good.  
  
Problem is slippage.  
I also opened an account, but I am seeing trade delays of up to 4000ms on some trades, which is crazy slow and causes massive slippage of up to 30 pips in that one trade.  
  
Might be a problem with my connection to them, although it is saying I have a 75ms connection to them.  
  
MyFxchoice is also a strange case.  
They seem to have better delays of about 500ms for 3 trades, but it is quite stable on MT4, still too slow.  
For some reason their MT5 connection have got a 100ms delay for 3 trades some times, which is very good and therefore makes a lot of profit, even though their spread/commission does not even come close to SMFX.  
My mfxchoice connection is about 15ms to their server.  
  
So it really looks like a broker specific problem, which is confusing seeing that it means you can not know if the broker can execute trades fast just by having a fast connection to them.  
  
  
I have written a partial latency arbitrage EA in the past that make latency trades on a slow broker by looking at the fast broker.  
Works good if the slow broker can execute trades fast ..... normally not.  
The point is that most of the time the fast broker it either LMAX or Dukascopy.  
  
I really want to try LMAX and Dukascopy to see if they have got the best connection and execution speeds, which is the most important part of most arbitrage systems.  
  
I am still testing a new unbalanced system, which might bypass the slippage problem, but still even profit after slippage means that the slippage ate a big chunk of your profit.  
  
Will update here if I found something.  
  
In any case.  
Let me know if your trades are faster on SMFX than mine.  
Easy to check.  
Check the log line just before the first trade is opened/closed then check the log line just after the last of the 3 trades are opened/closed.  
The last 3 numbers in the time field to the left of the log indicates the milliseconds so just subtract the first time from the last to get the amount of milliseconds\seconds it took.  
1000 milliseconds = 1 second  
  
  
  
@eatrader75  
Oops.  
I did not see your attached logs ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
  
I checked it.  
Not bad.  
300ms delay for 3 trades.  
Lets see if it can keep that speed going.  
Then I do not know what is going on with my connection ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#269](/thread/post/10355131#post10355131 "Post Permalink")

  * Oct 4, 2017 7:49pm  Oct 4, 2017 7:49pm 

  * [ eatrader75](eatrader75)

  * | Joined Aug 2017  | Status: Trader | [28 Posts](/search?do=process&provider=Member&searchuser=605097)

Jacques,  
  
According to the speed test on SMFX, the live account is much faster, then with VPS...  

Attached Image

![](/attachment/image/2505573?d=1507111402)

  
Have you tried the free VPS from Amazon AWS? [https://www.tradingheroes.com/get-fr...ng-amazon-ec2/](https://www.tradingheroes.com/get-free-mt4-vps-hosting-amazon-ec2/)  
  
Regarding the unbalanced system, found this here on FF. I wrote a small ea (using fxDreema) based on Renko bars to try out. It worked, however, due to some bug somewhere, after a while it forgets to communicate with the Renko chart and didn't place orders as it should be... I've tried to replace the Renko bars with grid-like orders but again due some bugs can't backtest on MT5...  

> [Quoting jeuro](/thread/post/5267296#post5267296 "View Quoted Post")
> 
> Disliked
> 
> ... Nevertheless I am somewhat an addict for hedging in any type of shape or form. Correlated pairs, Perfect market rings/inefficiency , arbitrages etc. Therefore, I have been testing a similar concept to the original posted by cash4u2 but with some twists. My results look promising in forward test, and would like to backtest the strategy to minimize risk. ( no risk, no profit, no matter what anybody say) but I am stuck in finding how to test the 3 pairs simultaneously. Not only because the strategy is multi-pair, but because we use an EA and because...
> 
> Ignored

> [Quoting jeuro](/thread/post/5270643#post5270643 "View Quoted Post")
> 
> Disliked
> 
> Here is 1 month of forward testing with 1 setting. Started Dec 5 and ended Jan 5 (I used peppertone demo. They are good for 1 month only). I used 0.30 lot in all 3 pairs. It made 781 trades for a total of 234 full round lots traded. $5000 account made $2761.56/55.23% . Total DD was 7.83%. I hope you see the need to get into a good backtest for the strategy. I mean if these stats would be similar every month, it would be wise to place a 10% safety global SL for the account and even if get triggered twice per month , the account still would in the...
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#270](/thread/post/10355147#post10355147 "Post Permalink")

  * Oct 4, 2017 7:55pm  Oct 4, 2017 7:55pm 

  * [ dukas_trader](dukas_trader)

  * | Membership Revoked  | Joined Mar 2010 | [2,525 Posts](/search?do=process&provider=Member&searchuser=136341)

looks really many did not start learning basic of market and math first.  
  
if you want win with triangle arbitrage systems, you need extrem good broker, very fast internet connection wire, best location servers, best trading condition with put in many 100k in money only to establish this over time.  
and even after this there are always bigger in market who simple are before you when you not have at least same technical and software level.  
  
then many test it in demo account, arbitrage systems can never be tested in demo accounts, only if expert can work for programming code errors this would be possible in demo or learning pascis of platform. but all the rest is useless, to 100% useless, because shows null. in real accounts all is different with arbitrage systems, from price, from volume tradeable, from slippage and even from brokers pay you out money. if you dont have aggregation of many liquity providers in one point to see all their seperated prices dont even think about it, why not first learn basics and see why it cant work in this kind you try to do. why wasting time in what is impossible to work by market and math, if done in this kind?  
  
and then "i will makle it available for free". hey, there is no big volume in market to do this arbitrage , often small and you want many can do this, this is simple impossible, in no way it can work what cant work. even if all would not be impossible, then each one would steal the volume from other one, and often you will get extrem different prices and slippage then you thougt because of this, when many trade same thing.  
  
dont take this serios if you want, this was only a tip to save extrem time in something that cant work in reality, if you dont invest extrem money in first (and even then you need at least on level of others ). anyone is the blacksmith of his own future. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#271](/thread/post/10356206#post10356206 "Post Permalink")

  * Edited 2:14am  Oct 5, 2017 12:49am | Edited 2:14am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar402047_21.gif) Fxentropy](fxentropy)

  * Joined Feb 2015 | Status: Who Dares Wins | [1,710 Posts](/search?do=process&provider=Member&searchuser=402047)

> [Quoting jvbJacques](/thread/post/10354831#post10354831 "View Quoted Post")
> 
> Disliked
> 
> @EVERYONE The reason I am so slow in development is because this project will take me about 3 months. I maybe have about a month left in full development time. Problem is I can only do this during my free time and I have to do 5 jobs just to support my monthly payments, which leaves me with about an hour or so worth of free time only some days. Therefore splitting a month of development into chunks of 1 hour increments make it extremely slow so just be patient. The EA is already about 1700 lines of code and beyond that I already discarded and coded...
> 
> Ignored

Thas remind me of Steve Jobs movie....when he was asked: What do you do?  
  

Inserted Video

  
  
Althought i will let you know if i hear anything, having couple of friends in Australia dealing with things outside mining, i cannot help you much in this request. But maybe someone else could give you more help, who knows;  
  
Anyway, @paul72 have a valid point ... worth to check it out deeper. 

"What would you attempt to do, if you knew your success was a certainty?"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#272](/thread/post/10356229#post10356229 "Post Permalink")

  * Oct 5, 2017 12:57am  Oct 5, 2017 12:57am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar402047_21.gif) Fxentropy](fxentropy)

  * Joined Feb 2015 | Status: Who Dares Wins | [1,710 Posts](/search?do=process&provider=Member&searchuser=402047)

> [Quoting dukas_trader](/thread/post/10355147#post10355147 "View Quoted Post")
> 
> Disliked
> 
> looks really many did not start learning basic of market and math first. if you want win with triangle arbitrage systems, you need extrem good broker, very fast internet connection wire, best location servers, best trading condition with put in many 100k in money only to establish this over time. and even after this there are always bigger in market who simple are before you when you not have at least same technical and software level. then many test it in demo account, arbitrage systems can never be tested in demo accounts, only if expert can work...
> 
> Ignored

  
"then each one would steal the volume from other one, and often you will get extrem different prices and slippage then you thougt because of this, when many trade same thing."  
  
You dont know what you are talking about mate....eeeeeerrrrgggghhhhh

"What would you attempt to do, if you knew your success was a certainty?"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#273](/thread/post/10356270#post10356270 "Post Permalink")

  * Oct 5, 2017 1:12am  Oct 5, 2017 1:12am 

  * [ dukas_trader](dukas_trader)

  * | Membership Revoked  | Joined Mar 2010 | [2,525 Posts](/search?do=process&provider=Member&searchuser=136341)

> [Quoting Fxentropy](/thread/post/10356229#post10356229 "View Quoted Post")
> 
> Disliked
> 
> {quote} "then each one would steal the volume from other one, and often you will get extrem different prices and slippage then you thougt because of this, when many trade same thing." You dont know what you are talking about mate....eeeeeerrrrgggghhhhh
> 
> Ignored

at least after your comment i know now you are a beginner in trading , and many posts (red flaged) dont tell anything here about you.  
learn the basics before you talk such things! you look extrem unexpierenced when you cant see what i am talked about, it was a help for beginners and now you set yourself on same level.  
  
but just to help you, what was your problem you did not understand and you did answer this way? you can also ask some people who know trading basics if you dont trust me, and then say simple sorry and ok for this. 

[1 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#274](/thread/post/10356311#post10356311 "Post Permalink")

  * Oct 5, 2017 1:24am  Oct 5, 2017 1:24am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar47674_5.gif) Price](price)

  * | Joined Sep 2007  | Status: Trader | [1,004 Posts](/search?do=process&provider=Member&searchuser=47674)

Guys, chill..... this is most likely not going to work. If you try to arbitrage at your br0ker, then you are just trying to take away from that br0ker due to imperfect pricing.  
  
This is specifically not allowed at each br0ker.  
  
If you are able to create a program which uses 3-way hedge to catch market inefficiencies, it would probably be more of a basket than an arbitrage. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#275](/thread/post/10356478#post10356478 "Post Permalink")

  * Oct 5, 2017 2:12am  Oct 5, 2017 2:12am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar402047_21.gif) Fxentropy](fxentropy)

  * Joined Feb 2015 | Status: Who Dares Wins | [1,710 Posts](/search?do=process&provider=Member&searchuser=402047)

> [Quoting dukas_trader](/thread/post/10356270#post10356270 "View Quoted Post")
> 
> Disliked
> 
> {quote} at least after your comment i know now you are a beginner in trading , and many posts (red flaged) dont tell anything here about you. learn the basics before you talk such things! you look extrem unexpierenced when you cant see what i am talked about, it was a help for beginners and now you set yourself on same level. but just to help you, what was your problem you did not understand and you did answer this way? you can also ask some people who know trading basics if you dont trust me, and then say simple sorry and ok for this.
> 
> Ignored

your badass attitude is everywhere on this forum.....i guess you have had a tough life so far.  
  
chill! 

"What would you attempt to do, if you knew your success was a certainty?"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#276](/thread/post/10356691#post10356691 "Post Permalink")

  * Edited 5:08am  Oct 5, 2017 3:01am | Edited 5:08am 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@everyone  
Please be civil in this forum.  
This forum was created to share my idea and to expand and test it.  
Not to attack each other.  
Attack me.  
I have big shoulders and can take it and will stand up afterwards ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
  
  
@eatrader75  
I really appreciate your input.  
You might have a point that a live account might have a faster speed also, which makes sense, but I do not have one to test on and beyond that this ea i not ready for live.  
As for the unbalanced EA.  
I already ran some tests and it looks good... very good ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
Still some way to make use of the new adaption plus I have got my own spin on it to have a semi unbalanced arbitrage for more predictable results, but still bigger swings for bigger profits to counter the slippage.  
  
I love movies, but I have not seen that movie yet.  
Still Steve Jobs, Bill Gates, Richard Charles Nicholas Branson and my fellow ex countrymen Elon Musk and Mark Shuttleworth are my heroes.  
I know they did not actually invent all their stuff, but they did what the inventors could not do and that is present it in such a way so that they could be funded for the development.  
Unfortunately there are more people in their positions that would rather abuse the inventors/developers for their own use and discard them once done, which does not seem to be what those 5 have done from what I have read.  
  
I will keep you up to date with my progress as I get time ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
  
  
@dukas_trader  
You have mentioned multiple times that this will not work and I respect that and I also appreciate your constructive input and have used it as test cases to improve my coding, so thanks for that.  
You are correct in saying that I am still new at forex.  
I am a programmer first and specialise in reverse engineering and automation on any new technology and I was surprised at how useful my skills are in forex so far.  
  
I have only been playing at forex for about 10 years now on and off so I have a lot to learn, but this theory really caught my attention and I'm like a dog with a bone and would like to see this through to the end until I prove myself wrong or right.  
I just love puzzles and I have proven so many people wrong in the past that just stopped a project because they said it was impossible and then some time later I could make the project work without their support.  
Yes some things are not possible, but then I need to know this myself and in this I can not see the impossibility yet.  
I'm not someone to stop just because it looks to be impossible when I see the possibility.  
  
Unfortunately it did not help that I got my hand on a live account running a kind of similar arbitrage EA, which is making a killing on the market and I'm also looking into how that works to maybe use the same strategy or adapt my own.  
  
As for the market volume being too small I struggle to see that, but I could be proved wrong there also.  
Same unfortunate thing happened to me here also by getting access to live accounts doing multiple scalping trades per hour using a minimum of 100 full lots at a time being filled without a problem.  
I actual saw multiple such account, but I also know those accounts was only made with special permission from a bank or big brokerage.  
Still volumes can be less with bucket shops, which I hope to identify and avoid when going live.  
  
But please do not stop giving suggestions, but keep it constructive and if negative and say it once for the forum remembers and I can look it up in history so no need to repeat. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#277](/thread/post/10357202#post10357202 "Post Permalink")

  * Edited 6:35am  Oct 5, 2017 6:07am | Edited 6:35am 

  * [ dukas_trader](dukas_trader)

  * | Membership Revoked  | Joined Mar 2010 | [2,525 Posts](/search?do=process&provider=Member&searchuser=136341)

> [Quoting Fxentropy](/thread/post/10356478#post10356478 "View Quoted Post")
> 
> Disliked
> 
> {quote} your badass attitude is everywhere on this forum.....i guess you have had a tough life so far. chill!
> 
> Ignored

  
wow, you look here as total beginner, tell wrong things, call me wrong only by not knowing basics and looking same time stupid.  
  
and then you tell this. come on, you make mistakes, play stupid boy, and tell others something? start helping and not only attacking, then i take you serios, until this you are a troll with your posts. you really deserve what you are, you live with your funny character, thats not my problem, but dont tell other people they are wrong when you have near zero experience in the basics. at least say sorry when you see you are total wrong and tdont start then to change topic because you are angry with yourself not knowing this basics. i cant imagine what you do in trading when you dont know this facts, because with higher volume this basics gets important.  
  
and chill is a good point for you, because you next time tell others whats wrong, think about it first by yourself. then other take you more serios and you dont look like a forum troll.  
  
at least try to say something in this treat with arguments, so that all can help you or you have so positive or negativ with arguments to tell and the threat get some help from it. you talk complete without arguments, not only that you are wrong so, wrong without arguments is worst case. so compelte useless content. its not easy to see, how you get red flag and same time has no content to write, then i dont want to see with what posts you got your red flag. your are now 3. person with red flag with this problem. looks common problem with red flags. 

[1 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#278](/thread/post/10357239#post10357239 "Post Permalink")

  * Oct 5, 2017 6:23am  Oct 5, 2017 6:23am 

  * [ dukas_trader](dukas_trader)

  * | Membership Revoked  | Joined Mar 2010 | [2,525 Posts](/search?do=process&provider=Member&searchuser=136341)

> [Quoting jvbJacques](/thread/post/10356691#post10356691 "View Quoted Post")
> 
> Disliked
> 
> @everyone Please be civil in this forum. This forum was created to share my idea and to expand and test it. Not to attack each other. Attack me. I have big shoulders and can take it and will stand up afterwards ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1) @eatrader75 I really appreciate your input. You might have a point that a live account might have a faster speed also, which makes sense, but I do not have one to test on and beyond that this ea i not ready for live. As for the unbalanced EA. I already ran some tests and it looks good... very good ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1) Still some way to make...
> 
> Ignored

  
all fine, but i dont tell you negative things, i only tell the true reality what will come:  
  
the problem is: the account you did see could be faked broker live accounts, demo accounts, or many tricks possible to use to fake big wins... that have this gigantiic wins in arbitrage, or they would have connection te each liquity provider seperatly or it cant work by math and market. your mentioned 10 million trade is not so high, this could be possible in usd currencies. why there should be filling problems? the problem will start with slippage and filling time if you want use arbitrage.  
  
its only help, you can try what you want, but many did exactly this before, ,and stop exactly this after they tried.  
the problem is not the theory, this in fine and lo9gic , but that its not possible to establish with big money in infrastructure and api programms and to get good big broker account with big broker with seperated liquitiy provier feeds or or aggregation pools....... and and and........ the software is the most simplest part and fastest part of this game, thats what many dont see. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#279](/thread/post/10357369#post10357369 "Post Permalink")

  * Oct 5, 2017 8:09am  Oct 5, 2017 8:09am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar402047_21.gif) Fxentropy](fxentropy)

  * Joined Feb 2015 | Status: Who Dares Wins | [1,710 Posts](/search?do=process&provider=Member&searchuser=402047)

> [Quoting dukas_trader](/thread/post/10357202#post10357202 "View Quoted Post")
> 
> Disliked
> 
> {quote} wow, you look here as total beginner, tell wrong things, call me wrong only by not knowing basics and looking same time stupid. and then you tell this. come on, you make mistakes, play stupid boy, and tell others something? start helping and not only attacking, then i take you serios, until this you are a troll with your posts. you really deserve what you are, you live with your funny character, thats not my problem, but dont tell other people they are wrong when you have near zero experience in the basics. at least say sorry when you see...
> 
> Ignored

never been more amased by the desire to explain things and nervousness of a beaten-to-death-as-a-child behaviour like you shown ![](https://resources.faireconomy.media/images/emojis/64/1f644.png?v=15.1)  
  
again, chill mate, im not here to give you heart-attacks nor to destroy you, like someone said earlier to you on another post....live and let live.  
  
peace (you are in my ignore as i dont want to start a fight with you, please do the same)  
  
(cant hold myself tho ![](https://resources.faireconomy.media/images/emojis/64/1f60b.png?v=15.1)...have to ask you.....you are so angry all the time? ...No need to answer , was a rethoric one) 

"What would you attempt to do, if you knew your success was a certainty?"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#280](/thread/post/10357459#post10357459 "Post Permalink")

  * Oct 5, 2017 9:03am  Oct 5, 2017 9:03am 

  * [ dukas_trader](dukas_trader)

  * | Membership Revoked  | Joined Mar 2010 | [2,525 Posts](/search?do=process&provider=Member&searchuser=136341)

> [Quoting Fxentropy](/thread/post/10357369#post10357369 "View Quoted Post")
> 
> Disliked
> 
> {quote} never been more amased by the desire to explain things and nervousness of a beaten-to-death-as-a-child behaviour like you shown ![](https://resources.faireconomy.media/images/emojis/64/1f644.png?v=15.1) again, chill mate, im not here to give you heart-attacks nor to destroy you, like someone said earlier to you on another post....live and let live. peace (you are in my ignore as i dont want to start a fight with you, please do the same) (cant hold myself tho ![](https://resources.faireconomy.media/images/emojis/64/1f60b.png?v=15.1)...have to ask you.....you are so angry all the time? ...No need to answer , was a rethoric one)
> 
> Ignored

thanks, now you give me the right call you offical a bad character. ofcourse you are not hear to give heart attack or destroy me, you did try but only thing was laughing because you are unable to have at least a correct argument and did start with 100% false statement. worst try babe , stupid is fair word to describe how you try to stand here and you are unable to see it, makes you not smartest candle on the cake. but not important, we dont speak here about how much you have to learn, thats your part.  
  
you call me i am wrong with what i wrote , but after you see you was wrong and "stupid" same time to tell me this without thinking about your low experience, you hide all behind stupid textes from you site and run to your mama (at least looks like). you say no sorry for your wrong text, dont have any argument.  
  
sorry to say, but you are really a good example for a bad person.  
but i think you know this already, bringing only bad things in discussion, dont say anything without attacking and on the end say "chill" after attacking with false statements.  
  
but whatever, you are never seen in any discussion, funny you did write hear only to make a fool of yourself. but whatever, its your problem. at least you have no content to the discussion, but looks like thats often your problem.  
  
to jv[bJacques ](https://www.forexfactory.com/jvbjacques): sorry that i have to write something about this crazy fxentropy, this fool is bringing no content, calls correct things wrong and without any arguments says nothing. sorry for write this in your thread, i hope you can understand. i will not write any more to him, he is what he is, cant change this. 

[1 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Simple High Profit low Drawdown Triangular Arbitrage
  *   * [ **Reply to Thread** ](/thread/676132-simple-high-profit-low-drawdown-triangular-arbitrage/reply#reply)

  * More

[](https://www.forexfactory.com "Homepage")

  * [Forums](forums)
  * [Trades](trades)
  * [Calendar](calendar)
  * [News](news)
  * [Market](market)
  * [Brokers](brokers)

****

[](https://www.faireconomy.com/)

  * 

[Triangular Arbitrage](/thread/64423-triangular-arbitrage "Admin, Please Delete Thread.") 258 replies

[Triangular Arbitrage](/thread/62477-triangular-arbitrage "Is going  
long 1 lot of eur/usd + 
long 1 lot of usd/jpy = long 1 lot of eur/jpy ?  
\(is the ratio of the number of lots correct for a...") 16 replies

[Triangular Arbitrage and carry trade](/thread/71997-triangular-arbitrage-and-carry-trade "Is it possible for us retail traders to be able to make use of Tri Arb or carry trades?  
 
Any one know of retail brokers 
 
 
\(I'm...") 6 replies

[Triangular Arbitrage](/thread/367072-triangular-arbitrage "I've been reading about triangular arbing and was surprised to find that the cross of two majors doesn't always equal what the calculation...") 7 replies

[Question: Trade Mechanics of Triangular Arbitrage](/thread/225246-question-trade-mechanics-of-triangular-arbitrage "Before I even ask this question, please allow me to be very clear.... I have no intention of attempting a triangular arbitrage trade\(for...") 6 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/676132-simple-high-profit-low-drawdown-triangular-arbitrage/reply#reply)
  * Subscribe
  * [147](javascript:void\(0\);)

Attachments: Simple High Profit low Drawdown Triangular Arbitrage

Tags: Simple High Profit low Drawdown Triangular Arbitrage

#  [](/thread/676132-simple-high-profit-low-drawdown-triangular-arbitrage)Simple High Profit low Drawdown Triangular Arbitrage 

  * 

  * [#281](/thread/post/10357520#post10357520 "Post Permalink")

  * Oct 5, 2017 9:47am  Oct 5, 2017 9:47am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar402047_21.gif) Fxentropy](fxentropy)

  * Joined Feb 2015 | Status: Who Dares Wins | [1,710 Posts](/search?do=process&provider=Member&searchuser=402047)

> [Quoting dukas_trader](/thread/post/10357459#post10357459 "View Quoted Post")
> 
> Disliked
> 
> {quote} thanks, now you give me the right call you offical a bad character. ofcourse you are not hear to give heart attack or destroy me, you did try but only thing was laughing because you are unable to have at least a correct argument and did start with 100% false statement. worst try babe , stupid is fair word to describe how you try to stand here and you are unable to see it, makes you not smartest candle on the cake. but not important, we dont speak here about how much you have to learn, thats your part. you call me i am wrong with what i wrote...
> 
> Ignored

I was looking into your other posts on others threads......you continuously fight to everybody, your tone is always aggresive and you are only willing to badmouth anyone dare to say something you dont like regardless whats the topic: you are incurable ill i guess....  
  
God thanks i dont have such friends around me....you are a ticking bomb mate, get help!  
  
Live a bit, stay optimist and constructive and dont rush to fight!  
  
cheers!  
  
(please put me on ignore now) 

"What would you attempt to do, if you knew your success was a certainty?"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#282](/thread/post/10357543#post10357543 "Post Permalink")

  * Oct 5, 2017 10:00am  Oct 5, 2017 10:00am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar47674_5.gif) Price](price)

  * | Joined Sep 2007  | Status: Trader | [1,004 Posts](/search?do=process&provider=Member&searchuser=47674)

> [Quoting jvbJacques](/thread/post/10356691#post10356691 "View Quoted Post")
> 
> Disliked
> 
> @everyone.... This forum was created to share my idea and to expand and test it.....
> 
> Ignored

Well I think you're doing a great job on research and testing, etc. The work you are putting in just on this is far more work than many others put in on their entire trading approach.  
  
And even if this doesn't end up making millions on its own, you would probably learn a great deal about market inefficiency that might help with gaining perfect entries on a more complete trading system.  
  
I wish you well in your discovery. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#283](/thread/post/10357686#post10357686 "Post Permalink")

  * Oct 5, 2017 11:34am  Oct 5, 2017 11:34am 

  * [ dukas_trader](dukas_trader)

  * | Membership Revoked  | Joined Mar 2010 | [2,525 Posts](/search?do=process&provider=Member&searchuser=136341)

> [Quoting Fxentropy](/thread/post/10357520#post10357520 "View Quoted Post")
> 
> Disliked
> 
> {quote} I was looking into your other posts on others threads......you continuously fight to everybody, your tone is always aggresive and you are only willing to badmouth anyone dare to say something you dont like regardless whats the topic: you are incurable ill i guess.... God thanks i dont have such friends around me....you are a ticking bomb mate, get help! Live a bit, stay optimist and constructive and dont rush to fight! cheers! (please put me on ignore now)
> 
> Ignored

ok , now i really have to write again (sorry thread owner), because now you have done something thats really show you as a bad ass, you start being a big heavy liar!! until now you was a stupid man with low experience in trading, but now you start offense liar image.  
  
show me one thing i wrote bad over someone who did not deserve it and i did not show by arguments why , and show in context , not one word and the lines before why i wrote something?  
  
you are extrem this man what you call me. you attack me, show how unexperienced you are, be a big liar, call things wrong what are correct and hide this facts all the time,...its like your brain is burning and you dont know what you do.  
  
do you really not see that your writing without arguments is only showing, how stupid you are? a crazy biting dog, nothing more.  
and why i should put you on ignore list, because you are crazy, stupid, a big liar, or what fact?  
  
really, you only came in this thread to attack and be a big asshole, and show all that you are without any argument and content. why you do yo? whats your problem in life or trading that you have without arguments nothing and can only attack?  
  
do what you want, but its funny to see you die in your own liar image. red flag liar, not seen all days, no wonder you have red flag here, when you write only this bullshit each day.  
  
and to your last part: you are no optimist, you are worst crazy possible man here to defend only his won bullshit (what was a big mistake and you cant hear what you wrote was extrem wrong) and contructive you never was here. all was fine in the threat, there was so many help to show what will work in reality and what have to been done , because in reality there are other rules then in demo. and then you come in and start your bullshit. no help from you, no argument, no advantage or disadvantage mentioned, only attacking for nothing and even with extrem wrong statements. thats you, and you can cry so often like you want, you cant hide this fact that you are only this little man like you show here. and ofcourse i can now start to speak about your friends, that you dont look like someone who has many people around who accept this behavior,.... but i am not on your level, i accept your crazy style but dont accept when you attack me without any argument! bring arguments and i will answer to all, or accept that you are not possible to use a forum to discuss.  
  
nothing else to say, or will you again be a liar and bring more wrong sentences? sometimes boring always to correct your sentences, can you at least start to write only the truth and with arguemnts, this would be something to speak about. and maybe start to invest in the threat, your only point was i was wrong , but there i was more then correct - thats not really a help to bring wrong points and nothing more. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#284](/thread/post/10358000#post10358000 "Post Permalink")

  * Oct 5, 2017 3:04pm  Oct 5, 2017 3:04pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar47674_5.gif) Price](price)

  * | Joined Sep 2007  | Status: Trader | [1,004 Posts](/search?do=process&provider=Member&searchuser=47674)

why use 12 words when 800 words would do just fine...... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#285](/thread/post/10358563#post10358563 "Post Permalink")

  * Oct 5, 2017 5:32pm  Oct 5, 2017 5:32pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar457690_1.gif) artico01](artico01)

  * Joined Apr 2016 | Status: Trader | [108 Posts](/search?do=process&provider=Member&searchuser=457690)

@jvbJacques  
  
USD/JPY has a swap very high. Can it be a problem for stretegy? 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: 2017-10-05.png
Size: 96 KB](/attachment/image/2506850/thumbnail?d=1507192302)](/attachment/image/2506850?d=1507192302)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#286](/thread/post/10358678#post10358678 "Post Permalink")

  * Oct 5, 2017 5:59pm  Oct 5, 2017 5:59pm 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

wow lots of action while I was gone... Not all good.  
  
@Price  
Thanks for the support and I agree.  
I have already learnt a lot and still learning.  
I still have a lot of tools in my toolbox that can counteract all the slippage and other problems that I have not yet tested and until I exhaust all options I will continue.  
Plus it is fun ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
  
  
@artico01  
I basically ignore swam and take the hit, because swap is such a small percentage of the losses.  
You can easily test it by opening a single trade and leaving it open in a back test for a year or so and you will see the swap barely affects what profit you make per trade.  
I see it as a minor cost of trading, except Wednesday monster swap, but still I ignore it.  
The big cost being the spread and commission.  
  
Unfortunately I removed the swap ignore part out of EA 19 .... oops.  
Still works, but I like to leave it out of the calculations.  
Will probably put it back in the next EA version.  
  
From your chart your trade should have opened and closed multiple times if there was no slippage.  
Dang slippage.  
Look out for the new EA in a few ..... days or months .... ![](https://resources.faireconomy.media/images/emojis/64/1f641.png?v=15.1)  
I tested a variable unbalanced triangle with great success, just need to finish its coding, which should handle slippage like a boss and even big [spreads](/brokers/spreads "View Live Spreads on the Broker Guide") and commissions.  
Still a lot of theory to test. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#287](/thread/post/10358680#post10358680 "Post Permalink")

  * Oct 5, 2017 6:00pm  Oct 5, 2017 6:00pm 

  * [ eatrader75](eatrader75)

  * | Joined Aug 2017  | Status: Trader | [28 Posts](/search?do=process&provider=Member&searchuser=605097)

Jacques,  
  
I've got yesterday 3 sets of trades. 2 of them closed in profit.  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot1.png
Size: 36 KB](/attachment/image/2506853/thumbnail?d=1507192582)](/attachment/image/2506853?d=1507192582)   

  
  
The 3rd one had about $5 floating profit in the evening, didn't close it manually - the swap killed this profit and missed many opportunities because of the open trades.  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot2.png
Size: 134 KB](/attachment/image/2506856/thumbnail?d=1507192775)](/attachment/image/2506856?d=1507192775)   

  
  
Did you manage to have a look at the free Amazon AWS VPS? 

Attached File(s)

![File Type: txt](https://assets.faireconomy.media/images/attach/txt.gif) [SMFX Standard.txt](/attachment/file/2506874?d=1507193965) 29 KB | 220 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#288](/thread/post/10358716#post10358716 "Post Permalink")

  * Oct 5, 2017 6:07pm  Oct 5, 2017 6:07pm 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@eatrader75  
Nice.  
  
No sorry.  
I did not have time to look at the amazon VPS yet, but thanks for the suggestion.  
I will certainly look at it.  
  
I am also falling in love with JTrader and Dukascopy.  
Execution speed looks very good and still better they have got a free VPS for all their accounts, maybe even demo accounts.  
The only VPS limitation is it need to only use about 50megs of memory, but in java anything is possible ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
Also another good thing about the VPS is that it sounds like it is running directly on their trading server, which means sub 1ms connection delay and it is multi-threaded, meaning no waiting for single trades.  
Still need to test most of that. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#289](/thread/post/10359627#post10359627 "Post Permalink")

  * Edited 10:10pm  Oct 5, 2017 9:51pm | Edited 10:10pm 

  * [ JRogerFX](jrogerfx)

  * | Joined Oct 2017  | Status: Trader | [4 Posts](/search?do=process&provider=Member&searchuser=617178)

Hello @jvbJacques,  
  
I'm trying to set your EA on an MT5 demo account, but getting newError=4302 at expert advisor log event. Any idea?  
  
Great work by the way!!  
  
  
********************* SOLVED ****************  
  
I think this was a newby question, was thinking to delete it, but maybe could help others!! This erros was due to all symbols wasn't added in the MarketWatch!! Just put them all (gbpjpy, usdjpy, gbpusd), restarted mt5, and attached EA. Now it's working. Let's see how does it does on ICMarkets demo account from InterServer VPS. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#290](/thread/post/10359826#post10359826 "Post Permalink")

  * Edited 10:57pm  Oct 5, 2017 10:24pm | Edited 10:57pm 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@JRogerFX  
Welcome.  
There is no such thing as a newbie question so keep asking and enjoy ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
  
Thanks for pointing that out to the others, I am sure there are many that will find it useful as you are not the first that had that problem.  
  
Just to recap.  
Just add the 3 symbols to the market watch, no need to open charts for each symbol. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#291](/thread/post/10360642#post10360642 "Post Permalink")

  * Oct 6, 2017 12:34am  Oct 6, 2017 12:34am 

  * [ eatrader75](eatrader75)

  * | Joined Aug 2017  | Status: Trader | [28 Posts](/search?do=process&provider=Member&searchuser=605097)

Jacques,  
  
I've closed those losing trades manually in the morning, giving a chance for new trades. But no new trades despite the opportunities...  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot2.png
Size: 151 KB](/attachment/image/2507467/thumbnail?d=1507216050)](/attachment/image/2507467?d=1507216050)   

  
  
It isn't possible to open 2 sets of trades (buy-sell-sell and sell-buy-buy) let say randomly, then when the signal comes, close the winner set or trail the profit/stop then reopen them? Just a thought... 

Attached File(s)

![File Type: txt](https://assets.faireconomy.media/images/attach/txt.gif) [SMFX Standard.txt](/attachment/file/2507478?d=1507216467) 2 KB | 236 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#292](/thread/post/10360814#post10360814 "Post Permalink")

  * Oct 6, 2017 1:15am  Oct 6, 2017 1:15am 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@eatrader75  
If you manually close the trades then you have to restart the EA.  
It is not smart enough yet to pick up the trades was closed and will wait forever.  
  
Yes it is possible, but they basically cancel each other out so not profit no matter how you look at it.  
  
Do not worry.  
  
An update is coming that might be the solution to our slippage problem.  
This EA will work if the slippage is low or nonexistent, which it is not.  
The new EA should work with any slippage or spread, depending on how much profit you want. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#293](/thread/post/10361027#post10361027 "Post Permalink")

  * Oct 6, 2017 2:17am  Oct 6, 2017 2:17am 

  * [ eatrader75](eatrader75)

  * | Joined Aug 2017  | Status: Trader | [28 Posts](/search?do=process&provider=Member&searchuser=605097)

Jacques,  
  
I think it needs to explain more my previous thought. The 2 sets of trades don't mean to cancel each other.  
\- Right now you **_open_** 1 set when the signal appears. According to the signal, you know that the GBPJPY-GBPUSD-USDJPY should be buy-sell-sell or sell-buy-buy.  
\- But if you want to use the signal to **_close_** the trades, you need to be prepared for both situations. 1 set of buy-sell-sell and 1 set of sell-buy-buy. Close only the winner set and reopen them. The other set is waiting for its right signal.  
  
The idea comes from a lock latency arbitrage site, and I just focused on to: "**Replace the orders opening by the orders closure, and thereby reduce the time of execution and therefore slippage."**<http://iticsoftware.com/en/lock-latency-arbitrage.html>  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot1.png
Size: 53 KB](/attachment/image/2507642/thumbnail?d=1507223072)](/attachment/image/2507642?d=1507223072)   

  
  
I know, that's different arbitrage than yours, so just a thought...  
Exited to see your updated ea!  
  
Thanks 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#294](/thread/post/10361112#post10361112 "Post Permalink")

  * Oct 6, 2017 2:37am  Oct 6, 2017 2:37am 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@eatrader75  
Unfortunately it will still not work.  
I see what you want to do.  
  
Problem is you need to look at the chart.  
It tries to open on the opposite side blue line.  
Then close on the middle line or the other blue line.  
  
Now that seem like a large distance, but it is actually just a few pips that is zoomed in a lot in the chart.  
Therefore if you open both trades say in the middle and close it on the outer edges then you make even less pip profit.  
  
We are already hitting the wall when it comes to slippage so now you have even less profit to cover the slippage.  
  
My very first EA was something like that.  
  
BUT BUT I Like small buts ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
  
The new EA will make use of something like that.  
Actually the new EA makes use of a grid system again, but also a unbalanced triangle.  
Initial tests looks good.  
  
As for the US and no hedging.  
  
I see no need ever for hedging, except if you want to use a cool multiple trade close trick ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1) Which might be one reason for hedging, but not for hedging and just for closing fast, but that is a story for another day.  
  
I handle hedging with cancelled orders sort of.  
If you have a BUY and SELL then you have nothing.  
People need that to calculate the movement of the trades normally, but using code I can calculate the movement without an actual live trade.  
The advantage is smaller sized and less trades and best of all only trades in ONE direction.  
  
So no problem with US no hedging rules for there is no actual hedging going on in the trades itself.  
Show me a hedge and I will show you how to do the same or better without a hedge.... Except for that darn awesome close trick, but then MT5 have that trick build in using hedging or no hedging. ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#295](/thread/post/10361822#post10361822 "Post Permalink")

  * Edited 8:06am  Oct 6, 2017 6:34am | Edited 8:06am 

  * [ eatrader75](eatrader75)

  * | Joined Aug 2017  | Status: Trader | [28 Posts](/search?do=process&provider=Member&searchuser=605097)

Jacques,  
  
As you've mentioned your good results with the unbalanced EA, thought that I might restart the forward testing with mine. The screenshot shows the last 8 hours of trading (ignore the "HEDGE-CLOSE-ORDER" in the top report).  
  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot1.png
Size: 172 KB](/attachment/image/2507868/thumbnail?d=1507236266)](/attachment/image/2507868?d=1507236266)   

  
  
Trading with 2 sets of EURUSD-USDCHF-EURCHF orders independently: buy-buy-sell and sell-sell-buy (in the comment with number 1 and 2). It mimics the Renko chart in a way that I've already mentioned in #Post 269, by jeuro. You may have an idea how to improve it, or maybe your new update has some similarity.  
  
Edit: I've removed an unnecessary line from the setting. Place the EA on any symbol, only 1 chart, any timeframe. Use the following settings for a quicker test:  

Attached Image

![](/attachment/image/2508022?d=1507244592)

Attached File(s)

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [hedging 3 pseudo renko v1.1.mq4](/attachment/file/2507992?d=1507243075) 205 KB | 774 downloads 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#296](/thread/post/10365974#post10365974 "Post Permalink")

  * Oct 7, 2017 4:01am  Oct 7, 2017 4:01am 

  * [ eatrader75](eatrader75)

  * | Joined Aug 2017  | Status: Trader | [28 Posts](/search?do=process&provider=Member&searchuser=605097)

Jacques,  
  
The U.S. Nonfarm Payrolls and Unemployment Rate announcement made your EA very busy today. This profit should be on my live account now.  
  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: SMFX profit 1.jpg
Size: 522 KB](/attachment/image/2509350/thumbnail?d=1507314738)](/attachment/image/2509350?d=1507314738)   

  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: SMFX profit 2.jpg
Size: 158 KB](/attachment/image/2509352/thumbnail?d=1507314746)](/attachment/image/2509352?d=1507314746)   

  
  
Thanks!

Attached File(s)

![File Type: txt](https://assets.faireconomy.media/images/attach/txt.gif) [SMFX experts.txt](/attachment/file/2509358?d=1507314769) 92 KB | 250 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#297](/thread/post/10366130#post10366130 "Post Permalink")

  * Oct 7, 2017 4:49am  Oct 7, 2017 4:49am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar438576_2.gif) raffus](raffus)

  * | Joined Dec 2015  | Status: Member RFP | [57 Posts](/search?do=process&provider=Member&searchuser=438576)

> [Quoting eatrader75](/thread/post/10361822#post10361822 "View Quoted Post")
> 
> Disliked
> 
> Jacques, As you've mentioned your good results with the unbalanced EA, thought that I might restart the forward testing with mine. The screenshot shows the last 8 hours of trading (ignore the "HEDGE-CLOSE-ORDER" in the top report). {image} Trading with 2 sets of EURUSD-USDCHF-EURCHF orders independently: buy-buy-sell and sell-sell-buy (in the comment with number 1 and 2). It mimics the Renko chart in a way that I've already mentioned in #Post 269, by jeuro. You may have an idea how to improve it, or maybe your new update has some similarity. Edit:...
> 
> Ignored

Hello @eatrader  
  
what are the group of 3 currency you have taken?  
i can see 3 charts so i suppose you are running 3x triple hedging system  
Correct?  
  
if yes please can you kindly write me ?  
tks! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#298](/thread/post/10366171#post10366171 "Post Permalink")

  * Oct 7, 2017 5:15am  Oct 7, 2017 5:15am 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@eatrader75  
Not a bad week there for you.  
  
Wish I could push the development faster to give you the multi triangle on now with better stops.  
Those stops are important and unfortunately not part of EA19.  
The stops prevent a trade opened with a lot of slippage to stay open forever, with a small amount of loss.  
  
Your trade execution speed seem very good with little to no slippage in the logs compared to my demo account trades.  
You say that is a live account ?  
If so then it looks like live is the way to go for less slippage strange enough.  
  
Good luck.  
  
  
  
@raffus  
This is is just being tested on the GBP triangle, but can work with any triangle out there and in a later EA I will insert the option to combine multiple triangles for faster trading with no extra draw-down. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#299](/thread/post/10366196#post10366196 "Post Permalink")

  * Oct 7, 2017 5:32am  Oct 7, 2017 5:32am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar457690_1.gif) artico01](artico01)

  * Joined Apr 2016 | Status: Trader | [108 Posts](/search?do=process&provider=Member&searchuser=457690)

Weekly results. Demo account SMFX. Logs. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: 2017-10-06.png
Size: 78 KB](/attachment/image/2509528/thumbnail?d=1507321669)](/attachment/image/2509528?d=1507321669)   

Attached File(s)

![File Type: txt](https://assets.faireconomy.media/images/attach/txt.gif) [10-01-17log.txt](/attachment/file/2509529?d=1507321731) 58 KB | 243 downloads 

![File Type: txt](https://assets.faireconomy.media/images/attach/txt.gif) [10-03-17log.txt](/attachment/file/2509530?d=1507321731) 33 KB | 218 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#300](/thread/post/10366209#post10366209 "Post Permalink")

  * Oct 7, 2017 5:40am  Oct 7, 2017 5:40am 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@artico01  
I'm pleasantly shocked at how good this EA is performing, even at this unfinished stage ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
I'll set it up and you knock it down ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Simple High Profit low Drawdown Triangular Arbitrage
  *   * [ **Reply to Thread** ](/thread/676132-simple-high-profit-low-drawdown-triangular-arbitrage/reply#reply)

  * More

[](https://www.forexfactory.com "Homepage")

  * [Forums](forums)
  * [Trades](trades)
  * [Calendar](calendar)
  * [News](news)
  * [Market](market)
  * [Brokers](brokers)

****

[](https://www.faireconomy.com/)

  * 

[Triangular Arbitrage](/thread/64423-triangular-arbitrage "Admin, Please Delete Thread.") 258 replies

[Triangular Arbitrage](/thread/62477-triangular-arbitrage "Is going  
long 1 lot of eur/usd + 
long 1 lot of usd/jpy = long 1 lot of eur/jpy ?  
\(is the ratio of the number of lots correct for a...") 16 replies

[Triangular Arbitrage and carry trade](/thread/71997-triangular-arbitrage-and-carry-trade "Is it possible for us retail traders to be able to make use of Tri Arb or carry trades?  
 
Any one know of retail brokers 
 
 
\(I'm...") 6 replies

[Triangular Arbitrage](/thread/367072-triangular-arbitrage "I've been reading about triangular arbing and was surprised to find that the cross of two majors doesn't always equal what the calculation...") 7 replies

[Question: Trade Mechanics of Triangular Arbitrage](/thread/225246-question-trade-mechanics-of-triangular-arbitrage "Before I even ask this question, please allow me to be very clear.... I have no intention of attempting a triangular arbitrage trade\(for...") 6 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/676132-simple-high-profit-low-drawdown-triangular-arbitrage/reply#reply)
  * Subscribe
  * [147](javascript:void\(0\);)

Attachments: Simple High Profit low Drawdown Triangular Arbitrage

Tags: Simple High Profit low Drawdown Triangular Arbitrage

#  [](/thread/676132-simple-high-profit-low-drawdown-triangular-arbitrage)Simple High Profit low Drawdown Triangular Arbitrage 

  * 

  * [#301](/thread/post/10366216#post10366216 "Post Permalink")

  * Oct 7, 2017 5:46am  Oct 7, 2017 5:46am 

  * [ eatrader75](eatrader75)

  * | Joined Aug 2017  | Status: Trader | [28 Posts](/search?do=process&provider=Member&searchuser=605097)

raffus,  
  
If you talking about the hedging 3 pseudo renko EA please check the following thread: <https://www.forexfactory.com/showthread.php?t=335072>  
Also please read again the #Post 295 on this page 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#302](/thread/post/10366326#post10366326 "Post Permalink")

  * Oct 7, 2017 7:17am  Oct 7, 2017 7:17am 

  * [ eatrader75](eatrader75)

  * | Joined Aug 2017  | Status: Trader | [28 Posts](/search?do=process&provider=Member&searchuser=605097)

Jacques,  
  
I'm in the UK, and this is still the Standard Demo account, no VPS. Maybe it would be nice to try it out on a small, let say $100 live account with them. Perhaps another one with Dukascopy? Will think about... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#303](/thread/post/10371153#post10371153 "Post Permalink")

  * Oct 10, 2017 2:04am  Oct 10, 2017 2:04am 

  * [ eatrader75](eatrader75)

  * | Joined Aug 2017  | Status: Trader | [28 Posts](/search?do=process&provider=Member&searchuser=605097)

Jacques,  
  
I'm setting up my $100 live account with SMFX. Just had some chat with them...  
They have a margin call at 200%, but your ea's margin level is 126%. Is it possible to adjust it? Without that can't-do a live test.  
My Metatrader's Journal says "Trades: use hosting service to speed up the execution - 1.54 ms via 'MQL5 New York 6 (MQL5 Ltd.)' instead of 111.98 ms". (I'm in Hungary this week.) How can I do that? SMFX says their VPS is a better option so thinking to set up a VPS with them, but they have 3 choices. I don't know which one is better for your ea.  
  
Thanks 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#304](/thread/post/10371194#post10371194 "Post Permalink")

  * Oct 10, 2017 2:17am  Oct 10, 2017 2:17am 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@eatrader75  
ea 19 is way too unstable to recommend for live trading.  
I suggest waiting for the next one.  
  
As for which VPS.  
That suggestion must be made by the broker SMFX.  
I would think the closest VPS to the SMFX server.  
  
Still I think using EA19 for a live test will be a waste, but that I will leave up to you.  
I myself would like to see the response time for trades on a live server and if there is a big difference between it and a demo.  
  
The EA adjusts to the available free margin, but I will test it on that broker when I get time.  
Sorry for taking so long.  
I'm struggling at work and therefore to get free time. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#305](/thread/post/10371221#post10371221 "Post Permalink")

  * Oct 10, 2017 2:27am  Oct 10, 2017 2:27am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar2942_8.gif) Nicholishen](nicholishen)

  * Joined Jul 2005 | Status: zzzzzzzzzzzzzzzzzzzzzzzzz zzzzzzzzzz | [1,261 Posts](/search?do=process&provider=Member&searchuser=2942)

> [Quoting artico01](/thread/post/10358563#post10358563 "View Quoted Post")
> 
> Disliked
> 
> @jvbJacques USD/JPY has a swap very high. Can it be a problem for stretegy? {image}
> 
> Ignored

Absolutely is a problem! Your net position is 0.003 short USDJPY. You're paying through the nose to hold that trade!  
  
I really don't understand the pursuit of this strategy from a retail paradigm. If you want to be successful with arbitrage you need a c++ algo running on a specialized kernel on a colocated server connected directly to LPs via FIX. Otherwise, slippage, swaps, and trading costs will erode any potential profits with this system. This strategy is what billion dollar HFT firms spend millions of dollars to beat out the next poorest billion dollar HFT firm by a micro-second. There is no way to compete with a retail broker and the metatrader platform. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#306](/thread/post/10371340#post10371340 "Post Permalink")

  * Oct 10, 2017 3:22am  Oct 10, 2017 3:22am 

  * [ dukas_trader](dukas_trader)

  * | Membership Revoked  | Joined Mar 2010 | [2,525 Posts](/search?do=process&provider=Member&searchuser=136341)

> [Quoting Nicholishen](/thread/post/10371221#post10371221 "View Quoted Post")
> 
> Disliked
> 
> {quote} Absolutely is a problem! Your net position is 0.003 short USDJPY. You're paying through the nose to hold that trade! I really don't understand the pursuit of this strategy from a retail paradigm. If you want to be successful with arbitrage you need a c++ algo running on a specialized kernel on a colocated server connected directly to LPs via FIX. Otherwise, slippage, swaps, and trading costs will erode any potential profits with this system. This strategy is what billion dollar HFT firms spend millions of dollars to beat out the next poorest...
> 
> Ignored

i told them already same. you are first with same opinion and trying to help them too to save time, looks like you trade also in real. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#307](/thread/post/10371427#post10371427 "Post Permalink")

  * Oct 10, 2017 4:10am  Oct 10, 2017 4:10am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar608462_3.gif) T4Trade](t4trade)

  * Joined Sep 2017 | Status: Trend Following,Price Action,Grid | [2,484 Posts](/search?do=process&provider=Member&searchuser=608462)

can someone plz tell us that will this EA*(JVB artibrage) close the trades by itself? and what criteria it picks buy or sell for the GBP and JPY? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#308](/thread/post/10371441#post10371441 "Post Permalink")

  * Oct 10, 2017 4:22am  Oct 10, 2017 4:22am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar440253_2.gif) badeel](badeel)

  * Joined Dec 2015 | Status: Trader | [257 Posts](/search?do=process&provider=Member&searchuser=440253)

creator of this EA has brilliant mind but unfortunately has no fund to develop this master piece for all of us . He is trying gradually due to lack of fund so may be this EA will complete in near future or will complete for our children when they grew up.  
anyway if someone want a quick up gradation of this EA, should cooperate in funding.  
thanks 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#309](/thread/post/10371527#post10371527 "Post Permalink")

  * Edited 8:17am  Oct 10, 2017 5:03am | Edited 8:17am 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@Nicholishen  
Swap does not play that much of a role.  
Problem with EA 19 is the slippage and invalid entry point.  
Once a trade is opened incorrectly then EA 19 cannot recover and will never recover, meaning swap will accumulate, but even multiple days worth of swap does not affect this strategy.  
Also.  
Trades normally lasts a couple of hours at most, so that by itself is showing a problem with EA 19, you can see that by back-testing the EA.  
Back testing does not suffer slippage, but will show you the affect, or none affect of swap on the strategy.  
The next version of the EA should cater for slippage after open and recalculate the exit point.  
Read on for more information.  
  
  
@T4Trade  
Yes it closes trades by itself, but there is a problem with EA 19 in that with slippage it sometimes opens trades out of place and the nature of triangular arbitrage is that it has got fixed highs and lows and therefore a way out of place trade will never hit it's profit target.  
  
I already have a solution planned for it in that I need to recalculate the full history arbitrage levels or as far back as possible after open to check for the correct close level, even if at a loss, to prevent perpetual open positions, which EA 19 is susceptible to.  
EA 18 uses a pre-calculated open and close, but suffers from the opposite problem in that it does not take into account slippage during the open and therefore will also close at the wrong position.  
  
The solution is a combination of the 2 methods by recalculating after open and then adapting the close over time.  
  
To see how the balance of the triangular arbitrage works then run it using a MT5 back test for a couple of months and look at the lines it draw on the chart to see the stability and potential entry and exit points.  
  
  
  
@badeel  
Thanks badeel.  
I am already training my 7 year old boy to finish the EA once I am gone in a few hundred years (I plan to live long) ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
  
Unfortunately you are right.  
I can only develop in my free time.  
Laws in my country prevent me from making a profit from my programs and inventions without giving the majority of my income to 3rd party connected companies and therefore I live from hand to mouth.  
Therefore free time is few and far in-between with only 5 to 6 hours sleep at night there is not much left.  
  
BUT I will continue until I am done.  
I already have about 4 new versions running here.  
Even some mutations like an unbalanced triangular arbitrage grid system and a single/double legged triangular arbitrage snowball system.  
  
All of which is unstable and just mutated from the tests so they did not take much time from the main EA development, but looks nice ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
  
I will continue and will update this forum with updates as they occur.  
Monitor post #1, which will always contain the main updates.  
  
  
  
  
  
@EVERYONE  
Slippage is mainly caused by the slow execution speed of the EA.  
The delay seem in part to be caused by metatrader itself, but I hope to be proved wrong by a fast broker somewhere out there, but alas after testing multiple brokers I could not find a really fast one so I went the route of sacrificing some profit to cover the slow speed and slippage.  
Still working on that and will continue working on that until done.  
  
I also whent to Dukascopy to test the rumours that they are faster with their Jtrader program.  
WOW and are they faster.  
According to people I talked to they said that Jtrader is faster on a live account than a demo account, which makes sense for any broker I guess, but I do not have funds to test on live so I went and used their FREE VPS, ANOTHER WOW ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
Even on their DEMO VPS ..... WOOOOOOOWWWWWW... ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)  
  
300ms to open all 3 trades fully and at the same time.  
Another 300ms to close all 3 trades.  
I once got 120ms for 3 trades.  
Basically 300ms per trade, but you can do multiple trades at the same time and therefore they finish at the same time and not one after the other like in metatrader.  
That is an massive amount faster than anything I could get on even MT5.  
Or about the same as metatrader for a single fast trade, but JTrader can do multiple trades at the same time with no slow down, unlike metatrader which need to do one after the other and even if you do multi threading then metatrader still have to first reconnect each thread if a trade is needed, which adds even more delay.  
  
I would suggest a live test on them before anything else, but I am getting ahead of myself.  
Let my first finish the EA.  
  
I'm now converting the EA to run on Dukascopy Jtrader.  
  
Other than the speed I hear only good things about dukascopy so if anyone know a reason as to not to trust them then please let me know.  
  
This also brings back my theory that to really boost this strategy that I need to incorporate each broker's unique API to really get to the bare bones of the forex to get good execution speed.  
The FIX API seem to be the go to for most fast brokers, but to develop it I need a demo account, which I can find no where, so any advice on getting a demo would be appreciated.  
A live FIX account I cannot afford so demo is best.  
  
If only more brokers used Jtrader for that is a wonderful platform, so powerful, but FIX is supported by many more, which tells me that once development is done and working on Dukascopy and ![](https://resources.faireconomy.media/images/emojis/64/1f641.png?v=15.1) Metatrader ![](https://resources.faireconomy.media/images/emojis/64/1f641.png?v=15.1) then FIX is next.  
  
Keep you fingers crossed.  
Here I go with a mountain of coding to do ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1) What fun ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#310](/thread/post/10383351#post10383351 "Post Permalink")

  * Oct 12, 2017 10:52pm  Oct 12, 2017 10:52pm 

  * [ ZanderZhang](zanderzhang)

  * | Joined Oct 2017  | Status: Trader | [4 Posts](/search?do=process&provider=Member&searchuser=618802)

I would like to know how to use this EA on MT4. Thank you 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#311](/thread/post/10391130#post10391130 "Post Permalink")

  * Oct 15, 2017 2:11am  Oct 15, 2017 2:11am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar457690_1.gif) artico01](artico01)

  * Joined Apr 2016 | Status: Trader | [108 Posts](/search?do=process&provider=Member&searchuser=457690)

Hi everyone  
  
This week the EA did not close the open trades.  
  
On the other hand I used the strategy tester of Metatrader 5, starting from a figure of 10000 EUR and a leverage 1: 100 and trial period of one year, with a speed of 72 ms.  
The EA has reached almost EUR 170000 in two months and has not traded anymore.  
Questions:  
Why stop at two months?  
Is it possible that in two months (2017/01/02 - 2017/02/13) you have multiplied the equity / balance by 17?  
  
I attached the test files 

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: 2017-10-13.png
Size: 51 KB](/attachment/image/2518801/thumbnail?d=1507999731)](/attachment/image/2518801?d=1507999731)   
[![Click to Enlarge

Name: ReportTester-89976-holding.png
Size: 17 KB](/attachment/image/2518824/thumbnail?d=1508001027)](/attachment/image/2518824?d=1508001027)   
[![Click to Enlarge

Name: ReportTester-89976-hst.png
Size: 32 KB](/attachment/image/2518825/thumbnail?d=1508001028)](/attachment/image/2518825?d=1508001028)   
[![Click to Enlarge

Name: ReportTester-89976-mfemae.png
Size: 40 KB](/attachment/image/2518827/thumbnail?d=1508001028)](/attachment/image/2518827?d=1508001028)   
[![Click to Enlarge

Name: ReportTester-89976.png
Size: 8 KB](/attachment/image/2518830/thumbnail?d=1508001028)](/attachment/image/2518830?d=1508001028)   

Attached File(s)

![File Type: xlsx](https://assets.faireconomy.media/images/attach/xlsx.gif) [ReportTester-89976.xlsx](/attachment/file/2518822?d=1508001004) 280 KB | 266 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#312](/thread/post/10391336#post10391336 "Post Permalink")

  * Oct 15, 2017 5:21am  Oct 15, 2017 5:21am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar2942_8.gif) Nicholishen](nicholishen)

  * Joined Jul 2005 | Status: zzzzzzzzzzzzzzzzzzzzzzzzz zzzzzzzzzz | [1,261 Posts](/search?do=process&provider=Member&searchuser=2942)

> [Quoting artico01](/thread/post/10391130#post10391130 "View Quoted Post")
> 
> Disliked
> 
> Hi everyone This week the EA did not close the open trades. On the other hand I used the strategy tester of Metatrader 5, starting from a figure of 10000 EUR and a leverage 1: 100 and trial period of one year, with a speed of 72 ms. The EA has reached almost EUR 170000 in two months and has not traded anymore. Questions: Why stop at two months? Is it possible that in two months (2017/01/02 - 2017/02/13) you have multiplied the equity / balance by 17? I attached the test files {image} {file} {image} {image} {image} {image}
> 
> Ignored

The MT5 tester is doesn't work with this strategy because ticks are not accurate and aren't properly synced. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#313](/thread/post/10391354#post10391354 "Post Permalink")

  * Oct 15, 2017 5:37am  Oct 15, 2017 5:37am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar616196_16.gif) OHLC](ohlc)

  * | Joined Oct 2017  | Status: Trader | [498 Posts](/search?do=process&provider=Member&searchuser=616196)

> [Quoting Nicholishen](/thread/post/10391336#post10391336 "View Quoted Post")
> 
> Disliked
> 
> {quote} The MT5 tester is doesn't work with this strategy because ticks are not accurate and aren't properly synced.
> 
> Ignored

Based on my experience, several other things don't work correctly on MT5. They should just continue allowing brokers to use MT4 until MT5 is sufficiently bug tested in order to get the basics right. Even then, hopefully they continue allowing the use of MT4 since there are already so many tools or solutions created for MT4. 

Here's Tom with the weather.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#314](/thread/post/10392316#post10392316 "Post Permalink")

  * Oct 16, 2017 1:39am  Oct 16, 2017 1:39am 

  * [ rizam34](rizam34)

  * | Joined Sep 2017  | Status: Trader | [44 Posts](/search?do=process&provider=Member&searchuser=611864)

my one ..no trade ...![](https://resources.faireconomy.media/images/emojis/64/1f600.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#315](/thread/post/10392426#post10392426 "Post Permalink")

  * Oct 16, 2017 2:52am  Oct 16, 2017 2:52am 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@ZanderZhang  
Please attach you log of the EA so I can have a look.  
  
Basically you just have to attache the EA to a GBPUSD minute chart and have the GBPJPY and USDJPY symbols listed in the market watch.  
  
Also make sure your metatrader is set to be able to run EAs.  
  
  
  
  
@artico01 AND @rizam34 AND @rizam34  
I have discovered a bug in EA19 in that it sometimes opens up a trade and then never closes it.  
I have already fixed it, but are still working on some other coding enhancements so I have not updated the forum with the updates yet.  
  
  
@artico01  
I am not sure why it stopped, but there is a couple of reasons.  
1) There is a 50 lot limit and once reached the EA will stop.  
I put it in seeing that the original broker I used had a 50 lot limit and to overcome it I have to open multiple trades, which just adds to the trade delay.  
  
2) There is a problem with EA 19 at the moment that it sometimes opens a trade and leaves it open forever.  
  
As for the accuracy.  
You seem to make a lot of profit during the back test, which is telling me you either have a fantastic broker with fantastic spread/commission OR you are using the wrong testing parameters.  
When you test on MT5 then do not select "EVERY TICK".  
Select "EVERY TICK BASED ON REAL DATA".  
  
Every tick based on real data is more accurate and are time synchronised for multiple currency testing.   
Not every broker have got accurate real tick data, but I found myfxchoice to have some good data for the past 3 to 5 months at least.  
  
You will see the profit drop a lot, but still good profit.  
  
  
  
  
@EVERYONE  
My phone broke and I could not afford a phone with whatsapp capabilities yet so those that contacted me over whatsapp please note that I am not ignoring you.  
I hope to have access to a whatsapp capable phone some time in future.  
  
I also am stuck between multiple odd jobs, which takes away most of my free time and therefore development has slowed down to a crawl.  
Will keep you up to date as I get time. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#316](/thread/post/10393014#post10393014 "Post Permalink")

  * Oct 16, 2017 11:16am  Oct 16, 2017 11:16am 

  * [ ZanderZhang](zanderzhang)

  * | Joined Oct 2017  | Status: Trader | [4 Posts](/search?do=process&provider=Member&searchuser=618802)

This is what I showed after loading 

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: 1.png
Size: 87 KB](/attachment/image/2519624/thumbnail?d=1508120033)](/attachment/image/2519624?d=1508120033)   
[![Click to Enlarge

Name: 2.png
Size: 96 KB](/attachment/image/2519625/thumbnail?d=1508120034)](/attachment/image/2519625?d=1508120034)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#317](/thread/post/10393049#post10393049 "Post Permalink")

  * Oct 16, 2017 11:58am  Oct 16, 2017 11:58am 

  * [ ZanderZhang](zanderzhang)

  * | Joined Oct 2017  | Status: Trader | [4 Posts](/search?do=process&provider=Member&searchuser=618802)

After loading on the MT4, the EA no orders, I set up according to your settings, I would like to ask what is the next reason? Thank you 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: 3.png
Size: 101 KB](/attachment/image/2519640/thumbnail?d=1508122700)](/attachment/image/2519640?d=1508122700)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#318](/thread/post/10393473#post10393473 "Post Permalink")

  * Oct 16, 2017 3:41pm  Oct 16, 2017 3:41pm 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@ZanderZhang  
According to your screenshots the EA seem to be running fine.  
Maybe zoom the chart a bit out so that you can see the lines a bit better, but it is running.  
Also you have attached the EA to a 5 minute chart, which will not show the EA lines that good, but will not affect the running of the EA.  
I suggest a 1minute chart, but again it does not matter for the running of the EA, just for the display of the lines.  
  
The logs can be accessed by right clicking in the "Experts" tab and selecting OPEN.  
Then the log text files will be displayed and that you can attached to this forum so I can check, but the Experts tab screen shot looks good and the lines on the chart is showing a very good spread/commission. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#319](/thread/post/10394031#post10394031 "Post Permalink")

  * Oct 16, 2017 6:29pm  Oct 16, 2017 6:29pm 

  * [ ZanderZhang](zanderzhang)

  * | Joined Oct 2017  | Status: Trader | [4 Posts](/search?do=process&provider=Member&searchuser=618802)

I still do not know it under the law, what kind of circumstances for automatic trading 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: 25.png
Size: 87 KB](/attachment/image/2520009/thumbnail?d=1508146066)](/attachment/image/2520009?d=1508146066)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#320](/thread/post/10396519#post10396519 "Post Permalink")

  * Oct 17, 2017 6:42am  Oct 17, 2017 6:42am 

  * [ speedyfx](speedyfx)

  * | Joined Jan 2017  | Status: Trader | [3 Posts](/search?do=process&provider=Member&searchuser=545486)

jacques  
if you happen to develop the ea/strategy for jplatform of dukascopy then do share 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Simple High Profit low Drawdown Triangular Arbitrage
  *   * [ **Reply to Thread** ](/thread/676132-simple-high-profit-low-drawdown-triangular-arbitrage/reply#reply)

  * More

[](https://www.forexfactory.com "Homepage")

  * [Forums](forums)
  * [Trades](trades)
  * [Calendar](calendar)
  * [News](news)
  * [Market](market)
  * [Brokers](brokers)

****

[](https://www.faireconomy.com/)

  * 

[Triangular Arbitrage](/thread/64423-triangular-arbitrage "Admin, Please Delete Thread.") 258 replies

[Triangular Arbitrage](/thread/62477-triangular-arbitrage "Is going  
long 1 lot of eur/usd + 
long 1 lot of usd/jpy = long 1 lot of eur/jpy ?  
\(is the ratio of the number of lots correct for a...") 16 replies

[Triangular Arbitrage and carry trade](/thread/71997-triangular-arbitrage-and-carry-trade "Is it possible for us retail traders to be able to make use of Tri Arb or carry trades?  
 
Any one know of retail brokers 
 
 
\(I'm...") 6 replies

[Triangular Arbitrage](/thread/367072-triangular-arbitrage "I've been reading about triangular arbing and was surprised to find that the cross of two majors doesn't always equal what the calculation...") 7 replies

[Question: Trade Mechanics of Triangular Arbitrage](/thread/225246-question-trade-mechanics-of-triangular-arbitrage "Before I even ask this question, please allow me to be very clear.... I have no intention of attempting a triangular arbitrage trade\(for...") 6 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/676132-simple-high-profit-low-drawdown-triangular-arbitrage/reply#reply)
  * Subscribe
  * [147](javascript:void\(0\);)

Attachments: Simple High Profit low Drawdown Triangular Arbitrage

Tags: Simple High Profit low Drawdown Triangular Arbitrage

#  [](/thread/676132-simple-high-profit-low-drawdown-triangular-arbitrage)Simple High Profit low Drawdown Triangular Arbitrage 

  * 

  * [#321](/thread/post/10400147#post10400147 "Post Permalink")

  * Oct 18, 2017 5:49am  Oct 18, 2017 5:49am 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@speedyfx  
I will do so.  
I have developed a couple of test EAs on dukascopy, but not close to converting this EA over yet.  
My idea is eventually to release all versions. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#322](/thread/post/10401739#post10401739 "Post Permalink")

  * Oct 18, 2017 6:56pm  Oct 18, 2017 6:56pm 

  * [ densol](densol)

  * | Joined Jan 2013  | Status: Trader | [52 Posts](/search?do=process&provider=Member&searchuser=322354)

hello can ur ea work on mt4?  
I tried back testing it but result comes nothing 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#323](/thread/post/10402421#post10402421 "Post Permalink")

  * Oct 18, 2017 10:08pm  Oct 18, 2017 10:08pm 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@densol  
Yes it will work on MT4 for forward testing, but not back testing.  
MT4 is not capable of doing multi currency back testing.  
  
If you want to see a back test result then use the MT5 EA on a broker that support MT5.  
  
I suggest MT5 in any case seeing that it executes trades faster than MT4. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#324](/thread/post/10407541#post10407541 "Post Permalink")

  * Oct 20, 2017 12:00am  Oct 20, 2017 12:00am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar457690_1.gif) artico01](artico01)

  * Joined Apr 2016 | Status: Trader | [108 Posts](/search?do=process&provider=Member&searchuser=457690)

@jvbJacques  
I have tested the strategy in MT5 with the configuration discussed in post # 315. These are the results. ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: 2017-10-19 \(4\).png
Size: 64 KB](/attachment/image/2525221/thumbnail?d=1508425146)](/attachment/image/2525221?d=1508425146)   
[![Click to Enlarge

Name: 2017-10-19 \(3\).png
Size: 37 KB](/attachment/image/2525223/thumbnail?d=1508425147)](/attachment/image/2525223?d=1508425147)   
[![Click to Enlarge

Name: 2017-10-19 \(2\).png
Size: 54 KB](/attachment/image/2525225/thumbnail?d=1508425147)](/attachment/image/2525225?d=1508425147)   
[![Click to Enlarge

Name: 2017-10-19 \(1\).png
Size: 176 KB](/attachment/image/2525228/thumbnail?d=1508425148)](/attachment/image/2525228?d=1508425148)   
[![Click to Enlarge

Name: 2017-10-19.png
Size: 164 KB](/attachment/image/2525230/thumbnail?d=1508425149)](/attachment/image/2525230?d=1508425149)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#325](/thread/post/10408128#post10408128 "Post Permalink")

  * Oct 20, 2017 3:28am  Oct 20, 2017 3:28am 

  * [ JRogerFX](jrogerfx)

  * | Joined Oct 2017  | Status: Trader | [4 Posts](/search?do=process&provider=Member&searchuser=617178)

Hi @jvbJacques,  
I was trying to find in previous post but didn't do it. Sorry if already posted. How do you know (or the EA) to enter buy-sell-sell or sell-buy-buy? If you look for trend ... wich pair do you look at? I want to try this theory by my own, maybe with some other pairs too, but is not clear for me how to choose in what direction should the trades be open. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#326](/thread/post/10408235#post10408235 "Post Permalink")

  * Oct 20, 2017 4:25am  Oct 20, 2017 4:25am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar2942_8.gif) Nicholishen](nicholishen)

  * Joined Jul 2005 | Status: zzzzzzzzzzzzzzzzzzzzzzzzz zzzzzzzzzz | [1,261 Posts](/search?do=process&provider=Member&searchuser=2942)

> [Quoting artico01](/thread/post/10407541#post10407541 "View Quoted Post")
> 
> Disliked
> 
> @jvbJacques I have tested the strategy in MT5 with the configuration discussed in post # 315. These are the results. ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1) {image} {image} {image} {image} {image}
> 
> Ignored

These results are false. The reason this is successful in the backtester is because the ticks are fake (interpolated) and/or not synchronized (MT5 tick sync is terrible). You will never get these opportunities IRL, and are arbing the backtester's inefficiency not the market's. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#327](/thread/post/10408424#post10408424 "Post Permalink")

  * Oct 20, 2017 5:54am  Oct 20, 2017 5:54am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar616196_16.gif) OHLC](ohlc)

  * | Joined Oct 2017  | Status: Trader | [498 Posts](/search?do=process&provider=Member&searchuser=616196)

> [Quoting Nicholishen](/thread/post/10408235#post10408235 "View Quoted Post")
> 
> Disliked
> 
> {quote} These results are false. The reason this is successful in the backtester is because the ticks are fake (interpolated) and/or not synchronized (MT5 tick sync is terrible). You will never get these opportunities IRL, and are arbing the backtester's inefficiency not the market's.
> 
> Ignored

It's true guys, don't waste your time with tick data optimizations, etc. At least not for a strategy that you expect to be long lasting. 

Here's Tom with the weather.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#328](/thread/post/10408441#post10408441 "Post Permalink")

  * Oct 20, 2017 6:04am  Oct 20, 2017 6:04am 

  * [ dukas_trader](dukas_trader)

  * | Membership Revoked  | Joined Mar 2010 | [2,525 Posts](/search?do=process&provider=Member&searchuser=136341)

> [Quoting OHLC](/thread/post/10408424#post10408424 "View Quoted Post")
> 
> Disliked
> 
> {quote} It's true guys, don't waste your time with tick data optimizations, etc. At least not for a strategy that you expect to be long lasting.
> 
> Ignored

many tried to help them to show this fact. they will not stop.  
  
even when you tell them that arbitrage experts cant be backtested or traded in demoaccounts for results, they will not believe you. they trade demo and backtest until the end of the world. i really dont understand why some people dont like to learn at least the basics first, and then start programming or trading. some things are impossible by math and in reality, but when not knowing the basics they cant see it. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#329](/thread/post/10408451#post10408451 "Post Permalink")

  * Oct 20, 2017 6:08am  Oct 20, 2017 6:08am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar616196_16.gif) OHLC](ohlc)

  * | Joined Oct 2017  | Status: Trader | [498 Posts](/search?do=process&provider=Member&searchuser=616196)

> [Quoting dukas_trader](/thread/post/10408441#post10408441 "View Quoted Post")
> 
> Disliked
> 
> {quote} many tried to help them to show this fact. they will not stop. even when you tell them that arbitrage experts cant be backtested or traded in demoaccounts for results, they will not believe you. they trade demo and backtest until the end of the world. i really dont understand why some people dont like to learn at least the basics first, and then start programming or trading. some things are impossible by math and in reality, but when not knowing the basics they cant see it.
> 
> Ignored

Traders are very determined and sometimes stubborn people. This is why they'll eventually succeed! It's just a part of the learning process but you're right, they would save themselves a lot of time by listening to more experienced people here. 

Here's Tom with the weather.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#330](/thread/post/10408547#post10408547 "Post Permalink")

  * Edited 7:34am  Oct 20, 2017 7:06am | Edited 7:34am 

  * [ dukas_trader](dukas_trader)

  * | Membership Revoked  | Joined Mar 2010 | [2,525 Posts](/search?do=process&provider=Member&searchuser=136341)

> [Quoting OHLC](/thread/post/10408451#post10408451 "View Quoted Post")
> 
> Disliked
> 
> {quote} Traders are very determined and sometimes stubborn people. This is why they'll eventually succeed! It's just a part of the learning process but you're right, they would save themselves a lot of time by listening to more experienced people here.
> 
> Ignored

you are correct, sometimes its just ok to try and try and thatswhy you can suceed by time or luck. but there are borders for this rule.  
when there are impossible things in reality and against math, its not so smart to hold on this parts. having difficulties to see what is possible to do and not possible to do is most dangerous for wasting time in life. some things need to accept. and by learning basics first, then start programming or trading is best to save time, you can save at least 3-5 years by this. i have never seen only 1 really sucessfull trader without knowing near all basics.  
  
a good trader should always see when he is not correct, because it can cost many money or more difficult even more time. and time is a value you get never back. thatswhy stubborn will be a big problem to need be solved to become a good trader. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#331](/thread/post/10408768#post10408768 "Post Permalink")

  * Oct 20, 2017 9:18am  Oct 20, 2017 9:18am 

  * [ mitcht615](mitcht615)

  * | Joined Oct 2017  | Status: Trader | [3 Posts](/search?do=process&provider=Member&searchuser=620904)

Hi all,  
  
I'm new to this forum but I've been trading for 30+ years. I traded volatility arbitrage in Asia for   
many years for a few banks and prop desks. I know from my own experiences that it became a race for   
the fastest systems. Sometimes paying hundreds of thousands /month for microwave data feeds.  
  
I've read about Triangle arbitrage since 2006. I have a hard time believing that in 2017 something  
like this is still profitable.   
  
I would love to be proven wrong. Is anyone actually making money from this arb who is not part of a large bank etc?  
  
I see the backtested returns......and I've driven down that road too many times........they usually don't don't come close to reality  
  
Can anyone show me real money being made in 2017 doing this? 

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#332](/thread/post/10409989#post10409989 "Post Permalink")

  * Oct 20, 2017 4:38pm  Oct 20, 2017 4:38pm 

  * [ moncsicsi78](moncsicsi78)

  * | Joined Sep 2011  | Status: Trader | [160 Posts](/search?do=process&provider=Member&searchuser=196773)

I have a system similar to the one of this topic.  
E.g.: Eurgbp long  
Eurusd short  
Gbpjpy long  
Usdjpy short   
  
All pairs are traded with the suitable lot size, so the this basket are balanced. Everything (every pairs, and currencies) is hedged.   
  
It is working in demo account. The basket can go to negative , and positive value. I can close the basket in profit.  
  
My only question is: is it working **only on demo** account? (I haven't tried it on live) - Or will it work on live acc. like on demo? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#333](/thread/post/10410560#post10410560 "Post Permalink")

  * Edited 7:28pm  Oct 20, 2017 6:51pm | Edited 7:28pm 

  * [ dukas_trader](dukas_trader)

  * | Membership Revoked  | Joined Mar 2010 | [2,525 Posts](/search?do=process&provider=Member&searchuser=136341)

> [Quoting moncsicsi78](/thread/post/10409989#post10409989 "View Quoted Post")
> 
> Disliked
> 
> I have a system similar to the one of this topic. E.g.: Eurgbp long Eurusd short Gbpjpy long Usdjpy short All pairs are traded with the suitable lot size, so the this basket are balanced. Everything (every pairs, and currencies) is hedged. It is working in demo account. The basket can go to negative , and positive value. I can close the basket in profit. My only question is: is it working only on demo account? (I haven't tried it on live) - Or will it work on live acc. like on demo?
> 
> Ignored

in backtest and demo you will get with all arbitrage systems extrem wins. easy, because you get wins that are not there in reality. most wins are in connection speed and to be faster then all other who do this. with some retail brokers (or even market makers) you will get even the problem to win and get the won money payed out, because any market maker will have your win as 100% loss same time and not one will accept this loss ( or loss values need to be small).  
  
dont waste time with this systems in backtest or demo account, do it with small values in real account or dont do it. then you can judge for your own very fast.  
because noone can know what system you trade (or software used), how many millions you put in in infrastructure or how is your connection to important people to get some advantages , so noone can say you if your system live traded will be winning system. all people can say: dont waste time with arbitrage systems in backtesting or demo trading, always do in real trading. if you judge arbitrage systems with no real account trading, then you can waste your time with many better ways.  
  
so to sum up: do it in real live account or dont say anything about any arbitrage system (because anything what you do in backtest or demo accounts is worthless information and you start to be far from reality and lose time in a dream world). and like always: learning basics step by step first, then start trading or programming (this will save years on time and much money), thats only way you learn whats useless and impossible to do, and whats possible or whats need to be done at first to come to the point that it can be possible.  
  
i can say this also in nice words, but the reality is this hard. if you put time in projects without any chance of sucess, you need to learn at least from this, that you really need to learn now the basics. trading is a hard world, 99% lose money and time for nothing, and 95% of this people only because they dont like to learn basics first ( or at least believe people who did learned it and think about this). people believe that 2+2=4, but that by math its impossible to win with this arbibtrage if you dont invest many money in infrastructure, this the people cant see. but both is same simple calculation and far from any subjective opinion. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#334](/thread/post/10410650#post10410650 "Post Permalink")

  * Oct 20, 2017 7:11pm  Oct 20, 2017 7:11pm 

  * [ mhammede](mhammede)

  * | Commercial User  | Joined Jul 2015 | [426 Posts](/search?do=process&provider=Member&searchuser=420391)

mathematically it should go to win after losing in first of entery, but i don't think it be like this in real live trading because maybe sometimes it will below the account 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#335](/thread/post/10410693#post10410693 "Post Permalink")

  * Oct 20, 2017 7:22pm  Oct 20, 2017 7:22pm 

  * [ moncsicsi78](moncsicsi78)

  * | Joined Sep 2011  | Status: Trader | [160 Posts](/search?do=process&provider=Member&searchuser=196773)

> [Quoting dukas_trader](/thread/post/10410560#post10410560 "View Quoted Post")
> 
> Disliked
> 
> {quote} in backtest and demo you will get with all arbitrage systems extrem wins. easy, because you get wins that are not there in reality. most wins are in connection speed and to be faster then all other who do this. with some retail brokers (or even market makers) you will get even the problem to win and get the won money payed out, because any market maker will have your win as 100% loss same time and not one will accept this loss ( or loss values need to be small). dont waste time with this systems in backtest or demo account, do it with small...
> 
> Ignored

Okay, I see what you would like to say. And I agree.  
Just one last sentence: the showed system (by me, above) is not arbitrage, and not necessary extremly fast connection or any other technical fraud or... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#336](/thread/post/10410719#post10410719 "Post Permalink")

  * Oct 20, 2017 7:26pm  Oct 20, 2017 7:26pm 

  * [ dukas_trader](dukas_trader)

  * | Membership Revoked  | Joined Mar 2010 | [2,525 Posts](/search?do=process&provider=Member&searchuser=136341)

> [Quoting moncsicsi78](/thread/post/10410693#post10410693 "View Quoted Post")
> 
> Disliked
> 
> {quote} Okay, I see what you would like to say. And I agree. Just one last sentence: the showed system (by me, above) is not arbitrage, and not necessary extremly fast connection or any other technical fraud or...
> 
> Ignored

so you dont open all this order at same time? then its no good trading strategy, you could be do much cheaper by different way.  
when you try to open all at same time, you do basket hedge arbitrage. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#337](/thread/post/10410780#post10410780 "Post Permalink")

  * Oct 20, 2017 7:41pm  Oct 20, 2017 7:41pm 

  * [ moncsicsi78](moncsicsi78)

  * | Joined Sep 2011  | Status: Trader | [160 Posts](/search?do=process&provider=Member&searchuser=196773)

> [Quoting dukas_trader](/thread/post/10410719#post10410719 "View Quoted Post")
> 
> Disliked
> 
> {quote} so you dont open all this order at same time? then its no good trading strategy, you could be do much cheaper by different way. when you try to open all at same time, you do basket hedge arbitrage.
> 
> Ignored

Of corse, I opened at the same time. But the fact in itself that we open more order at the same time, is not enough to say it is arbiratge -the brokers' point of view. As I know well... (Maybe I 'm wrong.)  
  
But as you wrote above: don't waste our time and effort on such strategies!  
  
EDIT: sorry, I uploaded a wrong pic before! Now is right. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: hedge.png
Size: 8 KB](/attachment/image/2526509/thumbnail?d=1508496314)](/attachment/image/2526509?d=1508496314)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#338](/thread/post/10410794#post10410794 "Post Permalink")

  * Oct 20, 2017 7:45pm  Oct 20, 2017 7:45pm 

  * [ dukas_trader](dukas_trader)

  * | Membership Revoked  | Joined Mar 2010 | [2,525 Posts](/search?do=process&provider=Member&searchuser=136341)

> [Quoting moncsicsi78](/thread/post/10410780#post10410780 "View Quoted Post")
> 
> Disliked
> 
> {quote} Of corse, I opened at the same time. But the fact in itself that we open more order at the same time, is not enough to say it is arbiratge -the brokers' point of view. As I know well... (Maybe I 'm wrong.) But as you wrote above: don't waste our time and effort on such strategies! {image}
> 
> Ignored

you do then simple basket hedge arbitrage!  
arbitrage is, when you buy 1 value cheaper (ok more expensive would be also negative arbitrage, but noone speaks about this, because its unimportant and noone tries to do) on one place and sell it higher on other place (the place can be other currency pair, other broker, other market, other style of creation ....). exactly that you do. you buy and sell eur, gbp, usd and jpy. you use differnet currency pairs for it, but you do nothing different then buying and selling this eur,gbp, usd,jpy.  
  
by the way, in your picture is 100% no arbitrage! you dont buy at same time, so its simple trading, and even expensive trading, you could do much cheaper buy only buying aud and cad and same time 0,02 euro. so more with because of less costs. or is your connection with this broker so long ,that it needed so much time for open 4 currency pairs (because in 1 second all prices can be total different)? are you using metatrader 4? maybe you should use 4 terminals, that you can open 4 times the order at same time at least, you need to send information to buy to each terminal by pipe and sync all. but metatrader is no good platform to using arbitrage trading. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#339](/thread/post/10410819#post10410819 "Post Permalink")

  * Oct 20, 2017 7:50pm  Oct 20, 2017 7:50pm 

  * [ moncsicsi78](moncsicsi78)

  * | Joined Sep 2011  | Status: Trader | [160 Posts](/search?do=process&provider=Member&searchuser=196773)

> [Quoting dukas_trader](/thread/post/10410794#post10410794 "View Quoted Post")
> 
> Disliked
> 
> {quote} you do then simple basket hedge arbitrage! arbitrage is, when you buy 1 value cheaper (ok more expensive would be also negative arbitrage, but noone speaks about this, because its unimportant and noone tries to do) on one place and sell it higher on other place (the place can be other currency pair, other broker, other market, other style of creation ....). exactly that you do. you buy and sell eur, gbp, usd and jpy. you use differnet currency pairs for it, but you do nothing different then buying and selling this eur,gbp, usd,jpy.
> 
> Ignored

Thanks!  
  
I will ask from brokers that this kind of strategy is acceptable or not, prohibited or not by terms and conditions of the company. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#340](/thread/post/10410852#post10410852 "Post Permalink")

  * Oct 20, 2017 8:00pm  Oct 20, 2017 8:00pm 

  * [ moncsicsi78](moncsicsi78)

  * | Joined Sep 2011  | Status: Trader | [160 Posts](/search?do=process&provider=Member&searchuser=196773)

> [Quoting dukas_trader](/thread/post/10410794#post10410794 "View Quoted Post")
> 
> Disliked
> 
> ...by the way, in your picture is 100% no arbitrage! you dont buy at same time, so its simple trading, and even expensive trading, you could do much cheaper buy only buying aud and cad and same time 0,02 euro. so more with because of less costs. or is your connection with this broker so long ,that it needed so much time for open 4 currency pairs (because in 1 second all prices can be total different)? are you using metatrader 4? maybe you should use 4 terminals, that you can open 4 times the order at same time at least, you need to send information...
> 
> Ignored

The most important: I don't want to trade arbitrage or any other prohibited way! I never mind the connection time to the brokers' server - it is not important so much. (Okay, don't be so looooong, but normal/average connection time is enough.)My goal is to trade by the way is acceptable by any broker's terms and conditions.  
  
I will ask them about this type of strategy. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Simple High Profit low Drawdown Triangular Arbitrage
  *   * [ **Reply to Thread** ](/thread/676132-simple-high-profit-low-drawdown-triangular-arbitrage/reply#reply)

  * More

[](https://www.forexfactory.com "Homepage")

  * [Forums](forums)
  * [Trades](trades)
  * [Calendar](calendar)
  * [News](news)
  * [Market](market)
  * [Brokers](brokers)

****

[](https://www.faireconomy.com/)

  * 

[Triangular Arbitrage](/thread/64423-triangular-arbitrage "Admin, Please Delete Thread.") 258 replies

[Triangular Arbitrage](/thread/62477-triangular-arbitrage "Is going  
long 1 lot of eur/usd + 
long 1 lot of usd/jpy = long 1 lot of eur/jpy ?  
\(is the ratio of the number of lots correct for a...") 16 replies

[Triangular Arbitrage and carry trade](/thread/71997-triangular-arbitrage-and-carry-trade "Is it possible for us retail traders to be able to make use of Tri Arb or carry trades?  
 
Any one know of retail brokers 
 
 
\(I'm...") 6 replies

[Triangular Arbitrage](/thread/367072-triangular-arbitrage "I've been reading about triangular arbing and was surprised to find that the cross of two majors doesn't always equal what the calculation...") 7 replies

[Question: Trade Mechanics of Triangular Arbitrage](/thread/225246-question-trade-mechanics-of-triangular-arbitrage "Before I even ask this question, please allow me to be very clear.... I have no intention of attempting a triangular arbitrage trade\(for...") 6 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/676132-simple-high-profit-low-drawdown-triangular-arbitrage/reply#reply)
  * Subscribe
  * [147](javascript:void\(0\);)

Attachments: Simple High Profit low Drawdown Triangular Arbitrage

Tags: Simple High Profit low Drawdown Triangular Arbitrage

#  [](/thread/676132-simple-high-profit-low-drawdown-triangular-arbitrage)Simple High Profit low Drawdown Triangular Arbitrage 

  * 

  * [#341](/thread/post/10410941#post10410941 "Post Permalink")

  * Oct 20, 2017 8:18pm  Oct 20, 2017 8:18pm 

  * [ dukas_trader](dukas_trader)

  * | Membership Revoked  | Joined Mar 2010 | [2,525 Posts](/search?do=process&provider=Member&searchuser=136341)

> [Quoting moncsicsi78](/thread/post/10410852#post10410852 "View Quoted Post")
> 
> Disliked
> 
> {quote} The most important: I don't want to trade arbitrage or any other prohibited way! I never mind the connection time to the brokers' server - it is not important so much. (Okay, don't be so looooong, but normal/average connection time is enough.)My goal is to trade by the way is acceptable by any broker's terms and conditions. I will ask them about this type of strategy.
> 
> Ignored

depends on the broker. when you are with high wins and with a pure marketmaker you will get problems by whatever trading style you do. because any of your wins is your brokers loss (minus the spread and commission). when he lose to much on you, you will get kicked out or get connection problems to let you lose more often.  
  
when you dont use a pure marketmaker broker, you can trade all trading styles. only arbitrage is special. when they have slower datafeed they make with all your wins as their losses and you get problems by pay money out. thatswhy for arbitrage you use normally big liquity providers direct connections and splitted with different liquity providers, so can arbitrage between this and dont have the risk the money will not be payed by broker. arbitrage is more a infrastructure game, the software to do is easy and smallest unimportanst part of this game.  
  
you basket hedge arbitrage should be no problem with the broker, because all is done so slow, only market makers with problems in price feed will get problems when you would have wins and so they lose by it. simple test with your broker with very small amounts. there are many more complicated arbitrage ways, so this very basic easy way is normally no problem for a broker, but normally also no big wins possible (with this long time to execute trades). 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#342](/thread/post/10410956#post10410956 "Post Permalink")

  * Oct 20, 2017 8:23pm  Oct 20, 2017 8:23pm 

  * [ densol](densol)

  * | Joined Jan 2013  | Status: Trader | [52 Posts](/search?do=process&provider=Member&searchuser=322354)

why cant I backtest this? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#343](/thread/post/10411002#post10411002 "Post Permalink")

  * Oct 20, 2017 8:35pm  Oct 20, 2017 8:35pm 

  * [ moncsicsi78](moncsicsi78)

  * | Joined Sep 2011  | Status: Trader | [160 Posts](/search?do=process&provider=Member&searchuser=196773)

> [Quoting dukas_trader](/thread/post/10410941#post10410941 "View Quoted Post")
> 
> Disliked
> 
> ...there are many more complicated arbitrage ways, so this very basic easy way is normally no problem for a broker, but normally also no big wins possible (with this long time to execute trades).
> 
> Ignored

Big wins is not possible without big risk.  
My system maybe has no big potential profit, but there is no big risk, too. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: hedge.png
Size: 8 KB](/attachment/image/2526590/thumbnail?d=1508499505)](/attachment/image/2526590?d=1508499505)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#344](/thread/post/10411009#post10411009 "Post Permalink")

  * Oct 20, 2017 8:38pm  Oct 20, 2017 8:38pm 

  * [ dukas_trader](dukas_trader)

  * | Membership Revoked  | Joined Mar 2010 | [2,525 Posts](/search?do=process&provider=Member&searchuser=136341)

> [Quoting moncsicsi78](/thread/post/10411002#post10411002 "View Quoted Post")
> 
> Disliked
> 
> {quote} Big wins is not possible without big risk. My system maybe has no big potential profit, but there is no big risk, too.
> 
> Ignored

arbitrage has the goal to have all risk putted on side of the broker. thatswhy you think you have no big risk ofcourse. when you have fast connection and very good infrastructure its true. but what happens when you dont get one of the 4 hedge trades because of offquotes .... there are more risks you can imagine and all need to be planed inside. and the broker dont will allow to have the risk all the time in your trades. they are not stupid. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#345](/thread/post/10411029#post10411029 "Post Permalink")

  * Oct 20, 2017 8:43pm  Oct 20, 2017 8:43pm 

  * [ moncsicsi78](moncsicsi78)

  * | Joined Sep 2011  | Status: Trader | [160 Posts](/search?do=process&provider=Member&searchuser=196773)

> [Quoting dukas_trader](/thread/post/10411009#post10411009 "View Quoted Post")
> 
> Disliked
> 
> {quote} arbitrage has the goal to have all risk putted on side of the broker. thatswhy you think you have no big risk ofcourse. when you have fast connection and very good infrastructure its true. but what happens when you dont get one of the 4 hedge trades because of offquotes .... there are more risks you can imagine and all need to be planed inside. and the broker dont will allow to have the risk all the time in your trades. they are not stupid.
> 
> Ignored

Maybe I was equivocal: I DON'T want to trade arbitrage and any other prohibited way of trading.  
And I also have risk, as I wrote - just it will be tolerable for me, I think.  
  
Offquotes, requotes can cause problems, of course.  
I should have to search for a broker who minimalize these... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#346](/thread/post/10413174#post10413174 "Post Permalink")

  * Oct 21, 2017 1:31pm  Oct 21, 2017 1:31pm 

  * [ nantong](nantong)

  * | Joined Oct 2017  | Status: Trader | [17 Posts](/search?do=process&provider=Member&searchuser=621135)

> [Quoting eatrader75](/thread/post/10366216#post10366216 "View Quoted Post")
> 
> Disliked
> 
> raffus, If you talking about the hedging 3 pseudo renko EA please check the following thread: <https://www.forexfactory.com/showthread.php?t=335072> Also please read again the #Post 295 on this page
> 
> Ignored

just for test only!  
attach [OPEN_EURGBPJPY.mq4](https://www.forexfactory.com/attachment.php?attachmentid=2527516&stc=1&d=1508559389) to eurgbp,gbpjpy,eurjpy renko chart,with 9 10 9 boxsize,  
attach [OPEN_EURGBPUSD.mq4](https://www.forexfactory.com/attachment.php?attachmentid=2527518&stc=1&d=1508559390) to eurgbp,gbpusd,eurusd renko chart,with 9 10 9 boxsize,  
attach [OPEN_EURUSDJPY.mq4](https://www.forexfactory.com/attachment.php?attachmentid=2527521&stc=1&d=1508559390) to eurusd,usdjpy,eurjpy renko chart,with 6 5 6 boxsize,  
attach close ea to any chart  
open lot=accountbalance/100000  
close orders=when any buy buy sell or sell sell buy or all profit >accountbalance*0.01+orderlot()*7 

Attached File(s)

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [CLOSE.mq4](/attachment/file/2527513?d=1508559387) 13 KB | 438 downloads 

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [OPEN_EURGBPJPY.mq4](/attachment/file/2527516?d=1508559388) 2 KB | 658 downloads 

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [OPEN_EURGBPUSD.mq4](/attachment/file/2527518?d=1508559388) 2 KB | 646 downloads 

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [OPEN_EURUSDJPY.mq4](/attachment/file/2527521?d=1508559389) 2 KB | 649 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#347](/thread/post/10413538#post10413538 "Post Permalink")

  * Oct 21, 2017 7:39pm  Oct 21, 2017 7:39pm 

  * [ eatrader75](eatrader75)

  * | Joined Aug 2017  | Status: Trader | [28 Posts](/search?do=process&provider=Member&searchuser=605097)

> [Quoting nantong](/thread/post/10413174#post10413174 "View Quoted Post")
> 
> Disliked
> 
> {quote} just for test only!
> 
> Ignored

Hi nantong,  
  
I might have to think about to open a new thread with jeuro's concept.  
  
But for now, could you please tell me more about your test?  
  
Thanks 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#348](/thread/post/10414275#post10414275 "Post Permalink")

  * Oct 22, 2017 7:46am  Oct 22, 2017 7:46am 

  * [ nantong](nantong)

  * | Joined Oct 2017  | Status: Trader | [17 Posts](/search?do=process&provider=Member&searchuser=621135)

> [Quoting eatrader75](/thread/post/10413538#post10413538 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi nantong, I might have to think about to open a new thread with jeuro's concept. But for now, could you please tell me more about your test? Thanks
> 
> Ignored

So far I didn't forward test enough time,as I can see,when trend goes up and down,the lots opened will increase very far if you had small boxsize,but they are partly hedged,and the drawdown is not that much with the lots opened.I think as time goes,opened lots will go between unbalanced and balanced,because we buy buy sell and sell sell buy at almost hedged distance when the price of EURUSD AND EURGBP do not goes that far,the boxsize will not change for a long time.When the lots increase enough,the little trend move will result in profit or drawdown,which is unknown. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#349](/thread/post/10416368#post10416368 "Post Permalink")

  * Oct 23, 2017 5:01pm  Oct 23, 2017 5:01pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar16703_6.gif) Me@Home](member.php?u=16703)

  * | Joined Aug 2006  | Status: Trader | [49 Posts](/search?do=process&provider=Member&searchuser=16703)

> [Quoting moncsicsi78](/thread/post/10411002#post10411002 "View Quoted Post")
> 
> Disliked
> 
> {quote} Big wins is not possible without big risk. My system maybe has no big potential profit, but there is no big risk, too. {image}
> 
> Ignored

Hi moncsicsi78, can you talk more about your system... as I see is a quadrangular hedging system.. right? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#350](/thread/post/10416461#post10416461 "Post Permalink")

  * Oct 23, 2017 5:47pm  Oct 23, 2017 5:47pm 

  * [ moncsicsi78](moncsicsi78)

  * | Joined Sep 2011  | Status: Trader | [160 Posts](/search?do=process&provider=Member&searchuser=196773)

> [Quoting Me@Home](/thread/post/10416368#post10416368 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi moncsicsi78, can you talk more about your system... as I see is a quadrangular hedging system.. right?
> 
> Ignored

Nothing special... as ypou wrote, it is a 4th hedge. Every pairs and currencies in the basket are balanced - almost balanced. I am trying to trade it with balanced lot sizes and equal lot sizes, too - I am just observing which way is better.  
If the basket goes wrong, I use grid: take all 4 orders again.   
Usually it is enough to take 1 or 2 other grid trade to close all them in profit. Most of the time (if the first basket was opened in the right conditions) it is enough to take only one basket/order to close all in profit.  
  
It is not an arbitrage system. Not necessary any special technical conditions (fast PC, internet connection, etc.)  
It has a risk. But limited - and of course, limited profit.   
It is good for ME because of its psychological aspects. ..and that's why it is very subjective.  
  
But I don't want to spam this topic, so sorry jvbJacques!   
My theme is closed. 

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#351](/thread/post/10416622#post10416622 "Post Permalink")

  * Oct 23, 2017 7:01pm  Oct 23, 2017 7:01pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar16703_6.gif) Me@Home](member.php?u=16703)

  * | Joined Aug 2006  | Status: Trader | [49 Posts](/search?do=process&provider=Member&searchuser=16703)

> [Quoting moncsicsi78](/thread/post/10416461#post10416461 "View Quoted Post")
> 
> Disliked
> 
> {quote} But I don't want to spam this topic, so sorry jvbJacques! My theme is closed.
> 
> Ignored

Thank you for this punctualization.... If you open a specific 3d I'll follow 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#352](/thread/post/10416642#post10416642 "Post Permalink")

  * Oct 23, 2017 7:12pm  Oct 23, 2017 7:12pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar438576_2.gif) raffus](raffus)

  * | Joined Dec 2015  | Status: Member RFP | [57 Posts](/search?do=process&provider=Member&searchuser=438576)

> [Quoting nantong](/thread/post/10413174#post10413174 "View Quoted Post")
> 
> Disliked
> 
> {quote} just for test only! attach [OPEN_EURGBPJPY.mq4](https://www.forexfactory.com/attachment.php?attachmentid=2527516&stc=1&d=1508559389) to eurgbp,gbpjpy,eurjpy renko chart,with 9 10 9 boxsize, attach [OPEN_EURGBPUSD.mq4](https://www.forexfactory.com/attachment.php?attachmentid=2527518&stc=1&d=1508559390) to eurgbp,gbpusd,eurusd renko chart,with 9 10 9 boxsize, attach [OPEN_EURUSDJPY.mq4](https://www.forexfactory.com/attachment.php?attachmentid=2527521&stc=1&d=1508559390) to eurusd,usdjpy,eurjpy renko chart,with...
> 
> Ignored

Sorry  
How can i open Renko chart?  
Also. May i compile your mq4 files in order to have ex4 files?  
  
Thanks a lot 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#353](/thread/post/10416757#post10416757 "Post Permalink")

  * Oct 23, 2017 8:26pm  Oct 23, 2017 8:26pm 

  * [ nantong](nantong)

  * | Joined Oct 2017  | Status: Trader | [17 Posts](/search?do=process&provider=Member&searchuser=621135)

> [Quoting raffus](/thread/post/10416642#post10416642 "View Quoted Post")
> 
> Disliked
> 
> {quote} Sorry How can i open Renko chart? Also. May i compile your mq4 files in order to have ex4 files? Thanks a lot
> 
> Ignored

Here is the file that can make renko chart you can find everywhere.Just attach it to 1m chart and select proper boxsize and timeframe(usually is m2,and if there is two same symbol,and second symbol you have to select m3 or else),and open offline from menu,that's it.Yes,you can compile. 

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [RenkoLiveChart_v3.4.ex4](/attachment/file/2529100?d=1508757596) 12 KB | 386 downloads 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#354](/thread/post/10416842#post10416842 "Post Permalink")

  * Oct 23, 2017 8:56pm  Oct 23, 2017 8:56pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar438576_2.gif) raffus](raffus)

  * | Joined Dec 2015  | Status: Member RFP | [57 Posts](/search?do=process&provider=Member&searchuser=438576)

> [Quoting Me@Home](/thread/post/10416622#post10416622 "View Quoted Post")
> 
> Disliked
> 
> {quote} Thank you for this punctualization.... If you open a specific 3d I'll follow
> 
> Ignored

  
me too! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#355](/thread/post/10416987#post10416987 "Post Permalink")

  * Oct 23, 2017 9:57pm  Oct 23, 2017 9:57pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar471664_3.gif) pandey](pandey)

  * | Membership Revoked  | Joined Jun 2016 | [62 Posts](/search?do=process&provider=Member&searchuser=471664)

is this EA have any restrictions ? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#356](/thread/post/10417197#post10417197 "Post Permalink")

  * Oct 23, 2017 11:05pm  Oct 23, 2017 11:05pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar16703_6.gif) Me@Home](member.php?u=16703)

  * | Joined Aug 2006  | Status: Trader | [49 Posts](/search?do=process&provider=Member&searchuser=16703)

Forward Test none happens ('till past friday)  
  
I attach here the today's log file...  

Inserted Code
    
    
    0 08:10:16.170 Expert Arbitrage\2017-09-18 09h00 JVB Arbitrage Auto Profit19 GBPUSD,M1: loaded successfully
    0 08:10:16.170 2017-09-18 09h00 JVB Arbitrage Auto Profit19 GBPUSD,M1 inputs: fxName1=GBPJPY; fxName2=GBPUSD; fxName3=USDJPY;
    0 08:10:19.436 2017-09-18 09h00 JVB Arbitrage Auto Profit19 GBPUSD,M1: jvbFuncOnInit=sym=GBPUSD TESTING=0
    0 08:10:19.436 2017-09-18 09h00 JVB Arbitrage Auto Profit19 GBPUSD,M1: Spies ok, waiting for events...
    0 08:10:19.436 2017-09-18 09h00 JVB Arbitrage Auto Profit19 GBPUSD,M1: **** INIT=AccountLeverage=500 true=1 false=0 marginPerMlot=0 acountDecrease=0 ticketProfitStart1000Lots=100
    0 08:10:19.436 2017-09-18 09h00 JVB Arbitrage Auto Profit19 GBPUSD,M1: initialized
    0 08:10:19.553 2017-09-18 09h00 JVB Arbitrage Auto Profit19 GBPUSD,M1: *** run() TimedLog1
    0 08:10:19.553 2017-09-18 09h00 JVB Arbitrage Auto Profit19 GBPUSD,M1: *****=maxDrawDown3=0 maxMargin=0 minMarginFreePers=1.5 dte=1508749833 maxAccountBalance=50 ERROR=
    0 08:10:19.553 2017-09-18 09h00 JVB Arbitrage Auto Profit19 GBPUSD,M1: setCommission=OrdersTotal=0
    0 08:10:19.553 2017-09-18 09h00 JVB Arbitrage Auto Profit19 GBPUSD,M1: setCommission=openTrade
    0 08:10:19.553 2017-09-18 09h00 JVB Arbitrage Auto Profit19 GBPUSD,M1: openTrade() in_IsBuy=1 newLotSize=0.01 in_LotSize=0 in_FxName=GBPUSD
    2 08:10:19.704 2017-09-18 09h00 JVB Arbitrage Auto Profit19 GBPUSD,M1: open #81913724 buy 0.01 GBPUSD at 1.32191 ok
    0 08:10:19.704 2017-09-18 09h00 JVB Arbitrage Auto Profit19 GBPUSD,M1: openTrade() rtOpen=1 in_IsBuy=1 lotSize=0.01 in_LotSize=0.01 in_FxName=GBPUSD
    2 08:10:22.876 2017-09-18 09h00 JVB Arbitrage Auto Profit19 GBPUSD,M1: close #81913724 buy 0.01 GBPUSD at 1.32191 at price 1.32177
    0 08:10:22.876 2017-09-18 09h00 JVB Arbitrage Auto Profit19 GBPUSD,M1: setCommission=OrdersTotal=1
    0 08:10:22.876 2017-09-18 09h00 JVB Arbitrage Auto Profit19 GBPUSD,M1: cc2= 0 deal_ticket=81913724 Symbol=GBPUSD Lots=0.01 Commission=0.00000000 commisionPerMLot=0
    0 08:10:22.876 2017-09-18 09h00 JVB Arbitrage Auto Profit19 GBPUSD,M1: setCommission-DONE commisionPerMLot=-0
    0 08:10:22.876 2017-09-18 09h00 JVB Arbitrage Auto Profit19 GBPUSD,M1: *****=maxDrawDown3=0 maxMargin=0 minMarginFreePers=1.4972 dte=1508749838 maxAccountBalance=50 ERROR=
    0 08:10:22.958 2017-09-18 09h00 JVB Arbitrage Auto Profit19 GBPUSD,M1: run()=drawline_fxValue1=150.259 drawline_fxValue2=1.3219 drawline_fxValue3=113.642
    0 08:10:22.958 2017-09-18 09h00 JVB Arbitrage Auto Profit19 GBPUSD,M1: drawLineAvgReset()=drawLine_PriceBase=1.32203

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#357](/thread/post/10423726#post10423726 "Post Permalink")

  * Oct 25, 2017 5:09pm  Oct 25, 2017 5:09pm 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@moncsicsi78  
Sounds very interesting and no need to stop posting.  
If it works then continue.  
You will not know until you test it over a period of time.  
  
  
  
@EVERYONE  
I am back, but only for a few seconds.  
I can see the conversations are heating up ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
  
I made a lot of enhancements, but all is hanging in the air as I ran out of free development time and I have to focus on my paying work or lose the very thing I need to do development with.  
So I will not be able to do many or any updates for a long time until I get time off again.  
  
But I will be back and I will finish this project when I get time again.  
  
Just keep in mind that the EA 19 is unstable as explained before, but useful to test the theory with.  
Enjoy testing.  
  
O and one of the updates that shows extremely good results are a semi unbalanced triangle.  
A bit bigger draw-down, but massive improved profits.  
To counter the draw-down the lot size need to decrease, meaning the profit drops to about the level of the current balanced triangle system.  
The advantage of the unbalanced system is that the movements are big enough that you can almost ignore spread and slippage seeing that the profit is big enough to go way past it, where a balanced triangle are extremely susceptible to slippage.  
You even get spike-less trends in the unbalanced one, that also show some trading opportunities in that unlike a normal trend you can follow it without the fear of a sudden reversal like normal trading, but that is something for another day.  
  
I actually got my hand on a account, which is trading the unbalanced system to some degree on a live account with great success, but I can not get hold of the EA or the developer, but I have already reverse engineered it and just have to put it into code to test it myself and maybe add some of my own code for profit on profit growth. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#358](/thread/post/10424455#post10424455 "Post Permalink")

  * Oct 25, 2017 8:01pm  Oct 25, 2017 8:01pm 

  * [ dukas_trader](dukas_trader)

  * | Membership Revoked  | Joined Mar 2010 | [2,525 Posts](/search?do=process&provider=Member&searchuser=136341)

> [Quoting jvbJacques](/thread/post/10423726#post10423726 "View Quoted Post")
> 
> Disliked
> 
> I actually got my hand on a account, which is trading the unbalanced system to some degree on a live account with great success, but I can not get hold of the EA or the developer, but I have already reverse engineered it and just have to put it into code to test it myself and maybe add some of my own code for profit on profit growth.
> 
> Ignored

just to help you, unbalanced trading is much more cheaper, when you simple open the unbalanced part. just normal trading.  
when your "got my hand on a account, which is trading the unbalanced system to some degree on a live account with great success" , then this account is always from a total beginner. and why you would like to copy a beginner? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#359](/thread/post/10424516#post10424516 "Post Permalink")

  * Oct 25, 2017 8:12pm  Oct 25, 2017 8:12pm 

  * [ nantong](nantong)

  * | Joined Oct 2017  | Status: Trader | [17 Posts](/search?do=process&provider=Member&searchuser=621135)

No risk no profit,unbalanced system contain risk,where the profit come from,so don't be afraid of risk,you need to control it not to avoid it.To control risk you can control your open lots. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#360](/thread/post/10424539#post10424539 "Post Permalink")

  * Oct 25, 2017 8:18pm  Oct 25, 2017 8:18pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar373412_1.gif) vanillanont](vanillanont)

  * | Joined May 2014  | Status: Trader | [2 Posts](/search?do=process&provider=Member&searchuser=373412)

Hello, I'm interesting to your EAs but, Can I ask some question ?  
  
How do you calculate ASK and BUY line with average ? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Simple High Profit low Drawdown Triangular Arbitrage
  *   * [ **Reply to Thread** ](/thread/676132-simple-high-profit-low-drawdown-triangular-arbitrage/reply#reply)

  * More

[](https://www.forexfactory.com "Homepage")

  * [Forums](forums)
  * [Trades](trades)
  * [Calendar](calendar)
  * [News](news)
  * [Market](market)
  * [Brokers](brokers)

****

[](https://www.faireconomy.com/)

  * 

[Triangular Arbitrage](/thread/64423-triangular-arbitrage "Admin, Please Delete Thread.") 258 replies

[Triangular Arbitrage](/thread/62477-triangular-arbitrage "Is going  
long 1 lot of eur/usd + 
long 1 lot of usd/jpy = long 1 lot of eur/jpy ?  
\(is the ratio of the number of lots correct for a...") 16 replies

[Triangular Arbitrage and carry trade](/thread/71997-triangular-arbitrage-and-carry-trade "Is it possible for us retail traders to be able to make use of Tri Arb or carry trades?  
 
Any one know of retail brokers 
 
 
\(I'm...") 6 replies

[Triangular Arbitrage](/thread/367072-triangular-arbitrage "I've been reading about triangular arbing and was surprised to find that the cross of two majors doesn't always equal what the calculation...") 7 replies

[Question: Trade Mechanics of Triangular Arbitrage](/thread/225246-question-trade-mechanics-of-triangular-arbitrage "Before I even ask this question, please allow me to be very clear.... I have no intention of attempting a triangular arbitrage trade\(for...") 6 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/676132-simple-high-profit-low-drawdown-triangular-arbitrage/reply#reply)
  * Subscribe
  * [147](javascript:void\(0\);)

Attachments: Simple High Profit low Drawdown Triangular Arbitrage

Tags: Simple High Profit low Drawdown Triangular Arbitrage

#  [](/thread/676132-simple-high-profit-low-drawdown-triangular-arbitrage)Simple High Profit low Drawdown Triangular Arbitrage 

  * 

  * [#361](/thread/post/10424670#post10424670 "Post Permalink")

  * Oct 25, 2017 8:41pm  Oct 25, 2017 8:41pm 

  * [ dukas_trader](dukas_trader)

  * | Membership Revoked  | Joined Mar 2010 | [2,525 Posts](/search?do=process&provider=Member&searchuser=136341)

> [Quoting nantong](/thread/post/10424516#post10424516 "View Quoted Post")
> 
> Disliked
> 
> No risk no profit,unbalanced system contain risk,where the profit come from,so don't be afraid of risk,you need to control it not to avoid it.To control risk you can control your open lots.
> 
> Ignored

this is simple just normal trading. so has nothing to do with arbitrage trading any more. and that normal trading is of course possible with good wins. but how jvbjacques described it, its "stupiest" most expensive way to open such positions, so he looks to the trade of total beginners and cant see it. and its important to help him so that at least he comes to a level to judge, what he sees. or you will lose years, its like with his arbitrage, he dont want to learn basics and thats why lose this many time with things, who cant win.  
in same time he could invent a really winning system just with normal trading.  
  
in trading , you need to learn basics and you need to see, when you are wrong. if you cant see and judge things correct, even after many long term traders help you with mistakes, its a near 100% chance you will no get it to a good level in trading. first important thing is being objective, always. the market dont care for subjective. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#362](/thread/post/10425839#post10425839 "Post Permalink")

  * Oct 26, 2017 12:12am  Oct 26, 2017 12:12am 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@dukas_trader  
Welcome back ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
I missed you ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
  
You are correct in that I am stupid when it comes to forex, but that is why I am doing this to learn.  
I have been doing forex for 10 years on and off and programming for 33 years, but I learned more in the last few months about forex than in the whole of my 10 forex years.  
Heck I even leaned both MT4 and MT5 code and in 3 days I learned Jtrader.  
What fun.  
  
I just thought that why must I learn alone and why not share what I learn and this thread is where I do it and WOW the response from most everyone was fantastic.  
  
In my 10 years I have written way more than 700 EAs, but none showed the potential of this arbitrage.  
  
As for unbalanced arbitrage not being arbitrage but normal trading THEN I can also say balanced arbitrage is also normal trading.  
Normal trading covers a wide range of trading strategies and this is what these are.  
Unbalanced is still arbitrage, but where one of the legs are not as well balanced as the others, but still creates a cushion against sharp movement, without completely removing trends and other potential profit situations.  
Technically it is impossible to get a perfect triangular arbitrage mathematically, but we can get close ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
The bigger the spread and slippage the more unbalanced the arbitrage must be to make up for it and @NANTONG is correct in that with NO RISK there is NO PROFIT, but this at least limits the risk.  
  
As for the EA I saw running the live account being a beginner for running profitable arbitrage for about 2 years or me for learning from what she did.  
Then yes.  
If that is how beginners do things then I am a noob, but that does not bother me in the least as I am enjoying the trip ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
Plus if I can make money like that noob then all noobs unite ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
  
I take in what everyone is saying, good or bad and learn from all.  
I still have not reached the point where I can say for certain this is profitable or non profitable, but it looks good and it is FAR from a waste of time from everything I have learned so far ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
  
If you have to discourage someone from trying something new like this then discourage me, but leave other people out of it please ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
I can take it and best of all I agree with a lot of your points, but I am not one to give up on something before I can prove it without a shadow of a doubt that it will not work and I am not there yet.  
  
And why do you think it is so expensive ?  
Yes it is 3 trades, but you pay about the same price in spread as one trade that is 3 times the size.  
Same rules as in "normal" trading applies to lot growth and trading according to a % of your account size.  
  
I would love to know what strategy you are using.  
I know the basics and I also know the basics alone will not make profit for you so you must have some sort of golden strategy.  
Please share as I have seem some wonderful strategies that was PMed to me that I would love to look into one day and yours could be one of them.  
I am sure you have something good you can share please.  
  
In any case.  
Enjoy ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
  
  
  
  
@VANILLANONT  
I basically do the following for the 3 symbols.  
1) I capture the current starting (1) ASK, (2) BID, (2) BID.  
  
2) WHITE LINE  
After every price movement I then do a triangular calculation using the starting prices in point (1) against and the current ASK, BID, BID and then calculate the amount of profit I would have had at that point.  
The line is the profit at that point.  
  
3) RED LINE  
After every price movement I then do a triangular calculation using the starting prices in point (1) against and the current BID, ASK, ASK and then calculate the amount of profit I would have had at that point.  
The line is the profit at that point.  
  
4) So basically the 2 lines are the same, with a spread in-between.  
I also add commission to the WHITE line to make sure I take that also into account.  
  
5) I then calculate the average between the lines over time and use that originally as the entry and exit points, but EA 19 is not doing that properly.  
Still to do is to recalculate everything after every trade open to get the new exit point seeing that with slippage the exit point and the WHITE/RED lines must move to accommodate the new starting slipped price, which is not a big thing, but takes time.  
  
  
  
@EVERYONE  
Well.  
Time to go for a bit.  
Enjoy.  
If you guys get a break-thru then please share.  
I will be checking in from time to time.  
  
And for those thinking that there question is too stupid to ask or their strategy does not belong here.  
I say bull twang.  
The only stupid question is no question at all.  
I have found that I learn the most from NOOBS, because they are not poisoned by others into believing that everything must work this way and not that way and this way I can start to think outside the box with them.  
  
I have had many students that have taught my great skills from thing I would never have guessed is relevant.  
Go mad and enjoy. 

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#363](/thread/post/10426093#post10426093 "Post Permalink")

  * Edited 8:08pm  Oct 26, 2017 12:51am | Edited 8:08pm 

  * [ dukas_trader](dukas_trader)

  * | Membership Revoked  | Joined Mar 2010 | [2,525 Posts](/search?do=process&provider=Member&searchuser=136341)

> [Quoting jvbJacques](/thread/post/10425839#post10425839 "View Quoted Post")
> 
> Disliked
> 
> @dukas_trader Welcome back ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1) I missed you ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1) You are correct in that I am stupid when it comes to forex, but that is why I am doing this to learn. I have been doing forex for 10 years on and off and programming for 33 years, but I learned more in the last few months about forex than in the whole of my 10 forex years. Heck I even leaned both MT4 and MT5 code and in 3 days I learned Jtrader. What fun. I just thought that why must I learn alone and why not share what I learn and this thread is where I do it and WOW the response from...
> 
> Ignored

i dont say you are stupid, just wasting a lot of time often with impossible things.  
  
of course arbitrage is a part of trading, but very special. most arbitrage systems in mt4 only try to let the broker pay for your wins, so the brokers had then the problem with the orders that was with wrong prices quoted, that are not so in the market. but anyway, lets say yes, its one kind of trading.  
  
to your point : "And why do you think it is so expensive ?  
Yes it is 3 trades, but you pay about the same price in spread as one trade that is 3 times the size.  
Same rules as in "normal" trading applies to lot growth and trading according to a % of your account size.  
"  
you pay much more spread in 3 currencies trading, then simple trade in one! plus commision, plus maybe rollover.  
and you have much less margin use and trading because you can tade with much smaller values exactly the same. you need to pain it on paper or do some example calculations. thats important points you need to know.  
  
when you know the basics , thats very good. but i have never seen one who knows the basics and then dont simple create working strategies. knowing the basics there is one part inside, how to find, develop, fair backtest , program and trade tradingsystems. learning the basics is not only learning some parts, you need to learn all basics. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#364](/thread/post/10428729#post10428729 "Post Permalink")

  * Oct 26, 2017 6:05pm  Oct 26, 2017 6:05pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar402047_21.gif) Fxentropy](fxentropy)

  * Joined Feb 2015 | Status: Who Dares Wins | [1,710 Posts](/search?do=process&provider=Member&searchuser=402047)

> [Quoting jvbJacques](/thread/post/10425839#post10425839 "View Quoted Post")
> 
> Disliked
> 
> @dukas_trader Welcome back ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1) I missed you ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)**I would love to know what strategy you are using**. I know the basics and I also know the basics alone will not make profit for you so you must have some sort of golden strategy. Please share as I have seem some wonderful strategies that was PMed to me that I would love to look into one day and yours could be one of them. I am sure you have something good you can share please. In any case. Enjoy ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)
> 
> Ignored

> [Quoting jvbJacques](/thread/post/10425839#post10425839 "View Quoted Post")
> 
> Disliked
> 
> If you have to discourage someone from trying something new like this then discourage me, but leave other people out of it please ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)
> 
> Ignored

Love the fine and smart answer here. But i think you ask too much, he will never ever show you anything as he never traded for real, he is just a talker.  
  
Geting back to topic, would you think that taking trades near S/R and here depend on how we define this S/R- either as last swing high/low, either classic ones, either NY Close level etc would improuve anything? I mean to add as 'filter' this condition, to trigger as per se + S/R. Ofcourse, all getting down to GBPUSD levels.  
  
thanks 

"What would you attempt to do, if you knew your success was a certainty?"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#365](/thread/post/10429246#post10429246 "Post Permalink")

  * Oct 26, 2017 8:07pm  Oct 26, 2017 8:07pm 

  * [ dukas_trader](dukas_trader)

  * | Membership Revoked  | Joined Mar 2010 | [2,525 Posts](/search?do=process&provider=Member&searchuser=136341)

> [Quoting Fxentropy](/thread/post/10428729#post10428729 "View Quoted Post")
> 
> Disliked
> 
> {quote} {quote} Love the fine and smart answer here. But i think you ask too much, he will never ever show you anything as he never traded for real, he is just a talker. Geting back to topic, would you think that taking trades near S/R and here depend on how we define this S/R- either as last swing high/low, either classic ones, either NY Close level etc would improuve anything? I mean to add as 'filter' this condition, to trigger as per se + S/R. Ofcourse, all getting down to GBPUSD levels. thanks
> 
> Ignored

the offical clown of forexfactory, fx trophy for no arguments is back ![](https://resources.faireconomy.media/images/emojis/64/1f923.png?v=15.1).  
i really missed you unqualified answers for some days ![](https://resources.faireconomy.media/images/emojis/64/1f61c.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f61c.png?v=15.1)  
  
learn the basics man, then you will learn, that telling a intraday trading strategy to many people, will destroy the strategy. you are such a beginner, you dont even know so most simple basics. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#366](/thread/post/10429335#post10429335 "Post Permalink")

  * Oct 26, 2017 8:28pm  Oct 26, 2017 8:28pm 

  * [ nantong](nantong)

  * | Joined Oct 2017  | Status: Trader | [17 Posts](/search?do=process&provider=Member&searchuser=621135)

@[ jvbJacques ](https://www.forexfactory.com/jvbjacques)  
"In my 10 years I have written way more than 700 EAs, but none showed the potential of this arbitrage."  
So if you can work all time on this thing,maybe you can make a living with this ea,and get rich and of course do not need to program for fee,but for fun.What a amazing thing to do,why not?You don't need to work for African greedy corporation and live a free life,you are free from your fight for living.If I were you,I would do this,save money to live for a period of time enough to make this thing online and collect some money to start trading for living.There are people living in hell,struggle to make a little money to keep alive,and because of greedy corporation and greedy big boss.I heart from the Internet that South Africa is ruled by blacks,they had destroyed the entire country and dominate the white people.Is it true? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#367](/thread/post/10429414#post10429414 "Post Permalink")

  * Oct 26, 2017 8:44pm  Oct 26, 2017 8:44pm 

  * [ dukas_trader](dukas_trader)

  * | Membership Revoked  | Joined Mar 2010 | [2,525 Posts](/search?do=process&provider=Member&searchuser=136341)

> [Quoting nantong](/thread/post/10429335#post10429335 "View Quoted Post")
> 
> Disliked
> 
> @[ jvbJacques ](https://www.forexfactory.com/jvbjacques) "In my 10 years I have written way more than 700 EAs, but none showed the potential of this arbitrage." So if you can work all time on this thing,maybe you can make a living with this ea,and get rich and of course do not need to program for fee,but for fun.What a amazing thing to do,why not?You don't need to work for African greedy corporation and live a free life,you are free from your fight for living.If I were you,I would do this,save money to live for a period of time enough...
> 
> Ignored

thats the problem with arbitrage experts. they looks good in theorie, backtest and demo account trading, people think this potnetial is extrem. they invest time in it and sometimes money. they check only later in reality that it cant work in this kind, hardware is much more important than software in arbitrage trading. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#368](/thread/post/10429455#post10429455 "Post Permalink")

  * Oct 26, 2017 8:50pm  Oct 26, 2017 8:50pm 

  * [ nantong](nantong)

  * | Joined Oct 2017  | Status: Trader | [17 Posts](/search?do=process&provider=Member&searchuser=621135)

> [Quoting dukas_trader](/thread/post/10429414#post10429414 "View Quoted Post")
> 
> Disliked
> 
> {quote} thats the problem with arbitrage experts. they looks good in theorie, backtest and demo account trading, people think this potnetial is extrem. they invest time in it and sometimes money. they check only later in reality that it cant work in this kind, hardware is much more important than software in arbitrage trading.
> 
> Ignored

I had forward test the unbalanced system I had post,it made 12% growth from this monday,and still growing,I can't wait to put it on live account,I am now thinking about the risk,yes,it contains risk,but this system surely show the potential,the key is to control risk,and then it will grow like rocket. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#369](/thread/post/10429571#post10429571 "Post Permalink")

  * Oct 26, 2017 9:03pm  Oct 26, 2017 9:03pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar402047_21.gif) Fxentropy](fxentropy)

  * Joined Feb 2015 | Status: Who Dares Wins | [1,710 Posts](/search?do=process&provider=Member&searchuser=402047)

> [Quoting dukas_trader](/thread/post/10429246#post10429246 "View Quoted Post")
> 
> Disliked
> 
> {quote} the offical clown of forexfactory, fx trophy for no arguments is back ![](https://resources.faireconomy.media/images/emojis/64/1f923.png?v=15.1). i really missed you unqualified answers for some days ![](https://resources.faireconomy.media/images/emojis/64/1f61c.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f61c.png?v=15.1) learn the basics man, then you will learn, that telling a intraday trading strategy to many people, will destroy the strategy. you are such a beginner, you dont even know so most simple basics.
> 
> Ignored

you are such a f*cked up dude  
  
i trade for living for more years now than you have been speaking about it. you're just a dirty mounth ready to 'teach' to 'correct' and to 'discipline' others when they want to try new things or interesting things. you're so ugly as character that not even your mother will kiss you if she would knew the truth about you ![](https://resources.faireconomy.media/images/emojis/64/274c.png?v=15.1)  
  
sorry to be so offtopic 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: y7zJe.png
Size: 52 KB](/attachment/image/2534588/thumbnail?d=1509019617)](/attachment/image/2534588?d=1509019617)   

"What would you attempt to do, if you knew your success was a certainty?"

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#370](/thread/post/10429601#post10429601 "Post Permalink")

  * Oct 26, 2017 9:05pm  Oct 26, 2017 9:05pm 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@dukas_trader  
The cost I see per trade is not actually per ticket, but per trade group.  
If you decide on using 1 % on your account then it does not matter if you use it on one ticket or 3 as in arbitrage.  
The 3 tickets together adds up to the cost of the 1 lone ticket.  
The cost is the same.  
Actually the cost on swap for arbitrage is less than if you normally trade a high swap currency.  
  
Theory is where everything begins, but the sad thing is that that is normally where it also ends.  
I am one of those that like to take a theory to its logical conclusion and if, like this theory, I stumble across other related theories that show potential then I want to follow them also, while giving focus to the main theory.  
  
You might be wring and I wrong, but I still have a lot to test before I give up and move to something else and so far I have seen some nice things.  
  
  
@Fxentropy  
This strategy in essence are using an extremely stable S/R.  
The unbalanced one will use more, but also much less than in normal trading.  
  
The problem with the current EA 19 is that its S/R are fixed and it need to be changes to calculate new S/R each time a order is opened to get the best exit S/R and then continue from there.  
  
  
@nantong  
That is a dream job to work on forex full time, even on other people's strategies.  
I just like the math and calculations behind it.  
I even made some A.I brains that can think for themselves and play games in a way to fool people that they are real .... for fun and the challenge ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
  
Problem is that if I go full time I need to save fund to support my monthly expenses, which I have done for other reasons, but to save money your income need to be more than what you spend, which in my case I spend more than what I earn and I only spend on the absolute minimum.  
So no money to save and therefore I am reliant on other paying jobs to at least keep me going for as long as possible.  
  
South Africa does have challenges, but I do not want to talk politics here.  
You are welcome to read up on its laws, especially what they call BEE and who really benefits, nkandla and our president's swimming pool ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
  
Still there are millions around the world that suffers so I have nothing to complain about compared to most others out there, still I am trying to get out of the hole and improve my situation to the best of my abilities.  
I am not one to go down without a fight and I can take a punch and get back up onto my feet. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#371](/thread/post/10429640#post10429640 "Post Permalink")

  * Oct 26, 2017 9:09pm  Oct 26, 2017 9:09pm 

  * [ dukas_trader](dukas_trader)

  * | Membership Revoked  | Joined Mar 2010 | [2,525 Posts](/search?do=process&provider=Member&searchuser=136341)

> [Quoting nantong](/thread/post/10429455#post10429455 "View Quoted Post")
> 
> Disliked
> 
> {quote} I had forward test the unbalanced system I had post,it made 12% growth from this monday,and still growing,I can't wait to put it on live account,I am now thinking about the risk,yes,it contains risk,but this system surely show the potential,the key is to control risk,and then it will grow like rocket.
> 
> Ignored

because unbalanced is same like normal trading, only with higher costs, ofcourse wins are possible, same a losses. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#372](/thread/post/10429671#post10429671 "Post Permalink")

  * Oct 26, 2017 9:11pm  Oct 26, 2017 9:11pm 

  * [ dukas_trader](dukas_trader)

  * | Membership Revoked  | Joined Mar 2010 | [2,525 Posts](/search?do=process&provider=Member&searchuser=136341)

> [Quoting Fxentropy](/thread/post/10429571#post10429571 "View Quoted Post")
> 
> Disliked
> 
> {quote} you are such a f*cked up dude i trade for living for more years now than you have been speaking about it. you're just a dirty mounth ready to 'teach' to 'correct' and to 'discipline' others when they want to try new things or interesting things. you're so ugly as character that not even your mother will kiss you if she would knew the truth about you ![](https://resources.faireconomy.media/images/emojis/64/274c.png?v=15.1) sorry to be so offtopic {image}
> 
> Ignored

trade for living ![](https://resources.faireconomy.media/images/emojis/64/1f606.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f923.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f61c.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f61c.png?v=15.1). good joke.  
  
such unexperniced trader i have never seen faking trading for living, looks you live very bad with your skill level as pontential.  
you have no arguments in all your posts, complete useless posts most of time, show big problems with often even extrem easy topics and look like having no plan of basics in trading.  
  
faking to be good in forex is so easy, looks like you are a winner in your dream world, in reality (easy to see by how and what you write) you look like a bigger loser in forex. maybe you have only extrem bad character and problem with all basic knowledge, and trade for luck, but i dont know, difficult to believe you anything with this low skill level you show here so often. you can only attack people for nothing and without arguments, i have never seen any different from you. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#373](/thread/post/10429739#post10429739 "Post Permalink")

  * Oct 26, 2017 9:17pm  Oct 26, 2017 9:17pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar402047_21.gif) Fxentropy](fxentropy)

  * Joined Feb 2015 | Status: Who Dares Wins | [1,710 Posts](/search?do=process&provider=Member&searchuser=402047)

> [Quoting dukas_trader](/thread/post/10429671#post10429671 "View Quoted Post")
> 
> Disliked
> 
> {quote} trade for living ![](https://resources.faireconomy.media/images/emojis/64/1f606.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f923.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f61c.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f61c.png?v=15.1). good joke. such unexperniced trader i have never seen faking trading for living, looks you live very bad with your skill level as pontential. you have no arguments in all your posts, complete useless posts most of time, show big problems with often even extrem easy topics and look like having no plan of basics in trading. faking to be good in forex is so easy, looks like you are a winner in your dream world, in reality...
> 
> Ignored

i only attacks rednecks. you qualify for that.  
  
again, i trade for living for lots of time now...but i'll not bragg here nor showoff with my skills as i was teach to be a humble person and also i know that those who talk lot eat lot of sh*t too. you qualify for that too.   
  
on the other hand, like jacques suggested, you should show up with something , other that barking around 'correction' correction' 

"What would you attempt to do, if you knew your success was a certainty?"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#374](/thread/post/10429752#post10429752 "Post Permalink")

  * Oct 26, 2017 9:19pm  Oct 26, 2017 9:19pm 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

> [Quoting nantong](/thread/post/10429455#post10429455 "View Quoted Post")
> 
> Disliked
> 
> {quote} I had forward test the unbalanced system I had post,it made 12% growth from this monday,and still growing,I can't wait to put it on live account,I am now thinking about the risk,yes,it contains risk,but this system surely show the potential,the key is to control risk,and then it will grow like rocket.
> 
> Ignored

That sounds very good @nantong.  
I will look at it a bit later.  
Code seems very simple so it could be a winner.  
Keep testing and good luck.  
  
If you keep getting 12% a week then try lowering the profit take to about 2% a week, which will still produce big profit in the long run, but will decrease your draw-down a lot.  
Think more in the line of your profit on profit per year than over the short term and you will be surprised with how little profit per week you can be happy with. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#375](/thread/post/10429792#post10429792 "Post Permalink")

  * Oct 26, 2017 9:25pm  Oct 26, 2017 9:25pm 

  * [ dukas_trader](dukas_trader)

  * | Membership Revoked  | Joined Mar 2010 | [2,525 Posts](/search?do=process&provider=Member&searchuser=136341)

> [Quoting Fxentropy](/thread/post/10429739#post10429739 "View Quoted Post")
> 
> Disliked
> 
> {quote} i only attacks rednecks. you qualify for that. again, i trade for living for lots of time now...but i'll not bragg here nor showoff with my skills as i was teach to be a humble person and also i know that those who talk lot eat lot of sh*t too. you qualify for that too. on the other hand, like jacques suggested, you should show up with something , other that barking around 'correction' correction'
> 
> Ignored

you are funny, you showed already that you have no skills, and no will apologize for cant showing skills.  
in your textes you are always to see as trading noob, so dont fake you trade for a living. people are crazy sometimes, write like stupid beginners and same time writing "trading for a living". maybe its only because you have a bad character with some bigger life problems, why you attack people without arguments, but whatever, live with your problems for you won, i dont hear any more your stupid blabla, i helped you a lot and you dont deserve it any more.  
  
its so funny to see, that you are still the same loser type like from beginning some months ago, you try and try and can jumo over your shadow to be a normal person.  
start having arguments, or clown of forexfactory will be my nickname for you, your realy deserve it, troll clowns always have no arguments like you. and troll clowns alsway tell how good they are and how good the are living from trading, same time writing only bullshit like you and show they are opposite of they write. again like you. is really 1:1 to see you as troll clown. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#376](/thread/post/10429819#post10429819 "Post Permalink")

  * Oct 26, 2017 9:27pm  Oct 26, 2017 9:27pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar402047_21.gif) Fxentropy](fxentropy)

  * Joined Feb 2015 | Status: Who Dares Wins | [1,710 Posts](/search?do=process&provider=Member&searchuser=402047)

> [Quoting dukas_trader](/thread/post/10429792#post10429792 "View Quoted Post")
> 
> Disliked
> 
> {quote} you are funny, you showed already that you have no skills, and no will apologize for cant showing skills. in your textes you are always to see as trading noob, so dont fake you trade for a living. people are crazy sometimes, write like stupid beginners and same time writing "trading for a living". maybe its only because you have a bad character with some bigger life problems, why you attack people without arguments, but whatever, live with your problems for you won, i dont hear any more your stupid blabla, i helped you a lot and you dont...
> 
> Ignored

lets say i lie i trade for living.......althought i do trade for living   
  
what you do for living????? 

"What would you attempt to do, if you knew your success was a certainty?"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#377](/thread/post/10429841#post10429841 "Post Permalink")

  * Oct 26, 2017 9:30pm  Oct 26, 2017 9:30pm 

  * [ dukas_trader](dukas_trader)

  * | Membership Revoked  | Joined Mar 2010 | [2,525 Posts](/search?do=process&provider=Member&searchuser=136341)

> [Quoting Fxentropy](/thread/post/10429819#post10429819 "View Quoted Post")
> 
> Disliked
> 
> {quote} lets say i lie i trade for living.......althought i do trade for living what you do for living?????
> 
> Ignored

i live since 20 years from trading baby. thatswhy i have arguments to each topic and about each questions, opposite to dream traders, when someone has no arguemnts, you can see very fast, he knows not even the basics and is never ever a good real trader.  
  
ok, i accept that you be a liar about it. and i accept that you still dream you trade for a living. accept your problems or come over it (some character problems you really have to clean), start learning basics, and some day you will get some wins. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#378](/thread/post/10429880#post10429880 "Post Permalink")

  * Oct 26, 2017 9:36pm  Oct 26, 2017 9:36pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar402047_21.gif) Fxentropy](fxentropy)

  * Joined Feb 2015 | Status: Who Dares Wins | [1,710 Posts](/search?do=process&provider=Member&searchuser=402047)

> [Quoting dukas_trader](/thread/post/10429841#post10429841 "View Quoted Post")
> 
> Disliked
> 
> {quote} i live since 20 years from trading baby. thatswhy i have arguments to each topic and about each questions, opposite to dream traders, when someone has no arguemnts, you can see very fast, he knows not even the basics and is never ever a good real trader. ok, i accept that you be a liar about it. and i accept that you still dream you trade for a living. accept your problems or come over it (some character problems you really have to clean), start learning basics, and some day you will get some wins.
> 
> Ignored

OK, can you prouve it?  
  
If you show your statement for 2017 i will show mine too.  
  
No BS, just pure truth!!  
  
i Dare you, oxymoron full of sh*t! You havent been able to show a simple chart as to this date......but a statement!! 

"What would you attempt to do, if you knew your success was a certainty?"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#379](/thread/post/10429911#post10429911 "Post Permalink")

  * Oct 26, 2017 9:40pm  Oct 26, 2017 9:40pm 

  * [ dukas_trader](dukas_trader)

  * | Membership Revoked  | Joined Mar 2010 | [2,525 Posts](/search?do=process&provider=Member&searchuser=136341)

> [Quoting Fxentropy](/thread/post/10429880#post10429880 "View Quoted Post")
> 
> Disliked
> 
> {quote} OK, can you prouve it? If you show your statement for 2017 i will show mine too. No BS, just pure truth!! i Dare you, oxymoron full of sh*t!
> 
> Ignored

why, i dont be interested in a statement of a faker and dreamer and a man , who only can attack without any arguments.  
how many times i did say you, when you stop to attack without arguments all whould be fine, but you always start to doing exactly this. i can only ask me: why?? what do you have by this, attacking someone and dont say any reason for it, not only one. all i did say here in forexfactory was with reasons , and when something is not correct in your eyes, tell me what post it was , and we can speak about (but it will be not easy to find some of this, because i try to speak very objective). but always your way its really boring. you can change your style, its only one step to do and i can start to take you at least serious and a dicussion would be start about some topics, not only about you.  
  
next to it, showing statements is showing what? you show one account with 100% plus and have 20 account with 100% minus what you dont show???  
  
i meet people who are worth it in reality to see in real who they are and go trough all parts, but what you say here, clear shows me, you really dont know basics or know what a real trader is. you ask for total usless things.  
  
again: learn the basics, many of the things you speak about ,you would not say after learning at least the basics of trading. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#380](/thread/post/10429998#post10429998 "Post Permalink")

  * Edited 10:07pm  Oct 26, 2017 9:53pm | Edited 10:07pm 

  * [ dukas_trader](dukas_trader)

  * | Membership Revoked  | Joined Mar 2010 | [2,525 Posts](/search?do=process&provider=Member&searchuser=136341)

> [Quoting Fxentropy](/thread/post/10429955#post10429955 "View Quoted Post")
> 
> Disliked
> 
> {quote} My account would show now to be in 6 figures. History of it will show you i went up to 7 figure then withdrawal. And its going back as history to 2013; Before than i had another broker and that history is going back to 2009. Same 6 figure account going into 7 figure. I cant fake a 6 figure account. nor cant play with it. Yes, i have some others smaller account that i test some new things (those at what you bark like a madmen) but im talking about main account herE. I dare you do the same or sssssshhhhttttttt! In any case, you are full of...
> 
> Ignored

hear, thats the problem!  
i started also some accounts with 6 figures because i had a good job.  
and i also do sometimes withdraw 6 figures per month for business opportunities or real estates. thats normal.  
but all we speak about here is our private thing. its useless to speak about, because anything we speak about here can be faked and not true.  
  
and by the way: faking with photoshop or even with html (when using metatrader) is so easy, that if anyone trust anything online, he would be have a problem.  
  
only by meeting someone in reality you can see by looking at their accounts, how they live, who they know, about speaking with them,..... you can trust someone. and most of time they use same brokers and are already known most of time inside broker..... i would never do anything other style, and i never met someone with money who did it different.  
  
if you really do different by having some millions, then really one good advice: dont do it. there are so many fakers outside, you lose time and show private things to no honest persons. and time i can spend only once, money you can get back, time never. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Simple High Profit low Drawdown Triangular Arbitrage
  *   * [ **Reply to Thread** ](/thread/676132-simple-high-profit-low-drawdown-triangular-arbitrage/reply#reply)

  * More

[](https://www.forexfactory.com "Homepage")

  * [Forums](forums)
  * [Trades](trades)
  * [Calendar](calendar)
  * [News](news)
  * [Market](market)
  * [Brokers](brokers)

****

[](https://www.faireconomy.com/)

  * 

[Triangular Arbitrage](/thread/64423-triangular-arbitrage "Admin, Please Delete Thread.") 258 replies

[Triangular Arbitrage](/thread/62477-triangular-arbitrage "Is going  
long 1 lot of eur/usd + 
long 1 lot of usd/jpy = long 1 lot of eur/jpy ?  
\(is the ratio of the number of lots correct for a...") 16 replies

[Triangular Arbitrage and carry trade](/thread/71997-triangular-arbitrage-and-carry-trade "Is it possible for us retail traders to be able to make use of Tri Arb or carry trades?  
 
Any one know of retail brokers 
 
 
\(I'm...") 6 replies

[Triangular Arbitrage](/thread/367072-triangular-arbitrage "I've been reading about triangular arbing and was surprised to find that the cross of two majors doesn't always equal what the calculation...") 7 replies

[Question: Trade Mechanics of Triangular Arbitrage](/thread/225246-question-trade-mechanics-of-triangular-arbitrage "Before I even ask this question, please allow me to be very clear.... I have no intention of attempting a triangular arbitrage trade\(for...") 6 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/676132-simple-high-profit-low-drawdown-triangular-arbitrage/reply#reply)
  * Subscribe
  * [147](javascript:void\(0\);)

Attachments: Simple High Profit low Drawdown Triangular Arbitrage

Tags: Simple High Profit low Drawdown Triangular Arbitrage

#  [](/thread/676132-simple-high-profit-low-drawdown-triangular-arbitrage)Simple High Profit low Drawdown Triangular Arbitrage 

  * 

  * [#381](/thread/post/10430089#post10430089 "Post Permalink")

  * Oct 26, 2017 10:04pm  Oct 26, 2017 10:04pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar402047_21.gif) Fxentropy](fxentropy)

  * Joined Feb 2015 | Status: Who Dares Wins | [1,710 Posts](/search?do=process&provider=Member&searchuser=402047)

> [Quoting dukas_trader](/thread/post/10429998#post10429998 "View Quoted Post")
> 
> Disliked
> 
> {quote} hear, thats the problem! i started also some accounts with 6 figures because i had a good job. and i also do sometimes withdraw 6 figures per month for business opportunities or real estates. thats normal. but all we speak about here is our private thing. its useless to speak about, because anything we speak about here can be faked and not true. only by meeting someone in reality you can see by looking at their accounts, how they live, who they know, about speaking with them,..... you can trust someone. and most of time they use same brokers...
> 
> Ignored

LOL..now i get advices from a newbie!  
  
I will delete all my mesagges here, no point to fight a fight i cant win anyway....and for what? never throw diamonds in pigs face. 

"What would you attempt to do, if you knew your success was a certainty?"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#382](/thread/post/10430116#post10430116 "Post Permalink")

  * Edited 11:09pm  Oct 26, 2017 10:06pm | Edited 11:09pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar402047_21.gif) Fxentropy](fxentropy)

  * Joined Feb 2015 | Status: Who Dares Wins | [1,710 Posts](/search?do=process&provider=Member&searchuser=402047)

Sorry Jacques for what just happened, it will not happen again.  
  
My apologise. 

"What would you attempt to do, if you knew your success was a certainty?"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#383](/thread/post/10430138#post10430138 "Post Permalink")

  * Edited 10:26pm  Oct 26, 2017 10:09pm | Edited 10:26pm 

  * [ dukas_trader](dukas_trader)

  * | Membership Revoked  | Joined Mar 2010 | [2,525 Posts](/search?do=process&provider=Member&searchuser=136341)

> [Quoting Fxentropy](/thread/post/10430089#post10430089 "View Quoted Post")
> 
> Disliked
> 
> {quote} LOL..now i get advices from a newbie! I will delete all my mesagges here, no point to fight a fight i cant win anyway....and for what? never throw diamonds in pigs face.
> 
> Ignored

hmm, if you would have only 7 figures from time to time, then call you the newbie baby.  
after 20 years i dont be any more near my starting 6 figures.  
  
its funny how fast you show as faker here. and of course you cant win with your low skill a fight without arguments, you have to learn basics first, stop faking, be honest, all things you dont do.  
  
i did think about a lot, now i ignore you simple. you fake really your money, funny. you really fake your experience , funny.  
but when you dont start to fake your bad character and psychic problems, it wortless to speak with you. so see you in your dreamland, where you have your only wins. here is impossible to speak to you,  
  
all the time i do try to make true discussion with you, and all the time when you see you are on the ground and dont have arguments and are exposed for being a faker and liar, then you run away. but thats ok, you are useless timewaste here. even beginners have bigger knowlege then you and know how to bring arguments. 

[1 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#384](/thread/post/10430820#post10430820 "Post Permalink")

  * Oct 26, 2017 11:42pm  Oct 26, 2017 11:42pm 

  * [ rizam34](rizam34)

  * | Joined Sep 2017  | Status: Trader | [44 Posts](/search?do=process&provider=Member&searchuser=611864)

Guys can we move fowards ?... continue improving the EA ...enlargements will never ends..everyone have their differences 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#385](/thread/post/10432811#post10432811 "Post Permalink")

  * Edited 9:00am  Oct 27, 2017 8:39am | Edited 9:00am 

  * [ nantong](nantong)

  * | Joined Oct 2017  | Status: Trader | [17 Posts](/search?do=process&provider=Member&searchuser=621135)

After one night's move,the system suffers serious drawdown,lose profit it made these days.It's like martingale,keep adding position to the lose one,and hope it will return and get profit,but they are a little different,the martingale is rely on trend,but this one rely on the unbalanced positon,just dukas_trader said,normal trade,and finally it's a trend.But here,still have a little difference,that is the so called "normal trade" is changing as the trend move,which I don't know. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#386](/thread/post/10432845#post10432845 "Post Permalink")

  * Oct 27, 2017 8:58am  Oct 27, 2017 8:58am 

  * [ dukas_trader](dukas_trader)

  * | Membership Revoked  | Joined Mar 2010 | [2,525 Posts](/search?do=process&provider=Member&searchuser=136341)

> [Quoting nantong](/thread/post/10432811#post10432811 "View Quoted Post")
> 
> Disliked
> 
> After one night's move,the system suffers serious drawdown,lose profit it made these days.It's like martingale.
> 
> Ignored

then you have always wins after win, but each day you risk big losses or risk complete account killing to get it. thats with any martingale systems with no SL or very high SL. all have same problem , on the end you risk to lose all. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#387](/thread/post/10432928#post10432928 "Post Permalink")

  * Oct 27, 2017 9:51am  Oct 27, 2017 9:51am 

  * [ nantong](nantong)

  * | Joined Oct 2017  | Status: Trader | [17 Posts](/search?do=process&provider=Member&searchuser=621135)

> [Quoting dukas_trader](/thread/post/10432845#post10432845 "View Quoted Post")
> 
> Disliked
> 
> {quote} then you have always wins after win, but each day you risk big losses or risk complete account killing to get it. thats with any martingale systems with no SL or very high SL. all have same problem , on the end you risk to lose all.
> 
> Ignored

You are right.The only method to creating a balanced position from unbalanced one,is to adding position,however I can see that when it return to balanced finally,the so called "normal trade" is getting small,maybe negative,and this is the magic of this system.Please correct me if I am wrong. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#388](/thread/post/10432997#post10432997 "Post Permalink")

  * Oct 27, 2017 10:49am  Oct 27, 2017 10:49am 

  * [ dukas_trader](dukas_trader)

  * | Membership Revoked  | Joined Mar 2010 | [2,525 Posts](/search?do=process&provider=Member&searchuser=136341)

> [Quoting nantong](/thread/post/10432928#post10432928 "View Quoted Post")
> 
> Disliked
> 
> {quote} You are right.The only method to creating a balanced position from unbalanced one,is to adding position,however I can see that when it return to balanced finally,the so called "normal trade" is getting small,maybe negative,and this is the magic of this system.Please correct me if I am wrong.
> 
> Ignored

i dont know. i only take a look in my own systems.  
i only valued what you spoke about. martingale is always the same, only with different settings and time to destroy account. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#389](/thread/post/10434220#post10434220 "Post Permalink")

  * Oct 27, 2017 7:10pm  Oct 27, 2017 7:10pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar373412_1.gif) vanillanont](vanillanont)

  * | Joined May 2014  | Status: Trader | [2 Posts](/search?do=process&provider=Member&searchuser=373412)

I'm testing on live account and it's running fine.  
EA opening  
BUY UJ 1.33  
BUY GU 1.01  
SELL GJ 1.01  
from yesterday till now, now total profit around -50 to -60 usd.  
My question is :  
Is this EA working fine ?  
Should I close it my self or wait them run to profit ?  
Usually,How long ea run to profit ?  
  
\---------------------------  
Balance : 1000 usd  
I'm using [pepperstone](/brokers/pepperstone "View Pepperstone Broker Profile") EDGE server spread around 8-15 with no commisson. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#390](/thread/post/10434323#post10434323 "Post Permalink")

  * Edited 7:46pm  Oct 27, 2017 7:32pm | Edited 7:46pm 

  * [ nantong](nantong)

  * | Joined Oct 2017  | Status: Trader | [17 Posts](/search?do=process&provider=Member&searchuser=621135)

> [Quoting jvbJacques](/thread/post/10429752#post10429752 "View Quoted Post")
> 
> Disliked
> 
> {quote} That sounds very good @nantong. I will look at it a bit later. Code seems very simple so it could be a winner. Keep testing and good luck. If you keep getting 12% a week then try lowering the profit take to about 2% a week, which will still produce big profit in the long run, but will decrease your draw-down a lot. Think more in the line of your profit on profit per year than over the short term and you will be surprised with how little profit per week you can be happy with.
> 
> Ignored

Yes,you're right.Now I make some change to the original ea,that is:bigger boxsize,smaller tp,and only tp when total profit of bbs and ssb reach the target.I think this maybe lower drawdown,because bbs and ssb are somewhat hedged,they're like two legs open position in opposite.And another change is just trade eurusdjpy and eurgbpusd,to avoid too much orders and thus the drawdown. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#391](/thread/post/10434783#post10434783 "Post Permalink")

  * Oct 27, 2017 9:33pm  Oct 27, 2017 9:33pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar457690_1.gif) artico01](artico01)

  * Joined Apr 2016 | Status: Trader | [108 Posts](/search?do=process&provider=Member&searchuser=457690)

> [Quoting nantong](/thread/post/10413174#post10413174 "View Quoted Post")
> 
> Disliked
> 
> {quote} just for test only! attach [OPEN_EURGBPJPY.mq4](https://www.forexfactory.com/attachment.php?attachmentid=2527516&stc=1&d=1508559389) to eurgbp,gbpjpy,eurjpy renko chart,with 9 10 9 boxsize, attach [OPEN_EURGBPUSD.mq4](https://www.forexfactory.com/attachment.php?attachmentid=2527518&stc=1&d=1508559390) to eurgbp,gbpusd,eurusd renko chart,with 9 10 9 boxsize, attach [OPEN_EURUSDJPY.mq4](https://www.forexfactory.com/attachment.php?attachmentid=2527521&stc=1&d=1508559390) to eurusd,usdjpy,eurjpy renko chart,with...
> 
> Ignored

The Metaquote editor recognizes OPEN_EURGBPJPY as an indicator, not as an EA. How do you get an indicator to open operations in MT4?  
I have tried it but nothing happens.  
Thank you 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#392](/thread/post/10434973#post10434973 "Post Permalink")

  * Oct 27, 2017 10:07pm  Oct 27, 2017 10:07pm 

  * [ dukas_trader](dukas_trader)

  * | Membership Revoked  | Joined Mar 2010 | [2,525 Posts](/search?do=process&provider=Member&searchuser=136341)

> [Quoting artico01](/thread/post/10434783#post10434783 "View Quoted Post")
> 
> Disliked
> 
> {quote} The Metaquote editor recognizes OPEN_EURGBPJPY as an indicator, not as an EA. How do you get an indicator to open operations in MT4? I have tried it but nothing happens. Thank you
> 
> Ignored

indicators cant open any operation? did you save it in expert or in indicator folder? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#393](/thread/post/10435006#post10435006 "Post Permalink")

  * Edited 10:24pm  Oct 27, 2017 10:12pm | Edited 10:24pm 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@nantong  
I still did not have time to look at the code, but from what you said it does not sound like you are working with a martingale system, but with a grid system.  
  
The draw back of a grid system is that eventually as the price moves away from the starting point you will have lingering grid points, which will never close and exponentially increase your draw down.  
  
The good thing about triangular arbitrage is that you have quite stable high and low points and therefore you can plan the number and size of your grid levels to fit into these high and low points, maybe a bit more for safety.  
Remember the high and low point must include spikes in price.  
  
Then you you can just work it as normal and wait for it to come back, or at least come back to a point where it is in profit, which is only half way from the starting point.  
No need to wait for a full price reversal.  
  
You will have grid points hanging at the edges of the high and low points, but you can close them with profit or with the half way return strategy.  
  
I see grids as a way to get out of a position and not to make profit.  
I only make profit on the first grid level.  
If the grid goes higher then get out on break even.  
Triangular arbitrage is special in that you might want to experiment in maybe profiting also from higher grid levels seeing that trends to not carry the grid so far into draw down.  
  
To find the high and low point I suggest you back test with at least a year or 2 worth of data and see what the high and low points are.  
Then add 50% to 100% extra to it and make sure a full grid draw down will survive it.  
  
Triangular arbitrage is not known for big reversals so grids work nice in them, even unbalanced triangles like the one you seem to be using.  
  
One more thing.  
Do not open grid levels immediately.  
I found that if you time delay grid opening points then you can avoid spikes from triggering unnecessary grid levels.  
Maybe make sure the price staid past a grid level for more than a few seconds before opening a new level, but no time delay for closing at profit or break even.  
  
  
@vanillanont  
YES  
EA 19 is unstable and sometimes do open trades without ever closing them again.  
Sort of losing track of them, but more giving them impossible take profits, which I know how to fix, but will first need to get development time to fix it.  
Do not use on live please.  
I can understand wanting to use an EA that you suspect might work, but in this case I know the EA 19 is not stable so rather wait for a stable EA or build one using the theory.  
  
I will get there to make it stable one day.  
  
Good Luck. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#394](/thread/post/10435858#post10435858 "Post Permalink")

  * Oct 28, 2017 12:25am  Oct 28, 2017 12:25am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar457690_1.gif) artico01](artico01)

  * Joined Apr 2016 | Status: Trader | [108 Posts](/search?do=process&provider=Member&searchuser=457690)

> [Quoting dukas_trader](/thread/post/10434973#post10434973 "View Quoted Post")
> 
> Disliked
> 
> {quote} indicators cant open any operation? did you save it in expert or in indicator folder?
> 
> Ignored

  
MT4 does not recognize this file as EA 

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: 2017-10-27 \(1\).png
Size: 24 KB](/attachment/image/2537054/thumbnail?d=1509117945)](/attachment/image/2537054?d=1509117945)   
[![Click to Enlarge

Name: 2017-10-27.png
Size: 17 KB](/attachment/image/2537055/thumbnail?d=1509117946)](/attachment/image/2537055?d=1509117946)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#395](/thread/post/10435905#post10435905 "Post Permalink")

  * Oct 28, 2017 12:39am  Oct 28, 2017 12:39am 

  * [ dukas_trader](dukas_trader)

  * | Membership Revoked  | Joined Mar 2010 | [2,525 Posts](/search?do=process&provider=Member&searchuser=136341)

> [Quoting artico01](/thread/post/10435858#post10435858 "View Quoted Post")
> 
> Disliked
> 
> {quote} MT4 does not recognize this file as EA {image} {image}
> 
> Ignored

difficult to see by not having this file. where did you get this mq4?  
whats the goal for this ea/indicator? open only trades? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#396](/thread/post/10435930#post10435930 "Post Permalink")

  * Oct 28, 2017 12:47am  Oct 28, 2017 12:47am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar457690_1.gif) artico01](artico01)

  * Joined Apr 2016 | Status: Trader | [108 Posts](/search?do=process&provider=Member&searchuser=457690)

> [Quoting dukas_trader](/thread/post/10435905#post10435905 "View Quoted Post")
> 
> Disliked
> 
> {quote} difficult to see by not having this file. where did you get this mq4? whats the goal for this ea/indicator? open only trades?
> 
> Ignored

See post #346 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#397](/thread/post/10436220#post10436220 "Post Permalink")

  * Oct 28, 2017 2:19am  Oct 28, 2017 2:19am 

  * [ dukas_trader](dukas_trader)

  * | Membership Revoked  | Joined Mar 2010 | [2,525 Posts](/search?do=process&provider=Member&searchuser=136341)

> [Quoting artico01](/thread/post/10435930#post10435930 "View Quoted Post")
> 
> Disliked
> 
> {quote} See post #346
> 
> Ignored

if nantong is the programmer/tester of this, then its maybe more easy to ask him. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#398](/thread/post/10436873#post10436873 "Post Permalink")

  * Oct 28, 2017 9:09am  Oct 28, 2017 9:09am 

  * [ nantong](nantong)

  * | Joined Oct 2017  | Status: Trader | [17 Posts](/search?do=process&provider=Member&searchuser=621135)

> [Quoting artico01](/thread/post/10435858#post10435858 "View Quoted Post")
> 
> Disliked
> 
> {quote} MT4 does not recognize this file as EA {image} {image}
> 
> Ignored

I don't have problem here,I upload ex4 files for you. 

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [CLOSE.ex4](/attachment/file/2537500?d=1509148950) 31 KB | 381 downloads 

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [OPEN_EURGBPJPY.ex4](/attachment/file/2537502?d=1509148951) 8 KB | 430 downloads 

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [OPEN_EURGBPUSD.ex4](/attachment/file/2537503?d=1509148952) 8 KB | 419 downloads 

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [OPEN_EURUSDJPY.ex4](/attachment/file/2537504?d=1509148952) 8 KB | 424 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#399](/thread/post/10436886#post10436886 "Post Permalink")

  * Edited 9:50am  Oct 28, 2017 9:28am | Edited 9:50am 

  * [ nantong](nantong)

  * | Joined Oct 2017  | Status: Trader | [17 Posts](/search?do=process&provider=Member&searchuser=621135)

@jvbJacques  
The strategy is from Three pairs hedging/Renko thread,the author is jeuro,eatrader75 mentioned.The system used renko chart with proper distance to create hedge position,not grid,but like grid,not at the same time,but slowly created,and from the start point,it's unbalanced,and risk,because of so called "normal trade",where the profit comes from,and as time goes,or trend goes,it would get close to balance,if the price do not go far.It risks when unbalanced,and limit the risk when balanced,so it has some potential,but I don't know if there is edge involved.  
For EURUSD,USDJPY,EURJPY,if the EURUSD price is 1.16075 now,the open lots rate must be 1:1.16075:1,so the renko boxsize rate must be 1.16075:1:1.16075,because the broker can not accept 1.16075 lot,to created a balance,so in stead it used renko boxsize to created the hedge position,and because of the market is random very much,3 pairs do not enter at the same time,and this give the risk,thus the profit comes from.  
  
"The good thing about triangular arbitrage is that you have quite stable high and low points and therefore you can plan the number and size of your grid levels to fit into these high and low points, maybe a bit more for safety."  
This is the Three pairs hedging/Renko system trying to do,the risk is limited,and profit is produced when market move.Go ahead for your work,it worth to try. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#400](/thread/post/10440960#post10440960 "Post Permalink")

  * Oct 30, 2017 10:37pm  Oct 30, 2017 10:37pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar617900_2.gif) HinaSheikh](hinasheikh)

  * | Joined Oct 2017  | Status: Trader | [5 Posts](/search?do=process&provider=Member&searchuser=617900)

Can anyone guide me? i am using MT5 and applied this EA on GBPUSD, GBPJPY and USDJPY, but EA is doing nothing, i waited for 2 days but EA executed not a single trade, am i missing something? kindly guide me 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Simple High Profit low Drawdown Triangular Arbitrage
  *   * [ **Reply to Thread** ](/thread/676132-simple-high-profit-low-drawdown-triangular-arbitrage/reply#reply)

  * More

[](https://www.forexfactory.com "Homepage")

  * [Forums](forums)
  * [Trades](trades)
  * [Calendar](calendar)
  * [News](news)
  * [Market](market)
  * [Brokers](brokers)

****

[](https://www.faireconomy.com/)

  * 

[Triangular Arbitrage](/thread/64423-triangular-arbitrage "Admin, Please Delete Thread.") 258 replies

[Triangular Arbitrage](/thread/62477-triangular-arbitrage "Is going  
long 1 lot of eur/usd + 
long 1 lot of usd/jpy = long 1 lot of eur/jpy ?  
\(is the ratio of the number of lots correct for a...") 16 replies

[Triangular Arbitrage and carry trade](/thread/71997-triangular-arbitrage-and-carry-trade "Is it possible for us retail traders to be able to make use of Tri Arb or carry trades?  
 
Any one know of retail brokers 
 
 
\(I'm...") 6 replies

[Triangular Arbitrage](/thread/367072-triangular-arbitrage "I've been reading about triangular arbing and was surprised to find that the cross of two majors doesn't always equal what the calculation...") 7 replies

[Question: Trade Mechanics of Triangular Arbitrage](/thread/225246-question-trade-mechanics-of-triangular-arbitrage "Before I even ask this question, please allow me to be very clear.... I have no intention of attempting a triangular arbitrage trade\(for...") 6 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/676132-simple-high-profit-low-drawdown-triangular-arbitrage/reply#reply)
  * Subscribe
  * [147](javascript:void\(0\);)

Attachments: Simple High Profit low Drawdown Triangular Arbitrage

Tags: Simple High Profit low Drawdown Triangular Arbitrage

#  [](/thread/676132-simple-high-profit-low-drawdown-triangular-arbitrage)Simple High Profit low Drawdown Triangular Arbitrage 

  * 

  * [#401](/thread/post/10442603#post10442603 "Post Permalink")

  * Oct 31, 2017 10:21am  Oct 31, 2017 10:21am 

  * [ nantong](nantong)

  * | Joined Oct 2017  | Status: Trader | [17 Posts](/search?do=process&provider=Member&searchuser=621135)

> [Quoting HinaSheikh](/thread/post/10440960#post10440960 "View Quoted Post")
> 
> Disliked
> 
> Can anyone guide me? i am using MT5 and applied this EA on GBPUSD, GBPJPY and USDJPY, but EA is doing nothing, i waited for 2 days but EA executed not a single trade, am i missing something? kindly guide me
> 
> Ignored

The ea is mt4 version,and you need to put it on renko chart,just search renko in this forum,or you can search jeuro,everything about this system is there. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#402](/thread/post/10450769#post10450769 "Post Permalink")

  * Nov 2, 2017 11:07am  Nov 2, 2017 11:07am 

  * [ nantong](nantong)

  * | Joined Oct 2017  | Status: Trader | [17 Posts](/search?do=process&provider=Member&searchuser=621135)

I added "DD" % to close all orders,and close at "BE".The "win" is the target. 

Attached File(s)

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [CLOSE.mq4](/attachment/file/2543626?d=1509588420) 13 KB | 506 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#403](/thread/post/10456788#post10456788 "Post Permalink")

  * Edited Nov 4, 2017 12:19am  Nov 3, 2017 9:30pm | Edited Nov 4, 2017 12:19am 

  * [ densol](densol)

  * | Joined Jan 2013  | Status: Trader | [52 Posts](/search?do=process&provider=Member&searchuser=322354)

hello I decide to test this ea on live account  
starting capital: 100 (withdraw 10) so 90 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#404](/thread/post/10505163#post10505163 "Post Permalink")

  * Nov 17, 2017 9:56pm  Nov 17, 2017 9:56pm 

  * [ antonder](antonder)

  * | Joined Nov 2017  | Status: Trader | [5 Posts](/search?do=process&provider=Member&searchuser=628874)

> [Quoting nantong](/thread/post/10413174#post10413174 "View Quoted Post")
> 
> Disliked
> 
> {quote} just for test only! attach [OPEN_EURGBPJPY.mq4](https://www.forexfactory.com/attachment.php?attachmentid=2527516&stc=1&d=1508559389) to eurgbp,gbpjpy,eurjpy renko chart,with 9 10 9 boxsize, attach [OPEN_EURGBPUSD.mq4](https://www.forexfactory.com/attachment.php?attachmentid=2527518&stc=1&d=1508559390) to eurgbp,gbpusd,eurusd renko chart,with 9 10 9 boxsize, attach [OPEN_EURUSDJPY.mq4](https://www.forexfactory.com/attachment.php?attachmentid=2527521&stc=1&d=1508559390) to eurusd,usdjpy,eurjpy renko chart,with...
> 
> Ignored

TimeFrame ??? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#405](/thread/post/10508713#post10508713 "Post Permalink")

  * Nov 19, 2017 11:57am  Nov 19, 2017 11:57am 

  * [ nantong](nantong)

  * | Joined Oct 2017  | Status: Trader | [17 Posts](/search?do=process&provider=Member&searchuser=621135)

> [Quoting antonder](/thread/post/10505163#post10505163 "View Quoted Post")
> 
> Disliked
> 
> {quote} TimeFrame ???
> 
> Ignored

Use Renko Chart to open orders,you do not need to consider TimeFrame. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#406](/thread/post/10508908#post10508908 "Post Permalink")

  * Nov 19, 2017 6:05pm  Nov 19, 2017 6:05pm 

  * [ antonder](antonder)

  * | Joined Nov 2017  | Status: Trader | [5 Posts](/search?do=process&provider=Member&searchuser=628874)

What is Renko chart ? How i can use it ?  
tank’s 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#407](/thread/post/10514948#post10514948 "Post Permalink")

  * Nov 21, 2017 6:48pm  Nov 21, 2017 6:48pm 

  * [ antonder](antonder)

  * | Joined Nov 2017  | Status: Trader | [5 Posts](/search?do=process&provider=Member&searchuser=628874)

> [Quoting nantong](/thread/post/10508713#post10508713 "View Quoted Post")
> 
> Disliked
> 
> {quote} Use Renko Chart to open orders,you do not need to consider TimeFrame.
> 
> Ignored

Please, help me   
I did not understand how to use renko, how do i put two EAs on the same graph ??? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#408](/thread/post/10522963#post10522963 "Post Permalink")

  * Nov 23, 2017 6:37pm  Nov 23, 2017 6:37pm 

  * [ nantong](nantong)

  * | Joined Oct 2017  | Status: Trader | [17 Posts](/search?do=process&provider=Member&searchuser=621135)

> [Quoting antonder](/thread/post/10514948#post10514948 "View Quoted Post")
> 
> Disliked
> 
> {quote} Please, help me I did not understand how to use renko, how do i put two EAs on the same graph ???
> 
> Ignored

Just download renko indicator I post before,attach it to say 1 minute EURUSD chart,and open m2 in you history data center,and now you have renko chart of EURUSD,and then attach openEURUSD.mq4 ea to renko chart of EURUSD.The close.mq4 is used to close orders when at profit,you can attach it to one different chart.And you must creat renko chart of say EURUSD,USDJPY and EURJPY to creat a basket of pairs to hedge each other,hope that helps 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#409](/thread/post/10550240#post10550240 "Post Permalink")

  * Dec 1, 2017 8:42pm  Dec 1, 2017 8:42pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar453832_1.gif) jesing](jesing)

  * Joined Mar 2016 | Status: Trader | [294 Posts](/search?do=process&provider=Member&searchuser=453832)

Dear JVB & coder,  
  
**nice strategy,**  
  
can you share here ENTRY logic ( **Script**),  
  
Like how to calculate open order and lot size for all pair and how to calculate pair position ( BUY BUY SELL or SELL SELL BUY )   
  
thanks in advance,  
  
regards,  
  
\- jesing 

Always Feel Good...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#410](/thread/post/10559143#post10559143 "Post Permalink")

  * Dec 5, 2017 4:30am  Dec 5, 2017 4:30am 

  * [ sergelight](sergelight)

  * | Joined Nov 2016  | Status: Trader | [4 Posts](/search?do=process&provider=Member&searchuser=525202)

Hi there! Awesome stuff you have done man @[jvbJacques](https://www.forexfactory.com/jvbjacques). I had one question. How do you calculate what the profit will be for a triangle? You mind sharing that calculation?  
  
Cheers

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#411](/thread/post/10577905#post10577905 "Post Permalink")

  * Dec 11, 2017 7:15am  Dec 11, 2017 7:15am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar453832_1.gif) jesing](jesing)

  * Joined Mar 2016 | Status: Trader | [294 Posts](/search?do=process&provider=Member&searchuser=453832)

> [Quoting jvbJacques](/thread/post/9988492#post9988492 "View Quoted Post")
> 
> Disliked
> 
> I will always update this POST #1 with the latest information. So if you do not want to read all the posts then just read this one. I will also keep the EAs up to date here. The rest of the posts are interesting and I love flame wars ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1) ******************************* Very basic summary ******************************* 1) Buy 1 unit GBPJPY 2) Sell 1 unit GBPUSD 3) Sell ?? units using the USD in point (2) in USDJPY to balance everything out Buy low and sell high. Rinse and repeat. Can this work or what is the pitfalls with this idea ? *******************************...
> 
> Ignored

Dear Jacques,  
  
nice creation,  
  
i found some bugs in EA,  
  
PM me, so we discuss it  
  
regards,  
  
\- jesing 

Always Feel Good...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#412](/thread/post/10577945#post10577945 "Post Permalink")

  * Dec 11, 2017 7:36am  Dec 11, 2017 7:36am 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@EVERYONE  
I am still alive ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
Sort of ![](https://resources.faireconomy.media/images/emojis/64/1f641.png?v=15.1)  
Still working to get funds to take off and finish the development on this.  
  
Please note that the EA in post one have got nothing to do with renco charts.  
The renco chart EA is somethings else made by someone else that posted it into this post thread.  
  
My EA runs on its own. but it will stop working at the end of 2017 and there are a HECK OF A LOT OF BUGS.  
Most I know how to fix, but require time to do it in.  
  
  
@jesing  
I assume you are seeing some of the bugs I already know of.  
You are welcome to PM me or talk about it.  
  
UPDATE  
Sorry jesing.  
I just saw your PM and messaged you back.  
Hope you get it right.  
Good luck.  
  
  
@sergelight  
Most everything of what the EA does is in this forum.  
If there is something not clear then you are welcome to ask or PM me.  
  
Seeing that I am stuck trying to find time for this I might miss some posts in this thread, so I might find your PM faster. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#413](/thread/post/10577980#post10577980 "Post Permalink")

  * Dec 11, 2017 8:02am  Dec 11, 2017 8:02am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar453832_1.gif) jesing](jesing)

  * Joined Mar 2016 | Status: Trader | [294 Posts](/search?do=process&provider=Member&searchuser=453832)

> [Quoting jvbJacques](/thread/post/10577945#post10577945 "View Quoted Post")
> 
> Disliked
> 
> @EVERYONE I am still alive ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1) Sort of ![](https://resources.faireconomy.media/images/emojis/64/1f641.png?v=15.1) Still working to get funds to take off and finish the development on this. Please note that the EA in post one have got nothing to do with renco charts. The renco chart EA is somethings else made by someone else that posted it into this post thread. My EA runs on its own. but it will stop working at the end of 2017 and there are a HECK OF A LOT OF BUGS. Most I know how to fix, but require time to do it in. @jesing I assume you are seeing some of the bugs I already know of. You are welcome...
> 
> Ignored

  
**Thanks For Support...**  
  
\- jesing 

Always Feel Good...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#414](/thread/post/10578714#post10578714 "Post Permalink")

  * Dec 11, 2017 4:50pm  Dec 11, 2017 4:50pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar2942_8.gif) Nicholishen](nicholishen)

  * Joined Jul 2005 | Status: zzzzzzzzzzzzzzzzzzzzzzzzz zzzzzzzzzz | [1,261 Posts](/search?do=process&provider=Member&searchuser=2942)

The term "arbitrage" seems to have somehow lost it's meaning in this thread. Multiple trades with mildly offsetting units is not triangular arbitrage, it's a position, and a foolish one at that. Triangular arbitrage is a purely price driven event that happens in the space of the sub-millisecond market micro-structure. This means if you are using a retail broker and a retail platform, you have no chance in competing banks and hedge-funds for this free money, none. If you still think you are doing arbitrage then you would need to meet the following criteria on 100% of your trades: 1) Achieve a near-instant and 100% market neutral position (on a live account NOT demo or backtester) and 2) cash in on risk-free profits that had zero draw-downs.   
  
It's not triangular arbitrage when there is anything other than a total net-zero position in all instruments, and if there is ever any draw-down then it's a dead giveaway that is not triangular arbitrage. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#415](/thread/post/10598834#post10598834 "Post Permalink")

  * Dec 18, 2017 2:12am  Dec 18, 2017 2:12am 

  * [ fransec](fransec)

  * | Joined Oct 2010  | Status: Trader | [2 Posts](/search?do=process&provider=Member&searchuser=158995)

Hello everyone, sorry for my English but I translate from Google :-). I find your project interested, unfortunately I have to say that this system on retail platforms like Metatrader I do not think can work. My advice is to create such a program on professional platforms like Rithmic 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#416](/thread/post/10619029#post10619029 "Post Permalink")

  * Dec 25, 2017 9:09am  Dec 25, 2017 9:09am 

  * [ rizam34](rizam34)

  * | Joined Sep 2017  | Status: Trader | [44 Posts](/search?do=process&provider=Member&searchuser=611864)

Merry Christmas & Happy New Year Everyone ... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#417](/thread/post/10619835#post10619835 "Post Permalink")

  * Dec 26, 2017 9:48am  Dec 26, 2017 9:48am 

  * [ nantong](nantong)

  * | Joined Oct 2017  | Status: Trader | [17 Posts](/search?do=process&provider=Member&searchuser=621135)

I found these two hedge ea in another forum,hope someone could forward test it. 

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [SoeHoe.ID_ATA_EA_v1.13.ex4](/attachment/file/2612570?d=1514249277) 202 KB | 611 downloads 

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [SoeHoe.ID_CoupleHedgeEA_v1.74(DEMO).ex4](/attachment/file/2612571?d=1514249291) 335 KB | 564 downloads 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#418](/thread/post/10621829#post10621829 "Post Permalink")

  * Dec 27, 2017 4:14pm  Dec 27, 2017 4:14pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar445871_4.gif) leppozdrav](leppozdrav)

  * Joined Feb 2016 | Status: Trader | [113 Posts](/search?do=process&provider=Member&searchuser=445871)

Great thread guys,  
And great work Jvbjacques!  
  
I always had a thing for triangular arbitrage.  
Since we are trading Gbpusd in this case, it might be also good to consider trading hours as an parameter. For example gbpusd has more potential to be pulled in the direction of Jpy currency during the asian session...since Jpy would normaly lead the market during that session. I am not sure if the Ea counts for that...but it might be helpful.  
  
Anyways..let's continue a great work beeing done here. 

The biggest risk is not taking a risk.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#419](/thread/post/10634381#post10634381 "Post Permalink")

  * Edited 4:28pm  Jan 3, 2018 5:01am | Edited 4:28pm 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@EVERYONE  
Happy new year everyone.  
No update yet.  
Will take a long time before I am back on my feet.  
  
In the mean time I have started investing in crypto and it shows promise.  
You can look at my youtube videos where I have also created an automation program.  

Inserted Video

  

Inserted Video

  
  
I am also working on a Davorcoin automation program than should be done by tomorrow.  
  
Funny thing is that it looks like Davorcoin seem to use a simular Arbitrage strategy as this strategy in this forum, just on cryptos.  
I also developed a bitcoin trading strategy that seem to create a lot of potential profit, but I do not have funds to trade it and the brokers that I found with demo accounts do not supply the demo accounts anymore so I can not forward test it.  
  
  
@leppozdrav  
Arbitrage can happen anytime.  
The determining factor is if the arbitrage is big enough to counter the spread and slippage, but timing it might also be good. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#420](/thread/post/10684953#post10684953 "Post Permalink")

  * Jan 18, 2018 7:17pm  Jan 18, 2018 7:17pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar453832_1.gif) jesing](jesing)

  * Joined Mar 2016 | Status: Trader | [294 Posts](/search?do=process&provider=Member&searchuser=453832)

**hello jvbjacques,**  
  
**any update....???**  
  
**still waiting....!!!**  
  
**\- jesing**

Always Feel Good...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Simple High Profit low Drawdown Triangular Arbitrage
  *   * [ **Reply to Thread** ](/thread/676132-simple-high-profit-low-drawdown-triangular-arbitrage/reply#reply)

  * More

[](https://www.forexfactory.com "Homepage")

  * [Forums](forums)
  * [Trades](trades)
  * [Calendar](calendar)
  * [News](news)
  * [Market](market)
  * [Brokers](brokers)

****

[](https://www.faireconomy.com/)

  * 

[Triangular Arbitrage](/thread/64423-triangular-arbitrage "Admin, Please Delete Thread.") 258 replies

[Triangular Arbitrage](/thread/62477-triangular-arbitrage "Is going  
long 1 lot of eur/usd + 
long 1 lot of usd/jpy = long 1 lot of eur/jpy ?  
\(is the ratio of the number of lots correct for a...") 16 replies

[Triangular Arbitrage and carry trade](/thread/71997-triangular-arbitrage-and-carry-trade "Is it possible for us retail traders to be able to make use of Tri Arb or carry trades?  
 
Any one know of retail brokers 
 
 
\(I'm...") 6 replies

[Triangular Arbitrage](/thread/367072-triangular-arbitrage "I've been reading about triangular arbing and was surprised to find that the cross of two majors doesn't always equal what the calculation...") 7 replies

[Question: Trade Mechanics of Triangular Arbitrage](/thread/225246-question-trade-mechanics-of-triangular-arbitrage "Before I even ask this question, please allow me to be very clear.... I have no intention of attempting a triangular arbitrage trade\(for...") 6 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/676132-simple-high-profit-low-drawdown-triangular-arbitrage/reply#reply)
  * Subscribe
  * [147](javascript:void\(0\);)

Attachments: Simple High Profit low Drawdown Triangular Arbitrage

Tags: Simple High Profit low Drawdown Triangular Arbitrage

#  [](/thread/676132-simple-high-profit-low-drawdown-triangular-arbitrage)Simple High Profit low Drawdown Triangular Arbitrage 

  * 

  * [#421](/thread/post/10687207#post10687207 "Post Permalink")

  * Jan 19, 2018 5:22am  Jan 19, 2018 5:22am 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@jesing  
I am sorry I took so long to reply.  
  
Was a rough couple of weeks.  
  
I replied to your pm now.  
  
  
  
@EVERYONE  
I am still here, but the project is still on hold until I can scrape together funds for the development and new pc hardware for the development.  
I will take this up again one day, but it might take many months as I am busy doing as much coding work as possible to build funds so that I can take off and work on this again.  
  
I was even playing with the idea of adapting this strategy to the crypto market and have already learned some of the api of some of the crypto brokers out there so my application can be adapted to it later.  
This strategy benefits a lot from volatility, instability and price lag.  
Forex does work for this, but in all 3 cases crypto currencies are king for this.  
I even played with multiple broker api single crypto currency latency arbitrage, which seem to be huge as unlike forex most broker contain their own trading platforms with minimal price synchronization, basically relying from outside trading the regulate the price at a great profit to those just playing the inefficiencies, but you need a lot of fund on the brokers to trade this profitable.  
  
Still.  
I will get back to the project one day. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#422](/thread/post/10765338#post10765338 "Post Permalink")

  * Feb 11, 2018 12:17am  Feb 11, 2018 12:17am 

  * [ SartSart](sartsart)

  * | Joined Feb 2018  | Status: Trader | [2 Posts](/search?do=process&provider=Member&searchuser=651134)

here is this abitrage trading in mt4 terminal:  
<https://www.mql5.com/ru/signals/394408>

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#423](/thread/post/10776976#post10776976 "Post Permalink")

  * Feb 14, 2018 6:35pm  Feb 14, 2018 6:35pm 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@SartSart  
  
Nice.  
Are you using the strategy in this thread or something else ?  
  
What broker are you using, what is your ping to the broker and what slippage are you getting ?  
What pairs are you using this on ? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#424](/thread/post/10777575#post10777575 "Post Permalink")

  * Edited 10:27pm  Feb 14, 2018 10:02pm | Edited 10:27pm 

  * [ dukas_trader](dukas_trader)

  * | Membership Revoked  | Joined Mar 2010 | [2,525 Posts](/search?do=process&provider=Member&searchuser=136341)

> [Quoting SartSart](/thread/post/10765338#post10765338 "View Quoted Post")
> 
> Disliked
> 
> here is this abitrage trading in mt4 terminal: <https://www.mql5.com/ru/signals/394408>
> 
> Ignored

thats useless with this demo account in best case, i would say its useless 100 times.  
arbitrage trading in demo has always extrem wins, anyone can do it, but why you should do it when it shows nothing! and in real account then no wins or cant pay out.  
  
at least use a cent account, even there the results are not same, but not this extrem like in a demoaccount where all is wrong whats important for this stategy: volume in market, slippage, server connection, data feed,... 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#425](/thread/post/10780149#post10780149 "Post Permalink")

  * Feb 15, 2018 7:35am  Feb 15, 2018 7:35am 

  * [ SartSart](sartsart)

  * | Joined Feb 2018  | Status: Trader | [2 Posts](/search?do=process&provider=Member&searchuser=651134)

1\. i use some modification of triangle arbitrage...  
2\. some guys say anybody can get such profit as mine on demo, well please try and i'll see...  
  
please look at this signal once more at now time status:  
<https://www.mql5.com/ru/signals/394408>

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#426](/thread/post/10788221#post10788221 "Post Permalink")

  * Feb 17, 2018 10:43am  Feb 17, 2018 10:43am 

  * [ theCyberGuy](thecyberguy)

  * | Joined Nov 2016  | Status: Trader | [2 Posts](/search?do=process&provider=Member&searchuser=525834)

> [Quoting jvbJacques](/thread/post/10776976#post10776976 "View Quoted Post")
> 
> Disliked
> 
> @SartSart Nice. Are you using the strategy in this thread or something else ? What broker are you using, what is your ping to the broker and what slippage are you getting ? What pairs are you using this on ?
> 
> Ignored

Hello JVB,   
  
I have been reading the entire forum for a while now and I cant seem to find the most up to date version and also have some confusion over the position sizing.   
  
On the other hand, if you are still looking for the financial backing for your EA, please PM me. thanks 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#427](/thread/post/10790646#post10790646 "Post Permalink")

  * Edited 9:03am  Feb 19, 2018 5:12am | Edited 9:03am 

  * [ dukas_trader](dukas_trader)

  * | Membership Revoked  | Joined Mar 2010 | [2,525 Posts](/search?do=process&provider=Member&searchuser=136341)

> [Quoting SartSart](/thread/post/10780149#post10780149 "View Quoted Post")
> 
> Disliked
> 
> 1\. i use some modification of triangle arbitrage... 2. some guys say anybody can get such profit as mine on demo, well please try and i'll see... please look at this signal once more at now time status: <https://www.mql5.com/ru/signals/394408>
> 
> Ignored

ok, somebody get much more win then you have on demo, but why you are so proud to fake wins much more big then others or smaller then other, near nobody trades your bullshit garbage any more, because its usless waste of time and only beginners and scammers do so? never ever compete your fake wins (and nothing more you have, only fake wins in demo account with arbitrage trading, what would be not this wins and often even losses in real account trading) with other fake wins, thats stupid. and dont ask some people to show same fake wins like you, thats even double stupid. noone has this time to invest to show this garbage fake wins for nothing, at maximum when you want sell this garbage bullshit to idiots later when you work as a scammer.  
  
it really looks like you know its big fake wins you have never ever in real account (even a big lose same time) or you dont know anything about trading? whats the reason to fake this wins and present a demo where arbitrage experts have always extrem wins?  
you want other also lose time with this worthless trading style and later want sell other idiots and beginners this garbage expert? or whats your reason behind testing useless garbage arbitrage expert in demaccount?? i see this coming with yourt style of writing that you want sell really this as a big scam. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#428](/thread/post/10799878#post10799878 "Post Permalink")

  * Feb 21, 2018 7:58pm  Feb 21, 2018 7:58pm 

  * [ swatch](swatch)

  * | Joined Feb 2018  | Status: Trader | [5 Posts](/search?do=process&provider=Member&searchuser=654206)

Hi,  
  
I am looking to do this 2 symbols only... I am looking for a EA/script that places buy and sell market orders on two FX pairs simultaneously - for example buy EUR/USD and sell GBP/USD.  
  
I do not want any SL or TP, just to be able to specify the particular symbol to buy and the symbol to sell, and their relevant volume. I am quite new to that, please help me. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#429](/thread/post/10870994#post10870994 "Post Permalink")

  * Mar 14, 2018 6:41pm  Mar 14, 2018 6:41pm 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@EVERYONE  
  
140% profit in less than 50 minutes.  
(Unrealistic I know based on a lot of factors, but still a nice prove of concept.)  
  
I could not stop myself so I created a little program to connect to Binance, just to see if it was even possible to make profit using triangular arbitrage on the real crypto market seeing that I understand the theory and have done successful tests on forex and manual tests on crypto, but never on the live crypto market.  
  
Understand that this was only a test and therefore I ignored the trading volume.  
You can only trade whatever volume is available and not more, therefore the profit is based on what is there and not your total account size.  
  
During my older tests I found that the crypto market is much more volatile and slow, compared to forex.  
Therefore it only made sense to me that a triangular arbitrage strategy that loves volatile markets and the slower the better, that it will work much better on the crypto market.  
  
Looking at the logs you can calculate the arbitrage manually to verify the results.  
There are 3 lines indicating which cryptos were used in the arbitrage. Symbol1, symbol2, symbol3.  
Each one also shows the ASK end BID prices at that time, which you must use in your arbitrage triangle calculation.  
Remember to subtract 0.05% after each of the 3 calculations for trading cost.  
The last *** line contains the total running profit if 1 bitcoin was traded every time, by only using the biggest profit during that round and not all.  
Also keep in mind the program only ran once every 5 seconds, so it missed a LOT of arbitrage signals in-between as it can run once every 0.001 seconds, depending on the exchange rules and connection speed, so it can potentially make a lot more profit.  
  
Basically the program checks the ASK and BID prices of all available currencies in the exchange for arbitrage opportunities once every 5 seconds.  
If multiple arbitrage opportunities are found then it only use the highest profit potential one for its profit calculation and ignores the rest.  
  
I ran it a couple of times, but here is the last part of my last run :  
Obviously you will trade with less volume so the profit will decrease a lot, but still it proves that there is a lot of profit to be made.  
  

Inserted Code
    
    
    2018-03-14 10h30s55m289 Starting
    Parameters *******
     Profit is dependent on :
         1) Server connection speed to exchange.
         2) Volume available for trading as you can not trade bigger volume than what is available.
         3) How often profit potential is checked. This test only does it once every 5 seconds
            , but can be increased to once every 0.001 seconds for much greater profit, depending on exchange rules and connection limitations.
         4) Persentage profit displayed is based on no slippage (1) and an unlimited volume (2).
         5) Exchanges with bigger trading volumes can make bigger profit so long as their trading costs are not too high.
         6) This test is run on Binance and performance will be different for other exchanges. (Better or worse), but can be tested before trading for real.
     Trading Fee=0.0500%
     Check for arbitrage potential every 5 seconds
    .
    .
    . **** logs cut out to fit. See attached log file for full log.****
    .
    
    2018-03-14 11h18s48m434 IS PROFIT POSSIBLE cc= 473 Profit = 1
    2018-03-14 11h18s50m239 Get all prices available.
    2018-03-14 11h18s50m740
    symbol1=BNBBTC ASK=0.00113300 Volume=315.88000000 BID=0.00113170 Volume=4.41000000
    symbol2=BCPTBNB ASK=0.06280000 Volume=0.53000000 BID=0.06249000 Volume=150.00000000
    symbol3=BCPTBTC ASK=0.00007135 Volume=984.00000000 BID=0.00007133 Volume=2123.00000000
    2018-03-14 11h18s50m740 symbol1=882.17122683135105 symbol2=14040.28887289701920 symbol3=1.00099305840109250734623200 result=1
    2018-03-14 11h18s50m740 symbol3=14008.40925017517275 symbol2=874.94780129642482187492625000 symbol1=0.98968333751380038893039611010643750000 result=-1
    2018-03-14 11h18s50m740
    symbol1=ETHBTC ASK=0.07599500 Volume=0.07000000 BID=0.07591300 Volume=0.75900000
    symbol2=LUNETH ASK=0.02197200 Volume=16.76000000 BID=0.02190000 Volume=0.01000000
    symbol3=LUNBTC ASK=0.00165640 Volume=44.31000000 BID=0.00165280 Volume=2.00000000
    2018-03-14 11h18s50m740 symbol1=13.15218106447765 symbol2=598.28895748879270 symbol3=0.98835756294300783627272000 result=-1
    2018-03-14 11h18s50m740 symbol3=603.41704902196190 symbol2=13.20822595689417512719500000 symbol1=1.00217471903717466267253865798250000000 result=1
    2018-03-14 11h18s50m742 Profit check done************************************************ totalProfit=1.40569746874650179693713299799745550000 Percentage Total Profit=140.56974687465017969371329979974555000000 %    biggestProfitDuringRound=1.00217471903717466267253865798250000000
     
     
    
    2018-03-14 11h18s55m742 IS PROFIT POSSIBLE cc= 474 Profit = 1
    2018-03-14 11h18s56m268 Get all prices available.
    2018-03-14 11h18s56m770
    symbol1=BNBBTC ASK=0.00113300 Volume=327.52000000 BID=0.00113290 Volume=0.01000000
    symbol2=BCPTBNB ASK=0.06280000 Volume=0.53000000 BID=0.06250000 Volume=92.90000000
    symbol3=BCPTBTC ASK=0.00007135 Volume=984.00000000 BID=0.00007133 Volume=2120.00000000
    2018-03-14 11h18s56m770 symbol1=882.17122683135105 symbol2=14040.28887289701920 symbol3=1.00099305840109250734623200 result=1
    2018-03-14 11h18s56m770 symbol3=14008.40925017517275 symbol2=875.08781534688032272656250000 symbol1=0.99089129251347747725811419492187500000 result=-1
    2018-03-14 11h18s56m771
    symbol1=ETHBTC ASK=0.07600400 Volume=0.61700000 BID=0.07592100 Volume=0.33800000
    symbol2=LUNETH ASK=0.02197200 Volume=16.76000000 BID=0.02190000 Volume=0.01000000
    symbol3=LUNBTC ASK=0.00165640 Volume=44.31000000 BID=0.00165280 Volume=2.00000000
    2018-03-14 11h18s56m771 symbol1=13.15062365137375 symbol2=598.21811121185160 symbol3=0.98824052676384285031776000 result=-1
    2018-03-14 11h18s56m771 symbol3=603.41704902196190 symbol2=13.20822595689417512719500000 symbol1=1.00228033201192598849685570920250000000 result=1
    2018-03-14 11h18s56m772 Profit check done************************************************ totalProfit=1.40797780075842778543398870719995550000 Percentage Total Profit=140.79778007584277854339887071999555000000 %    biggestProfitDuringRound=1.00228033201192598849685570920250000000

Attached File(s)

![File Type: txt](https://assets.faireconomy.media/images/attach/txt.gif) [CryTri2018-03-14 10h30s54m250.txt](/attachment/file/2716922?d=1521019957) 649 KB | 649 downloads 

[0 ](javascript:void\(0\);) [3 ](javascript:void\(0\);)

  * [#430](/thread/post/10873225#post10873225 "Post Permalink")

  * Mar 15, 2018 5:01am  Mar 15, 2018 5:01am 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

Some more logs.  
  
I left the program running in a continues loop.  
So far it ran 6735 times, once every 5 seconds for a demo profit of 1507%.  
  
Unfortunately My connection is to slow for live trading testing, but the crypto works and the way I adapted the strategy to crypto, you can trade with as little as you want on the exchange.  
$1 if you want, but I think the exchange limit might be $10 or more, depending on the transaction cost of bitcoin. 

Attached File(s)

![File Type: zip](https://assets.faireconomy.media/images/attach/zip.gif) [CryTri2018-03-14 10h30s54m250.txt.zip](/attachment/file/2717925?d=1521057451) 1.1 MB | 1,150 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#431](/thread/post/10873305#post10873305 "Post Permalink")

  * Mar 15, 2018 5:36am  Mar 15, 2018 5:36am 

  * [ amando77](amando77)

  * | Joined Nov 2008  | Status: Trader | [91 Posts](/search?do=process&provider=Member&searchuser=85299)

try to use it on MT5 but i get some error  
  
2018.03.14 21:33:53.490 2017-09-18 09h00 JVB Arbitrage Auto Profit19 (USDJPY,H1) **** ERROR1=lastError=**** ERROR at=Time=2018-3-14 21:33 newError=4302 in_Str=Start1 lastStr=  
  
can you help?  
  
thanks 

The biggest drawdown is ahead of you

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#432](/thread/post/10873346#post10873346 "Post Permalink")

  * Mar 15, 2018 5:57am  Mar 15, 2018 5:57am 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@amando77  
  
I disabled all EAs as it stands now for anything beyond 2017.  
There are many bugs in the code.  
  
Too many for me to fix in the little free time I have.  
  
As it stands now I am saving up to fund further development, but at the moment development is standing still.  
I have created an indigogo campaign in the hopes of getting some funding for the development and testing process.  
  
When I get back on my feet I will update this forum with a new post on it again.  
  
Error 4302 basically means you did not load the symbol in the market watch window.  
Make sure all 3 symbols/currencies are loaded.  
Open their charts just to make sure.  
Then the error should go away. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#433](/thread/post/10874980#post10874980 "Post Permalink")

  * Edited 7:59pm  Mar 15, 2018 7:42pm | Edited 7:59pm 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@EVERYONE  
  
Another interesting update.  
  
I modified the program to artificially delay the profit calculations.  
  
Basically.  
I check the prices and determine if there is an triangular arbitrage opportunity like normal.  
I then wait for 1 to 2 seconds and then ask for the prices again and then I force the program to trade the arbitrage opportunity it detected previously, whatever the outcome.  
This simulates my pathetic internet connection by saying to only trade the arbitrage 1 to 2 seconds later.  
  
As you can see at the end of the attached logs there are 2 losing trades.  
There are many more losing trades in the log because of this massive delay also.  
  
But as explained in post one, even with losing trades because of slippage, in the long run the profitable trades cancels them out and still makes profit seeing that triangular arbitrage by its nature contains extremely low draw down.  
  
Ultimately the logs were started at 2018-03-14 23h49s14m068 and ran until 2018-03-15 12h21s01m795 for a total profit of 1466% over the 13 hours it ran.  
  
Keep in mind that it trades as if there is no limit to the volume of the currency and therefore in reality the profit for the total account will be much less seeing it can only trade what is available.  
Also keep in mind that the program only checks for opportunities once every 5 seconds and it can be sped up to twice a second or even more if the exchange allows that many trades.  
  
Speed wise I suspect the exchange limits trades to 8 a second and for triangular arbitrage you require 3 trades to make the round trip, so 2 program runs equals 6 trades and therefore 2 runs a second is possible.  
  
Some information about reading the logs :  
In the log CC = indicates the loop number of the program.  
There is 2 CCs per loop.  
The program starts on a odd number EXAMPLE CC=21;  
The program only does the actual profit calculation on an even number EXAMPLE CC=22.  
  
Therefore in the logs odd CC numbers check for opportunities and only even CC numbers contain the profit calculation after some delay.  
So the profit is displayed after an even CC number loop.  
  
For easy viewing you will see **** and .... lines after the even CC loop.  
**** mean that there was no slippage since the opportunity was detected during the odd CC loop.  
.... mean that there was slippage since the opportunity was detected during the odd CC loop.  
  
At the end of each of those lines you will see the biggestProfitDuringRound variable that shows if profit was made or not.  
If biggestProfitDuringRound is bigger than 1 then profit was made.  
If biggestProfitDuringRound is smaller that 1 then a loss was made.  
  
Percentage Total Profit=The total running profit/loss so far.  
  
It seems like arbitrage opportunities tend to stick around for a while in crypto markets, unlike fiat where it happens in a split second. 

Attached File(s)

![File Type: zip](https://assets.faireconomy.media/images/attach/zip.gif) [CryTri2018-03-14 23h49s13m234.txt.zip](/attachment/file/2718823?d=1521109487) 1.5 MB | 824 downloads 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#434](/thread/post/10914961#post10914961 "Post Permalink")

  * Edited 1:29pm  Mar 28, 2018 1:12pm | Edited 1:29pm 

  * [ avch1202](avch1202)

  * | Joined Mar 2018  | Status: Trader | [1 Post](/search?do=process&provider=Member&searchuser=664675)

Hello JVB, Im novate in the trading, and interested on your EA [Triangular Arbitrage](https://www.forexfactory.com/showthread.php?p=10345498). I ve download the last version 2017-09-18 for mt4, but I dont know how it works.  
  
Could you help me, please.  
  
My email is  
  
alejandro  
.  
vielma  
@  
gmail  
.  
com  
  
  
Best regards  
  
From Chile 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#435](/thread/post/10925508#post10925508 "Post Permalink")

  * Apr 1, 2018 5:54pm  Apr 1, 2018 5:54pm 

  * [ k0ngoz](k0ngoz)

  * | Joined Nov 2015  | Status: Trader | [1 Post](/search?do=process&provider=Member&searchuser=434810)

> [Quoting jvbJacques](/thread/post/10874980#post10874980 "View Quoted Post")
> 
> Disliked
> 
> @EVERYONE Another interesting update. I modified the program to artificially delay the profit calculations. Basically. I check the prices and determine if there is an triangular arbitrage opportunity like normal. I then wait for 1 to 2 seconds and then ask for the prices again and then I force the program to trade the arbitrage opportunity it detected previously, whatever the outcome. This simulates my pathetic internet connection by saying to only trade the arbitrage 1 to 2 seconds later. As you can see at the end of the attached logs there are...
> 
> Ignored

Your algo looks very interesting, im currently working on something similar on binance aswell.  
Do you use skype or discord? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#436](/thread/post/10927532#post10927532 "Post Permalink")

  * Apr 2, 2018 10:27pm  Apr 2, 2018 10:27pm 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@avch1202  
The EA will not work past 2017 until I can get around to update it again.  
My email jvbccc at gmail  
  
@k0ngoz  
Nice.  
Hope your binance program work good.  
I am having a lot of fun on binance and discovered some nice functions and strategies.  
I mostly use email and whatsapp.  
PM me for email and whatsapp information.  
My email jvbccc at gmail 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#437](/thread/post/11108294#post11108294 "Post Permalink")

  * May 29, 2018 8:21am  May 29, 2018 8:21am 

  * [ M.Azeem](m.azeem)

  * | Joined Aug 2016  | Status: Trader | [1 Post](/search?do=process&provider=Member&searchuser=482983)

Dear JVB  
Can you post last updated virgin also what is recommended setting and time frame too? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#438](/thread/post/11125394#post11125394 "Post Permalink")

  * Jun 2, 2018 12:51am  Jun 2, 2018 12:51am 

  * [ polenergy](polenergy)

  * | Joined Jun 2018  | Status: Trader | [2 Posts](/search?do=process&provider=Member&searchuser=683768)

Hi JVB,  
  
Concerning your Binance Bot. IN your logfile I see that you did the trades always with 1 BTC, but there is not always enough liquidity in the order book.  
  
Here the example: you have not enough volume in the order book to fill the orders:  
  
symbol1=BNBBTC ASK=0.00107670 Volume=85.23000000 BID=0.00107520 Volume=32.07000000  
symbol2=VENBNB ASK=0.43640000 Volume=0.30000000 BID=0.43560000 Volume=470.13000000  
symbol3=VENBTC ASK=0.00047216 Volume=10.00000000 BID=0.00047150 Volume=2006.00000000  
2018-03-14 23h49s31m036 symbol1=928.29943345401915 symbol2=2126.11201589655080 symbol3=1.00196058458747609034890000 result=1  
2018-03-14 23h49s31m036 symbol3=2116.86716367323170 symbol2=921.64628282781169865574000000 symbol1=0.99045860625481490682545432217600000000 result=-1  
2018-03-14 23h49s31m075 Profit check done************************************************ Quick ***  
  
  
Can I ask you which profit percentage you are getting in real?  
Thanks for your reply![](https://resources.faireconomy.media/images/emojis/64/1f604.png?v=15.1)  
Best regards,  
Polenergy 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#439](/thread/post/11164354#post11164354 "Post Permalink")

  * Edited 6:56am  Jun 14, 2018 6:42am | Edited 6:56am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar53444_2.gif) dagoods](dagoods)

  * Joined Nov 2007 | Status: Trader | [3,059 Posts](/search?do=process&provider=Member&searchuser=53444)

> [Quoting jvbJacques](/thread/post/10323597#post10323597 "View Quoted Post")
> 
> Disliked
> 
> @Everyone I did not include the modifiable parameters into the EAs. The newly attached ones contains the parameters so you can make sure the symbols match your broker's symbols. Keep in mind that the EAs is set to not use a lot of your account balance. If you back-test you will see the maximum draw-down is quite low. A 3rd parameter allows you to set the amount in % .. 0.5 = 50% of the account balance not to use. If you want to make it aggressive then try 0.1 or 0.2 on a leverage of 1:200. Problem is not that you will bottom out your account, but...
> 
> Ignored

It does not make sense to my brain. Why can you not get out of your losses at break even then? There will always be a day when price goes the other way, no matter how strong of a trend. If we are talking 10 -20 pips. (take a trade wait for +- 10 pips, THEN hedge). Then why can't you always get out of your losses at break even? You may have to wait a week, but so what? I'm calling my idea a straddled triangular hedge. My crazy brain invented it. LOL What am i missing? ![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#440](/thread/post/11166807#post11166807 "Post Permalink")

  * Jun 14, 2018 9:44pm  Jun 14, 2018 9:44pm 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@EVERYONE  
Long time no see.  
  
I made a lot of test EAs.  
One triangular arbitrage is even running live on Binance.  
Some good profits at about 0.2% profit a day.  
Then again it is not very aggressive, but wow there is a lot of slippage.  
Mostly because there is a large delay from the time your market order completes, till the time the new funds of that market order reflects in my account and in the mean time the market slips away.  
  
That and there is not nearly the same amount of volume as on forex ![](https://resources.faireconomy.media/images/emojis/64/1f641.png?v=15.1)  
Still.  
Not bad.  
  
  
I also found a good way to make some peanuts by applying a grid onto the TUSD/USDT symbol pair for some nice profits, without worrying about slippage much as these are limit orders and set long ahead of time.  
Stable coins seem to be a very nice place to make some good profit for their natural arbitrage opportunities on the same exchange even.  
  
  
  
@polenergy  
You are correct.  
That time I was not running it on a real account yet.  
  
Now I am.  
Profit is very low, but still good for me.  
Started with 19.63298312 BNB and ended with 19.66216005 BNB.  
That is 0.148611802 % profit in 7 hours.  
  
You can see it in the logs by searching for "checkArb start=accountBalance=".  
  
In the attached logs you will see a 7 hour snippet before the EA crashed because BINANCE did not update my account balance in time after the last order.  
I inserted more checks since then and it does not crash anymore, but wow sometimes it can take ages for the account balance to reflect and I am still looking for a solution to that, because it eats a LOT of profit.  
  
The logs contain multiple strategies running together, but only the triangular one is running on live money.  
1) Triangular arbitrage  
Search for "CryTri{checkIfProfitPossible(resultZero)} retestCC=2"  
"retestCC=1" is failed tests and not traded for multiple reasons, but mostly because of the binance API problems and to somehow bypass those problems.  
If binance can sort out there API delays then you can see that the triangular EA have got multiple times more hits it can process, but until then "retestCC=2" will do for now ![](https://resources.faireconomy.media/images/emojis/64/1f641.png?v=15.1)  
  
There is a lot of A.I code in there so maybe one day I will explain, but it is running well.  
Can use a lot more TLC to improve the code to run faster and more profitable.  
  
  
2) Grid EAs  
There are multiple grid EAs running.  
Search for:  
GridSpikeHalfStrategy{} thisName=GridSpikeHalfStrategyName=isIncreaseAccountUsage=false isSwapCurrencies=false gridPriceStepPercentage=0.0004 gridAccountPercentage=0.1 GridSpikeHalfStrategy{} thisName=GridSpikeHalfStrategyName=isIncreaseAccountUsage=true isSwapCurrencies=false gridPriceStepPercentage=0.0004 gridAccountPercentage=0.1 GridSpikeHalfStrategy{} thisName=GridSpikeHalfStrategyName=isIncreaseAccountUsage=false isSwapCurrencies=true gridPriceStepPercentage=0.0004 gridAccountPercentage=0.1 GridSpikeHalfStrategy{} thisName=GridSpikeHalfStrategyName=isIncreaseAccountUsage=true isSwapCurrencies=true gridPriceStepPercentage=0.0004 gridAccountPercentage=0.1 GridPreCalcStrategy{} thisName=GridPreCalcStrategyName=isSwapCurrencies=false gridPriceSizePerc=0.0001 in_GridMaxLevels=20  
GridPreCalcStrategy{} thisName=GridPreCalcStrategyName=isSwapCurrencies=false gridPriceSizePerc=0.0002 in_GridMaxLevels=20  
GridPreCalcStrategy{} thisName=GridPreCalcStrategyName=isSwapCurrencies=false gridPriceSizePerc=0.0005 in_GridMaxLevels=20  
GridPreCalcStrategy{} thisName=GridPreCalcStrategyName=isSwapCurrencies=false gridPriceSizePerc=0.001 in_GridMaxLevels=20  
GridPreCalcStrategy{} thisName=GridPreCalcStrategyName=isSwapCurrencies=false gridPriceSizePerc=0.002 in_GridMaxLevels=20  
GridPreCalcStrategy{} thisName=GridPreCalcStrategyName=isSwapCurrencies=false gridPriceSizePerc=0.005 in_GridMaxLevels=20  
  
3)  
The best grid strategy I just started testing now so it still need to prove itself, but it looks good in theory and runs on the above mentioned TUSD/USDT grid arbitrage strategy.  
Looks like it will even run better than the triangular arbitrage.  
Not because the triangular does not work as it has proven itself, but binance seem to have problems with their API interface and that interferes less with the grid EA than it does to the triangular EA.  
  
  
  
@Dagoods  
It also does not make sense to my brain.  
Maybe if you can explain your question in another way I can answer you.  
Maybe I am just to tired to understand at the moment and for that I am sorry. Not you fault. My brain is week at the moment ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1) need zzzzzz  
  
If you meant to ask why I do not keep the triangle open all the time and way for profit.  
Short answer is . "SWAP"  
Swap is a killer so I want to be in and out as fast as possible.  
  
As for the crypto version of the triangle.  
My crypto EA works differently in that it transfers the money to actual live wallets, but as I am typing I realise that I probably can buy and hold.  
Problem is that then you have to home all the potential arbitrage wallets as I play in all of them using the current method.  
Not only is that very expensive, bit will also decrease the profit as your account is not split between a hundred wallets and normally only one hit on one wallet happens at a time and a very small hit.  
Binance have got no good leverage system in place for this and then only good leverage is bitmex and they only have pairs connected to BTC, so no triangle is possible.  
  
Still there is a lot to do. 

Attached File(s)

![File Type: zip](https://assets.faireconomy.media/images/attach/zip.gif) [CryTri2018-06-10 10h56s42m820.zip](/attachment/file/2851739?d=1528978576) 52 KB | 992 downloads 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Simple High Profit low Drawdown Triangular Arbitrage
  *   * [ **Reply to Thread** ](/thread/676132-simple-high-profit-low-drawdown-triangular-arbitrage/reply#reply)

  * More

[](https://www.forexfactory.com "Homepage")

  * [Forums](forums)
  * [Trades](trades)
  * [Calendar](calendar)
  * [News](news)
  * [Market](market)
  * [Brokers](brokers)

****

[](https://www.faireconomy.com/)

  * 

[Triangular Arbitrage](/thread/64423-triangular-arbitrage "Admin, Please Delete Thread.") 258 replies

[Triangular Arbitrage](/thread/62477-triangular-arbitrage "Is going  
long 1 lot of eur/usd + 
long 1 lot of usd/jpy = long 1 lot of eur/jpy ?  
\(is the ratio of the number of lots correct for a...") 16 replies

[Triangular Arbitrage and carry trade](/thread/71997-triangular-arbitrage-and-carry-trade "Is it possible for us retail traders to be able to make use of Tri Arb or carry trades?  
 
Any one know of retail brokers 
 
 
\(I'm...") 6 replies

[Triangular Arbitrage](/thread/367072-triangular-arbitrage "I've been reading about triangular arbing and was surprised to find that the cross of two majors doesn't always equal what the calculation...") 7 replies

[Question: Trade Mechanics of Triangular Arbitrage](/thread/225246-question-trade-mechanics-of-triangular-arbitrage "Before I even ask this question, please allow me to be very clear.... I have no intention of attempting a triangular arbitrage trade\(for...") 6 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/676132-simple-high-profit-low-drawdown-triangular-arbitrage/reply#reply)
  * Subscribe
  * [147](javascript:void\(0\);)

Attachments: Simple High Profit low Drawdown Triangular Arbitrage

Tags: Simple High Profit low Drawdown Triangular Arbitrage

#  [](/thread/676132-simple-high-profit-low-drawdown-triangular-arbitrage)Simple High Profit low Drawdown Triangular Arbitrage 

  * 

  * [#441](/thread/post/11309089#post11309089 "Post Permalink")

  * Jul 28, 2018 5:29pm  Jul 28, 2018 5:29pm 

  * [ dareking](dareking)

  * | Joined May 2012  | Status: Trader | [116 Posts](/search?do=process&provider=Member&searchuser=253845)

> [Quoting jvbJacques](/thread/post/9988492#post9988492 "View Quoted Post")
> 
> Disliked
> 
> I will always update this POST #1 with the latest information. So if you do not want to read all the posts then just read this one. I will also keep the EAs up to date here. The rest of the posts are interesting and I love flame wars ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1) ******************************* Very basic summary ******************************* 1) Buy 1 unit GBPJPY 2) Sell 1 unit GBPUSD 3) Sell ?? units using the USD in point (2) in USDJPY to balance everything out Buy low and sell high. Rinse and repeat. Can this work or what is the pitfalls with this idea ? *******************************...
> 
> Ignored

Hi friends Thank you for your best system, I was searching this EA, Please i need some Help from You,  
  
I m unable to test this EA on Meta trader tester i want to test this EA so i have active this EA on Live market?  
  
Time frame M1? pair? Please need some help thank you 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#442](/thread/post/11309115#post11309115 "Post Permalink")

  * Jul 28, 2018 5:46pm  Jul 28, 2018 5:46pm 

  * [ goodways100](goodways100)

  * Joined Dec 2013 | Status: Trader | [615 Posts](/search?do=process&provider=Member&searchuser=358325)

Subs. thanks and  
Regards 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#443](/thread/post/11679241#post11679241 "Post Permalink")

  * Nov 10, 2018 5:13am  Nov 10, 2018 5:13am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar648528_1.gif) samet](samet)

  * Joined Feb 2018 | Status: Trader | [219 Posts](/search?do=process&provider=Member&searchuser=648528)

similiar one ı have maybe u guys want to test ( theres little differences between these eas ) 

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [kucluk1.ex4](/attachment/file/3082399?d=1541794330) 13 KB | 698 downloads 

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [kucluk2 (1).ex4](/attachment/file/3082401?d=1541794340) 16 KB | 661 downloads 

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [kucluk3.ex4](/attachment/file/3082402?d=1541794347) 13 KB | 735 downloads 

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [Kucluk_ProfitLock.ex4](/attachment/file/3082405?d=1541794357) 13 KB | 879 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#444](/thread/post/12207786#post12207786 "Post Permalink")

  * Apr 9, 2019 8:53pm  Apr 9, 2019 8:53pm 

  * [ D-TickTrader](d-ticktrader)

  * | Joined Dec 2009  | Status: Trader | [28 Posts](/search?do=process&provider=Member&searchuser=126054)

Hello Experts  
  
I was reading this thread, I searched on google and this came out, because I am watching this. I have no Ideas of any coding or so.  
  
I am watching these accounts and its Triangular Correlation, making every single day money with very very low DD.  
  
If any expert can understand make EA.  
  
Really appreciate what you do here.  
Thank you   
  
60304  
r6pimbd  
CSIGroupLtd-Live  
  
84899440  
alD1ouk  
CSIGroupLtd-Live  
  
60500  
fu4gzmr  
CSIGroupLtd-Live  
  
Login only on the Phone.  
  
Thank You 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#445](/thread/post/12223017#post12223017 "Post Permalink")

  * Apr 14, 2019 4:00am  Apr 14, 2019 4:00am 

  * [ peterbabs](peterbabs)

  * | Joined Aug 2007  | Status: Trader | [29 Posts](/search?do=process&provider=Member&searchuser=45365)

> [Quoting D-TickTrader](/thread/post/12207786#post12207786 "View Quoted Post")
> 
> Disliked
> 
> Hello Experts I was reading this thread, I searched on google and this came out, because I am watching this. I have no Ideas of any coding or so. I am watching these accounts and its Triangular Correlation, making every single day money with very very low DD. If any expert can understand make EA. Really appreciate what you do here. Thank you 60304 r6pimbd CSIGroupLtd-Live 84899440 alD1ouk CSIGroupLtd-Live 60500 fu4gzmr CSIGroupLtd-Live Login only on the Phone. Thank You
> 
> Ignored

Hi D-TickTrader,  
I like what I saw. ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
I can make an EA for it if I understand the following:  
  
What makes it work when the batch closes positive? And what makes it failed when it's negative.  
Is there any time lag between the entries? It only showed the hour and minute. I'd love to see the timestamp to the second.  
Were the trades entered and closed manually or with an EA?  
Your response is appreciated. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#446](/thread/post/12223286#post12223286 "Post Permalink")

  * Apr 14, 2019 6:05pm  Apr 14, 2019 6:05pm 

  * [ kakashis](kakashis)

  * | Joined Apr 2019  | Status: Trader | [3 Posts](/search?do=process&provider=Member&searchuser=795484)

I'm just plucking these ABCD patterns in as per Mr. Pips rules and seeing how I go. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#447](/thread/post/12226809#post12226809 "Post Permalink")

  * Apr 17, 2019 12:09am  Apr 17, 2019 12:09am 

  * [ D-TickTrader](d-ticktrader)

  * | Joined Dec 2009  | Status: Trader | [28 Posts](/search?do=process&provider=Member&searchuser=126054)

> [Quoting kakashis](/thread/post/12223286#post12223286 "View Quoted Post")
> 
> Disliked
> 
> I'm just plucking these ABCD patterns in as per Mr. Pips rules and seeing how I go.
> 
> Ignored

Hello Peterbabs  
  
I have only the same access which you have just to watch the account, as I said I have no knowledge of any coding.  
So I have no there more information then same as you can have to long in the accounts and just watch that with very very low DD making daily profit.  
  
Those are not my accounts.  
  
Thank you for taking time. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#448](/thread/post/12243561#post12243561 "Post Permalink")

  * Apr 29, 2019 10:42am  Apr 29, 2019 10:42am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar53444_2.gif) dagoods](dagoods)

  * Joined Nov 2007 | Status: Trader | [3,059 Posts](/search?do=process&provider=Member&searchuser=53444)

Any update for with this. Appreciate the sound ideas/theories. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#449](/thread/post/12300653#post12300653 "Post Permalink")

  * May 30, 2019 4:45pm  May 30, 2019 4:45pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar474698_2.gif) stevanuss](stevanuss)

  * | Joined Jul 2016  | Status: Anak Betawi | [401 Posts](/search?do=process&provider=Member&searchuser=474698)

> [Quoting samet](/thread/post/11679241#post11679241 "View Quoted Post")
> 
> Disliked
> 
> similiar one ı have maybe u guys want to test ( theres little differences between these eas ) {file} {file} {file} {file}
> 
> Ignored

![](https://resources.faireconomy.media/images/emojis/64/1f62c.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f62c.png?v=15.1) Thats my EA, I build that 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#450](/thread/post/12374191#post12374191 "Post Permalink")

  * Jul 10, 2019 5:57pm  Jul 10, 2019 5:57pm 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

Hi all  
  
Long time no talk.  
  
Difficult to find time to work on trading, but I did do a lot and got a small update on what I have more recently did:  
  
Look at this thread :  
[https://www.forexfactory.com/showthr...4#post12374184](https://www.forexfactory.com/showthread.php?p=12374184#post12374184)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#451](/thread/post/12374683#post12374683 "Post Permalink")

  * Jul 10, 2019 9:46pm  Jul 10, 2019 9:46pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar71675_5.gif) Alberto_Jazz](alberto_jazz)

  * Joined Jun 2008 | Status: Trader | [593 Posts](/search?do=process&provider=Member&searchuser=71675)

Hi jvbJacques, could you describe how do you calculate the average profit in the first post?  
Thank you!  
  

> [Quoting jvbJacques](/thread/post/9988492#post9988492 "View Quoted Post")
> 
> Disliked
> 
> I now calculate what the average profit would be if I did a BUY, SELL, SELL and also SELL,BUY,BUY.  
>  This gives me 2 lines.  
>  Call the higher line the ASK line and the lower line the BUY line.  
>  Between the 2 lines is the average line calculated over some time, which if mostly a straight line as the buy and sell lines basically cancels each other out there.
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#452](/thread/post/12411414#post12411414 "Post Permalink")

  * Jul 30, 2019 11:17pm  Jul 30, 2019 11:17pm 

  * [ geniousphp](geniousphp)

  * | Joined May 2019  | Status: Trader | [9 Posts](/search?do=process&provider=Member&searchuser=807345)

> [Quoting D-TickTrader](/thread/post/12207786#post12207786 "View Quoted Post")
> 
> Disliked
> 
> Hello Experts I was reading this thread, I searched on google and this came out, because I am watching this. I have no Ideas of any coding or so. I am watching these accounts and its Triangular Correlation, making every single day money with very very low DD. If any expert can understand make EA. Really appreciate what you do here. Thank you 60304 r6pimbd CSIGroupLtd-Live 84899440 alD1ouk CSIGroupLtd-Live 60500 fu4gzmr CSIGroupLtd-Live Login only on the Phone. Thank You
> 
> Ignored

Recently, I was watching this account closely and it seems the results is fabricated. For example it shows that the trade is closes at a specific time while it was closed few minutes later. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#453](/thread/post/12434493#post12434493 "Post Permalink")

  * Aug 11, 2019 8:47pm  Aug 11, 2019 8:47pm 

  * [ mps](mps)

  * | Joined Oct 2016  | Status: Trader | [5 Posts](/search?do=process&provider=Member&searchuser=524154)

> [Quoting D-TickTrader](/thread/post/12207786#post12207786 "View Quoted Post")
> 
> Disliked
> 
> Hello Experts I was reading this thread, I searched on google and this came out, because I am watching this. I have no Ideas of any coding or so. I am watching these accounts and its Triangular Correlation, making every single day money with very very low DD. If any expert can understand make EA. Really appreciate what you do here. Thank you 60304 r6pimbd CSIGroupLtd-Live 84899440 alD1ouk CSIGroupLtd-Live 60500 fu4gzmr CSIGroupLtd-Live Login only on the Phone. Thank You
> 
> Ignored

good morning. interesting these accounts ... but which and where do you use robots? thank you 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#454](/thread/post/12511984#post12511984 "Post Permalink")

  * Sep 19, 2019 4:08pm  Sep 19, 2019 4:08pm 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@Alberto_Jazz  
As explained.  
I do the calculation on a BUY,SELL,SELL round trip and get a result.  
I plot that result on the chart as a point.  
  
I then do the calculation on a SELL,BUY,BUY round trip and get a result.  
I plot that result on the chart as a point.  
  
The average is a point in the middle between these 2 points.  
  
I then repeat this for every tick coming in and then all the points form the 3 lines.  
  
  
@geniousphp  
@mps  
I have seen a couple of these accounts.  
I can not say if they are true or scams.  
One I could figure out was a more basic version than my strategy that does not account for slippage.  
Now that made me think on where it runs.  
I found for that one that the strategy was run directly on the bank's servers using a ridiculously fast connection.  
Basically getting to the orders before everyone else ... therefore no slippage.  
  
Still later I found out that this was a ploy of the bank to get people to invest.  
Problem is that we as mere mortals will not get this fast connection and therefore will lose out with slippage.  
  
I am not saying that the one you mentioned does this, but just keep that in mind.  
Plus why do they not share their strategy or did they and can you share it ?  
  
  
The strategy is simple.  
The difficult part is to make it run fast enough and not spend too much time in processing, which I achieved to combine MQ4 and java hybrid.  
Then also time consuming is to automate everything so that it can recover from problems like network problems, hardware problems, missed orders, slippage, volume, ...... and a whole lot more.  
  
Using back testing it makes a crazy amount of profit, but this is because back testing does not take into account slippage, volume and also not always so accurate.   
Accuracy of data is extremely important and therefore forward testing using a real account is the best test.  
  
I used it on crypto that is less affected by slippage.  
It actually works very well on low volume brokers for the speed is slowed down if there is not a lot of trades, causing a lot of arbitrage opportunities.  
Still low volume mean low profit, but profit is profit and I do not complain. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#455](/thread/post/12577837#post12577837 "Post Permalink")

  * Oct 23, 2019 7:55pm  Oct 23, 2019 7:55pm 

  * [ Dreamboy10](dreamboy10)

  * | Joined Apr 2019  | Status: Trader | [6 Posts](/search?do=process&provider=Member&searchuser=794056)

Hello jvbJacques, I really do admire your work. I try it on my own demo account, but the 3 order keep the same level of the loss for the several hours.   
  
How long does an order take on average?  
  

> [Quoting jvbJacques](/thread/post/12511984#post12511984 "View Quoted Post")
> 
> Disliked
> 
> @Alberto_Jazz As explained. I do the calculation on a BUY,SELL,SELL round trip and get a result. I plot that result on the chart as a point. I then do the calculation on a SELL,BUY,BUY round trip and get a result. I plot that result on the chart as a point. The average is a point in the middle between these 2 points. I then repeat this for every tick coming in and then all the points form the 3 lines. @geniousphp @mps I have seen a couple of these accounts. I can not say if they are true or scams. One I could figure out was a more basic version...
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#456](/thread/post/12578932#post12578932 "Post Permalink")

  * Oct 24, 2019 5:48am  Oct 24, 2019 5:48am 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@Dreamboy10  
I have not traded this live on forex yet, but swap does not play a role.  
Those lines are just calculations and no real orders therefore no swap.  
Only when the lines spike into profit do you actually place the orders, because then you know it will reverse back quickly.  
  
So your orders are only in place for a few seconds at a time.  
  
The problem comes with slippage.  
The profit is low and therefore slippage can erase your profits.  
I do take into account for some slippage, but you still need as fast as possible connection and a trustworthy broker.  
  
I mostly used it on my cryto currency account on Binance for they have got hundreds of coins and therefore thousands of triangles, giving lots more opportunities, even with no leverage it is still a bit profitable.  
Slippage still plays a role, but I have got a 1ms connection to them and their processing time of 30 milliseconds allows for a triangle trade round time of about 100 ms.  
Slippage does still play a role, especially with low volume coins and therefore to negate it I do allow for a little longer trading time before taking a small loss if it did not recover and exclude the extremely low volume coins for slippage on them can be big where as with others you are looking more in the line of worst case 0.001% loss and best case 1% profit.  
  
Ok I do have got a lot more trickery in my trading strategy, mostly to counter slippage and increase profits.  
  
I have not used this on binance in a few months.  
Profit was very low at about 0.1% a day, but with little risk it is prime candidate for margin trading which binance just started to do.  
  
Unfortunately I must first find time to update my program to use the new binance api to trade with it.  
So for the moment I'm just holding the coins, which has also been a bit profitable, but I write that up as luck. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#457](/thread/post/12579187#post12579187 "Post Permalink")

  * Oct 24, 2019 10:25am  Oct 24, 2019 10:25am 

  * [ Dreamboy10](dreamboy10)

  * | Joined Apr 2019  | Status: Trader | [6 Posts](/search?do=process&provider=Member&searchuser=794056)

Hi [_jvbJacques,_](https://www.forexfactory.com/jvbjacques)  
  
_Thank you for your r_ espone. I use your EA 19 at my demo account, and hire a VPS for it. But there is NO orders at all, nearly one day passed.   
  
And I wirte an EA by myself, with the same logic, is randomly entry GU, GJ and UJ with the balance lots, but they keep losing the same amount all the time.  
  
Can you explain it, please. Thanks! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#458](/thread/post/12602443#post12602443 "Post Permalink")

  * Nov 6, 2019 10:27pm  Nov 6, 2019 10:27pm 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@Dreamboy10  
  
The EA is disabled and will not run on data after 2017.  
Therefore will not trade at all on a demo account anymore.  
  
Your logic seem different than mine.  
I do not enter randomly.  
  
I wait until GU, GJ and UJ together does not balance.  
Then I trade in the direction of the correction.  
  
Basically I enter a GU, GJ and UJ trade.(Just in a calculation, not actual trades. Call this virtual orders.)  
Together they should cancel each other out and if you plot their sum on a chart you should get a straight line.  
  
Then I monitor that line until it goes off course up or down and then only I actually open 3 orders for GU, GJ and UJ in the reverse direction for I know it must return back to the average line soon and close a few seconds later in profit.  
  
This is an extremely simplified explanation.  
Putting this in code is not so simple, but doable.  
Just make sure you make the calculations as efficient as possible to not miss the trade.  
All calculations can be done in less than 1 millisecond.  
  
Works well in crypto for they become unbalanced quite a bit without the need for leverage.  
  
Good luck 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#459](/thread/post/12900721#post12900721 "Post Permalink")

  * Apr 25, 2020 11:17pm  Apr 25, 2020 11:17pm 

  * [ fxanson](fxanson)

  * | Joined Apr 2020  | Status: Trader | [1 Post](/search?do=process&provider=Member&searchuser=944340)

hello, javJacques, love your sharing. Can you tell more about how it work on crypto? It looks like all the crypo are pairing with USD, I don't know how to triangle them. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#460](/thread/post/12901297#post12901297 "Post Permalink")

  * Apr 26, 2020 6:12pm  Apr 26, 2020 6:12pm 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@fxanson  
  
It actually works quite well with crypto.  
The triangles depends on the broker u use.  
  
If you can only form triangles using USD then it is the limitation of your broker.  
  
Nothing wrong with limitations.  
  
Take Binance for instance.  
There I can form hundreds of triangles, even using just one base currency.  
If I remember correctly I could get about 600 triangles using just TUSD as my base currency seeing that most cryptos intersect with TUSD (which is basically USD without tax and swap)  
  
Triangles without leverage in crypto is actually way simpler than in forex.  
  
In forex you have to do quite a bit of calculations to determine what the resulting price would be depending on whether you go long or short and how many longs and shorts you must take ex...  
Plus there is the swap to contend with.  
Also the dreaded slippage, which is made worse on bucket shop forex brokers and brokers that does not give you access to the actual order book .... grrr.. Crypto really opened my eyes to the scam that is forex brokers.  
  
In crypto it is as simple as just have multiple wallets.  
Hundreds of wallets in fact when looking at a broker like binance.  
Only your base wallet (say the TUSD wallet) contains your funds.  
I normally have got multiple base wallets for I like BTC and ETH also a lot.  
All your other wallets are empty. ZERO nada, nothing, full of dust (really .. dust can be valuable too.).  
Do not worry about having a wallet in a shit coin currency for you will ultimately store no funds in it.  
The wallets are just pathways to link currencies together.  
  
Then the calculation simplifies in that you just calculate what the resulting funds would be if you transfer your TSUD to another wallet say B then to another wallet say C and then back into TUSD using the current market prices.  
If the result is that you end up with more TUSD than what you began with then do the trade.  
Just make sure to account for trading cost and some slippage as it takes time to make the 3 trades.  
  
Do this for all 500 wallets forming exponentially more triangles within a spit second.  
I could get it down to taking about 1 to 2 milliseconds to scan all prices for all wallets and prices.  
This is using the slowest free amazon server I could finds, so a faster server should be ... faster ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
I make do with what I got ...  
  
The slow part is that trades take time.  
I could speed this up also using my multiple base wallets and only trading triangles touching 2 more of my wallets, therefore I can do multiple trades at the same time for I do not have to wait for trades into wallets already containing currency to complete to trade the funds out of those wallets.  
At most the trade time is the time it takes to do 2 trades, even with round trips through 5 wallets.  
( Not a triangle anymore, but o well ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1), in the world of triangular arbitrage everything is a triangle, even a circle. )  
  
Also note that when I say triangles I do not really mean just 3 wallets.  
I sometimes trades 4 or 5 wallets round trip if the profit was good enough, but that was slow so the profit really needed to be good or those round trips had to touch multiple of my funded wallets.  
  
Another advantage, which eludes me with latency arbitrage is leverage.  
Triangular arbitrage works very well with leverage so even a very small profit can be increased with leverage, whereas leverage does not work across brokers for latency arbitrage.  
A loan might work if you can get a loan in the currencies traded with latency arbitrage.  
  
Still even in this simplified state it is a very complicated strategy.  
Takes a lot of time to code it and also catering for all other real world problems like internet problems, slippage, broker problems, ex....  
  
Latency seem to make more profit and is MUCH simpler in its base format without leverage.  
Also latency have got an upper limit which is linked to the liquidity available in the brokers you use and the amount of funds you have, plus no leverage, which triangular does not. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Simple High Profit low Drawdown Triangular Arbitrage
  *   * [ **Reply to Thread** ](/thread/676132-simple-high-profit-low-drawdown-triangular-arbitrage/reply#reply)

  * More

[](https://www.forexfactory.com "Homepage")

  * [Forums](forums)
  * [Trades](trades)
  * [Calendar](calendar)
  * [News](news)
  * [Market](market)
  * [Brokers](brokers)

****

[](https://www.faireconomy.com/)

  * 

[Triangular Arbitrage](/thread/64423-triangular-arbitrage "Admin, Please Delete Thread.") 258 replies

[Triangular Arbitrage](/thread/62477-triangular-arbitrage "Is going  
long 1 lot of eur/usd + 
long 1 lot of usd/jpy = long 1 lot of eur/jpy ?  
\(is the ratio of the number of lots correct for a...") 16 replies

[Triangular Arbitrage and carry trade](/thread/71997-triangular-arbitrage-and-carry-trade "Is it possible for us retail traders to be able to make use of Tri Arb or carry trades?  
 
Any one know of retail brokers 
 
 
\(I'm...") 6 replies

[Triangular Arbitrage](/thread/367072-triangular-arbitrage "I've been reading about triangular arbing and was surprised to find that the cross of two majors doesn't always equal what the calculation...") 7 replies

[Question: Trade Mechanics of Triangular Arbitrage](/thread/225246-question-trade-mechanics-of-triangular-arbitrage "Before I even ask this question, please allow me to be very clear.... I have no intention of attempting a triangular arbitrage trade\(for...") 6 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/676132-simple-high-profit-low-drawdown-triangular-arbitrage/reply#reply)
  * Subscribe
  * [147](javascript:void\(0\);)

Attachments: Simple High Profit low Drawdown Triangular Arbitrage

Tags: Simple High Profit low Drawdown Triangular Arbitrage

#  [](/thread/676132-simple-high-profit-low-drawdown-triangular-arbitrage)Simple High Profit low Drawdown Triangular Arbitrage 

  * 

  * [#461](/thread/post/12909765#post12909765 "Post Permalink")

  * Apr 30, 2020 8:12am  Apr 30, 2020 8:12am 

  * [ a.cihanunal](a.cihanunal)

  * | Joined Apr 2017  | Status: Trader | [5 Posts](/search?do=process&provider=Member&searchuser=575969)

> [Quoting samet](/thread/post/11679241#post11679241 "View Quoted Post")
> 
> Disliked
> 
> similiar one ı have maybe u guys want to test ( theres little differences between these eas ) {file} {file} {file} {file}
> 
> Ignored

Hocam bunu 1 lot olarak ayarlayabilir misiniz?  
Can You Fix it for 1 lot? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#462](/thread/post/12910559#post12910559 "Post Permalink")

  * Apr 30, 2020 5:45pm  Apr 30, 2020 5:45pm 

  * [ a.cihanunal](a.cihanunal)

  * | Joined Apr 2017  | Status: Trader | [5 Posts](/search?do=process&provider=Member&searchuser=575969)

> [Quoting samet](/thread/post/11679241#post11679241 "View Quoted Post")
> 
> Disliked
> 
> similiar one ı have maybe u guys want to test ( theres little differences between these eas ) {file} {file} {file} {file}
> 
> Ignored

For MT5 ![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#463](/thread/post/12910730#post12910730 "Post Permalink")

  * Apr 30, 2020 6:46pm  Apr 30, 2020 6:46pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar946848_7.gif) ryuryu](ryuryu)

  * Joined Apr 2020 | Status: Trader | [1,922 Posts](/search?do=process&provider=Member&searchuser=946848)

> [Quoting jvbJacques](/thread/post/12578932#post12578932 "View Quoted Post")
> 
> Disliked
> 
> I mostly used it on my cryto currency account on Binance for they have got hundreds of coins and therefore thousands of triangles, giving lots more opportunities, even with no leverage it is still a bit profitable.
> 
> Ignored

Hi there! Thank you for great job you did! What language you are using for binance robot? 

Observer effect

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#464](/thread/post/12917962#post12917962 "Post Permalink")

  * May 4, 2020 8:22pm  May 4, 2020 8:22pm 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

> [Quoting ryuryu](/thread/post/12910730#post12910730 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi there! Thank you for great job you did! What language you are using for binance robot?
> 
> Ignored

I'm using JAVAFX.  
I prefer it for it can run on anything and I really enjoy the extra speed that Linux gives me, plus online linux servers are cheap and sometimes free.  
Plus I can control it using a mobile version I created to monitor the server.  
  
Created my own API drivers seeing that I do not like using API drivers I do not control and so that I can access the Root API directly for extra speed and better fail over control.  
Plus having it in pure JAVA makes the application very fast and small seeing that it does not rely on apache or any other 3rd party dll.  
Only 500kb in size with a couple thousand lines of code is nice.  
  
It does not matter which language you use.  
I known multiple languages.  
Java is just my favourite the past 22 years.  
  
So long as it can do trades fast.  
Metatrader is very slow, but augmented with some JAVA in the back ground you can speed it up considerably, better yet is just replace Metatrader completely with JAVA and only use metatrader to monitor everything with its nice graphs. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#465](/thread/post/12919059#post12919059 "Post Permalink")

  * May 5, 2020 6:50am  May 5, 2020 6:50am 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

Begging for the quantum embrace.  
Not knowing the ending you feel the pounding of the ether and the strings unwind to reveal the frailness of reality.  
Look into me I hear whisper and I reach.  
Nothingness. astounding. what is nothingness. incomprehensible.  
The ultimate void of thought.  
It is pulling stronger.  
Help is but words that is meaningless in the awe of it all.  
But help is not for there is ... nothing.  
Nothing responds.  
Why become if you can unravels what is.  
Grab hold of what is and struggle against the void for it is relentless.  
I'm being pulled back.  
The strings are singing the song of reality as nothing vibrate into duality of matter.  
The warmth embraces me as thought forms into words and I hear the faint sound of .. help.  
Who might it be on the other side of nothingness looking back at me.  
Is that me.  
Split by the imaginings of reality for the string of it all is now broken and reality bleeds through with a birth cry that springs forth everything.  
Grab hold of it and never let go for nothing will claim you if you ever imagine the futility of it all. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#466](/thread/post/13012025#post13012025 "Post Permalink")

  * Jun 18, 2020 8:45pm  Jun 18, 2020 8:45pm 

  * [ ali-mohamed](ali-mohamed)

  * | Joined Feb 2020  | Status: Trader | [5 Posts](/search?do=process&provider=Member&searchuser=918628)

i have an awesome EA for triangular arbitrage, his idea depends on watching market till it found a chance to enter with a triangular positions but there is one problem, it some times open wrong positions ( open just one or two positions ) and it dose not close it till you close it manually and that may cause in some of loss a 

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: 125.jpg
Size: 155 KB](/attachment/image/3668068/thumbnail?d=1592480703)](/attachment/image/3668068?d=1592480703)   
[![Click to Enlarge

Name: fncontrolfile.jpg
Size: 42 KB](/attachment/image/3668069/thumbnail?d=1592480704)](/attachment/image/3668069?d=1592480704)   
[![Click to Enlarge

Name: var.jpg
Size: 45 KB](/attachment/image/3668070/thumbnail?d=1592480705)](/attachment/image/3668070?d=1592480705)   

Attached File(s)

![File Type: zip](https://assets.faireconomy.media/images/attach/zip.gif) [MQL5.zip](/attachment/file/3668071?d=1592480713) 232 KB | 845 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#467](/thread/post/13239013#post13239013 "Post Permalink")

  * Oct 31, 2020 2:54pm  Oct 31, 2020 2:54pm 

  * [ Jackson113](jackson113)

  * | Joined Aug 2020  | Status: Trader | [1 Post](/search?do=process&provider=Member&searchuser=985636)

Hi, jvbJacques, nice to meet you, I am interested your EA, but I downloaded it and test in MT4 demo, it’s no working. Can you please send again the version here?  
  
Appreciate and thanks your help. Thanks jvbJacques 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#468](/thread/post/13243642#post13243642 "Post Permalink")

  * Nov 4, 2020 2:40am  Nov 4, 2020 2:40am 

  * [ tiborf71](tiborf71)

  * Joined Apr 2011 | Status: survivor | [4,103 Posts](/search?do=process&provider=Member&searchuser=177839)

> [Quoting Jackson113](/thread/post/13239013#post13239013 "View Quoted Post")
> 
> Disliked
> 
> Hi, jvbJacques, nice to meet you, I am interested your EA, but I downloaded it and test in MT4 demo, it’s no working. Can you please send again the version here? Appreciate and thanks your help. Thanks jvbJacques
> 
> Ignored

I do not understand why the need is, ea.  
when you can trade by hand, the payback will take several days anyway.  
just open the positions and check it daily. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#469](/thread/post/13251923#post13251923 "Post Permalink")

  * Nov 8, 2020 11:00pm  Nov 8, 2020 11:00pm 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@Jackson113  
and  
@tiborf71  
  
I have not updated the EA in a long time.  
Mostly using a new version of it on crypto exchanges.  
As it is I am stuck with my paying programming job to the point where I get too little free time to spend on this EA, my crypto investments and work.  
I wish I could get time to do this again, but it have to wait until I can save up to work on it or get a job where I have free time to work on this for free.  
But please feel free to ask any questions on the theory and build one yourself if you are capable for the information in here is free for anyone's use.  
  
The EA currently in post one was disabled after 2018 and a computer with a clock after 2018 will cause the EA to shut down.  
This was done because a lot of people started using the EA for live trading and the EA is too unstable to be used for live trading, only for testing on demo accounts.  
After many calls on updating it for internet breaks, network delays, and a whole lot of non forex related things I decided to stop the EA until I can get time to really invest some time into building it properly.  
Thing is the theory behind triangular arbitrage is quite simple, but implementing it in a EA takes a lot of coding to make it safe.  
  
@tiborf71  
You are correct.  
If you are super human and can respond to market price fluctuations within a split second then yes you can do it manually.  
Just a joke ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
Unfortunately the market moves too fast to do this manually.  
Also keeping the 3 trades open will incur swap penalties which will eat into you profits.  
So you need to be online 24/7 and only enter when the opportunity presents and trade the opportunity within a few seconds in and out, which is 3 buys and 3 sells. 3 in and 3 out.  
  
In these few seconds you have to calculate the amount of potential slippage.  
The profit you need.  
The types of trades.  
And even the average market movement to make sure you will make profit.  
  
A lot to do.  
  
I for one can not be online 24/7.  
I need at least 4 hours sleep a day. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#470](/thread/post/13274783#post13274783 "Post Permalink")

  * Nov 21, 2020 1:45am  Nov 21, 2020 1:45am 

  * [ karthik11128](karthik11128)

  * | Joined Apr 2016  | Status: Trader | [11 Posts](/search?do=process&provider=Member&searchuser=461312)

Dear Team,  
  
Thank you all for your valuable inputs about triangle arbitrage, this is what i search so many days.  
  
My fund manager doing same logic and continuously getting profit and he share the profit with me. I am curious to know the calculation behind the entry.  
But, my fund manager didn't share with me and he will change the password during trading, i can't able to see the order, during the trading. Once all the orders are closed, then i can able to see the orders. Still i cant able to understand the logic.   
  
Herewith i attach my trading statement, if you are understand the logic, can you share with me.  
  
I am very much interested to know the logic. Please help me.

Attached File(s)

![File Type: pdf](https://assets.faireconomy.media/images/attach/pdf.gif) [Statement.pdf](/attachment/file/3794305?d=1605890606) 1.2 MB | 1,045 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#471](/thread/post/13275054#post13275054 "Post Permalink")

  * Nov 21, 2020 5:54am  Nov 21, 2020 5:54am 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@karthik11128  
I have only skimmed the document, but you are correct.  
  
That does look like triangular arbitrage.  
  
The very basic idea behind triangular arbitrage is to use currency A to buy B.  
Then use B to buy currency C.  
Then use C to buy currency A again.  
  
You can calculate this round trip before actually taking the trades.  
If this round trip would result in profit then take it, otherwise wait until a profit opportunity presents itself.  
  
This can be applied to any 3 currencies.  
  
In forex this results in 2 BUYS and one SELL  
OR 2 SELLs and one BUY.  
  
The direction of the round trip will determine the buys and sells.  
  
Also there is a % depending on the currency pairs used to balance the triangle. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#472](/thread/post/13275297#post13275297 "Post Permalink")

  * Nov 21, 2020 5:17pm  Nov 21, 2020 5:17pm 

  * [ karthik11128](karthik11128)

  * | Joined Apr 2016  | Status: Trader | [11 Posts](/search?do=process&provider=Member&searchuser=461312)

> [Quoting jvbJacques](/thread/post/13275054#post13275054 "View Quoted Post")
> 
> Disliked
> 
> @karthik11128 I have only skimmed the document, but you are correct. That does look like triangular arbitrage. The very basic idea behind triangular arbitrage is to use currency A to buy B. Then use B to buy currency C. Then use C to buy currency A again. You can calculate this round trip before actually taking the trades. If this round trip would result in profit then take it, otherwise wait until a profit opportunity presents itself. This can be applied to any 3 currencies. In forex this results in 2 BUYS and one SELL OR 2 SELLs and one BUY. The...
> 
> Ignored

Dear [jvbJacques](https://www.forexfactory.com/jvbjacques),  
  
Thanks for your input.  
  
R u have any calculating mechanism or EA for above calculation.  
  
If any, please share with me.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#473](/thread/post/13275802#post13275802 "Post Permalink")

  * Nov 22, 2020 4:01pm  Nov 22, 2020 4:01pm 

  * [ tiborf71](tiborf71)

  * Joined Apr 2011 | Status: survivor | [4,103 Posts](/search?do=process&provider=Member&searchuser=177839)

> [Quoting jvbJacques](/thread/post/13251923#post13251923 "View Quoted Post")
> 
> Disliked
> 
> @Jackson113 and @tiborf71 I have not updated the EA in a long time. Mostly using a new version of it on crypto exchanges. As it is I am stuck with my paying programming job to the point where I get too little free time to spend on this EA, my crypto investments and work. I wish I could get time to do this again, but it have to wait until I can save up to work on it or get a job where I have free time to work on this for free. But please feel free to ask any questions on the theory and build one yourself if you are capable for the information in...
> 
> Ignored

I understand.  
but I tested many arbitrage possibilities and experienced something completely different. in the meantime, I tested all possible combinations.  
and I only found one variation that works.  
and I don’t have to add the EA because I have to put it down by hand, the payback is usually 1-10 days, if I deduct the cost even then there will still be a benefit. (usually)úgy hogy nem értelek mi a probléma. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#474](/thread/post/13275806#post13275806 "Post Permalink")

  * Nov 22, 2020 4:12pm  Nov 22, 2020 4:12pm 

  * [ tiborf71](tiborf71)

  * Joined Apr 2011 | Status: survivor | [4,103 Posts](/search?do=process&provider=Member&searchuser=177839)

I think it is conceivable that 99.99% of the variations require EA, but the remaining 1% can also be loaded manually. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#475](/thread/post/13303491#post13303491 "Post Permalink")

  * Dec 9, 2020 9:23am  Dec 9, 2020 9:23am 

  * [ DollaMite](dollamite)

  * | Joined Feb 2020  | Status: Trader | [6 Posts](/search?do=process&provider=Member&searchuser=917689)

> [Quoting swatch](/thread/post/10799878#post10799878 "View Quoted Post")
> 
> Disliked
> 
> Hi, I am looking to do this 2 symbols only... I am looking for a EA/script that places buy and sell market orders on two FX pairs simultaneously - for example buy EUR/USD and sell GBP/USD. I do not want any SL or TP, just to be able to specify the particular symbol to buy and the symbol to sell, and their relevant volume. I am quite new to that, please help me.
> 
> Ignored

In the example you've just given, you wil both buy and sell usd. You need to use 3 pairs to cover all of your trades.  
Ps. This reply is because im too new to FF to start my own thread and im bored lol 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#476](/thread/post/13838162#post13838162 "Post Permalink")

  * Dec 28, 2021 7:38am  Dec 28, 2021 7:38am 

  * [ jprizain](jprizain)

  * | Joined Oct 2013  | Status: Trader | [17 Posts](/search?do=process&provider=Member&searchuser=352852)

Bump on this thread. Theres lot of knowledge and i see power in it. Hope [jvbJacques](https://www.forexfactory.com/jvbjacques) keep sharing his beautiful idea of trading. To me this thread talk more about technology on trades 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#477](/thread/post/13930772#post13930772 "Post Permalink")

  * Mar 14, 2022 5:33am  Mar 14, 2022 5:33am 

  * [ jvbJacques](jvbjacques)

  * Joined Jun 2017 | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=588409)

@jprizain  
Nice to see people still reading this thread.  
I am still playing with ideas and arbitrage.  
Got lots more ideas like auto adapting grid systems and more advanced arbitrage.  
  
I mostly moved over to crypto and although my arbitrage system is working there it is slow going.  
Had some major setbacks where I had to sell my account to cover my living expenses.  
  
Unfortunately trying to find work and maintaining that last contract I have left is taking a lot of time so not much time for development.  
Only dreaming and planning for one day ![](https://resources.faireconomy.media/images/emojis/64/1f600.png?v=15.1)  
This one day seem to be years away and I was hoping to reach my goals by now, but unfortunately not yet.  
One day 

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#478](/thread/post/14276246#post14276246 "Post Permalink")

  * Jan 5, 2023 9:13am  Jan 5, 2023 9:13am 

  * [ creativeX](creativex)

  * | Joined Jan 2023  | Status: Trader | [1 Post](/search?do=process&provider=Member&searchuser=1564809)

Wow ... long ongoing thread. I read the first couple of pages back from 2017 and then skipped ahead to the last page to see your progress. Good on you. Incredible to still be perfecting your system over that time. Where are things at now? Do you ever get to using the system on live accounts and what has been your results?  
  
I was actually just googling looking for a good accurate drawdown indicator for mt4 and it brought up this page. Great bunny trail ;-) 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#479](/thread/post/14783497#post14783497 "Post Permalink")

  * Mar 6, 2024 10:15pm  Mar 6, 2024 10:15pm 

  * [ nmthang3321](nmthang3321)

  * | Joined May 2023  | Status: Trader | [3 Posts](/search?do=process&provider=Member&searchuser=1633374)

Hello @jvbJacques  
  
I intersted in your strategy, but I am confusing about how to you calculate entry point. could you share your EA as *mql4 file? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#480](/thread/post/14783704#post14783704 "Post Permalink")

  * Mar 6, 2024 11:43pm  Mar 6, 2024 11:43pm 

  * [ nmthang3321](nmthang3321)

  * | Joined May 2023  | Status: Trader | [3 Posts](/search?do=process&provider=Member&searchuser=1633374)

> [Quoting jvbJacques](/thread/post/9988492#post9988492 "View Quoted Post")
> 
> Disliked
> 
> ******************************************************************************* RULE UPDATE : 2017-09-23 ******************************************************************************* Ok this is a MAJOR update. Rules changed a bit. Still triangular on the 3 symbols. But. I now calculate what the average profit would be if I did a BUY, SELL, SELL and also SELL,BUY,BUY. This gives me 2 lines. Call the higher line the ASK line and the lower line the BUY line. Between the 2 lines is the average line calculated over some time, which if mostly a straight...
> 
> Ignored

Regarding calculate the averange line between ask and bid, which specific pair you used? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Simple High Profit low Drawdown Triangular Arbitrage
  *   * [ **Reply to Thread** ](/thread/676132-simple-high-profit-low-drawdown-triangular-arbitrage/reply#reply)

  * More

[](https://www.forexfactory.com "Homepage")

  * [Forums](forums)
  * [Trades](trades)
  * [Calendar](calendar)
  * [News](news)
  * [Market](market)
  * [Brokers](brokers)

****

[](https://www.faireconomy.com/)

  * 

[Triangular Arbitrage](/thread/64423-triangular-arbitrage "Admin, Please Delete Thread.") 258 replies

[Triangular Arbitrage](/thread/62477-triangular-arbitrage "Is going  
long 1 lot of eur/usd + 
long 1 lot of usd/jpy = long 1 lot of eur/jpy ?  
\(is the ratio of the number of lots correct for a...") 16 replies

[Triangular Arbitrage and carry trade](/thread/71997-triangular-arbitrage-and-carry-trade "Is it possible for us retail traders to be able to make use of Tri Arb or carry trades?  
 
Any one know of retail brokers 
 
 
\(I'm...") 6 replies

[Triangular Arbitrage](/thread/367072-triangular-arbitrage "I've been reading about triangular arbing and was surprised to find that the cross of two majors doesn't always equal what the calculation...") 7 replies

[Question: Trade Mechanics of Triangular Arbitrage](/thread/225246-question-trade-mechanics-of-triangular-arbitrage "Before I even ask this question, please allow me to be very clear.... I have no intention of attempting a triangular arbitrage trade\(for...") 6 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/676132-simple-high-profit-low-drawdown-triangular-arbitrage/reply#reply)
  * Subscribe
  * [147](javascript:void\(0\);)

Attachments: Simple High Profit low Drawdown Triangular Arbitrage

Tags: Simple High Profit low Drawdown Triangular Arbitrage

#  [](/thread/676132-simple-high-profit-low-drawdown-triangular-arbitrage)Simple High Profit low Drawdown Triangular Arbitrage 

  * 

  * [#481](/thread/post/14943614#post14943614 "Post Permalink")

  * Last Post: Jul 26, 2024 12:27am  Jul 26, 2024 12:27am 

  * [ 1080p](1080p)

  * | Joined Apr 2023  | Status: Trader | [2 Posts](/search?do=process&provider=Member&searchuser=1629024)

Can anyone operate this robot? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Simple High Profit low Drawdown Triangular Arbitrage
  *   * [ **Reply to Thread** ](/thread/676132-simple-high-profit-low-drawdown-triangular-arbitrage/reply#reply)

[](https://www.forexfactory.com "Homepage")

  * [Forums](forums)
  * [Trades](trades)
  * [Calendar](calendar)
  * [News](news)
  * [Market](market)
  * [Brokers](brokers)

****

[](https://www.faireconomy.com/)
