

  * 

[Trading multipair triangles, no stoploss](/thread/917648-trading-multipair-triangles-no-stoploss "Hello forex Folks! 
  
I'd like to share with You my system that I was comming to for many years. I am testing it these days and it gives...") 78 replies

['Blessing' EA Modification Wanted](/thread/271525-blessing-ea-modification-wanted "Hello. 
 
here is a version of BLESSING \(old\) love this version. 
I wonder if someone could if possible to change this code. 
 
I like that...") 3 replies

[Single, Few Pair Traders (1-4) vs. MultiPair Traders (8-20)](/thread/964171-single-few-pair-traders-1-4-vs-multipair-traders "Who gets better results ?? 
  
Put it in another way , if you went for a trading competition and want to achieve &gt;300% ~ 2000% , what would...") 0 replies

[Coding Request for Multipair MTF ADR Dashboard](/thread/683340-coding-request-for-multipair-mtf-adr-dashboard "Can someone code this into indicator???") 2 replies

[trying to make a multipair buy and sell script](/thread/241746-trying-to-make-a-multipair-buy-and-sell "what i like to do is that i add a script on a chart and it will do 
 
open 3 pairs buys or sells. 
 
for example 0.1 lot EURUSD 
          ...") 6 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/973998-blessing-multipair-ea/reply#reply)
  * Subscribe
  * [97](javascript:void\(0\);)

Attachments: Blessing Multipair EA

Tags: Blessing Multipair EA

#  [](/thread/973998-blessing-multipair-ea)Blessing Multipair EA 

  * 

  * [#1](/thread/973998-blessing-multipair-ea "Post Permalink")

  * First Post: Edited Feb 5, 2020 6:15am  Jan 12, 2020 1:22pm | Edited Feb 5, 2020 6:15am 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

My first thread in this forum, I am so excited...  
  
The idea for this EA started in another thread:  
<https://www.forexfactory.com/showthread.php?t=792598>  
  
Therefore this EA is based on the wonderful EA called “Blessing 3 v3.9.6.09”.  
  
The idea to try to build a multipair version came up in the above mentioned thread. After some brainstorming I began to like the idea. Though Blessing and multipair is kind of a contradiction. Blessing has so many parameters to finetune the EA exactly to your pair to trade, the time frame, your risk and and and.  
But anyway it might be worth a try to find some “global settings” that work well for all pairs. Just adjusted to the time frame and other global parameters (risk, broker and and and).  
  
What did I basically do?

  1. I took the latest source code from the original thread (“Blessing 3 v3.9.6.13”).
  2. … cleaned it from almost all display output
  3. … introduced a big struct that holds the variables for the pair to trade
  4. The start function is running a long “for to” loop over an array of the structs for the pairs to trade
  5. I took out the hedge function
  6. only one and fixed magical number to be able to monitor the trades via a dashboard
  7. ...moved the main part of the holiday check to the beginning of the start function

  
Sounds simple but gave me some headache as the debug options for bugfixing in MT4 are really poor, compared to a “real” compiler.  
I can only perform backtesting with one pair at a time, which is not enough for a multipair EA. In realtime mode I can see whether it is working, but it is difficult to see if it is working **in the right way**.  
Enough words written: please take a look at the code and feel free to give feedback. There are for sure still many open points that I would love to discuss here in this thread.  
Especially when it comes to global settings (e.g. number of open trades) that might need to be moved into the struct.  
And please play around with different set-files to see which settings come close to “one size fits all” (thx Grand Wazoo). As a good starting point I can recommend the collection from Richard96816, that can be found in this post:  
  
[https://www.forexfactory.com/showthr...4#post12628494](https://www.forexfactory.com/showthread.php?p=12628494#post12628494)  
(thanks a million, Richard!)  
  
→ for backtesting, the setting for „Use the 28 default pairs“ must be set to false and in the „comma separated own pair list“ only the symbol (e.g. XAUUSD) that is used in the tester has to be input.  
→ for live testing (better on a demo first..) please do NOT use small timeframes and many pairs with only one entry condition. The EA will open, close, modify in such a high frequency, that your broker will close your account faster than you can click. Happened to me ;-)  
  
Have fun!  
  

_**REMEMBER**_

 _**This is a code for learning and testing purposes only. Everything you do, you do on you own risk!**_

_**In no event I will be liable for any damages whatsoever.**_

Attached File(s)

![File Type: txt](https://assets.faireconomy.media/images/attach/txt.gif) [BlessingV24beta-XUSUSDTest.set.txt](/attachment/file/3527008?d=1578802208) 9 KB | 4,191 downloads 

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [BlessingLite_3_v3.9.6.34_gamma.ex4](/attachment/file/3538253?d=1580049676) 192 KB | 3,539 downloads | Uploaded Jan 26, 2020 11:41pm 

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [BlessingLite_3_v3.9.6.34_gamma.mq4](/attachment/file/3545995?d=1580850892) 130 KB | 4,600 downloads | Uploaded Feb 5, 2020 6:14am 

  * [#2](/thread/post/12698722#post12698722 "Post Permalink")

  * Jan 12, 2020 1:54pm  Jan 12, 2020 1:54pm 

  * [ ajaykarkhane](ajaykarkhane)

  * | Joined Jun 2014  | Status: Trader | [130 Posts](/search?do=process&provider=Member&searchuser=374248)

Thanks a lot for starting this journey with new thread  
I have very little knowledge on coding part but from time to time I can test with the setup I am having and present the case here .  
Thanks .. yes thanks to Richard also he has given lots of new ideas to use the old blessing code definitely in new way. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#3](/thread/post/12698762#post12698762 "Post Permalink")

  * Jan 12, 2020 3:52pm  Jan 12, 2020 3:52pm 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

Remember that post?  
[https://www.forexfactory.com/showthr...7#post12551567](https://www.forexfactory.com/showthread.php?p=12551567#post12551567)  
Well, I used the settings and made a backtest from 01.Nov.2019 to 10.Jan.2020. 5 Minutes timeframe, for all 28 pairs. What can I say: that already looks like the winner to be tested on the Blessing-Multipair. Can't wait for Sidney open...  
Here are the results: 

Attached Image

![](/attachment/image/3527046?d=1578811878)

[0 ](javascript:void\(0\);) [5 ](javascript:void\(0\);)

  * [#4](/thread/post/12698792#post12698792 "Post Permalink")

  * Jan 12, 2020 6:01pm  Jan 12, 2020 6:01pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar338950_1.gif) cescof](cescof)

  * Joined Jun 2013 | Status: Trader | [1,006 Posts](/search?do=process&provider=Member&searchuser=338950)

> [Quoting ursinho4711](/thread/post/12698762#post12698762 "View Quoted Post")
> 
> Disliked
> 
> Remember that post? [https://www.forexfactory.com/showthr...7#post12551567](https://www.forexfactory.com/showthread.php?p=12551567#post12551567) Well, I used the settings and made a backtest from 01.Nov.2019 to 10.Jan.2020. 5 Minutes timeframe, for all 28 pairs. What can I say: that already looks like the winner to be tested on the Blessing-Multipair. Can't wait for Sidney open... Here are the results: {image}
> 
> Ignored

Thanks for new 3dand new blessing multipairs...  
So if i understood the result above are backtested using the 5min set file from other 3d right?  
What about set file you posted xususd... ?   
And how many max pairs do you seggests to use to avoid broker limits?  
Thanks  
Regards 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#5](/thread/post/12698797#post12698797 "Post Permalink")

  * Edited 7:05pm  Jan 12, 2020 6:28pm | Edited 7:05pm 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

> [Quoting cescof](/thread/post/12698792#post12698792 "View Quoted Post")
> 
> Disliked
> 
> Thanks for new 3dand new blessing multipairs...
> 
> Ignored

Your welcome! And thank you for joining the thread!  
  

> [Quoting cescof](/thread/post/12698792#post12698792 "View Quoted Post")
> 
> Disliked
> 
> So if i understood the result above are backtested using the 5min set file from other 3d right?
> 
> Ignored

Right! I have a bunch of setfiles from the other Blessing thread. I picked that one for backtesting first, as it is alread used successfully on a live account (with the original blessing).  
  

> [Quoting cescof](/thread/post/12698792#post12698792 "View Quoted Post")
> 
> Disliked
> 
> What about set file you posted xususd... ?
> 
> Ignored

That is just a set-file example for backtesting with the MT4 strategy tester. One pair, no 28 default pairs.  
  

> [Quoting cescof](/thread/post/12698792#post12698792 "View Quoted Post")
> 
> Disliked
> 
> And how many max pairs do you seggests to use to avoid broker limits?
> 
> Ignored

The number of pairs is not the biggest problem: the entry conditions are much more important. The default setting has only the MA as entry indicator. This opens trades for almost every pair instantly. Good for testing, bad for trading ;-)  
  
The set-file I used for backtesting is using Bollinger Bands. Does not open too many trades over the time, not even in the M5 time frame. You can see it in the statistics. Okay, that's backtesting on a demo account. Tonight I will start with forward testing on the demo account...  
  
I should get some sleep as well...  
  
************************edit********************************  
here is the direct link to the "BLESS 5 MINUTES ALL PAIRS ONE DAY 50 DOLLARS.set":  
[https://www.forexfactory.com/attachm...9&d=1532217693](https://www.forexfactory.com/attachment.php/2906229?attachmentid=2906229&d=1532217693)

[0 ](javascript:void\(0\);) [3 ](javascript:void\(0\);)

  * [#6](/thread/post/12698812#post12698812 "Post Permalink")

  * Jan 12, 2020 7:08pm  Jan 12, 2020 7:08pm 

  * [ mankindeg](mankindeg)

  * | Joined Mar 2015  | Status: Trader | [143 Posts](/search?do=process&provider=Member&searchuser=405444)

Do we have a setfile to test on monday? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#7](/thread/post/12698818#post12698818 "Post Permalink")

  * Jan 12, 2020 7:22pm  Jan 12, 2020 7:22pm 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

> [Quoting mankindeg](/thread/post/12698812#post12698812 "View Quoted Post")
> 
> Disliked
> 
> Do we have a setfile to test on monday?
> 
> Ignored

Basically you can use any testfile from older "original" blessing versions. Parameters that do not exist anymore will be omitted, new parameters that are not contained in older setfiles will use default settings.  
  
As the default for BlessingLite Multipair is UseDefaultPairs = true, you just need to load any blessing setfile that you like and then get started...  
  
*************edit**********  
I will try that one tonight: 

Attached File(s)

![File Type: txt](https://assets.faireconomy.media/images/attach/txt.gif) [BlessingLiteV24-5Min-AllPairs.set.txt](/attachment/file/3527087?d=1578824928) 2 KB | 2,166 downloads 

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#8](/thread/post/12698827#post12698827 "Post Permalink")

  * Jan 12, 2020 7:46pm  Jan 12, 2020 7:46pm 

  * [ richard96816](richard96816)

  * Joined Dec 2018 | Status: Trader | [564 Posts](/search?do=process&provider=Member&searchuser=741833)

Good show!  
  
You might want to create a settable minimum delay between trades to fix the over-trading problem. That's a common feature on multi-pair EAs.  
  
You could save the time from the most recent open of each pair, then compare with current time each attempt to open another trade. Only allow new opens to succeed if elapsed time is greater than some externally set value.  
  
Good luck! 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#9](/thread/post/12698942#post12698942 "Post Permalink")

  * Jan 13, 2020 12:28am  Jan 13, 2020 12:28am 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

> [Quoting richard96816](/thread/post/12698827#post12698827 "View Quoted Post")
> 
> Disliked
> 
> Good show!
> 
> Ignored

Thanks for the feedback Richard! That's the way I hope this thread will continue...  
  

> [Quoting richard96816](/thread/post/12698827#post12698827 "View Quoted Post")
> 
> Disliked
> 
> You might want to create a settable minimum delay between trades to fix the over-trading problem. That's a common feature on multi-pair EAs. You could save the time from the most recent open of each pair, then compare with current time each attempt to open another trade. Only allow new opens to succeed if elapsed time is greater than some externally set value.
> 
> Ignored

The challenge is not only over-trading, it is also the "over-modifying". Moving TP, moving buy/sell/limits/stops: all this has to be monitored. I will wait and see how the EA will behave tonight, with the bollinger band indicator compared to the MA. In the backtest even on the M5 timeframe bollinger is much more calm...  
  

> [Quoting richard96816](/thread/post/12698827#post12698827 "View Quoted Post")
> 
> Disliked
> 
> Good luck!
> 
> Ignored

Thanks... but luck is not the only thing I need: my idea was to use this thread as an open source community. Everybody can and should take a look at the source code and see where it can be improved or find these small bugs... if someone knows how to transfer the code into mq5 quickly, this would be advantageous for debugging. Setting breakpoints in the strategy tester would already save hours during development.  
  
Okay, next to-do would be the delay parameter and something like this (setting from a dashboard EA): 

Attached Image

![](/attachment/image/3527153?d=1578842863)

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#10](/thread/post/12698965#post12698965 "Post Permalink")

  * Jan 13, 2020 1:30am  Jan 13, 2020 1:30am 

  * [ kofix11](kofix11)

  * | Joined Dec 2011  | Status: Trader | [828 Posts](/search?do=process&provider=Member&searchuser=209345)

> [Quoting ursinho4711](/thread/post/12698762#post12698762 "View Quoted Post")
> 
> Disliked
> 
> Remember that post? [https://www.forexfactory.com/showthr...7#post12551567](https://www.forexfactory.com/showthread.php?p=12551567#post12551567) Well, I used the settings and made a backtest from 01.Nov.2019 to 10.Jan.2020. 5 Minutes timeframe, for all 28 pairs. What can I say: that already looks like the winner to be tested on the Blessing-Multipair. Can't wait for Sidney open... Here are the results: {image}
> 
> Ignored

Thanks for your effort! Looks interesting. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#11](/thread/post/12699039#post12699039 "Post Permalink")

  * Jan 13, 2020 3:54am  Jan 13, 2020 3:54am 

  * [ pantera1](pantera1)

  * | Joined Mar 2018  | Status: Trader | [50 Posts](/search?do=process&provider=Member&searchuser=658798)

The EA works fine in the Strategy Tester but when I try to install it on a live chart, my MT4 won't let me. Accordingly, the following error message appears in the Journal:   
  
"_2020.01.12 10:29:02.624 'BlessingLite_3_v3.9.6.24_beta' is not expert and cannot be executed_ " 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#12](/thread/post/12699052#post12699052 "Post Permalink")

  * Jan 13, 2020 4:29am  Jan 13, 2020 4:29am 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

> [Quoting pantera1](/thread/post/12699039#post12699039 "View Quoted Post")
> 
> Disliked
> 
> The EA works fine in the Strategy Tester but when I try to install it on a live chart, my MT4 won't let me. Accordingly, the following error message appears in the Journal: "2020.01.12 10:29:02.624 'BlessingLite_3_v3.9.6.24_beta' is not expert and cannot be executed"
> 
> Ignored

Which build are you using? Did you put the EA in the right folder?  
  
I used the mq4 file in different broker installations, all build 1220. No problems. Compiles without error. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#13](/thread/post/12699053#post12699053 "Post Permalink")

  * Jan 13, 2020 4:30am  Jan 13, 2020 4:30am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar662190_6.gif) Paolino](paolino)

  * | Joined Mar 2018  | Status: Trader | [87 Posts](/search?do=process&provider=Member&searchuser=662190)

> [Quoting pantera1](/thread/post/12699039#post12699039 "View Quoted Post")
> 
> Disliked
> 
> The EA works fine in the Strategy Tester but when I try to install it on a live chart, my MT4 won't let me. Accordingly, the following error message appears in the Journal: "2020.01.12 10:29:02.624 'BlessingLite_3_v3.9.6.24_beta' is not expert and cannot be executed"
> 
> Ignored

  
I initially encountered the same issue with other Blessing versions and solved changing int start() method with void OnTick().  
See here:  
[https://www.forexfactory.com/showthr...4#post12673354](https://www.forexfactory.com/showthread.php?p=12673354#post12673354)  
  
Perhaps it could be useful to update source code naming according to new MT4 Build 600+ compliance.  
Best regards. 

Discipline and winning attitude

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#14](/thread/post/12699060#post12699060 "Post Permalink")

  * Jan 13, 2020 4:39am  Jan 13, 2020 4:39am 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

> [Quoting Paolino](/thread/post/12699053#post12699053 "View Quoted Post")
> 
> Disliked
> 
> {quote} I initially encountered the same issue with other Blessing versions and solved changing int start() method with void OnTick(). See here: [https://www.forexfactory.com/showthr...4#post12673354](https://www.forexfactory.com/showthread.php?p=12673354#post12673354) Perhaps it could be useful to update source code naming according to new MT4 Build 600+ compliance. Best regards.
> 
> Ignored

Jipp, I was reading about that as well. Anyone knows why it works fine on all my new 1220 build installations?  
  
Remember: when you change to OnTick(), you have to change also all the return calls! 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#15](/thread/post/12699061#post12699061 "Post Permalink")

  * Jan 13, 2020 4:40am  Jan 13, 2020 4:40am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar638535_1.gif) detector](detector)

  * Joined Dec 2017 | Status: Trader | [3,710 Posts](/search?do=process&provider=Member&searchuser=638535)

> [Quoting pantera1](/thread/post/12699039#post12699039 "View Quoted Post")
> 
> Disliked
> 
> The EA works fine in the Strategy Tester but when I try to install it on a live chart, my MT4 won't let me. Accordingly, the following error message appears in the Journal: "2020.01.12 10:29:02.624 'BlessingLite_3_v3.9.6.24_beta' is not expert and cannot be executed"
> 
> Ignored

Just to verify, I placed the EA on to a live chart with no issues, not tried ST but the assumption would be, no issues, (MT4 version 4 build 1220) still testing the older version of blessing.  
Ursinho, well done and good luck on the new thread![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)D 

I don't need to be good at the game, only good enough to beat my opponent,

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#16](/thread/post/12699065#post12699065 "Post Permalink")

  * Jan 13, 2020 4:45am  Jan 13, 2020 4:45am 

  * [ pantera1](pantera1)

  * | Joined Mar 2018  | Status: Trader | [50 Posts](/search?do=process&provider=Member&searchuser=658798)

Just to confirm; I am using build 1220 and the EA is in the correct folder. I had been using _Blessing_3_v3.9.6.13_beta_ without any issues. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#17](/thread/post/12699067#post12699067 "Post Permalink")

  * Jan 13, 2020 4:49am  Jan 13, 2020 4:49am 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

> [Quoting pantera1](/thread/post/12699065#post12699065 "View Quoted Post")
> 
> Disliked
> 
> Just to confirm; I am using build 1220 and the EA is in the correct folder. I had been using Blessing_3_v3.9.6.13_beta without any issues.
> 
> Ignored

Any messages when you compile it in the Meta-Editor? I will change the code to OnTick when my daughter goes to sleep (probably not before midnight ;-)) ) 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#18](/thread/post/12699068#post12699068 "Post Permalink")

  * Jan 13, 2020 4:54am  Jan 13, 2020 4:54am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar662190_6.gif) Paolino](paolino)

  * | Joined Mar 2018  | Status: Trader | [87 Posts](/search?do=process&provider=Member&searchuser=662190)

> [Quoting ursinho4711](/thread/post/12699060#post12699060 "View Quoted Post")
> 
> Disliked
> 
> {quote} Jipp, I was reading about that as well. Anyone knows why it works fine on all my new 1220 build installations? Remember: when you change to OnTick(), you have to change also all the return calls!
> 
> Ignored

Yes, I forgot to write that to maintain backward compatibility with Blessing code I renamed _int start()_ to _int DoStart()_ called by void OnTick():  
  
void OnTick()  
{  
int retValue = DoStart();  
}  
  
int DoStart() // ex start()  
{  
... 

Discipline and winning attitude

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#19](/thread/post/12699075#post12699075 "Post Permalink")

  * Jan 13, 2020 5:03am  Jan 13, 2020 5:03am 

  * [ pantera1](pantera1)

  * | Joined Mar 2018  | Status: Trader | [50 Posts](/search?do=process&provider=Member&searchuser=658798)

No warnings or errors when I compile the .mq4  
  

Attached Image

![](/attachment/image/3527284?d=1578859553)

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#20](/thread/post/12699079#post12699079 "Post Permalink")

  * Jan 13, 2020 5:19am  Jan 13, 2020 5:19am 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

> [Quoting pantera1](/thread/post/12699075#post12699075 "View Quoted Post")
> 
> Disliked
> 
> No warnings or errors when I compile the .mq4 {image}
> 
> Ignored

See if that one works, I changed everything to OnXXX... 

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [BlessingLite_3_v3.9.6.25_beta.ex4](/attachment/file/3527287?d=1578860341) 186 KB | 1,415 downloads 

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [BlessingLite_3_v3.9.6.25_beta.mq4](/attachment/file/3527288?d=1578860371) 126 KB | 1,880 downloads 

[0 ](javascript:void\(0\);) [4 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Blessing Multipair EA
  *   * [ **Reply to Thread** ](/thread/973998-blessing-multipair-ea/reply#reply)

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

[Trading multipair triangles, no stoploss](/thread/917648-trading-multipair-triangles-no-stoploss "Hello forex Folks! 
  
I'd like to share with You my system that I was comming to for many years. I am testing it these days and it gives...") 78 replies

['Blessing' EA Modification Wanted](/thread/271525-blessing-ea-modification-wanted "Hello. 
 
here is a version of BLESSING \(old\) love this version. 
I wonder if someone could if possible to change this code. 
 
I like that...") 3 replies

[Single, Few Pair Traders (1-4) vs. MultiPair Traders (8-20)](/thread/964171-single-few-pair-traders-1-4-vs-multipair-traders "Who gets better results ?? 
  
Put it in another way , if you went for a trading competition and want to achieve &gt;300% ~ 2000% , what would...") 0 replies

[Coding Request for Multipair MTF ADR Dashboard](/thread/683340-coding-request-for-multipair-mtf-adr-dashboard "Can someone code this into indicator???") 2 replies

[trying to make a multipair buy and sell script](/thread/241746-trying-to-make-a-multipair-buy-and-sell "what i like to do is that i add a script on a chart and it will do 
 
open 3 pairs buys or sells. 
 
for example 0.1 lot EURUSD 
          ...") 6 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/973998-blessing-multipair-ea/reply#reply)
  * Subscribe
  * [97](javascript:void\(0\);)

Attachments: Blessing Multipair EA

Tags: Blessing Multipair EA

#  [](/thread/973998-blessing-multipair-ea)Blessing Multipair EA 

  * 

  * [#21](/thread/post/12699104#post12699104 "Post Permalink")

  * Jan 13, 2020 5:53am  Jan 13, 2020 5:53am 

  * [ pantera1](pantera1)

  * | Joined Mar 2018  | Status: Trader | [50 Posts](/search?do=process&provider=Member&searchuser=658798)

Problem solved. Thanks! 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#22](/thread/post/12699114#post12699114 "Post Permalink")

  * Jan 13, 2020 6:00am  Jan 13, 2020 6:00am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar405432_1.gif) fabio.g](fabio.g)

  * | Joined Mar 2015  | Status: Trader | [658 Posts](/search?do=process&provider=Member&searchuser=405432)

> [Quoting ursinho4711](/thread/post/12699079#post12699079 "View Quoted Post")
> 
> Disliked
> 
> {quote} See if that one works, I changed everything to OnXXX... {file} {file}
> 
> Ignored

this complies fine for me, thanks, loaded on demo 

[GridEA](fabio.g#67 "View Trade Explorer") Return This Year: na

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#23](/thread/post/12699162#post12699162 "Post Permalink")

  * Jan 13, 2020 7:09am  Jan 13, 2020 7:09am 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

it's running... ;-) 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot1.png
Size: 20 KB](/attachment/image/3527340/thumbnail?d=1578866987)](/attachment/image/3527340?d=1578866987)   

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#24](/thread/post/12699192#post12699192 "Post Permalink")

  * Jan 13, 2020 7:43am  Jan 13, 2020 7:43am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar638535_1.gif) detector](detector)

  * Joined Dec 2017 | Status: Trader | [3,710 Posts](/search?do=process&provider=Member&searchuser=638535)

> [Quoting ursinho4711](/thread/post/12699162#post12699162 "View Quoted Post")
> 
> Disliked
> 
> it's running... ;-) {image}
> 
> Ignored

Ursinho, hope you don't mind me posting this one and only time, I am testing the older version on the same pairs but omitted the CHF crosses, (live) I have been doing some backtesting and found a very good low DD, while I know this is a little conflicting, I thought I may add my post only in the research terms that any good finding can be tuped over to the new version, if however you would like the post removed, or anyone would, I will do so immediately and will not be offended in any way, D 

I don't need to be good at the game, only good enough to beat my opponent,

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#25](/thread/post/12699196#post12699196 "Post Permalink")

  * Jan 13, 2020 7:51am  Jan 13, 2020 7:51am 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

> [Quoting detector](/thread/post/12699192#post12699192 "View Quoted Post")
> 
> Disliked
> 
> {quote} Ursinho, hope you don't mind me posting
> 
> Ignored

Not at all! That's want I wanted, an open discussion...  
  

> [Quoting detector](/thread/post/12699192#post12699192 "View Quoted Post")
> 
> Disliked
> 
> I am testing the older version on the same pairs but omitted the CHF crosses, (live) I have been doing some backtesting and found a very good low DD
> 
> Ignored

So you are testing each pair in a separate chart, right? Do you use the same setfiles for them? If yes, just share it or use it over the BlessingLite.  
  
As I mentioned before: "it's running" does not necessarily mean "it's running properly" ;-) 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#26](/thread/post/12699202#post12699202 "Post Permalink")

  * Jan 13, 2020 8:00am  Jan 13, 2020 8:00am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar638535_1.gif) detector](detector)

  * Joined Dec 2017 | Status: Trader | [3,710 Posts](/search?do=process&provider=Member&searchuser=638535)

> [Quoting ursinho4711](/thread/post/12699196#post12699196 "View Quoted Post")
> 
> Disliked
> 
> {quote} Not at all! That's want I wanted, an open discussion... {quote} So you are testing each pair in a separate chart, right? Do you use the same setfiles for them? If yes, just share it or use it over the BlessingLite. As I mentioned before: "it's running" does not necessarily mean "it's running properly" ;-)
> 
> Ignored

Yes all on separate charts with unique MN, trouble is they use Bollinger bands & MACD in reverse trading, something Blessing light does not allow, or have I missed something? the trades are not as frequent and I may be overstetched a little, however, less frequent will put less stress on the account, I can post the set file if required, thank you for sanctioning my post![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)D  
EDIT  
Same set file for all. 

I don't need to be good at the game, only good enough to beat my opponent,

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#27](/thread/post/12699204#post12699204 "Post Permalink")

  * Jan 13, 2020 8:04am  Jan 13, 2020 8:04am 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

> [Quoting detector](/thread/post/12699202#post12699202 "View Quoted Post")
> 
> Disliked
> 
> trouble is they use Bollinger bands & MACD in reverse trading, something Blessing light does not allow, or have I missed something?
> 
> Ignored

Sure BlessingLite allows it. The "only" difference to the normal Blessing is, that it runs one setting over many pairs at once. Without needing to open 28 charts and having to think about 28 setfiles... 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#28](/thread/post/12699211#post12699211 "Post Permalink")

  * Jan 13, 2020 8:08am  Jan 13, 2020 8:08am 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

The grid seems to work (but does it work right?): 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot1.png
Size: 28 KB](/attachment/image/3527366/thumbnail?d=1578870507)](/attachment/image/3527366?d=1578870507)   

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#29](/thread/post/12699216#post12699216 "Post Permalink")

  * Jan 13, 2020 8:13am  Jan 13, 2020 8:13am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar638535_1.gif) detector](detector)

  * Joined Dec 2017 | Status: Trader | [3,710 Posts](/search?do=process&provider=Member&searchuser=638535)

> [Quoting ursinho4711](/thread/post/12699204#post12699204 "View Quoted Post")
> 
> Disliked
> 
> {quote} Sure BlessingLite allows it. The "only" difference to the normal Blessing is, that it runs one setting over many pairs at once. Without needing to open 28 charts and having to think about 28 setfiles...
> 
> Ignored

Sorry me bad, your right, click on action and noticed "reverse", ok will continue as is, looks like the thread needs to be clear while your testing, will not be far,![](https://resources.faireconomy.media/images/emojis/64/1f441-fe0f.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)D 

I don't need to be good at the game, only good enough to beat my opponent,

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#30](/thread/post/12699227#post12699227 "Post Permalink")

  * Jan 13, 2020 8:24am  Jan 13, 2020 8:24am 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

@ll!  
  
Here is another reason why I wanted to have the EA as multipair-version: now I can monitor and control all open trades via one dashboard. I can set a basket TP, basket SL, close all manually... 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot1.png
Size: 74 KB](/attachment/image/3527370/thumbnail?d=1578871443)](/attachment/image/3527370?d=1578871443)   

[0 ](javascript:void\(0\);) [6 ](javascript:void\(0\);)

  * [#31](/thread/post/12699241#post12699241 "Post Permalink")

  * Jan 13, 2020 8:50am  Jan 13, 2020 8:50am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar638535_1.gif) detector](detector)

  * Joined Dec 2017 | Status: Trader | [3,710 Posts](/search?do=process&provider=Member&searchuser=638535)

> [Quoting ursinho4711](/thread/post/12699227#post12699227 "View Quoted Post")
> 
> Disliked
> 
> @ll! Here is another reason why I wanted to have the EA as multipair-version: now I can monitor and control all open trades via one dashboard. I can set a basket TP, basket SL, close all manually... {image}
> 
> Ignored

Excellent addition![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)

I don't need to be good at the game, only good enough to beat my opponent,

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#32](/thread/post/12699246#post12699246 "Post Permalink")

  * Jan 13, 2020 9:01am  Jan 13, 2020 9:01am 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

... is anyone else besides me enjoying the EA? I think it's fun watching. Better than TV... 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot1.png
Size: 15 KB](/attachment/image/3527384/thumbnail?d=1578873706)](/attachment/image/3527384?d=1578873706)   

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#33](/thread/post/12699251#post12699251 "Post Permalink")

  * Jan 13, 2020 9:05am  Jan 13, 2020 9:05am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar638535_1.gif) detector](detector)

  * Joined Dec 2017 | Status: Trader | [3,710 Posts](/search?do=process&provider=Member&searchuser=638535)

> [Quoting ursinho4711](/thread/post/12699246#post12699246 "View Quoted Post")
> 
> Disliked
> 
> ... is anyone else besides me enjoying the EA? I think it's fun watching. Better than TV... {image}
> 
> Ignored

Suppose I can relate but my own programme is playing, 21 pairs LOL, good luck, time for my bed, hope I wake to us both getting great results, D 

I don't need to be good at the game, only good enough to beat my opponent,

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#34](/thread/post/12699320#post12699320 "Post Permalink")

  * Jan 13, 2020 10:51am  Jan 13, 2020 10:51am 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

As I already feared, now comes the difficult part in bugfixing... basically the EA runs. Opens pending orders. Everything was cool.  
Suddenly it decided to close everything:  
Closed 15 position because Profit Trailing Stop Reached 50%  
  
Analyzing the code, I assume following happened: one pair really reached the condition PTS reached. Went into the Exit Trade Function with the parameter "A" for All. Means: close **all** positions with the corresponding magic number.  
\--> we have to be sure, that when a condition for a pair is met, only actions for that pair should be taken. In this case "close all positions for that pair".  
I will dive into the code again... (didn't I want to sleep?) 

[0 ](javascript:void\(0\);) [3 ](javascript:void\(0\);)

  * [#35](/thread/post/12699337#post12699337 "Post Permalink")

  * Edited 11:55am  Jan 13, 2020 11:17am | Edited 11:55am 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

Okay, more coding ahead. But not today, my head is empty. At least I know where to start:  
  
In the start function:

  1. Count Open Orders, Lots and Totals
  2. Check for and Delete hanging pending orders
  3. Trade Selection Logic

in the subfunction:

  1. Exit Trade Function

Everywhere, where the _**OrdersTotal()**_ appears it needs to be replaced by something like "OrdersTotalPair". Which is the sum of  
  
struct pairinf  
{  
int CbB; // Count buy  
int CbS; // Count sell  
int CpBL; // Count buy limit  
int CpSL; // Count sell limit  
int CpBS; // Count buy stop  
int CpSS; // Count sell stop  
  
Right? Somebody wants to join me coding...? 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#36](/thread/post/12699357#post12699357 "Post Permalink")

  * Jan 13, 2020 11:48am  Jan 13, 2020 11:48am 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

> [Quoting ursinho4711](/thread/post/12699337#post12699337 "View Quoted Post")
> 
> Disliked
> 
> Count Open Orders, Lots and Totals
> 
> Ignored

Some piece of code as discussed in that thread can be used in the part "Count Open Orders, Lots and Totals"  
<https://www.mql5.com/en/forum/142179>  
  
Hm, maybe a new function? I will think about it in my sleep...  
  
(in C++ or mq5 I would work with doubly linked lists: just a chain of ticket-numbers in the struct. Probably I have to stick with arrays in mq4 though...)

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#37](/thread/post/12699370#post12699370 "Post Permalink")

  * Jan 13, 2020 12:03pm  Jan 13, 2020 12:03pm 

  * [ Hackoba](hackoba)

  * | Joined Jun 2019  | Status: Trader | [6 Posts](/search?do=process&provider=Member&searchuser=823396)

> [Quoting ursinho4711](/thread/post/12699079#post12699079 "View Quoted Post")
> 
> Disliked
> 
> {quote} See if that one works, I changed everything to OnXXX... {file} {file}
> 
> Ignored

First of all I would like to Thank you all the coder whose efforts and talents you shared to us.  
  
I try to install on Live account ([XM](/brokers/xm "View XM Broker Profile") ultra low) even BlessingLite_3_v3.9.6.24_beta but have no luck.  
  
MT4 ver 4.00 Build 1220  
  
2020.01.13 10:53:16.047 Expert BlessingLite_3_v3.9.6.25_beta EURUSD#,M5: removed  
2020.01.13 10:53:14.027 Expert BlessingLite_3_v3.9.6.25_beta EURUSD#,M5: loaded successfully 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#38](/thread/post/12699376#post12699376 "Post Permalink")

  * Jan 13, 2020 12:24pm  Jan 13, 2020 12:24pm 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

> [Quoting Hackoba](/thread/post/12699370#post12699370 "View Quoted Post")
> 
> Disliked
> 
> {quote} First of all I would like to Thank you all the coder whose efforts and talents you shared to us. I try to install on Live account (XM ultra low) even BlessingLite_3_v3.9.6.24_beta but have no luck. MT4 ver 4.00 Build 1220 2020.01.13 10:53:16.047 Expert BlessingLite_3_v3.9.6.25_beta EURUSD#,M5: removed 2020.01.13 10:53:14.027 Expert BlessingLite_3_v3.9.6.25_beta EURUSD#,M5: loaded successfully
> 
> Ignored

In the terminal go to expert and see if there is some kind of error message. Might be a division by zero because of missing market-info for a pair in the list. Known problem, it's on my to-do... 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#39](/thread/post/12699377#post12699377 "Post Permalink")

  * Jan 13, 2020 12:26pm  Jan 13, 2020 12:26pm 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

> [Quoting ursinho4711](/thread/post/12699357#post12699357 "View Quoted Post")
> 
> Disliked
> 
> Hm, maybe a new function? I will think about it in my sleep...
> 
> Ignored

Ha! I was thinking too complicated! As simple   
  
if(OrderMagicNumber() != Magic || OrderSymbol() != TradePairs[i])  
continue;  
should do it...  
  
NOW I can go to sleep ;-)  
Good night @all! 

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#40](/thread/post/12699430#post12699430 "Post Permalink")

  * Jan 13, 2020 1:37pm  Jan 13, 2020 1:37pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar102021_3.gif) fx4money](fx4money)

  * Joined May 2009 | Status: Trader | [985 Posts](/search?do=process&provider=Member&searchuser=102021)

> [Quoting ursinho4711](/thread/post/12699079#post12699079 "View Quoted Post")
> 
> Disliked
> 
> {quote} See if that one works, I changed everything to OnXXX... {file} {file}
> 
> Ignored

will test this on demo to see how it work and if it really work and if need to be revised ![](https://resources.faireconomy.media/images/emojis/64/1f61c.png?v=15.1)

golen trades

[2024 lucky gold trade](fx4money#30 "View Trade Explorer") All Time Return: -3.5%

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Blessing Multipair EA
  *   * [ **Reply to Thread** ](/thread/973998-blessing-multipair-ea/reply#reply)

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

[Trading multipair triangles, no stoploss](/thread/917648-trading-multipair-triangles-no-stoploss "Hello forex Folks! 
  
I'd like to share with You my system that I was comming to for many years. I am testing it these days and it gives...") 78 replies

['Blessing' EA Modification Wanted](/thread/271525-blessing-ea-modification-wanted "Hello. 
 
here is a version of BLESSING \(old\) love this version. 
I wonder if someone could if possible to change this code. 
 
I like that...") 3 replies

[Single, Few Pair Traders (1-4) vs. MultiPair Traders (8-20)](/thread/964171-single-few-pair-traders-1-4-vs-multipair-traders "Who gets better results ?? 
  
Put it in another way , if you went for a trading competition and want to achieve &gt;300% ~ 2000% , what would...") 0 replies

[Coding Request for Multipair MTF ADR Dashboard](/thread/683340-coding-request-for-multipair-mtf-adr-dashboard "Can someone code this into indicator???") 2 replies

[trying to make a multipair buy and sell script](/thread/241746-trying-to-make-a-multipair-buy-and-sell "what i like to do is that i add a script on a chart and it will do 
 
open 3 pairs buys or sells. 
 
for example 0.1 lot EURUSD 
          ...") 6 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/973998-blessing-multipair-ea/reply#reply)
  * Subscribe
  * [97](javascript:void\(0\);)

Attachments: Blessing Multipair EA

Tags: Blessing Multipair EA

#  [](/thread/973998-blessing-multipair-ea)Blessing Multipair EA 

  * 

  * [#41](/thread/post/12699432#post12699432 "Post Permalink")

  * Jan 13, 2020 1:39pm  Jan 13, 2020 1:39pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar102021_3.gif) fx4money](fx4money)

  * Joined May 2009 | Status: Trader | [985 Posts](/search?do=process&provider=Member&searchuser=102021)

> [Quoting ursinho4711](/thread/post/12699227#post12699227 "View Quoted Post")
> 
> Disliked
> 
> @ll! Here is another reason why I wanted to have the EA as multipair-version: now I can monitor and control all open trades via one dashboard. I can set a basket TP, basket SL, close all manually... {image}
> 
> Ignored

nice dashboard to have ![](https://resources.faireconomy.media/images/emojis/64/1f61c.png?v=15.1)

golen trades

[2024 lucky gold trade](fx4money#30 "View Trade Explorer") All Time Return: -3.5%

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#42](/thread/post/12699452#post12699452 "Post Permalink")

  * Jan 13, 2020 2:12pm  Jan 13, 2020 2:12pm 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

> [Quoting fx4money](/thread/post/12699430#post12699430 "View Quoted Post")
> 
> Disliked
> 
> {quote} will test this on demo to see how it work and if it really work and if need to be revised ![](https://resources.faireconomy.media/images/emojis/64/1f61c.png?v=15.1)
> 
> Ignored

It works (basically), but please wait: I am just testing the bugfix for closing all positions instead of just closing positions for the TradePair  
  
still did not sleep... 

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#43](/thread/post/12699453#post12699453 "Post Permalink")

  * Jan 13, 2020 2:19pm  Jan 13, 2020 2:19pm 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

> [Quoting fx4money](/thread/post/12699430#post12699430 "View Quoted Post")
> 
> Disliked
> 
> {quote} will test this on demo to see how it work and if it really work and if need to be revised ![](https://resources.faireconomy.media/images/emojis/64/1f61c.png?v=15.1)
> 
> Ignored

Try that one, I introduced the TradePair into the ExitTrade... please see if the exits now work better. Still some work ahead... 

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [BlessingLite_3_v3.9.6.26_beta_odersymbol.ex4](/attachment/file/3527520?d=1578892756) 187 KB | 601 downloads 

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [BlessingLite_3_v3.9.6.26_beta_odersymbol.mq4](/attachment/file/3527521?d=1578892757) 127 KB | 848 downloads 

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#44](/thread/post/12699515#post12699515 "Post Permalink")

  * Jan 13, 2020 3:44pm  Jan 13, 2020 3:44pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar338950_1.gif) cescof](cescof)

  * Joined Jun 2013 | Status: Trader | [1,006 Posts](/search?do=process&provider=Member&searchuser=338950)

> [Quoting ursinho4711](/thread/post/12699246#post12699246 "View Quoted Post")
> 
> Disliked
> 
> ... is anyone else besides me enjoying the EA? I think it's fun watching. Better than TV... {image}
> 
> Ignored

Ok i've started yesterday with setting file you posted and suppose are you using.... (bollinger) But on 5min tf i have totally different pairs traded....  
Broker [ic markets](/brokers/ic-markets "View IC Markets Broker Profile")  
Sure not the same setting i suppose...  
Thanks for effort   
Best regards

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Cattura.PNG
Size: 29 KB](/attachment/image/3527550/thumbnail?d=1578897882)](/attachment/image/3527550?d=1578897882)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#45](/thread/post/12699528#post12699528 "Post Permalink")

  * Jan 13, 2020 4:07pm  Jan 13, 2020 4:07pm 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

> [Quoting cescof](/thread/post/12699515#post12699515 "View Quoted Post")
> 
> Disliked
> 
> {quote} Ok i've started yesterday with setting file you posted and suppose are you using.... (bollinger) But on 5min tf i have totally different pairs traded.... Broker ic markets Sure not the same setting i suppose... Thanks for effort Best regards{image}
> 
> Ignored

unless you did not start the EA **exactly** at the same time, with **exactly** the same environment... then it is almost a must that you have different pairs to trade! Don't forget that we are on a fast timeframe... what did you expect?  
I think I will sleep now...  
  
Bugfixed (closing wrong pending positions) version comes today in the evening... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#46](/thread/post/12699532#post12699532 "Post Permalink")

  * Jan 13, 2020 4:12pm  Jan 13, 2020 4:12pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar338950_1.gif) cescof](cescof)

  * Joined Jun 2013 | Status: Trader | [1,006 Posts](/search?do=process&provider=Member&searchuser=338950)

> [Quoting ursinho4711](/thread/post/12699528#post12699528 "View Quoted Post")
> 
> Disliked
> 
> {quote} unless you did not start the EA exactly at the same time, with exactly the same environment... then it is almost a must that you have different pairs to trade! Don't forget that we are on a fast timeframe... what did you expect? I think I will sleep now... Bugfixed (closing wrong pending positions) version comes today in the evening...
> 
> Ignored

Thanks  
Take care  
Regards 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#47](/thread/post/12699633#post12699633 "Post Permalink")

  * Jan 13, 2020 5:32pm  Jan 13, 2020 5:32pm 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

betabugfix looks good, I will let it run for some more time. Behaviour as expected (or at least hoped): here and there small but steady wins, until now low DD. Just like a squirrel ;-) 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot1.png
Size: 52 KB](/attachment/image/3527582/thumbnail?d=1578904293)](/attachment/image/3527582?d=1578904293)   

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#48](/thread/post/12699748#post12699748 "Post Permalink")

  * Jan 13, 2020 6:44pm  Jan 13, 2020 6:44pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar338950_1.gif) cescof](cescof)

  * Joined Jun 2013 | Status: Trader | [1,006 Posts](/search?do=process&provider=Member&searchuser=338950)

Is this normal? Just order for jpy related pairs?  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Cattura.PNG
Size: 134 KB](/attachment/image/3527638/thumbnail?d=1578908653)](/attachment/image/3527638?d=1578908653)   

  
  
no it wasn't... now i changed chart (AUDUSD) and load again Ea and i have some order placed for all pairs a part jpy ones....still confused  
Regards 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#49](/thread/post/12699754#post12699754 "Post Permalink")

  * Jan 13, 2020 6:46pm  Jan 13, 2020 6:46pm 

  * [ AlexeyRoss](alexeyross)

  * | Joined Mar 2019  | Status: Trader | [45 Posts](/search?do=process&provider=Member&searchuser=779467)

> [Quoting cescof](/thread/post/12699748#post12699748 "View Quoted Post")
> 
> Disliked
> 
> Is this normal? Just order for jpy related pairs? {image}
> 
> Ignored

The same here on H1 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot2.png
Size: 86 KB](/attachment/image/3527640/thumbnail?d=1578908782)](/attachment/image/3527640?d=1578908782)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#50](/thread/post/12699761#post12699761 "Post Permalink")

  * Jan 13, 2020 6:51pm  Jan 13, 2020 6:51pm 

  * [ richard96816](richard96816)

  * Joined Dec 2018 | Status: Trader | [564 Posts](/search?do=process&provider=Member&searchuser=741833)

Sticking with the original Inputs / Properties names would have been nice. Especially for compatibility with the Blessing manual and for those of us that have optimized the original a few thousand times ... :-)  
  
Also nice when you're looking at the code and making adjustments.  
  
That's what all those double semicolons were for. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#51](/thread/post/12699874#post12699874 "Post Permalink")

  * Jan 13, 2020 7:54pm  Jan 13, 2020 7:54pm 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

> [Quoting richard96816](/thread/post/12699761#post12699761 "View Quoted Post")
> 
> Disliked
> 
> That's what all those double semicolons were for.
> 
> Ignored

Ah, thanks for this info! When I looked at the code from versions .10 on following, I thought: "what the heck...". Now it makes sense...  
  

> [Quoting richard96816](/thread/post/12699761#post12699761 "View Quoted Post")
> 
> Disliked
> 
> Sticking with the original Inputs / Properties names would have been nice
> 
> Ignored

I think I did it, or at least tried to as much as possible. Many variables just got an pairinfo[]. in front of their original name, as they moved into the big struct. I tried to avoid as much work as possible ;-) ...  
... and to keep the blessing "heart" as original as possible  
  
(did not get much sleep the last days before Sidney open..)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#52](/thread/post/12699914#post12699914 "Post Permalink")

  * Jan 13, 2020 8:13pm  Jan 13, 2020 8:13pm 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

> [Quoting richard96816](/thread/post/12699761#post12699761 "View Quoted Post")
> 
> Disliked
> 
> Especially for compatibility with the Blessing manual and for those of us that have optimized the original a few thousand times ...
> 
> Ignored

If we wanted to, we could restart from version 09 (or better 13?) again. I stuck with most of the delta-files, that's why I already counted to 26 in the version number.  
The first approach was to see whether it makes sense to follow the idea of a multipair-Blessing. When I look at the results of my last beta-version (with the 5-minutes set-file) I have to say: certainly yes!  
The big difference from the original version to the multipair version is "just" the struct and the big for-to loop. And cleaning the code from parts that are not needed or even contraproductive in the multipair version (e.g. ForceMarketCond or hedging on another pair).  
  
That the compatibility to older versions is given, can be seen in the fact that older set-files still can be used.  
  
Have a great start into the week @ll and thanks for any further helpful input! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#53](/thread/post/12700017#post12700017 "Post Permalink")

  * Jan 13, 2020 9:11pm  Jan 13, 2020 9:11pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar405432_1.gif) fabio.g](fabio.g)

  * | Joined Mar 2015  | Status: Trader | [658 Posts](/search?do=process&provider=Member&searchuser=405432)

> [Quoting ursinho4711](/thread/post/12699453#post12699453 "View Quoted Post")
> 
> Disliked
> 
> {quote} Try that one, I introduced the TradePair into the ExitTrade... please see if the exits now work better. Still some work ahead... {file} {file}
> 
> Ignored

Hello i would like to report the following bug i guess 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot2.png
Size: 3 KB](/attachment/image/3527753/thumbnail?d=1578917444)](/attachment/image/3527753?d=1578917444)   

Attached Image

![](/attachment/image/3527752?d=1578917424)

[GridEA](fabio.g#67 "View Trade Explorer") Return This Year: na

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#54](/thread/post/12700154#post12700154 "Post Permalink")

  * Jan 13, 2020 10:35pm  Jan 13, 2020 10:35pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar836530_33.gif) josi](josi)

  * Joined Aug 2019 | Status: Trader | [730 Posts](/search?do=process&provider=Member&searchuser=836530)

> [Quoting richard96816](/thread/post/12699761#post12699761 "View Quoted Post")
> 
> Disliked
> 
> Sticking with the original Inputs / Properties names would have been nice. Especially for compatibility with the Blessing manual and for those of us that have optimized the original a few thousand times ... :-)
> 
> Ignored

as to set-files and optimizing, you may want to take a look at Andreas Clenow's new book:  
  
Rules and Variations  
Generally speaking, you should aim for as few rules as possible and as few variations as possible.  
Once you have arrived at a model purpose, you need to figure out how to formulate this purpose in terms of trading rules. These rules should be as simple and as few as you can muster. Robust trading models, those that work over the long run, tend to be the ones that keep things simple.  
Any complexity you add needs to pay off. You should see complexity as something inherently bad, something which needs to justify its existence. Any complexity you want to add to your model needs to have a clear and meaningful benefit.  
Moreover, any complication or rule that you add needs to have a real life explanation. You can’t just add a rule just because it seems to improve backtest performance. The rule needs to fit into the logic of the model purpose and play a clear rule in achieving that purpose.  
Once you have arrived at a set of rules for testing your market theory, you probably want to try some variations. Note that there is a world apart between testing variations and optimization.  
As an example, let’s assume that you want to test a mean reversion type of strategy. You believe that when a stock has fallen four standard deviations below its 60 day linear regression line, it tends to bounce two standard deviations up again.  
Now you already have multiple parameters in play. Modeling and testing these rules is a fairly simple task. You could try a few variations of this, perhaps to expect the bounce by three or five standard deviations, using 30 or 90 day regression or a variation in the target bounce distance.  
Making a few variations like this can be useful, both for testing parameter stability and to actually trade some variations of the rules to mitigate over-fitting risks.  
What you don’t want to do is to run an optimizer to figure out that the optimal entry is at 3.78 standard deviations, on a 73 day regression, using a target of 1.54 standard deviations. Such data is absolute rubbish.  
Optimizers will tell you what the perfect parameters was for the past. They will also con you into a false sense of security, and make you believe that they have any sort of predictive value. Which they don’t.  
No, skip the optimization. But make a few variations of the rules, using reasonable, sensible numbers.  
From: Clenow's new book Trading Evolved - Anyone can Build Killer Trading Strategies in Python  
See also: Carver, Systematic Trading, 2015 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#55](/thread/post/12700182#post12700182 "Post Permalink")

  * Jan 13, 2020 10:52pm  Jan 13, 2020 10:52pm 

  * [ richard96816](richard96816)

  * Joined Dec 2018 | Status: Trader | [564 Posts](/search?do=process&provider=Member&searchuser=741833)

> [Quoting josi](/thread/post/12700154#post12700154 "View Quoted Post")
> 
> Disliked
> 
> {quote} as to set-files and optimizing, you may want to take a look at Andreas Clenow's new book: Rules and Variations Generally speaking, you should aim for as few rules as possible and as few variations as possible. Once you have arrived at a model purpose, you need to figure out how to formulate this purpose in terms of trading rules. These rules should be as simple and as few as you can muster. Robust trading models, those that work over the long run, tend to be the ones that keep things simple. Any complexity you add needs to pay off. You should...
> 
> Ignored

Oh jeez.  
  
We're so far past that book it's not funny. We have Blessing. Yes, it's complex and a hassle to optimize. But god does it work! It was originally designed to change fewer rules, and that works. Or you can change more rules and make more money. You choose.  
  
We're not starting from scratch, which is what books like that one usually address. We have a tool that can be relatively easily tailored to almost any currency pair and made to lock into useful repeating patterns. It works! Backwards and forwards! Money in the bank. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#56](/thread/post/12700198#post12700198 "Post Permalink")

  * Jan 13, 2020 11:02pm  Jan 13, 2020 11:02pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar836530_33.gif) josi](josi)

  * Joined Aug 2019 | Status: Trader | [730 Posts](/search?do=process&provider=Member&searchuser=836530)

> [Quoting richard96816](/thread/post/12700182#post12700182 "View Quoted Post")
> 
> Disliked
> 
> {quote} Oh jeez. We're so far past that book it's not funny. We have Blessing. Yes, it's complex and a hassle to optimize. But god does it work! It was originally designed to change fewer rules, and that works. Or you can change more rules and make more money. You choose. We're not starting from scratch, which is what books like that one usually address. We have a tool that can be relatively easily tailored to almost any currency pair and made to lock into useful repeating patterns. It works! Backwards and forwards! Money in the bank.
> 
> Ignored

well, I wasn't trying to undermine your project.  
What you write tells me, though, that you haven't read any of the books mentioned - but nevertheless feel inclined to criticize their content. I can only hope that you are a bit more rational and diligent in your optimizations.  
Best of luck. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#57](/thread/post/12700640#post12700640 "Post Permalink")

  * Jan 14, 2020 3:30am  Jan 14, 2020 3:30am 

  * [ Mcxtrader](mcxtrader)

  * | Joined Jun 2017  | Status: Trader | [203 Posts](/search?do=process&provider=Member&searchuser=589792)

Any idea on this please.   
I keep seeing this message continuously. Anyway to stop this message please. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot2.png
Size: 42 KB](/attachment/image/3528022/thumbnail?d=1578940219)](/attachment/image/3528022?d=1578940219)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#58](/thread/post/12700646#post12700646 "Post Permalink")

  * Jan 14, 2020 3:41am  Jan 14, 2020 3:41am 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

> [Quoting Mcxtrader](/thread/post/12700640#post12700640 "View Quoted Post")
> 
> Disliked
> 
> Any idea on this please. I keep seeing this message continuously. Anyway to stop this message please. {image}
> 
> Ignored

in the source file, around line 245, find "bool Debug = true;" and set it to "bool Debug = false";  
To make it more comfortable, you can write "input bool Debug = false;"  
In this way you can switch the option on/off via the EA settings. Will change this in the next version. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#59](/thread/post/12700842#post12700842 "Post Permalink")

  * Jan 14, 2020 6:25am  Jan 14, 2020 6:25am 

  * [ richard96816](richard96816)

  * Joined Dec 2018 | Status: Trader | [564 Posts](/search?do=process&provider=Member&searchuser=741833)

> [Quoting josi](/thread/post/12700198#post12700198 "View Quoted Post")
> 
> Disliked
> 
> {quote} well, I wasn't trying to undermine your project. What you write tells me, though, that you haven't read any of the books mentioned - but nevertheless feel inclined to criticize their content. I can only hope that you are a bit more rational and diligent in your optimizations. Best of luck.
> 
> Ignored

I've read many of the books. Useful and helpful, for writing EAs. All the important (and high-falutin) issues regarding optimization of new EAs. Blessing is not new. It's already written. It works fairly well, better than any others I've tested or written.  
  
One issue I left out. Optimization needs to be fast. Because you need to forward test five or 10 or more instances and choose the good ones. That's the main reason many of the classical works suggest a small rule-set, to speed up the terribly slow optimization process. (And to make the results last a long time, which I find less important.) Forward testing is the real test.  
  
My apologies if my response was overly strident. It was late. I've read quite a few good books and lots of online discussions with lots of smart people. I'm starting to get the hang of this stuff. :-)  
  
I keep having ideas on how to enhance Blessing's trading abilities. And then I remember how effective it is already and how I really don't want to damage it in the process.  
  
I've had the idea of deploying a fair number of instances on difference pairs to hopefully make the results more robust. Or perhaps to turn her into a multi-pair system. That seems like pretty good idea. But keeping the core as it is seems like a great plan, at least for now. That means that most of the advanced and foundational optimization techniques are unnecessary and already done.  
  
Thanks very much for your contribution to the discussion. I should not have been so dismissive. You put a lot of thought and effort into your post and are very much appreciated for that. Many will likely learn from it, and that's a good thing.  
  
Best of luck! 

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#60](/thread/post/12701181#post12701181 "Post Permalink")

  * Edited 2:41pm  Jan 14, 2020 2:29pm | Edited 2:41pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar405432_1.gif) fabio.g](fabio.g)

  * | Joined Mar 2015  | Status: Trader | [658 Posts](/search?do=process&provider=Member&searchuser=405432)

first day of trading, demo, let see how it goes 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot1.png
Size: 10 KB](/attachment/image/3528319/thumbnail?d=1578980464)](/attachment/image/3528319?d=1578980464)   

[GridEA](fabio.g#67 "View Trade Explorer") Return This Year: na

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Blessing Multipair EA
  *   * [ **Reply to Thread** ](/thread/973998-blessing-multipair-ea/reply#reply)

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

[Trading multipair triangles, no stoploss](/thread/917648-trading-multipair-triangles-no-stoploss "Hello forex Folks! 
  
I'd like to share with You my system that I was comming to for many years. I am testing it these days and it gives...") 78 replies

['Blessing' EA Modification Wanted](/thread/271525-blessing-ea-modification-wanted "Hello. 
 
here is a version of BLESSING \(old\) love this version. 
I wonder if someone could if possible to change this code. 
 
I like that...") 3 replies

[Single, Few Pair Traders (1-4) vs. MultiPair Traders (8-20)](/thread/964171-single-few-pair-traders-1-4-vs-multipair-traders "Who gets better results ?? 
  
Put it in another way , if you went for a trading competition and want to achieve &gt;300% ~ 2000% , what would...") 0 replies

[Coding Request for Multipair MTF ADR Dashboard](/thread/683340-coding-request-for-multipair-mtf-adr-dashboard "Can someone code this into indicator???") 2 replies

[trying to make a multipair buy and sell script](/thread/241746-trying-to-make-a-multipair-buy-and-sell "what i like to do is that i add a script on a chart and it will do 
 
open 3 pairs buys or sells. 
 
for example 0.1 lot EURUSD 
          ...") 6 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/973998-blessing-multipair-ea/reply#reply)
  * Subscribe
  * [97](javascript:void\(0\);)

Attachments: Blessing Multipair EA

Tags: Blessing Multipair EA

#  [](/thread/973998-blessing-multipair-ea)Blessing Multipair EA 

  * 

  * [#61](/thread/post/12701218#post12701218 "Post Permalink")

  * Jan 14, 2020 3:24pm  Jan 14, 2020 3:24pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar836530_33.gif) josi](josi)

  * Joined Aug 2019 | Status: Trader | [730 Posts](/search?do=process&provider=Member&searchuser=836530)

> [Quoting richard96816](/thread/post/12700842#post12700842 "View Quoted Post")
> 
> Disliked
> 
> {quote}I should not have been so dismissive. You put a lot of thought and effort into your post and are very much appreciated for that. Many will likely learn from it, and that's a good thing. Best of luck!
> 
> Ignored

Not to worry! People tend to get carried away once they're in the midst of a huge project.  
Reading your thread one can feel that you're in it, heart and soul - for now.  
And I very much appreciate that.   
All the best. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#62](/thread/post/12701280#post12701280 "Post Permalink")

  * Jan 14, 2020 4:20pm  Jan 14, 2020 4:20pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar102021_3.gif) fx4money](fx4money)

  * Joined May 2009 | Status: Trader | [985 Posts](/search?do=process&provider=Member&searchuser=102021)

> [Quoting cescof](/thread/post/12699748#post12699748 "View Quoted Post")
> 
> Disliked
> 
> Is this normal? Just order for jpy related pairs? {image} no it wasn't... now i changed chart (AUDUSD) and load again Ea and i have some order placed for all pairs a part jpy ones....still confused Regards
> 
> Ignored

means there are still bugs inside i guess ![](https://resources.faireconomy.media/images/emojis/64/1f61c.png?v=15.1)

golen trades

[2024 lucky gold trade](fx4money#30 "View Trade Explorer") All Time Return: -3.5%

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#63](/thread/post/12701310#post12701310 "Post Permalink")

  * Jan 14, 2020 4:44pm  Jan 14, 2020 4:44pm 

  * [ AlexeyRoss](alexeyross)

  * | Joined Mar 2019  | Status: Trader | [45 Posts](/search?do=process&provider=Member&searchuser=779467)

2 days of testing, that looks nice! 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot2.png
Size: 80 KB](/attachment/image/3528401/thumbnail?d=1578987894)](/attachment/image/3528401?d=1578987894)   

[0 ](javascript:void\(0\);) [3 ](javascript:void\(0\);)

  * [#64](/thread/post/12702413#post12702413 "Post Permalink")

  * Jan 15, 2020 1:20am  Jan 15, 2020 1:20am 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

> [Quoting AlexeyRoss](/thread/post/12701310#post12701310 "View Quoted Post")
> 
> Disliked
> 
> 2 days of testing, that looks nice! {image}
> 
> Ignored

Thanks for the feedback!  
  
Yes, also mine looks good in M5 and with the M5 "fits all" setfile.  
  
I know, and that is why I posted the mq4 sourcefile, that there are still open points. These need to be handled with care, as debugging is not that easy with MT4. Okay, with live data it is a little bit better, but still a hassle.  
My biggest headache, still, is the exit-function: I see that it does not work correctly now, as we do not only have one pair but many pairs. Therefore we have to compare **magic number and symbols** when it comes to pair-related exits (e.g. Profit Trailing Stop Reached) or just the magic number on a full exit (e.g. Equity Stop Loss). Sounds simple but as I am tired, I would appreciate any help ;-)  
I already made a matrix, on which conditions Blessing closes trades and pending orders: 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot1.png
Size: 26 KB](/attachment/image/3528881/thumbnail?d=1579018699)](/attachment/image/3528881?d=1579018699)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#65](/thread/post/12702460#post12702460 "Post Permalink")

  * Jan 15, 2020 1:46am  Jan 15, 2020 1:46am 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

> [Quoting AlexeyRoss](/thread/post/12701310#post12701310 "View Quoted Post")
> 
> Disliked
> 
> 2 days of testing, that looks nice! {image}
> 
> Ignored

I f I was to rename the EA, I would rename it from "Blessing" to "Squirrel" ![](https://resources.faireconomy.media/images/emojis/64/1f43f-fe0f.png?v=15.1)  
Started this morning, better don't touch because the exits do not work well up to now 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot1.png
Size: 51 KB](/attachment/image/3528916/thumbnail?d=1579020347)](/attachment/image/3528916?d=1579020347)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#66](/thread/post/12702497#post12702497 "Post Permalink")

  * Jan 15, 2020 2:03am  Jan 15, 2020 2:03am 

  * [ AlexeyRoss](alexeyross)

  * | Joined Mar 2019  | Status: Trader | [45 Posts](/search?do=process&provider=Member&searchuser=779467)

> [Quoting ursinho4711](/thread/post/12702460#post12702460 "View Quoted Post")
> 
> Disliked
> 
> {quote} I f I was to rename the EA, I would rename it from "Blessing" to "Squirrel" ![](https://resources.faireconomy.media/images/emojis/64/1f43f-fe0f.png?v=15.1) Started this morning, better don't touch because the exits do not work well up to now {image}
> 
> Ignored

Thats True, but still its profitable, iv had 2 or 3 pending loses, but he waits for a little profit on them and it works. Hope that one big lose wont blow all this wins up)) 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#67](/thread/post/12702533#post12702533 "Post Permalink")

  * Jan 15, 2020 2:26am  Jan 15, 2020 2:26am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar338950_1.gif) cescof](cescof)

  * Joined Jun 2013 | Status: Trader | [1,006 Posts](/search?do=process&provider=Member&searchuser=338950)

> [Quoting ursinho4711](/thread/post/12702413#post12702413 "View Quoted Post")
> 
> Disliked
> 
> {quote} Thanks for the feedback! Yes, also mine looks good in M5 and with the M5 "fits all" setfile. I know, and that is why I posted the mq4 sourcefile, that there are still open points. These need to be handled with care, as debugging is not that easy with MT4. Okay, with live data it is a little bit better, but still a hassle. My biggest headache, still, is the exit-function: I see that it does not work correctly now, as we do not only have one pair but many pairs. Therefore we have to compare magic number and symbols when it comes to pair-related...
> 
> Ignored

please how could we help you?  
Thanks  
Best regards 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#68](/thread/post/12702603#post12702603 "Post Permalink")

  * Jan 15, 2020 3:10am  Jan 15, 2020 3:10am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar405432_1.gif) fabio.g](fabio.g)

  * | Joined Mar 2015  | Status: Trader | [658 Posts](/search?do=process&provider=Member&searchuser=405432)

could you the dev check the highlighted 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot1.png
Size: 126 KB](/attachment/image/3528990/thumbnail?d=1579025294)](/attachment/image/3528990?d=1579025294)   

Attached Image

![](/attachment/image/3528992?d=1579025422)

[GridEA](fabio.g#67 "View Trade Explorer") Return This Year: na

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#69](/thread/post/12702665#post12702665 "Post Permalink")

  * Jan 15, 2020 3:45am  Jan 15, 2020 3:45am 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

I am impressed... I was following the GBPJPY during the day, as in another thread we discussed a pattern that assumed "GBPJPY sell". Well, Blessing resolved it alone. Better than me manually...  
  
It works. Now comes the finetuning (see above: ExitTrade function)  
  
obs: I don't think it is a good idea (please correct me) to use XAUUSD with the settings for the forex pairs at the same time 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Image1.png
Size: 6 KB](/attachment/image/3529019/thumbnail?d=1579027361)](/attachment/image/3529019?d=1579027361)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#70](/thread/post/12703303#post12703303 "Post Permalink")

  * Jan 15, 2020 3:03pm  Jan 15, 2020 3:03pm 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

New version (29 beta) in post #1.  
  
Hehe, if anyone wondered, why so many trades opened: there was a nice bug that calculated some indicators in a wrong way. Nothing big and impossible to see on the data, the results were good, weren't they? But this is more like winning in the lottery than real forex trading.  
The actual version is now using the correct indicator parameters. The result is, that less trades open. But better they open in a reliable way than just coincidentally ;-)  
  
Known issues: ExitTrades still not merged to multipair (see this post: [https://www.forexfactory.com/showthr...3#post12702413](https://www.forexfactory.com/showthread.php?p=12702413#post12702413))  
  
Anyway: I am so confident, I put the EA on a small live account. Using a basket stop loss via dashboard, though...  
  
Thanks to fxraider for searching and finding that nasty bug! 

[0 ](javascript:void\(0\);) [3 ](javascript:void\(0\);)

  * [#71](/thread/post/12703304#post12703304 "Post Permalink")

  * Jan 15, 2020 3:07pm  Jan 15, 2020 3:07pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar102021_3.gif) fx4money](fx4money)

  * Joined May 2009 | Status: Trader | [985 Posts](/search?do=process&provider=Member&searchuser=102021)

> [Quoting ursinho4711](/thread/post/12703303#post12703303 "View Quoted Post")
> 
> Disliked
> 
> New version (29 beta) in post #1. Hehe, if anyone wondered, why so many trades opened: there was a nice bug that calculated some indicators in a wrong way. Nothing big and impossible to see on the data, the results were good, weren't they? But this is more like winning in the lottery than real forex trading. The actual version is now using the correct indicator parameters. The result is, that less trades open. But better they open in a reliable way than just coincidentally ;-) Known issues: ExitTrades still not merged to multipair (see this post:...
> 
> Ignored

hi, sorry to ask, the ea now is ready to be tested? i want to test it on demo to see how it really work too ![](https://resources.faireconomy.media/images/emojis/64/1f61c.png?v=15.1)

golen trades

[2024 lucky gold trade](fx4money#30 "View Trade Explorer") All Time Return: -3.5%

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#72](/thread/post/12703321#post12703321 "Post Permalink")

  * Jan 15, 2020 3:23pm  Jan 15, 2020 3:23pm 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

> [Quoting fx4money](/thread/post/12703304#post12703304 "View Quoted Post")
> 
> Disliked
> 
> {quote} hi, sorry to ask, the ea now is ready to be tested? i want to test it on demo to see how it really work too ![](https://resources.faireconomy.media/images/emojis/64/1f61c.png?v=15.1)
> 
> Ignored

Hi! On demo it is already running since a while.  
As I wrote: I am using this version live now! Even knowing some issues with the ExitTrades. On Demo you can test it without problems. It does not even opencloseopencloseopenclose anymore ;-)  
  
Have fun and please give us feedback! Maybe you can take a look into the source code, function "ExitTrades". There is my stomache ache... 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#73](/thread/post/12703399#post12703399 "Post Permalink")

  * Edited 6:03pm  Jan 15, 2020 4:39pm | Edited 6:03pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar3294_6.gif) JackJones](jackjones)

  * Joined Aug 2005 | Status: 888 | [1,021 Posts](/search?do=process&provider=Member&searchuser=3294)

> [Quoting ursinho4711](/thread/post/12698762#post12698762 "View Quoted Post")
> 
> Disliked
> 
> Remember that post? [https://www.forexfactory.com/showthr...7#post12551567](https://www.forexfactory.com/showthread.php?p=12551567#post12551567) Well, I used the settings and made a backtest from 01.Nov.2019 to 10.Jan.2020. 5 Minutes timeframe, for all 28 pairs. What can I say: that already looks like the winner to be tested on the Blessing-Multipair. Can't wait for Sidney open... Here are the results: {image}
> 
> Ignored

2months? ![](https://resources.faireconomy.media/images/emojis/64/1f4aa.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f4aa.png?v=15.1) whats the risk like? ![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1) demo time 

grist for the mill

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#74](/thread/post/12703566#post12703566 "Post Permalink")

  * Jan 15, 2020 6:18pm  Jan 15, 2020 6:18pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar102021_3.gif) fx4money](fx4money)

  * Joined May 2009 | Status: Trader | [985 Posts](/search?do=process&provider=Member&searchuser=102021)

> [Quoting ursinho4711](/thread/post/12703321#post12703321 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi! On demo it is already running since a while. As I wrote: I am using this version live now! Even knowing some issues with the ExitTrades. On Demo you can test it without problems. It does not even opencloseopencloseopenclose anymore ;-) Have fun and please give us feedback! Maybe you can take a look into the source code, function "ExitTrades". There is my stomache ache...
> 
> Ignored

what time frame, and in which folder should put the setfiles? never used em before ![](https://resources.faireconomy.media/images/emojis/64/1f61c.png?v=15.1)

golen trades

[2024 lucky gold trade](fx4money#30 "View Trade Explorer") All Time Return: -3.5%

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#75](/thread/post/12703567#post12703567 "Post Permalink")

  * Jan 15, 2020 6:18pm  Jan 15, 2020 6:18pm 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

Good morning @all!  
  
Could not sleep and took a look at my VPS on mobile phone. Quickly got up to fast-fix one annoying bug: when ExitTrades "A" is sent from e.g. _**Trailing SL reached**_ , then ALL open trades were closed and not only the specific pair.  
I replaced the "A" with "B" in a new version, hope this already improves things, knowing that this is not all related to ExitTrades  
  
@all:  
I do not want to sound rude, but I was hoping for more help and work-sharing on the code. It is not "my" project. Blessing was left as open source and I started to do a multipair version, trying to stay with the Blessing core. That does not mean that I should do all the work ;-)  
I do not get paid for this and I am using my holiday time for coding. My wife and kid are not really happy to see a tired husband/dad the whole day...  
So: please contribute!  
Thanks  
  
(Richard and Neo: thanks for your help) 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#76](/thread/post/12703595#post12703595 "Post Permalink")

  * Jan 15, 2020 6:35pm  Jan 15, 2020 6:35pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar102021_3.gif) fx4money](fx4money)

  * Joined May 2009 | Status: Trader | [985 Posts](/search?do=process&provider=Member&searchuser=102021)

testing is on. using ea v30, preset v24 5min allpairs. please confirm if i am using the right or latest combo 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: 20115 blessing v30.png
Size: 166 KB](/attachment/image/3529454/thumbnail?d=1579080907)](/attachment/image/3529454?d=1579080907)   

golen trades

[2024 lucky gold trade](fx4money#30 "View Trade Explorer") All Time Return: -3.5%

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#77](/thread/post/12703625#post12703625 "Post Permalink")

  * Jan 15, 2020 6:46pm  Jan 15, 2020 6:46pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar338950_1.gif) cescof](cescof)

  * Joined Jun 2013 | Status: Trader | [1,006 Posts](/search?do=process&provider=Member&searchuser=338950)

> [Quoting ursinho4711](/thread/post/12703567#post12703567 "View Quoted Post")
> 
> Disliked
> 
> Good morning @all! Could not sleep and took a look at my VPS on mobile phone. Quickly got up to fast-fix one annoying bug: when ExitTrades "A" is sent from e.g. Trailing SL reached, then ALL open trades were closed and not only the specific pair. I replaced the "A" with "B" in a new version, hope this already improves things, knowing that this is not all related to ExitTrades @all: I do not want to sound rude, but I was hoping for more help and work-sharing on the code. It is not "my" project. Blessing was left as open source and I started to do...
> 
> Ignored

ok it was same think i'm studying now....with 0.29....and all orders closed when trailing tp for one order is reached...  
Now i will try with 0.30  
Best regards 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#78](/thread/post/12703629#post12703629 "Post Permalink")

  * Jan 15, 2020 6:48pm  Jan 15, 2020 6:48pm 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

> [Quoting fx4money](/thread/post/12703595#post12703595 "View Quoted Post")
> 
> Disliked
> 
> testing is on. using ea v30, preset v24 5min allpairs. please confirm if i am using the right or latest combo {image}
> 
> Ignored

Looks good! Btw, the V30 version does not need a set-file for the demo-tests. I changed the presets in the code to the values from the 5-minutes-setfile. I am lazy...  
One hint: change the comment in the settings to e.g. BL30-1 (Blessing 30, first run) and activate the comment in the terminal. In this way you can trace the trades and orders easier.  
Remember: ExitTrades is still under construction ;-) 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot1.png
Size: 47 KB](/attachment/image/3529468/thumbnail?d=1579081663)](/attachment/image/3529468?d=1579081663)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#79](/thread/post/12703650#post12703650 "Post Permalink")

  * Jan 15, 2020 6:55pm  Jan 15, 2020 6:55pm 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

> [Quoting cescof](/thread/post/12703625#post12703625 "View Quoted Post")
> 
> Disliked
> 
> {quote} ok it was same think i'm studying now....with 0.29....and all orders closed when trailing tp for one order is reached... Now i will try with 0.30 Best regards
> 
> Ignored

V30 does not do it anymore (which does not mean that it doesn't hold other surprises for us ;-) ) 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot1.png
Size: 18 KB](/attachment/image/3529470/thumbnail?d=1579082097)](/attachment/image/3529470?d=1579082097)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#80](/thread/post/12703732#post12703732 "Post Permalink")

  * Jan 15, 2020 7:26pm  Jan 15, 2020 7:26pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar116307_2.gif) rosalieone](rosalieone)

  * Joined Sep 2009 | Status: Trader | [540 Posts](/search?do=process&provider=Member&searchuser=116307)

> [Quoting ursinho4711](/thread/post/12703650#post12703650 "View Quoted Post")
> 
> Disliked
> 
> {quote} V30 does not do it anymore (which does not mean that it doesn't hold other surprises for us ;-) ) {image}
> 
> Ignored

Hi,  
Thanks for that wonderful EA.  
In order for me to contribute could you please add a line for brokers with pairs with suffix ?  
Thanks  
Best 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Blessing Multipair EA
  *   * [ **Reply to Thread** ](/thread/973998-blessing-multipair-ea/reply#reply)

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

[Trading multipair triangles, no stoploss](/thread/917648-trading-multipair-triangles-no-stoploss "Hello forex Folks! 
  
I'd like to share with You my system that I was comming to for many years. I am testing it these days and it gives...") 78 replies

['Blessing' EA Modification Wanted](/thread/271525-blessing-ea-modification-wanted "Hello. 
 
here is a version of BLESSING \(old\) love this version. 
I wonder if someone could if possible to change this code. 
 
I like that...") 3 replies

[Single, Few Pair Traders (1-4) vs. MultiPair Traders (8-20)](/thread/964171-single-few-pair-traders-1-4-vs-multipair-traders "Who gets better results ?? 
  
Put it in another way , if you went for a trading competition and want to achieve &gt;300% ~ 2000% , what would...") 0 replies

[Coding Request for Multipair MTF ADR Dashboard](/thread/683340-coding-request-for-multipair-mtf-adr-dashboard "Can someone code this into indicator???") 2 replies

[trying to make a multipair buy and sell script](/thread/241746-trying-to-make-a-multipair-buy-and-sell "what i like to do is that i add a script on a chart and it will do 
 
open 3 pairs buys or sells. 
 
for example 0.1 lot EURUSD 
          ...") 6 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/973998-blessing-multipair-ea/reply#reply)
  * Subscribe
  * [97](javascript:void\(0\);)

Attachments: Blessing Multipair EA

Tags: Blessing Multipair EA

#  [](/thread/973998-blessing-multipair-ea)Blessing Multipair EA 

  * 

  * [#81](/thread/post/12703943#post12703943 "Post Permalink")

  * Jan 15, 2020 9:05pm  Jan 15, 2020 9:05pm 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

> [Quoting rosalieone](/thread/post/12703732#post12703732 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi, Thanks for that wonderful EA. In order for me to contribute could you please add a line for brokers with pairs with suffix ? Thanks Best
> 
> Ignored

Just for you ;-)  
  
Please test it, as I don`t have the possibility to do so...  
  
__**Alternatively**__ , I guess, you can use the V30 version and create your own comma separated list. For example with the suffix "i":  
AUDCADi,AUDCHFi,AUDJPYi,AUDNZDi,AUDUSDi,CADCHFi,CADJPYi,CHFJPYi,EURAUDi,EURCADi,EURCHFi,EURGBPi,EURJPYi,EURNZDi,EURUSDi,GBPAUDi,GBPCADi,GBPCHFi,GBPJPYi,GBPNZDi,GBPUSDi,NZDCADi,NZDCHFi,NZDJPYi,NZDUSDi,USDCADi,USDCHFi,USDJPYi  
  
But please try the v31 and see whether it works... Grüzi! 

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [BlessingLite_3_v3.9.6.31_gamma.ex4](/attachment/file/3529594?d=1579089854) 193 KB | 693 downloads 

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#82](/thread/post/12704000#post12704000 "Post Permalink")

  * Jan 15, 2020 9:48pm  Jan 15, 2020 9:48pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar116307_2.gif) rosalieone](rosalieone)

  * Joined Sep 2009 | Status: Trader | [540 Posts](/search?do=process&provider=Member&searchuser=116307)

> [Quoting ursinho4711](/thread/post/12703943#post12703943 "View Quoted Post")
> 
> Disliked
> 
> {quote} Just for you ;-) Please test it, as I don`t have the possibility to do so... Alternatively, I guess, you can use the V30 version and create your own comma separated list. For example with the suffix "i": AUDCADi,AUDCHFi,AUDJPYi,AUDNZDi,AUDUSDi,CADCHFi,CADJPYi,CHFJPYi,EURAUDi,EURCADi,EURCHFi,EURGBPi,EURJPYi,EURNZDi,EURUSDi,GBPAUDi,GBPCADi,GBPCHFi,GBPJPYi,GBPNZDi,GBPUSDi,NZDCADi,NZDCHFi,NZDJPYi,NZDUSDi,USDCADi,USDCHFi,USDJPYi But please try the v31 and see whether it works... Grüzi! {file}
> 
> Ignored

Hi, Thanks amigo !  
I've read it twice but i cant find the line for the suffix  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: blessing31.png
Size: 95 KB](/attachment/image/3529622/thumbnail?d=1579092495)](/attachment/image/3529622?d=1579092495)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#83](/thread/post/12704002#post12704002 "Post Permalink")

  * Jan 15, 2020 9:49pm  Jan 15, 2020 9:49pm 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

> [Quoting JackJones](/thread/post/12703399#post12703399 "View Quoted Post")
> 
> Disliked
> 
> {quote} 2months? ![](https://resources.faireconomy.media/images/emojis/64/1f4aa.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f4aa.png?v=15.1) whats the risk like? ![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1) demo time
> 
> Ignored

No risk, no fun!  
Soon we will all fall into the grave, become [He] 2s2^2p^2 (C, not CO2)  
How long do you want to wait? Alternatively you can go to your bank and ask for -1% ;-) 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#84](/thread/post/12704006#post12704006 "Post Permalink")

  * Edited 10:23pm  Jan 15, 2020 9:51pm | Edited 10:23pm 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

> [Quoting rosalieone](/thread/post/12704000#post12704000 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi, Thanks amigo ! I've read it twice but i cant find the line for the suffix {image}
> 
> Ignored

Don't need: it should find it automatically... just start the EA.  
Adding a suffix in the settings would have been too easy ;-) 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#85](/thread/post/12704014#post12704014 "Post Permalink")

  * Jan 15, 2020 9:54pm  Jan 15, 2020 9:54pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar116307_2.gif) rosalieone](rosalieone)

  * Joined Sep 2009 | Status: Trader | [540 Posts](/search?do=process&provider=Member&searchuser=116307)

> [Quoting ursinho4711](/thread/post/12704002#post12704002 "View Quoted Post")
> 
> Disliked
> 
> {quote} No risk, no fun! Soon we will all fall into the grave, become [He] 2s2^2p^2 (C, not CO2) How long do you want to wait? Alternatively you can go to your bank and ask for -1% ;-)
> 
> Ignored

Depends how much 1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p3 you take

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#86](/thread/post/12704033#post12704033 "Post Permalink")

  * Jan 15, 2020 10:08pm  Jan 15, 2020 10:08pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar116307_2.gif) rosalieone](rosalieone)

  * Joined Sep 2009 | Status: Trader | [540 Posts](/search?do=process&provider=Member&searchuser=116307)

> [Quoting ursinho4711](/thread/post/12704006#post12704006 "View Quoted Post")
> 
> Disliked
> 
> {quote} Don't need: it should find it automaticall... just start the EA. Adding a suffix in the settings would have been too easy ;-)
> 
> Ignored

Well done, thanks ! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#87](/thread/post/12704096#post12704096 "Post Permalink")

  * Edited 11:32pm  Jan 15, 2020 10:35pm | Edited 11:32pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar3294_6.gif) JackJones](jackjones)

  * Joined Aug 2005 | Status: 888 | [1,021 Posts](/search?do=process&provider=Member&searchuser=3294)

> [Quoting ursinho4711](/thread/post/12704002#post12704002 "View Quoted Post")
> 
> Disliked
> 
> {quote} No risk, no fun!
> 
> Ignored

sure, then we get news events.. speaking of which does this bad boy have a news filter?  
  
well 30%/100% returns always have risk, its implied! 

grist for the mill

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#88](/thread/post/12704239#post12704239 "Post Permalink")

  * Jan 15, 2020 11:37pm  Jan 15, 2020 11:37pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar116307_2.gif) rosalieone](rosalieone)

  * Joined Sep 2009 | Status: Trader | [540 Posts](/search?do=process&provider=Member&searchuser=116307)

And here we go  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: 2020-01-15_1534.png
Size: 19 KB](/attachment/image/3529728/thumbnail?d=1579098946)](/attachment/image/3529728?d=1579098946)   

  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: 2020-01-15_1534_001.png
Size: 25 KB](/attachment/image/3529729/thumbnail?d=1579098946)](/attachment/image/3529729?d=1579098946)   

  
With 5 min set Ursinho4711 mentioned  
The beast love Japan 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#89](/thread/post/12704256#post12704256 "Post Permalink")

  * Jan 15, 2020 11:41pm  Jan 15, 2020 11:41pm 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

> [Quoting JackJones](/thread/post/12704096#post12704096 "View Quoted Post")
> 
> Disliked
> 
> speaking of which does this bad boy have a news filter?
> 
> Ignored

At least it survived this challenge today (on a live account, small but alive)...: 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot1.png
Size: 6 KB](/attachment/image/3529736/thumbnail?d=1579099147)](/attachment/image/3529736?d=1579099147)   

Attached Image

![](/attachment/image/3529739?d=1579099289)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#90](/thread/post/12705121#post12705121 "Post Permalink")

  * Edited 10:17am  Jan 16, 2020 9:50am | Edited 10:17am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar3294_6.gif) JackJones](jackjones)

  * Joined Aug 2005 | Status: 888 | [1,021 Posts](/search?do=process&provider=Member&searchuser=3294)

i have two running on different brokers and one took a long on eur/cad highs last night and i'm trying to figure out why... it seems to get long on BB breakouts , but mostly shorts them at other times.. is that part of the 'blessing' code?  
  
i'd look myself later today but i haven't hacked code since the early naughties.  
  

> [Quoting rosalieone](/thread/post/12704239#post12704239 "View Quoted Post")
> 
> Disliked
> 
> The beast love Japan
> 
> Ignored

you mean like GODZILLA ?? ![](https://resources.faireconomy.media/images/emojis/64/1f3c3-200d-2642-fe0f.png?v=15.1)

grist for the mill

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#91](/thread/post/12705494#post12705494 "Post Permalink")

  * Jan 16, 2020 4:47pm  Jan 16, 2020 4:47pm 

  * [ kodakwhite](kodakwhite)

  * | Joined Sep 2016  | Status: Trader | [166 Posts](/search?do=process&provider=Member&searchuser=490920)

You need to start trades manually or it's open close on it's own?   
  
Can somebody post code for this EA? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#92](/thread/post/12706507#post12706507 "Post Permalink")

  * Jan 17, 2020 12:21am  Jan 17, 2020 12:21am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar102021_3.gif) fx4money](fx4money)

  * Joined May 2009 | Status: Trader | [985 Posts](/search?do=process&provider=Member&searchuser=102021)

> [Quoting ursinho4711](/thread/post/12704256#post12704256 "View Quoted Post")
> 
> Disliked
> 
> {quote} At least it survived this challenge today (on a live account, small but alive)...: {image} {image}
> 
> Ignored

best if you run the ea on demo and live accounts at the same time to see how much difference is there in term of executions. demo test so far is making profit. 

golen trades

[2024 lucky gold trade](fx4money#30 "View Trade Explorer") All Time Return: -3.5%

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#93](/thread/post/12706618#post12706618 "Post Permalink")

  * Jan 17, 2020 1:04am  Jan 17, 2020 1:04am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar102021_3.gif) fx4money](fx4money)

  * Joined May 2009 | Status: Trader | [985 Posts](/search?do=process&provider=Member&searchuser=102021)

open positions and profits so far ![](https://resources.faireconomy.media/images/emojis/64/1f61c.png?v=15.1)

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: 20117 bless multi.png
Size: 174 KB](/attachment/image/3530876/thumbnail?d=1579190624)](/attachment/image/3530876?d=1579190624)   
[![Click to Enlarge

Name: 20117 bless multi profit.png
Size: 184 KB](/attachment/image/3530878/thumbnail?d=1579190650)](/attachment/image/3530878?d=1579190650)   

golen trades

[2024 lucky gold trade](fx4money#30 "View Trade Explorer") All Time Return: -3.5%

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#94](/thread/post/12706635#post12706635 "Post Permalink")

  * Jan 17, 2020 1:11am  Jan 17, 2020 1:11am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar405432_1.gif) fabio.g](fabio.g)

  * | Joined Mar 2015  | Status: Trader | [658 Posts](/search?do=process&provider=Member&searchuser=405432)

bad day for me, -100 

[GridEA](fabio.g#67 "View Trade Explorer") Return This Year: na

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#95](/thread/post/12706647#post12706647 "Post Permalink")

  * Jan 17, 2020 1:14am  Jan 17, 2020 1:14am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar338950_1.gif) cescof](cescof)

  * Joined Jun 2013 | Status: Trader | [1,006 Posts](/search?do=process&provider=Member&searchuser=338950)

> [Quoting fabio.g](/thread/post/12706635#post12706635 "View Quoted Post")
> 
> Disliked
> 
> bad day for me, -100
> 
> Ignored

same here , but some recover now.....  
I'd like to change set file to try ... can i use every blessing set file or what?  
I'm asking because i'm tryong to use an old set file customized by me but seems nothing happen here no any scan from Ea is this normal?  
Thanks regards 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#96](/thread/post/12706652#post12706652 "Post Permalink")

  * Jan 17, 2020 1:16am  Jan 17, 2020 1:16am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar338950_1.gif) cescof](cescof)

  * Joined Jun 2013 | Status: Trader | [1,006 Posts](/search?do=process&provider=Member&searchuser=338950)

> [Quoting fx4money](/thread/post/12706618#post12706618 "View Quoted Post")
> 
> Disliked
> 
> open positions and profits so far ![](https://resources.faireconomy.media/images/emojis/64/1f61c.png?v=15.1) {image} {image}
> 
> Ignored

seems your h1 set file is better then 5min one... 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#97](/thread/post/12706662#post12706662 "Post Permalink")

  * Jan 17, 2020 1:20am  Jan 17, 2020 1:20am 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

The Squirrel ;-)  
Thanks for the feedback. My both running EAs, Demo and Live, look well also. Anyway I think we should introduce a new parameter: maximimum pairs to trade at once (MaxTradePairs or something like this). When this number is reached, no new pending orders are placed and all others should be deleted.  
Setting the value to 0 on a running EA could be used for a slow shutdown, without killing open trades.  
  
I follow the EA more or less 24 hours a day&night, good that I don't like to watch TV. Just my family thinks I am a little bit eeehm strange..  
I saw that at some time many (20?) pairs were being traded at once. The DD was also getting bigger (3%).  
I don't know yet, which is a reasonable number. Maybe 7 or 14? 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#98](/thread/post/12706688#post12706688 "Post Permalink")

  * Jan 17, 2020 1:30am  Jan 17, 2020 1:30am 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

> [Quoting fabio.g](/thread/post/12706635#post12706635 "View Quoted Post")
> 
> Disliked
> 
> bad day for me, -100
> 
> Ignored

paciência, cara. Por isso o nome é Blessing e não corre corre... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#99](/thread/post/12706749#post12706749 "Post Permalink")

  * Jan 17, 2020 2:00am  Jan 17, 2020 2:00am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar73206_1.gif) Vicente](vicente)

  * Joined Jun 2008 | Status: Trader | [247 Posts](/search?do=process&provider=Member&searchuser=73206)

[quote = ursinho4711; 12706662] The Squirrel ;-) Gracias por los comentarios. Mis dos EA en ejecución, Demo y Live, también se ven bien. De todos modos, creo que deberíamos introducir un nuevo parámetro: pares de maximimum para comerciar a la vez (MaxTradePairs o algo así). Cuando se alcanza este número, no se colocan nuevos pedidos pendientes y se deben eliminar todos los demás. Establecer el valor a 0 en un EA en ejecución podría usarse para un apagado lento, sin matar las operaciones abiertas. Sigo el EA más o menos las 24 horas del día y de la noche, bueno que no me gusta ver la televisión. Solo mi familia piensa que soy un poco eeehm extraño. Vi que en algún momento se intercambiaron muchos (20?) Pares a la vez. El DD también se estaba haciendo más grande (3%). Todavía no lo sé, que es un número razonable. ¿Quizás 7 o 14? [/ Quote]  
  
  
First of all thank you for your work. I don't speak English so I use the translator.  
  
I paid a long time ago for a multi-currency EA, it did not work as I expected but it has some characteristics that I considered appropriate at the time. You can control the N. of trades per pair by balance the n. toatla de trades. You can put a limit on opening the trade in% and open again the possibility of continuing to work exceeding a% less.  
  
It is a bit complicated to explain but I attach a pdf with the characteristics.  
  
If it helps, I am willing to share the code to see if you can work some interesting things.  
  
I await your confirmation ..  
  
Greetings from Ecuador

Attached Image

![](/attachment/image/3530944?d=1579194369)

Attached File(s)

![File Type: pdf](https://assets.faireconomy.media/images/attach/pdf.gif) [1 multi.pdf](/attachment/file/3530938?d=1579194030) 697 KB | 643 downloads 

[IH - B221](vicente#23 "View Trade Explorer") Return Today: -0.2%

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#100](/thread/post/12706753#post12706753 "Post Permalink")

  * Jan 17, 2020 2:01am  Jan 17, 2020 2:01am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar102021_3.gif) fx4money](fx4money)

  * Joined May 2009 | Status: Trader | [985 Posts](/search?do=process&provider=Member&searchuser=102021)

> [Quoting ursinho4711](/thread/post/12706662#post12706662 "View Quoted Post")
> 
> Disliked
> 
> The Squirrel ;-) Thanks for the feedback. My both running EAs, Demo and Live, look well also. Anyway I think we should introduce a new parameter: maximimum pairs to trade at once (MaxTradePairs or something like this). When this number is reached, no new pending orders are placed and all others should be deleted. Setting the value to 0 on a running EA could be used for a slow shutdown, without killing open trades. I follow the EA more or less 24 hours a day&night, good that I don't like to watch TV. Just my family thinks I am a little bit eeehm...
> 
> Ignored

would be nice if pairs to trade could be chosen. dont like to trade chf, jpy and gbp ![](https://resources.faireconomy.media/images/emojis/64/1f61c.png?v=15.1)

golen trades

[2024 lucky gold trade](fx4money#30 "View Trade Explorer") All Time Return: -3.5%

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Blessing Multipair EA
  *   * [ **Reply to Thread** ](/thread/973998-blessing-multipair-ea/reply#reply)

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

[Trading multipair triangles, no stoploss](/thread/917648-trading-multipair-triangles-no-stoploss "Hello forex Folks! 
  
I'd like to share with You my system that I was comming to for many years. I am testing it these days and it gives...") 78 replies

['Blessing' EA Modification Wanted](/thread/271525-blessing-ea-modification-wanted "Hello. 
 
here is a version of BLESSING \(old\) love this version. 
I wonder if someone could if possible to change this code. 
 
I like that...") 3 replies

[Single, Few Pair Traders (1-4) vs. MultiPair Traders (8-20)](/thread/964171-single-few-pair-traders-1-4-vs-multipair-traders "Who gets better results ?? 
  
Put it in another way , if you went for a trading competition and want to achieve &gt;300% ~ 2000% , what would...") 0 replies

[Coding Request for Multipair MTF ADR Dashboard](/thread/683340-coding-request-for-multipair-mtf-adr-dashboard "Can someone code this into indicator???") 2 replies

[trying to make a multipair buy and sell script](/thread/241746-trying-to-make-a-multipair-buy-and-sell "what i like to do is that i add a script on a chart and it will do 
 
open 3 pairs buys or sells. 
 
for example 0.1 lot EURUSD 
          ...") 6 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/973998-blessing-multipair-ea/reply#reply)
  * Subscribe
  * [97](javascript:void\(0\);)

Attachments: Blessing Multipair EA

Tags: Blessing Multipair EA

#  [](/thread/973998-blessing-multipair-ea)Blessing Multipair EA 

  * 

  * [#101](/thread/post/12706766#post12706766 "Post Permalink")

  * Jan 17, 2020 2:09am  Jan 17, 2020 2:09am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar338950_1.gif) cescof](cescof)

  * Joined Jun 2013 | Status: Trader | [1,006 Posts](/search?do=process&provider=Member&searchuser=338950)

> [Quoting fx4money](/thread/post/12706753#post12706753 "View Quoted Post")
> 
> Disliked
> 
> {quote} would be nice if pairs to trade could be chosen. dont like to trade chf, jpy and gbp ![](https://resources.faireconomy.media/images/emojis/64/1f61c.png?v=15.1)
> 
> Ignored

i think tou can just edit setting file.....and chose your preferred instead of all 28... 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#102](/thread/post/12706775#post12706775 "Post Permalink")

  * Jan 17, 2020 2:14am  Jan 17, 2020 2:14am 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

> [Quoting cescof](/thread/post/12706766#post12706766 "View Quoted Post")
> 
> Disliked
> 
> {quote} i think tou can just edit setting file.....and chose your preferred instead of all 28...
> 
> Ignored

Jipp, that's it. You can even trade soy-beans if you like ;-)  
  
Anyway, my dream would be a dashboard with integrated blessing one day... 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot1.png
Size: 20 KB](/attachment/image/3530961/thumbnail?d=1579195091)](/attachment/image/3530961?d=1579195091)   

[0 ](javascript:void\(0\);) [3 ](javascript:void\(0\);)

  * [#103](/thread/post/12706779#post12706779 "Post Permalink")

  * Jan 17, 2020 2:18am  Jan 17, 2020 2:18am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar73206_1.gif) Vicente](vicente)

  * Joined Jun 2008 | Status: Trader | [247 Posts](/search?do=process&provider=Member&searchuser=73206)

> [Quoting ursinho4711](/thread/post/12706775#post12706775 "View Quoted Post")
> 
> Disliked
> 
> {quote} Jipp, that's it. You can even trade soy-beans if you like ;-) Anyway, my dream would be a dashboard with integrated blessing one day...
> 
> Ignored

[https://www.forexfactory.com/showthr...9#post12706749](https://www.forexfactory.com/showthread.php?p=12706749#post12706749)

[IH - B221](vicente#23 "View Trade Explorer") Return Today: -0.2%

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#104](/thread/post/12706784#post12706784 "Post Permalink")

  * Jan 17, 2020 2:20am  Jan 17, 2020 2:20am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar7798_2.gif) Spikehunter](spikehunter)

  * Joined Mar 2006 | Status: Trader | [699 Posts](/search?do=process&provider=Member&searchuser=7798)

Hi All,  
Could someone point me in the direction of the system philosophy please. I have read the thread and have it running but would like to know more.  
Regards 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#105](/thread/post/12706826#post12706826 "Post Permalink")

  * Jan 17, 2020 2:38am  Jan 17, 2020 2:38am 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

> [Quoting Spikehunter](/thread/post/12706784#post12706784 "View Quoted Post")
> 
> Disliked
> 
> Hi All, Could someone point me in the direction of the system philosophy please. I have read the thread and have it running but would like to know more. Regards
> 
> Ignored

<https://www.forexfactory.com/showthread.php?t=792598>  
That's where the heart comes from. I've already been using it though long time before joining ForexFactory... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#106](/thread/post/12706828#post12706828 "Post Permalink")

  * Jan 17, 2020 2:39am  Jan 17, 2020 2:39am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar7798_2.gif) Spikehunter](spikehunter)

  * Joined Mar 2006 | Status: Trader | [699 Posts](/search?do=process&provider=Member&searchuser=7798)

> [Quoting ursinho4711](/thread/post/12706826#post12706826 "View Quoted Post")
> 
> Disliked
> 
> {quote} <https://www.forexfactory.com/showthread.php?t=792598> That's where the heart comes from. I've already been using it though long time before joining ForexFactory...
> 
> Ignored

Thank you 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#107](/thread/post/12707197#post12707197 "Post Permalink")

  * Jan 17, 2020 7:14am  Jan 17, 2020 7:14am 

  * [ richard96816](richard96816)

  * Joined Dec 2018 | Status: Trader | [564 Posts](/search?do=process&provider=Member&searchuser=741833)

> [Quoting ursinho4711](/thread/post/12706826#post12706826 "View Quoted Post")
> 
> Disliked
> 
> {quote} <https://www.forexfactory.com/showthread.php?t=792598> That's where the heart comes from. I've already been using it though long time before joining ForexFactory...
> 
> Ignored

Do you favor one group of settings for all pairs or do you plan on eventually making things more complex? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#108](/thread/post/12707221#post12707221 "Post Permalink")

  * Jan 17, 2020 7:37am  Jan 17, 2020 7:37am 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

> [Quoting richard96816](/thread/post/12707197#post12707197 "View Quoted Post")
> 
> Disliked
> 
> {quote} Do you favor one group of settings for all pairs or do you plan on eventually making things more complex?
> 
> Ignored

Hi Richard! No, on-size-fits all was my plan. I know that it is difficult to find out and can be a little bit dangerous as Blessing has this Martingale-like style (no, it is not real Martingale), depending on the multiplier. I am just experiencing this on GBPJPY ;-)  
If it was too complex, it would be like single Blessings on separate charts and no gain. My opinion... you probably thought of an individual settings-array for each pair to trade?  
The dashboards that I know use one settings for all pairs. Do you have an example for a more complex one?  
Hm... hm... I mean, that would REALLY be cool to click on a pair in a dashboard and alter the setting individually. hm hm hm... I need some more weeks of holiday... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#109](/thread/post/12707243#post12707243 "Post Permalink")

  * Jan 17, 2020 8:00am  Jan 17, 2020 8:00am 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

@Richard  
Individual settings for each pair:  
I was thinking while doing the laundry... from the programming aspect it is not that difficult, thanks to the struct for each pair to trade. The question is, which parameters should be set individually? All?  
As I write this, I am thinking of loading parameter files for single pairs. Now I am really on a trip... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#110](/thread/post/12707249#post12707249 "Post Permalink")

  * Jan 17, 2020 8:06am  Jan 17, 2020 8:06am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar102021_3.gif) fx4money](fx4money)

  * Joined May 2009 | Status: Trader | [985 Posts](/search?do=process&provider=Member&searchuser=102021)

> [Quoting ursinho4711](/thread/post/12707243#post12707243 "View Quoted Post")
> 
> Disliked
> 
> @Richard Individual settings for each pair: I was thinking while doing the laundry... from the programming aspect it is not that difficult, thanks to the struct for each pair to trade. The question is, which parameters should be set individually? All? As I write this, I am thinking of loading parameter files for single pairs. Now I am really on a trip...
> 
> Ignored

certainly will be best for each pair to have it own setting since the average daily range is different for most pairs. 

golen trades

[2024 lucky gold trade](fx4money#30 "View Trade Explorer") All Time Return: -3.5%

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#111](/thread/post/12707266#post12707266 "Post Permalink")

  * Jan 17, 2020 8:44am  Jan 17, 2020 8:44am 

  * [ richard96816](richard96816)

  * Joined Dec 2018 | Status: Trader | [564 Posts](/search?do=process&provider=Member&searchuser=741833)

I've tested quite a few multi-pair EAs. Many start out with very impressive results and then degrade into large draw downs and slow trading after a while or other problems.  
  
Here's an example:  
BGNBGN832CL832CL  

Inserted Code
    
    
    Symbol Trdes Win%   Profit  P/day ProfFac STime Etime T/Day EA
    GBPAUD    7  100%   181.46   5.13    --    9/09 10/15  0.2  v3w     +++++++
    GBPCHF    6  100%   198.30   5.05    --    9/06 10/15  0.2  v3w     ++++++
    GBPCAD   10  100%   372.94   5.02    --    9/05 11/18  0.1  v3w     ++++++++++
    GBPJPY    4  100%   200.81   2.92    --    9/04 11/12  0.1  v3w     ++++
    GBPUSD    5  100%   148.29   2.46    --    9/05 11/04  0.1  v3w     +++++
    AUDCAD    2  100%    15.15   1.64    --    9/04  9/13  0.2  v3w     ++
    EURCAD    2  100%    15.07   1.61    --    9/04  9/13  0.2  v3w     ++
    USDCAD    6   83%   164.32   1.49  50.49   9/12 12/31  0.1  v3w     ++-+++
    CADJPY    5  100%    54.63   1.03    --    9/05 10/27  0.1  v3w     +++++
    USDCHF    2  100%   108.92   1.00    --    9/13 12/31  0.0  v3w     ++
    NZDJPY    6  100%   102.03   0.89    --    9/03 12/27  0.1  v3w     ++++++
    AUDJPY    5  100%   100.23   0.88    --    9/03 12/26  0.0  v3w     +++++
    CHFJPY    6  100%    86.56   0.86    --    9/04 12/13  0.1  v3w     ++++++
    AUDCHF    1  100%     6.31   0.85    --    9/06  9/13  0.1  v3w     +
    EURGBP    2  100%    43.23   0.79    --    9/05 10/29  0.0  v3w     ++
    EURCHF    1  100%     4.65   0.63    --    9/06  9/13  0.1  v3w     +
    EURJPY    3  100%    67.55   0.62    --    9/04 12/23  0.0  v3w     +++
    USDJPY    3  100%    27.48   0.35    --    9/04 11/21  0.0  v3w     +++
    NZDUSD    2  100%    33.12   0.25    --    9/03  1/15  0.0  v3w     ++
    AUDUSD    3  100%    24.96   0.19    --    9/04  1/16  0.0  v3w     +++
    CADCHF    1    0%    -0.54  -0.54   0.00  10/08 10/08  1.0  v3w     -
    Total    82        1955.47  33.12

Wonderful win rate. But it required a $50K account! I've seen others that rack up amazing profits at first, only to stop trading for months with equity tied up in wandering trades.  
  
If you could trade five or ten pairs with optimized parameters for each, while profiting from multi-pair basket logic too, you might outperform all the others. Even if you relied on a single genetic optimization pass for each pair I think you could do very well.   
  
Fill a folder (directory) with set files and have the EA access them by name creating the pair list and parameters from the files it finds. After reading a file it could be moved to an archive folder. New files appearing in the primary folder would cause old parameters to be overwritten or new pairs to be added.  
  
(Or even build in auto-optimization, but that's a whole new batch of craziness.) :-)  
  
Trading 28 pairs, especially with the same parameters for each will eventually require a large account or produce unacceptable losses. 

[0 ](javascript:void\(0\);) [5 ](javascript:void\(0\);)

  * [#112](/thread/post/12707277#post12707277 "Post Permalink")

  * Jan 17, 2020 9:12am  Jan 17, 2020 9:12am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar86801_11.gif) emmanuel7788](emmanuel7788)

  * Joined Nov 2008 | Status: Trader | [47,707 Posts](/search?do=process&provider=Member&searchuser=86801)

> [Quoting richard96816](/thread/post/12707266#post12707266 "View Quoted Post")
> 
> Disliked
> 
> I've tested quite a few multi-pair EAs. Many start out with very impressive results and then degrade into large draw downs and slow trading after a while or other problems. Here's an example: BGNBGN832CL832CL Symbol Trdes Win% Profit P/day ProfFac STime Etime T/Day EA GBPAUD 7 100% 181.46 5.13 -- 9/09 10/15 0.2 v3w +++++++ GBPCHF 6 100% 198.30 5.05 -- 9/06 10/15 0.2 v3w ++++++ GBPCAD 10 100% 372.94 5.02 -- 9/05 11/18 0.1 v3w ++++++++++ GBPJPY 4 100% 200.81 2.92 -- 9/04 11/12 0.1 v3w ++++ GBPUSD 5 100% 148.29 2.46 -- 9/05 11/04 0.1 v3w +++++ AUDCAD...
> 
> Ignored

  
![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1) trading dangerously is not recommended when trading with real hard earned money.  
  
play with demo money and learn how Blessing3 works in all market conditions and master how B3 works and **tame this monster and take it on your daily stroll in the forex park .. make some money.**

Honesty is a very expensive gift. You wont find it in cheap people.WBuffett

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#113](/thread/post/12707290#post12707290 "Post Permalink")

  * Edited 10:02am  Jan 17, 2020 9:30am | Edited 10:02am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar3294_6.gif) JackJones](jackjones)

  * Joined Aug 2005 | Status: 888 | [1,021 Posts](/search?do=process&provider=Member&searchuser=3294)

> [Quoting richard96816](/thread/post/12707266#post12707266 "View Quoted Post")
> 
> Disliked
> 
> added. (Or even build in auto-optimization, but that's a whole new batch of craziness.) :-) Trading 28 pairs, especially with the same parameters for each will eventually require a large account or produce unacceptable losses.
> 
> Ignored

nice post thanks for the info. i've cut my second demo down to 6-10 pairs that i filter out of the all-pairs EA (the ones it seems to be trading well) .  
  
so far this week the all_pairs is up about 4% but it's still holding the EUR/CAD long and a g/j short (2% DD), wonder what it will do. 

grist for the mill

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#114](/thread/post/12707332#post12707332 "Post Permalink")

  * Jan 17, 2020 10:36am  Jan 17, 2020 10:36am 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

> [Quoting JackJones](/thread/post/12707290#post12707290 "View Quoted Post")
> 
> Disliked
> 
> g/j short (2% DD), wonder what it will do.
> 
> Ignored

Mine is at the third stage (0.01 / 0.03 / 0.09) and waiting to sell more 0.27 lots... the last stage. Would have done something similar manually ;-)  
  
@all  
thanks for sharing your thoughts and ideas in this thread. I really appreciate it. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#115](/thread/post/12707884#post12707884 "Post Permalink")

  * Jan 17, 2020 7:00pm  Jan 17, 2020 7:00pm 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

> [Quoting JackJones](/thread/post/12707290#post12707290 "View Quoted Post")
> 
> Disliked
> 
> but it's still holding the EUR/CAD long and a g/j short (2% DD), wonder what it will do.
> 
> Ignored

Hehe, went well. Though I did not sleep much, one eye was with the dashboard. DD went up to -5.65%. Okay, nothing to become nervous about, but as the EA is still in a pre-beta version, I needed to take care of my testing live account. I mean, it is real money. Not too much, but real..  
(Blessing)Slippage helped in the gbpaud, took some of the win in the gbpjpy. But so what: this was the only basket that closed with a small minus. All others green and over the testing time, very green in the big basket ;-)  
Anyway I will reduce the set of pairs, maybe take out gbp and jpy. They make me nervous... 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot1.png
Size: 29 KB](/attachment/image/3531492/thumbnail?d=1579255038)](/attachment/image/3531492?d=1579255038)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#116](/thread/post/12707919#post12707919 "Post Permalink")

  * Jan 17, 2020 7:13pm  Jan 17, 2020 7:13pm 

  * [ procmail](procmail)

  * | Joined May 2018  | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=676819)

> [Quoting ursinho4711](/thread/post/12707884#post12707884 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hehe, went well. Though I did not sleep much, one eye was with the dashboard. DD went up to -5.65%. Okay, nothing to become nervous about, but as the EA is still in a pre-beta version, I needed to take care of my testing live account. I mean, it is real money. Not too much, but real.. (Blessing)Slippage helped in the gbpaud, took some of the win in the gbpjpy. But so what: this was the only basket that closed with a small minus. All others green and over the testing time, very green in the big basket ;-) Anyway I will reduce the set of pairs,...
> 
> Ignored

Curious, how much did you use for your live account? What would be a nice minimum to use? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#117](/thread/post/12707929#post12707929 "Post Permalink")

  * Jan 17, 2020 7:17pm  Jan 17, 2020 7:17pm 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

> [Quoting procmail](/thread/post/12707919#post12707919 "View Quoted Post")
> 
> Disliked
> 
> Curious, how much did you use for your live account?
> 
> Ignored

2000€  
But, as Richard already stated, it is not enough if you trade with 28 pairs. As I was watching the EA all the time, I stopped new trades and even closed some green ones manually, to get more margin in case the gbpjpy would need the 0.27 lots. It did not need though, but it was close... 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#118](/thread/post/12707980#post12707980 "Post Permalink")

  * Jan 17, 2020 7:39pm  Jan 17, 2020 7:39pm 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

> [Quoting procmail](/thread/post/12707919#post12707919 "View Quoted Post")
> 
> Disliked
> 
> What would be a nice minimum to use?
> 
> Ignored

Depends on your settings ;-) Remember to have enough free margin if things get tough. If the EA cannot open bigger trades, then the system is worthless.  
See the example gbpaud in my last screenshot: the EA had a pending order sell limit with 0.09 lots to help the other trades in DD. At 11:20:03 the limit was reached, ten minutes later the basket closed with a win ;-)  
The gbpjpy was even worse, but came back without needing help from the 0.27 lots.  
  
Back to your question: I think not less than 500USD for each pair to trade is the minimum in a real and serious setup. What do the others think? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#119](/thread/post/12708171#post12708171 "Post Permalink")

  * Jan 17, 2020 8:58pm  Jan 17, 2020 8:58pm 

  * [ procmail](procmail)

  * | Joined May 2018  | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=676819)

> [Quoting ursinho4711](/thread/post/12707929#post12707929 "View Quoted Post")
> 
> Disliked
> 
> {quote} 2000€ But, as Richard already stated, it is not enough if you trade with 28 pairs. As I was watching the EA all the time, I stopped new trades and even closed some green ones manually, to get more margin in case the gbpjpy would need the 0.27 lots. It did not need though, but it was close...
> 
> Ignored

Hmmm, I see. Maybe I should remove some volatile pairs like GBPJPY and also CHF pairs while testing on a small live account.  
  
How do you handle weekends? Do you close them all manually on friday or just let them be? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#120](/thread/post/12708197#post12708197 "Post Permalink")

  * Jan 17, 2020 9:18pm  Jan 17, 2020 9:18pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar3294_6.gif) JackJones](jackjones)

  * Joined Aug 2005 | Status: 888 | [1,021 Posts](/search?do=process&provider=Member&searchuser=3294)

i might try close risky pairs before the weekend if they are just floating for a small loss.  
  
the demo my all-pairs EA seems to have handled the week well.  
  
the second demo i have been filtering and playing with to 'best traded' pairs and it seems to have misshandled eur/cad and decided it wanted to sell 20 mlots of e/u, so not sure if that was me messing with it or what, but interesting to see.  
  
the two demos are with two different brokers so it seems it traded and is also holding some pairs the other broker account never opened.. so i will look at those over the weekend.  
  
might be to do with the computer rebooting one night or maybe a lost internet connection, not sure ?? have not run EAs for many years ![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)

grist for the mill

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Blessing Multipair EA
  *   * [ **Reply to Thread** ](/thread/973998-blessing-multipair-ea/reply#reply)

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

[Trading multipair triangles, no stoploss](/thread/917648-trading-multipair-triangles-no-stoploss "Hello forex Folks! 
  
I'd like to share with You my system that I was comming to for many years. I am testing it these days and it gives...") 78 replies

['Blessing' EA Modification Wanted](/thread/271525-blessing-ea-modification-wanted "Hello. 
 
here is a version of BLESSING \(old\) love this version. 
I wonder if someone could if possible to change this code. 
 
I like that...") 3 replies

[Single, Few Pair Traders (1-4) vs. MultiPair Traders (8-20)](/thread/964171-single-few-pair-traders-1-4-vs-multipair-traders "Who gets better results ?? 
  
Put it in another way , if you went for a trading competition and want to achieve &gt;300% ~ 2000% , what would...") 0 replies

[Coding Request for Multipair MTF ADR Dashboard](/thread/683340-coding-request-for-multipair-mtf-adr-dashboard "Can someone code this into indicator???") 2 replies

[trying to make a multipair buy and sell script](/thread/241746-trying-to-make-a-multipair-buy-and-sell "what i like to do is that i add a script on a chart and it will do 
 
open 3 pairs buys or sells. 
 
for example 0.1 lot EURUSD 
          ...") 6 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/973998-blessing-multipair-ea/reply#reply)
  * Subscribe
  * [97](javascript:void\(0\);)

Attachments: Blessing Multipair EA

Tags: Blessing Multipair EA

#  [](/thread/973998-blessing-multipair-ea)Blessing Multipair EA 

  * 

  * [#121](/thread/post/12708227#post12708227 "Post Permalink")

  * Jan 17, 2020 9:32pm  Jan 17, 2020 9:32pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar116307_2.gif) rosalieone](rosalieone)

  * Joined Sep 2009 | Status: Trader | [540 Posts](/search?do=process&provider=Member&searchuser=116307)

Two days trading on demo and it continues loving japan (i wonder why...)  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: res2.png
Size: 68 KB](/attachment/image/3531636/thumbnail?d=1579264346)](/attachment/image/3531636?d=1579264346)   

  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: res1.png
Size: 26 KB](/attachment/image/3531637/thumbnail?d=1579264346)](/attachment/image/3531637?d=1579264346)   

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#122](/thread/post/12708255#post12708255 "Post Permalink")

  * Jan 17, 2020 9:51pm  Jan 17, 2020 9:51pm 

  * [ cool366](cool366)

  * | Additional Username  | Joined Jan 2020 | [6 Posts](/search?do=process&provider=Member&searchuser=907756)

Hy anyone check this eA on live account or not, anyone have any EA that place sl and tp both i really like Budak Ubat but thats not with SL 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#123](/thread/post/12708516#post12708516 "Post Permalink")

  * Jan 17, 2020 11:41pm  Jan 17, 2020 11:41pm 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

> [Quoting procmail](/thread/post/12708171#post12708171 "View Quoted Post")
> 
> Disliked
> 
> How do you handle weekends? Do you close them all manually on friday or just let them be?
> 
> Ignored

I was thinking of following:

  1. on London close, close all trades in profit (green)
  2. close all pending orders for new pairs
  3. do not allow pending orders for new pairs
  4. let open the other (red) open trades

will do that manually today, a flag "UseWeekendShutDown" would be good in the next version  
Another thing I thought of, to be able to use the lot-increment for open trades: for every pending order on an open trade, reduce the new variable "MaxOpenPairs" (or whatever the name will be) by one and delete the oldest pending orders for a new pair 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#124](/thread/post/12708519#post12708519 "Post Permalink")

  * Jan 17, 2020 11:42pm  Jan 17, 2020 11:42pm 

  * [ procmail](procmail)

  * | Joined May 2018  | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=676819)

> [Quoting rosalieone](/thread/post/12708227#post12708227 "View Quoted Post")
> 
> Disliked
> 
> Two days trading on demo and it continues loving japan (i wonder why...) {image} {image}
> 
> Ignored

No such issue for me. It traded all sorts of currencies.  
  
I'm going to have to remove some pairs and re-test. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#125](/thread/post/12708588#post12708588 "Post Permalink")

  * Jan 18, 2020 12:16am  Jan 18, 2020 12:16am 

  * [ fxtrue](fxtrue)

  * | Joined May 2019  | Status: Trader | [46 Posts](/search?do=process&provider=Member&searchuser=801801)

I've been collaborating with Ursinho (he mentioned me as 'fxraider') to help bug-fix the project and fast-track the testing process.  
  
For those interested in assisting, I've attached an MT5 version (based on additional fixes to v3.9.6.30 gamma) that permits multi-pair back-testing.  
  
Please be aware that there seems to be an issue with "once per bar" functionality, so I suggest turning that off for the time being.  
  
Visual testing in MT5 is SLOW ...but speeds up dramatically when the visual tester window is minimised.  
  
Another tip for faster testing is to select the "M1 OHLC" data option (rather that "every tick"), but understand that testing speed is linear, so if a single-pair test takes 1hr then a 28-pair test is going to take about 28 hours.  
  
Have fun ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

Attached File(s)

![File Type: ex5](https://assets.faireconomy.media/images/attach/ex5.gif) [BlessingLite.ex5](/attachment/file/3531788?d=1579274088) 771 KB | 449 downloads 

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#126](/thread/post/12708641#post12708641 "Post Permalink")

  * Jan 18, 2020 12:39am  Jan 18, 2020 12:39am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar338950_1.gif) cescof](cescof)

  * Joined Jun 2013 | Status: Trader | [1,006 Posts](/search?do=process&provider=Member&searchuser=338950)

> [Quoting fxtrue](/thread/post/12708588#post12708588 "View Quoted Post")
> 
> Disliked
> 
> I've been collaborating with Ursinho (he mentioned me as 'fxraider') to help bug-fix the project and fast-track the testing process. For those interested in assisting, I've attached an MT5 version (based on additional fixes to v3.9.6.30 gamma) that permits multi-pair back-testing. Please be aware that there seems to be an issue with "once per bar" functionality, so I suggest turning that off for the time being. Visual testing in MT5 is SLOW ...but speeds up dramatically when the visual tester window is minimised. Another tip for faster testing is...
> 
> Ignored

Thnaks really aprreciate 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#127](/thread/post/12708644#post12708644 "Post Permalink")

  * Jan 18, 2020 12:40am  Jan 18, 2020 12:40am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar338950_1.gif) cescof](cescof)

  * Joined Jun 2013 | Status: Trader | [1,006 Posts](/search?do=process&provider=Member&searchuser=338950)

> [Quoting ursinho4711](/thread/post/12708516#post12708516 "View Quoted Post")
> 
> Disliked
> 
> {quote} I was thinking of following: on London close, close all trades in profit (green) close all pending orders for new pairs do not allow pending orders for new pairs let open the other (red) open trades will do that manually today, a flag "UseWeekendShutDown" would be good in the next version Another thing I thought of, to be able to use the lot-increment for open trades: for every pending order on an open trade, reduce the new variable "MaxOpenPairs" (or whatever the name will be) by one and delete the oldest pending orders for a new pair
> 
> Ignored

Hy.. is possibile use two isntances of Ea with different magic and set file in the same mt4 ?  
Thanks  
Regards 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#128](/thread/post/12708676#post12708676 "Post Permalink")

  * Jan 18, 2020 12:51am  Jan 18, 2020 12:51am 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

> [Quoting cescof](/thread/post/12708644#post12708644 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hy.. is possibile use two isntances of Ea with different magic and set file in the same mt4 ? Thanks Regards
> 
> Ignored

Yipp, should not be a problem. Just change the magic number in the settings... all code related to orders use the magic number 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#129](/thread/post/12709054#post12709054 "Post Permalink")

  * Jan 18, 2020 4:48am  Jan 18, 2020 4:48am 

  * [ Mkal86](mkal86)

  * | Joined Jul 2016  | Status: Trader | [40 Posts](/search?do=process&provider=Member&searchuser=475128)

I started testing it 2 days ago, and so far its performing really well.   
Can you tell me about option "percentage of balance loss before trading stops", in what order does close trades 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#130](/thread/post/12709133#post12709133 "Post Permalink")

  * Jan 18, 2020 5:46am  Jan 18, 2020 5:46am 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

> [Quoting Mkal86](/thread/post/12709054#post12709054 "View Quoted Post")
> 
> Disliked
> 
> Can you tell me about option "percentage of balance loss before trading stops", in what order does close trades
> 
> Ignored

Here is the code:  
  

Inserted Code
    
    
          //+-----------------------------------------------------------------+
          //| Calculate  Stop Trade Percent                                   |
          //+-----------------------------------------------------------------+
          double StepAB = InitialAB * (1 + StopTradePercent_);
          double StepSTB = AccountBalance() * (1 - StopTradePercent_);
          double NextISTB = StepAB * (1 - StopTradePercent_);
          if(StepSTB > NextISTB)
            {
             InitialAB = StepAB;
             StopTradeBalance = StepSTB;
            }
          // Stop Trade Amount:
          double InitialAccountMultiPortion = StopTradeBalance * PortionPC_;
          stop_trade_amount = InitialAccountMultiPortion;
          if(pairinfo[i].PortionBalance < InitialAccountMultiPortion)
            {
             if(pairinfo[i].CbT == 0)
               {
                AllowTrading = false;
                if(PlaySounds)
                   PlaySound(AlertSound);
                Print("Portion Balance dropped below stop-trading percentage");
                MessageBox("Reset required - account balance dropped below stop-trading percentage on " + DTS(AccountNumber(), 0) + " " + TradePairs[i] + " " + (string) Period(), "Blessing 3: Warning", 48);
                return (0);
               }
             else
                if(!ShutDown_ && !RecoupClosedLoss)
                  {
                   ShutDown_ = true;
                   if(PlaySounds)
                      PlaySound(AlertSound);
                   Print("Portion Balance dropped below stop-trading percentage");
                   return (0);
                  }
            }

  
All pending orders are closed in this order:  

Inserted Code
    
    
       for(int Order = OrdersTotal() - 1; Order >= 0; Order--)

  
AllowTrading is set to false, open trades continue to trade 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#131](/thread/post/12709155#post12709155 "Post Permalink")

  * Jan 18, 2020 5:58am  Jan 18, 2020 5:58am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar338950_1.gif) cescof](cescof)

  * Joined Jun 2013 | Status: Trader | [1,006 Posts](/search?do=process&provider=Member&searchuser=338950)

> [Quoting fxtrue](/thread/post/12708588#post12708588 "View Quoted Post")
> 
> Disliked
> 
> I've been collaborating with Ursinho (he mentioned me as 'fxraider') to help bug-fix the project and fast-track the testing process. For those interested in assisting, I've attached an MT5 version (based on additional fixes to v3.9.6.30 gamma) that permits multi-pair back-testing. Please be aware that there seems to be an issue with "once per bar" functionality, so I suggest turning that off for the time being. Visual testing in MT5 is SLOW ...but speeds up dramatically when the visual tester window is minimised. Another tip for faster testing is...
> 
> Ignored

seems backtest results in mt5 are totally different from mt4.. also lot size entries are totally different....  
I'll continue my attempts  
Thanks  
Regards 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#132](/thread/post/12709172#post12709172 "Post Permalink")

  * Jan 18, 2020 6:13am  Jan 18, 2020 6:13am 

  * [ fxtrue](fxtrue)

  * | Joined May 2019  | Status: Trader | [46 Posts](/search?do=process&provider=Member&searchuser=801801)

Not sure why lot sizing should differ between versions - the only things that *might* vary are calculations based on margin requirements as the return values in MT5 are not always the same as in MT4.  
  
Beyond that, results should be fairly similar as long as settings are the same... just remember that MT5 testing is subject to things like variable spread and slippage, so the numbers will never be identical. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#133](/thread/post/12709214#post12709214 "Post Permalink")

  * Jan 18, 2020 6:57am  Jan 18, 2020 6:57am 

  * [ Mkal86](mkal86)

  * | Joined Jul 2016  | Status: Trader | [40 Posts](/search?do=process&provider=Member&searchuser=475128)

> [Quoting ursinho4711](/thread/post/12709133#post12709133 "View Quoted Post")
> 
> Disliked
> 
> {quote} Here is the code: //+-----------------------------------------------------------------+ //| Calculate Stop Trade Percent | //+-----------------------------------------------------------------+ double StepAB = InitialAB * (1 + StopTradePercent_); double StepSTB = AccountBalance() * (1 - StopTradePercent_); double NextISTB = StepAB * (1 - StopTradePercent_); if(StepSTB > NextISTB) { InitialAB = StepAB; StopTradeBalance = StepSTB; } // Stop Trade Amount: double InitialAccountMultiPortion = StopTradeBalance * PortionPC_; stop_trade_amount =...
> 
> Ignored

Thank you for the answer 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#134](/thread/post/12709249#post12709249 "Post Permalink")

  * Jan 18, 2020 7:30am  Jan 18, 2020 7:30am 

  * [ psynapse](psynapse)

  * | Joined Aug 2017  | Status: Trader | [9 Posts](/search?do=process&provider=Member&searchuser=602064)

Thank you so much Ursinho for your hard work on coding this beast  
  
Been following this on a demo - XAUUSD seems to be a pair to ban (closed it manually, opened trade without any logic).  
  
Closed all trades in London close, but seems a nice idea to close all trades before weekend auto by default?  
  
Gonna keep testing it.  
  
Cheers 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#135](/thread/post/12709257#post12709257 "Post Permalink")

  * Jan 18, 2020 7:43am  Jan 18, 2020 7:43am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar338950_1.gif) cescof](cescof)

  * Joined Jun 2013 | Status: Trader | [1,006 Posts](/search?do=process&provider=Member&searchuser=338950)

> [Quoting fxtrue](/thread/post/12709172#post12709172 "View Quoted Post")
> 
> Disliked
> 
> Not sure why lot sizing should differ between versions - the only things that *might* vary are calculations based on margin requirements as the return values in MT5 are not always the same as in MT4. Beyond that, results should be fairly similar as long as settings are the same... just remember that MT5 testing is subject to things like variable spread and slippage, so the numbers will never be identical.
> 
> Ignored

Tomorrow i will try again and I will post result...   
Thanks   
Regards 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#136](/thread/post/12709312#post12709312 "Post Permalink")

  * Jan 18, 2020 9:50am  Jan 18, 2020 9:50am 

  * [ richard96816](richard96816)

  * Joined Dec 2018 | Status: Trader | [564 Posts](/search?do=process&provider=Member&searchuser=741833)

Blessing has a lot of testing and history behind it. This multi-pair version: not so much. Especially since it departs from many of the primary techniques used to make the original version profitable.  
  
The general idea seemed like a good one. But taking one setup and applying it to many pairs seems almost silly. How is this supposed to work? It certainly doesn't work with the original. Jumping quickly into forward testing and live trading is a little shocking. As if Blessing was a magic wand and applying it to any old crazy scheme will make it profitable.  
  
There are lots of powerful things possible with multi-pair EAs. I don't see any of them being applied here yet.  
  
Blessing setups for one currency pair very seldom work for other pairs. So how is this iteration of the multi-pair Blessing supposed to work?  
  
This is a whole new EA. Very different from Blessing. So a week or two of forward testing means next to nothing. This is where years of data must be traversed to see if this scheme makes sense. Blessing has years of testing built into it and much confidence accrued. This new incarnation is too different to benefit from those years of concerted effort and testing.  
  
This new EA seems like a good idea. Especially cashing in on Blessing's success. Sadly, the current version really doesn't seem to do that very well.  
  
Blessing is not a set-it-and-forget-it smart EA. From what I've seen converting it to a multi-pair system will not change that. At sometime, perhaps a month or two down the road, you can expect it to crash and burn when just the right set of conditions conspire against it.  
  
If you look at specific issues that original Blessing still faces and apply the multi-pair strengths to address them then you could make something even better than Blessing. I don't see that happening here, yet.  
  
Blessing is open source, so anyone can change and modify and build upon it, which is very cool. Maybe it's too easy.  
  
The biggest, most common failing I've seen of multi-pair EAs is the one-size-fits-all approach to trading a list of pairs. 

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#137](/thread/post/12709332#post12709332 "Post Permalink")

  * Jan 18, 2020 10:53am  Jan 18, 2020 10:53am 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

Thanks Richard! This is how I wanted the thread to run: as an open discussion about an open source.  
I am not the blessing programer. The approach is (still) to make the EA easier to handle and to overview when trading some pairs at the same time.  
I know that there is no set-file that works perfectly on all pairs. But maybe there is a setting that works good enough for many pairs.  
In the blessing thread I found this 5-minute timeframe setting that, according to the user, works well since three years on 14 pairs or so. Not making THE huge wins, but consecutive small amounts that sum up at the end.  
Anyway I will continue working on that multipair idea. See how it can be made more complex without losing the overview.  
I love coding and while implementing blessing into a multipair (dashboard) environment I understand more and more how the heart of blessing beats.  
The better you understand an EA, the better you can use it and find the best parameters.  
  
Have a great weekend @all! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#138](/thread/post/12709357#post12709357 "Post Permalink")

  * Jan 18, 2020 12:01pm  Jan 18, 2020 12:01pm 

  * [ procmail](procmail)

  * | Joined May 2018  | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=676819)

> [Quoting richard96816](/thread/post/12709312#post12709312 "View Quoted Post")
> 
> Disliked
> 
> There are lots of powerful things possible with multi-pair EAs.
> 
> Ignored

I’m very interested in this. What are some of these things that multi-pair EAs could do? Or can you point me to book or resources that address this? Thanks! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#139](/thread/post/12709360#post12709360 "Post Permalink")

  * Jan 18, 2020 12:13pm  Jan 18, 2020 12:13pm 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

I did a reset on my brain to think clearly again...  

> [Quoting richard96816](/thread/post/12707266#post12707266 "View Quoted Post")
> 
> Disliked
> 
> Fill a folder (directory) with set files and have the EA access them by name creating the pair list and parameters from the files it finds. After reading a file it could be moved to an archive folder. New files appearing in the primary folder would cause old parameters to be overwritten or new pairs to be added. (Or even build in auto-optimization, but that's a whole new batch of craziness.) :-) Trading 28 pairs, especially with the same parameters for each will eventually require a large account or produce unacceptable losses.
> 
> Ignored

Sounds lika a good approach and not that difficult to program. Okay, I did not think of all details yet (resetting variables, grids...). If the file names follow a rule, e.g. BL3-EURUSD-5MIN, then it's kind of simple though...  
But first I have to get the the actual version in a stable state. The ExitTrades is still under construction... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#140](/thread/post/12709365#post12709365 "Post Permalink")

  * Jan 18, 2020 12:28pm  Jan 18, 2020 12:28pm 

  * [ mselvi](mselvi)

  * | Membership Revoked  | Joined Jul 2019 | [28 Posts](/search?do=process&provider=Member&searchuser=833311)

<https://www.forexfactory.com/showthread.php?t=973909>

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Blessing Multipair EA
  *   * [ **Reply to Thread** ](/thread/973998-blessing-multipair-ea/reply#reply)

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

[Trading multipair triangles, no stoploss](/thread/917648-trading-multipair-triangles-no-stoploss "Hello forex Folks! 
  
I'd like to share with You my system that I was comming to for many years. I am testing it these days and it gives...") 78 replies

['Blessing' EA Modification Wanted](/thread/271525-blessing-ea-modification-wanted "Hello. 
 
here is a version of BLESSING \(old\) love this version. 
I wonder if someone could if possible to change this code. 
 
I like that...") 3 replies

[Single, Few Pair Traders (1-4) vs. MultiPair Traders (8-20)](/thread/964171-single-few-pair-traders-1-4-vs-multipair-traders "Who gets better results ?? 
  
Put it in another way , if you went for a trading competition and want to achieve &gt;300% ~ 2000% , what would...") 0 replies

[Coding Request for Multipair MTF ADR Dashboard](/thread/683340-coding-request-for-multipair-mtf-adr-dashboard "Can someone code this into indicator???") 2 replies

[trying to make a multipair buy and sell script](/thread/241746-trying-to-make-a-multipair-buy-and-sell "what i like to do is that i add a script on a chart and it will do 
 
open 3 pairs buys or sells. 
 
for example 0.1 lot EURUSD 
          ...") 6 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/973998-blessing-multipair-ea/reply#reply)
  * Subscribe
  * [97](javascript:void\(0\);)

Attachments: Blessing Multipair EA

Tags: Blessing Multipair EA

#  [](/thread/973998-blessing-multipair-ea)Blessing Multipair EA 

  * 

  * [#141](/thread/post/12709383#post12709383 "Post Permalink")

  * Jan 18, 2020 1:13pm  Jan 18, 2020 1:13pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar3294_6.gif) JackJones](jackjones)

  * Joined Aug 2005 | Status: 888 | [1,021 Posts](/search?do=process&provider=Member&searchuser=3294)

> [Quoting psynapse](/thread/post/12709249#post12709249 "View Quoted Post")
> 
> Disliked
> 
> Thank you so much Ursinho for your hard work on coding this beast Been following this on a demo - XAUUSD seems to be a pair to ban (closed it manually, opened trade without any logic). Closed all trades in London close, but seems a nice idea to close all trades before weekend auto by default? Gonna keep testing it. Cheers
> 
> Ignored

if you want to trade XAU there is a set file with a backtest in the original blessing thread that seems okay. i also tried the all pairs with XAU and i agree with you, i think it was lucky to get out of the trades it made. 

grist for the mill

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#142](/thread/post/12709395#post12709395 "Post Permalink")

  * Jan 18, 2020 1:34pm  Jan 18, 2020 1:34pm 

  * [ richard96816](richard96816)

  * Joined Dec 2018 | Status: Trader | [564 Posts](/search?do=process&provider=Member&searchuser=741833)

> [Quoting ursinho4711](/thread/post/12709360#post12709360 "View Quoted Post")
> 
> Disliked
> 
> I did a reset on my brain to think clearly again... {quote} Sounds lika a good approach and not that difficult to program. Okay, I did not think of all details yet (resetting variables, grids...). If the file names follow a rule, e.g. BL3-EURUSD-5MIN, then it's kind of simple though... But first I have to get the the actual version in a stable state. The ExitTrades is still under construction...
> 
> Ignored

Simplicity is good. File name could be eurusd-5min. The prefix could be the directory name.  
  
Even the pair name and timeframe could be contained within the file. I've been tempted to build these into Blessing's settings just to keep everything together and reduce errors. Even if you put a set file on the wrong chart it will still work, though maybe not on the pair and TF in the chart. :-)   
  
It would also make the timeframe choice optimizable with Strategy Tester! Not sure why I haven't done that yet!  
  
These are key parameters that aren't in the set file at all! Except as comments. :-(  
  
Just a thought. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#143](/thread/post/12709403#post12709403 "Post Permalink")

  * Jan 18, 2020 1:46pm  Jan 18, 2020 1:46pm 

  * [ richard96816](richard96816)

  * Joined Dec 2018 | Status: Trader | [564 Posts](/search?do=process&provider=Member&searchuser=741833)

> [Quoting procmail](/thread/post/12709357#post12709357 "View Quoted Post")
> 
> Disliked
> 
> {quote} I’m very interested in this. What are some of these things that multi-pair EAs could do? Or can you point me to book or resources that address this? Thanks!
> 
> Ignored

Google**forex basket trading** and stand back! :-) 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#144](/thread/post/12709407#post12709407 "Post Permalink")

  * Jan 18, 2020 1:49pm  Jan 18, 2020 1:49pm 

  * [ procmail](procmail)

  * | Joined May 2018  | Status: Trader | [156 Posts](/search?do=process&provider=Member&searchuser=676819)

> [Quoting richard96816](/thread/post/12709403#post12709403 "View Quoted Post")
> 
> Disliked
> 
> {quote} Google forex basket trading and stand back! :-)
> 
> Ignored

Thank you. First result is a FF thread. Will read up as much as I can from this thread as well as the other search results. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#145](/thread/post/12709567#post12709567 "Post Permalink")

  * Jan 18, 2020 9:59pm  Jan 18, 2020 9:59pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar3294_6.gif) JackJones](jackjones)

  * Joined Aug 2005 | Status: 888 | [1,021 Posts](/search?do=process&provider=Member&searchuser=3294)

how about we codename Blessing Multipair EA : Maddog? 

grist for the mill

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#146](/thread/post/12709568#post12709568 "Post Permalink")

  * Jan 18, 2020 10:00pm  Jan 18, 2020 10:00pm 

  * [ fxtrue](fxtrue)

  * | Joined May 2019  | Status: Trader | [46 Posts](/search?do=process&provider=Member&searchuser=801801)

Richard's points are very valid to this discussion - if you run the MT5 version then you'll definitely see "crash and burn" scenarios from time to time.  
  
I ran a "quick" test from 01/01/2019 through to now and the results were mostly manageable (DD hovering around the $2k level), but there were still several big hits during that relatively short period that would have wiped out a $15k account in hours ...despite starting each sequence with 0.01 lots.  
  
Over the past year, I've been able to back-test test a number of multi-pair EAs (Hedge Rocks, Arbitrage Synthetic & a few other triangular systems, Basket 14, Confirm 14, Phantom 14, Trim 6, Multi-Currency Hedge, Slopey Peaky, Steroid Peaky, some of the "spaghetti indicator" variants, and a bunch more) through MT5 and the results have always been the same: crash & burn ![](https://resources.faireconomy.media/images/emojis/64/1f641.png?v=15.1)  
  
The basic issue is that you can't anticipate black swan days, nor can you anticipate irrational wild spikes or markets that run away without provocation. With that in mind, the logical approach is Richard's: try to make 100% quickly while risking 50%, and do that on as many pairs as you can in the hope that your successes outpace your failures. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#147](/thread/post/12709572#post12709572 "Post Permalink")

  * Jan 18, 2020 10:03pm  Jan 18, 2020 10:03pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar3294_6.gif) JackJones](jackjones)

  * Joined Aug 2005 | Status: 888 | [1,021 Posts](/search?do=process&provider=Member&searchuser=3294)

yeap run it until you get your money back, take your money and put it somewhere and then let the EA run .. unlikely it will survive six months if it is going to basket trade or grid ie. double down !! as youre trading randomness and there is no real edge, just luck. 

grist for the mill

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#148](/thread/post/12709679#post12709679 "Post Permalink")

  * Jan 19, 2020 12:48am  Jan 19, 2020 12:48am 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

First of all thanks to everyone for the unemotional discussion. More of it!  
  

> [Quoting fxtrue](/thread/post/12709568#post12709568 "View Quoted Post")
> 
> Disliked
> 
> Richard's points are very valid to this discussion - if you run the MT5 version then you'll definitely see "crash and burn" scenarios from time to time
> 
> Ignored

But this happens to the "normal" Blessing as well. A setup that works good for some weeks can suddenly eat your wins if you just forget about it and don't take the money and run.  
There is probably no EA out that works alone and let you enjoy the life on the beach. Some work always has to be invested...  
If there was a holy grail, this forum would not be that full of old folks ;-) 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#149](/thread/post/12709703#post12709703 "Post Permalink")

  * Jan 19, 2020 1:25am  Jan 19, 2020 1:25am 

  * [ kzean](kzean)

  * | Joined Aug 2014  | Status: Trader | [17 Posts](/search?do=process&provider=Member&searchuser=380085)

> [Quoting ursinho4711](/thread/post/12699227#post12699227 "View Quoted Post")
> 
> Disliked
> 
> @ll! Here is another reason why I wanted to have the EA as multipair-version: now I can monitor and control all open trades via one dashboard. I can set a basket TP, basket SL, close all manually... {image}
> 
> Ignored

**Phantastic**

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#150](/thread/post/12709715#post12709715 "Post Permalink")

  * Jan 19, 2020 1:52am  Jan 19, 2020 1:52am 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

> [Quoting kzean](/thread/post/12709703#post12709703 "View Quoted Post")
> 
> Disliked
> 
> {quote} Phantastic
> 
> Ignored

The best ideas come on toilet ;-)  
  
If the multipair-EA is too dangerous for trading alive, it has one big benefit: you can easily forward test (on an demo) your settings. With the dashboard you have an great overview: if things always end in red and never recoup, then change the settings ;-) 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#151](/thread/post/12709725#post12709725 "Post Permalink")

  * Jan 19, 2020 2:13am  Jan 19, 2020 2:13am 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

> [Quoting richard96816](/thread/post/12709403#post12709403 "View Quoted Post")
> 
> Disliked
> 
> {quote} Google forex basket trading and stand back! :-)
> 
> Ignored

This is one of the important points why I wanted to have a discussion and a new thread: how should this be implemented in the multi-pair-blessing? Which logic, flow should be behind it? Remember that in the current constellation one pair could eat all the nice wins from all the other pairs. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#152](/thread/post/12709756#post12709756 "Post Permalink")

  * Jan 19, 2020 4:03am  Jan 19, 2020 4:03am 

  * [ Mjy](mjy)

  * | Joined Jan 2020  | Status: Trader | [2 Posts](/search?do=process&provider=Member&searchuser=908565)

> [Quoting ursinho4711](/thread/post/12709725#post12709725 "View Quoted Post")
> 
> Disliked
> 
> {quote} This is one of the important points why I wanted to have a discussion and a new thread: how should this be implemented in the multi-pair-blessing? Which logic, flow should be behind it? Remember that in the current constellation one pair could eat all the nice wins from all the other pairs.
> 
> Ignored

  
  
I ran a demo account using the basic Blessing ea starting with $5,000 from last Oct thru December applied to 11 different pairs...showed profit up to $1,300 but then had DD around $4,000...I suspect I was using too many pairs. Few days ago set up new Demo account with $5,000 using 5 pairs...hoping for good results. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#153](/thread/post/12709763#post12709763 "Post Permalink")

  * Jan 19, 2020 4:13am  Jan 19, 2020 4:13am 

  * [ fxtrue](fxtrue)

  * | Joined May 2019  | Status: Trader | [46 Posts](/search?do=process&provider=Member&searchuser=801801)

Something that I've made good use of in other multi-pair systems is a "chipping" mechanism whereby the system identifies a pair that's got into trouble (this can be based on the number of open levels, floating loss, or any combination of relevant criteria) and then automatically reduces whichever order has the largest pip loss provided that it can be done within say 10 pips.  
  
For example, assume AUDUSD has 4 levels open and the smallest order is currently 0.05 lots which is negative 200 pips i.e. that order P/L is $-100.00  
  
Now, if GBPUSD has 3 open levels and its basket value is $3.50 per pip then that would result in $35 extra profit if the GBPUSD TP was shifted 10 pips. Since the smallest AUDUSD position (0.01 lots) would require $20 to cover its loss, it would be possible to do that if the GBPUSD basket TP was extended by just 6 pips and, upon closure of the GBPUSD basket, the 0.05 lot AUDUSD order could be reduced to 0.04 lots... or even to 0.03 lots if the GBPUSD basket TP had been extended by 12 pips.  
  
The advantage of this method is that it's able to self-adapt i.e. the value of loss that can be offset is dependent upon the the tick value of the donor basket, and that "offset" can easily equate to more than 0.01 lots each time. Moreover, with all pairs helping the struggling basket, drawdowns can be kept in check more effectively. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#154](/thread/post/12709801#post12709801 "Post Permalink")

  * Jan 19, 2020 5:17am  Jan 19, 2020 5:17am 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

> [Quoting fxtrue](/thread/post/12709763#post12709763 "View Quoted Post")
> 
> Disliked
> 
> Something that I've made good use of in other multi-pair systems is a "chipping" mechanism
> 
> Ignored

And with a clean dashboard it is easy to overview.  
I wish the day had 48 hours. 12 for my family and 36 for forex ;-) 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#155](/thread/post/12709824#post12709824 "Post Permalink")

  * Jan 19, 2020 6:14am  Jan 19, 2020 6:14am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar638535_1.gif) detector](detector)

  * Joined Dec 2017 | Status: Trader | [3,710 Posts](/search?do=process&provider=Member&searchuser=638535)

Hello Ursinho, if all magic numbers are linked together, can blessing close all with a designated TP, think you may know what I am asking, but yeah, all linked to take a collective profit and close all on objective complete, your doing a marvellous job BTW, enjoying seeing some very constructive posts, D 

I don't need to be good at the game, only good enough to beat my opponent,

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#156](/thread/post/12709832#post12709832 "Post Permalink")

  * Edited 6:54am  Jan 19, 2020 6:36am | Edited 6:54am 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

> [Quoting detector](/thread/post/12709824#post12709824 "View Quoted Post")
> 
> Disliked
> 
> Hello Ursinho, if all magic numbers are linked together, can blessing close all with a designated TP, think you may know what I am asking, but yeah, all linked to take a collective profit and close all on objective complete, your doing a marvellous job BTW, enjoying seeing some very constructive posts, D
> 
> Ignored

Hi Detector!  
Thanks for the question.  
At the moment I am using my dashboard for the basket take profit. But my goal was to implement this into blessing. Or, the big goal, implement blessing into a dashboard.  
  
As I wrote some time ago, the ExitTrades is still under construction. Should work for single pairs, but the multi-pair idea has not been inplemented yet. I wanted to discuss some points here in this thread. The logic when to exit all, partially, when to delete pending orders and so on.  
Already implementing a basket close for all open trades sould not be so difficult. I will put it on my priority one list. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot1.png
Size: 24 KB](/attachment/image/3532431/thumbnail?d=1579384450)](/attachment/image/3532431?d=1579384450)   

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#157](/thread/post/12709835#post12709835 "Post Permalink")

  * Jan 19, 2020 6:46am  Jan 19, 2020 6:46am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar638535_1.gif) detector](detector)

  * Joined Dec 2017 | Status: Trader | [3,710 Posts](/search?do=process&provider=Member&searchuser=638535)

> [Quoting ursinho4711](/thread/post/12709832#post12709832 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi Detector! Thanks for the question. At the moment I am using my dashboard for the basket take profit. But my goal was to implement this into blessing. Or, the big goal, implement blessing into a dashboard. As I wrote some time ago, the ExitTrades is still under construction. Should work for single pairs, but the multi-pair idea has not been inplemented yet. I wanted to discuss some points here in this thread. The logic when to exit all, partially, when to delete pending orders and so on. Already implementing a basket close for all open...
> 
> Ignored

Thanks for the reply Ursinho,just off the cuff, Blessing has a "cease trading" when the account goes into a X%loss, maybe "close for the day X%profit".  
Currently looking at the numbers of orders opened, seems, while being a benefit and the heart of the system, it's it's worst enemy at times, also looking at time frequency, some trades minutes, some days, just to let you know the avenue I'm going down with my bit of research/testing, D 

I don't need to be good at the game, only good enough to beat my opponent,

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#158](/thread/post/12709842#post12709842 "Post Permalink")

  * Jan 19, 2020 7:06am  Jan 19, 2020 7:06am 

  * [ richard96816](richard96816)

  * Joined Dec 2018 | Status: Trader | [564 Posts](/search?do=process&provider=Member&searchuser=741833)

Multi-pair systems can also be used to feed the flat-weekend frenzy.   
  
Profit may take a hit, but with a reasonable target the losers should be overshadowed by the winners. Usually holding over the weekend only if the target isn't hit. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#159](/thread/post/12709844#post12709844 "Post Permalink")

  * Jan 19, 2020 7:17am  Jan 19, 2020 7:17am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar638535_1.gif) detector](detector)

  * Joined Dec 2017 | Status: Trader | [3,710 Posts](/search?do=process&provider=Member&searchuser=638535)

Ursinho, would like to ask, how does Blessing capitalise on good trades, sorry if I'm a bit naive, while there are many permutations for setting take profit,BE, has anyone had a Eureka moment in finding such parameters, from my experience, and could be wrong, Blessing does not add to good profit, am I wrong, if not it could be a future concept, please some one could enlighten me.  
With regard to my last post, on a back test, using max 2 orders, Blessing retained profit, add one more, total 3+, wipe out on close, suppose it's all relative, time frequency, again as a concept could trigger the hedge, ideal situation to take opposite trades but this brings it's own issues with FIFO, just spouting my thoughts, could be contagious, D 

I don't need to be good at the game, only good enough to beat my opponent,

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#160](/thread/post/12709851#post12709851 "Post Permalink")

  * Jan 19, 2020 7:42am  Jan 19, 2020 7:42am 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

> [Quoting detector](/thread/post/12709844#post12709844 "View Quoted Post")
> 
> Disliked
> 
> Ursinho, would like to ask, how does Blessing capitalise on good trades
> 
> Ignored

Hi detector! If you have questions to Blessing itself, there are some threads already treating those questions. There you can also find much (original!) documentation on the EA. Short questions like yours would lead to pages of answers...  
I did not alter anything in the logic of Blessing. Until now I just took out parts that (I think) do not make sense in a multipair version. 

Attached File(s)

![File Type: pdf](https://assets.faireconomy.media/images/attach/pdf.gif) [blessing-3-v3.7-manual.pdf](/attachment/file/3532434?d=1579387053) 1.3 MB | 793 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Blessing Multipair EA
  *   * [ **Reply to Thread** ](/thread/973998-blessing-multipair-ea/reply#reply)

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

[Trading multipair triangles, no stoploss](/thread/917648-trading-multipair-triangles-no-stoploss "Hello forex Folks! 
  
I'd like to share with You my system that I was comming to for many years. I am testing it these days and it gives...") 78 replies

['Blessing' EA Modification Wanted](/thread/271525-blessing-ea-modification-wanted "Hello. 
 
here is a version of BLESSING \(old\) love this version. 
I wonder if someone could if possible to change this code. 
 
I like that...") 3 replies

[Single, Few Pair Traders (1-4) vs. MultiPair Traders (8-20)](/thread/964171-single-few-pair-traders-1-4-vs-multipair-traders "Who gets better results ?? 
  
Put it in another way , if you went for a trading competition and want to achieve &gt;300% ~ 2000% , what would...") 0 replies

[Coding Request for Multipair MTF ADR Dashboard](/thread/683340-coding-request-for-multipair-mtf-adr-dashboard "Can someone code this into indicator???") 2 replies

[trying to make a multipair buy and sell script](/thread/241746-trying-to-make-a-multipair-buy-and-sell "what i like to do is that i add a script on a chart and it will do 
 
open 3 pairs buys or sells. 
 
for example 0.1 lot EURUSD 
          ...") 6 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/973998-blessing-multipair-ea/reply#reply)
  * Subscribe
  * [97](javascript:void\(0\);)

Attachments: Blessing Multipair EA

Tags: Blessing Multipair EA

#  [](/thread/973998-blessing-multipair-ea)Blessing Multipair EA 

  * 

  * [#161](/thread/post/12709852#post12709852 "Post Permalink")

  * Jan 19, 2020 7:54am  Jan 19, 2020 7:54am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar638535_1.gif) detector](detector)

  * Joined Dec 2017 | Status: Trader | [3,710 Posts](/search?do=process&provider=Member&searchuser=638535)

> [Quoting ursinho4711](/thread/post/12709851#post12709851 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi detector! If you have questions to Blessing itself, there are some threads already treating those questions. There you can also find much (original!) documentation on the EA. Short questions like yours would lead to pages of answers... I did not alter anything in the logic of Blessing. Until now I just took out parts that (I think) do not make sense in a multipair version. {image}
> 
> Ignored

Sorry just my thoughts Ursinhoe, don't want to corrupt the thread![](https://resources.faireconomy.media/images/emojis/64/1f64f.png?v=15.1)D 

I don't need to be good at the game, only good enough to beat my opponent,

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#162](/thread/post/12709854#post12709854 "Post Permalink")

  * Jan 19, 2020 8:02am  Jan 19, 2020 8:02am 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

> [Quoting detector](/thread/post/12709852#post12709852 "View Quoted Post")
> 
> Disliked
> 
> Sorry
> 
> Ignored

No problem at all!  
To be honest it was a good opportunity to note again that in this thread we should discuss multipair issues. That's why I opened this thread out of that one:  
<https://www.forexfactory.com/showthread.php?t=792598>

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#163](/thread/post/12709868#post12709868 "Post Permalink")

  * Jan 19, 2020 8:38am  Jan 19, 2020 8:38am 

  * [ farmabioq](farmabioq)

  * | Commercial User  | Joined Dec 2014 | [55 Posts](/search?do=process&provider=Member&searchuser=394496)

Hello. They could publish the open code of the Ea that works best to add a news filter that works correctly. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#164](/thread/post/12709903#post12709903 "Post Permalink")

  * Jan 19, 2020 10:35am  Jan 19, 2020 10:35am 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

Next week I will reduce my pairs to trade to following 14 pairs:  
  
AUDJPY,AUDUSD,CHFJPY,EURCHF,EURGBP,EURJPY,EURUSD,GBPCHF,GBPJPY,GBPUSD,NZDJPY,NZDUSD,USDCHF,USDJPY  
  
I found them in a "basket trade" thread (thanks, Richard!). The reason for this combination is, that they hedge each others. I will analyze it on Demo first. Live account is too exciting in that early development stage. Though I made real (not much, but real) win last week. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#165](/thread/post/12710062#post12710062 "Post Permalink")

  * Jan 19, 2020 7:59pm  Jan 19, 2020 7:59pm 

  * [ richard96816](richard96816)

  * Joined Dec 2018 | Status: Trader | [564 Posts](/search?do=process&provider=Member&searchuser=741833)

> [Quoting ursinho4711](/thread/post/12709903#post12709903 "View Quoted Post")
> 
> Disliked
> 
> Next week I will reduce my pairs to trade to following 14 pairs: AUDJPY,AUDUSD,CHFJPY,EURCHF,EURGBP,EURJPY,EURUSD,GBPCHF,GBPJPY,GBPUSD,NZDJPY,NZDUSD,USDCHF,USDJPY I found them in a "basket trade" thread (thanks, Richard!). The reason for this combination is, that they hedge each others. I will analyze it on Demo first. Live account is too exciting in that early development stage. Though I made real (not much, but real) win last week.
> 
> Ignored

Many different ways to go with pair selection and orientation.  
  
Correlated pairs will show you one set of behaviors and non-correlated pairs a whole different set.  
Non-correlated pairs might be more profitable and simpler, unless you've got a specific hedge scheme in mind.  
Non-correlated pairs suggest less chance of news affecting more than one pair, and better diversification. One of the main, easily attainable strengths of a multi-pair Blessing, I suspect. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#166](/thread/post/12710274#post12710274 "Post Permalink")

  * Jan 20, 2020 2:29am  Jan 20, 2020 2:29am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar817367_1.gif) ecryptom](ecryptom)

  * | Joined Jun 2019  | Status: Trader | [140 Posts](/search?do=process&provider=Member&searchuser=817367)

nice work !  
can i ask if will be added more indicators ?  
as example make Blessing more trend trading than anything else ..  
BB alone dont work (too many false signals) and need a very good trend filter  
rsi and stoch are no good for forex  
and there are a lot of better choices than cci as trend  
  
yes 1 -5 good trend trades per week in 1 day candle is more profitable than  
xxx trades per week in 5min (make profits only for the broker) 

Everything flows. Learn to Earn.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#167](/thread/post/12710588#post12710588 "Post Permalink")

  * Jan 20, 2020 10:19am  Jan 20, 2020 10:19am 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

> [Quoting ecryptom](/thread/post/12710274#post12710274 "View Quoted Post")
> 
> Disliked
> 
> nice work ! can i ask if will be added more indicators ?
> 
> Ignored

Hi!  
Thanks for the flowers ;-)  
  
To your question: this is something that should be discussed in a "Blessing only" thread. Here is just the try to make a multipair version out of an already existing advisor. Here for example:  
<https://www.forexfactory.com/showthread.php?t=792598>  
  
I do not know how good you are in coding, but adding a new indicator into any blessing version is probably the easiest thing to do in this code.  
This was also the first thing I did, when starting to try to understand the Blessing EA. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#168](/thread/post/12710725#post12710725 "Post Permalink")

  * Jan 20, 2020 2:50pm  Jan 20, 2020 2:50pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar836530_33.gif) josi](josi)

  * Joined Aug 2019 | Status: Trader | [730 Posts](/search?do=process&provider=Member&searchuser=836530)

> [Quoting ecryptom](/thread/post/12710274#post12710274 "View Quoted Post")
> 
> Disliked
> 
> BB alone dont work (too many false signals) and need a very good trend filter rsi and stoch are no good for forex and there are a lot of better choices than cci as trend yes 1 -5 good trend trades per week in 1 day candle is more profitable than xxx trades per week in 5min (make profits only for the broker)
> 
> Ignored

very helpful:  
now we know which indicators don't work (for you?) but not one is mentioned that does work (for you?)  
wasn't it customary - at some stage - not just to make claims (a is x) but to give reasons why (I think a is x because of the following reasons...)  
arguments, I think, they called it:  
An argument consists of a conclusion supported by at least one premise. Both conclusions and premises must be statements, that is, sentences with truth value (i.e., that are capable of being either true or false). The point of an argument is to provide evidence for the conclusion (i.e., show why we should believe the conclusion). 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#169](/thread/post/12710758#post12710758 "Post Permalink")

  * Edited 8:04pm  Jan 20, 2020 3:38pm | Edited 8:04pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar3294_6.gif) JackJones](jackjones)

  * Joined Aug 2005 | Status: 888 | [1,021 Posts](/search?do=process&provider=Member&searchuser=3294)

> [Quoting richard96816](/thread/post/12710062#post12710062 "View Quoted Post")
> 
> Disliked
> 
> {quote} Many different ways to go with pair selection and orientation. Correlated pairs will show you one set of behaviors and non-correlated pairs a whole different set. Non-correlated pairs might be more profitable and simpler, unless you've got a specific hedge scheme in mind. Non-correlated pairs suggest less chance of news affecting more than one pair, and better diversification. One of the main, easily attainable strengths of a multi-pair Blessing, I suspect.
> 
> Ignored

BS orginal (B3) provides a correlation trade setting that one may select if one feels so inclined!!  
  

> [Quoting ursinho4711](/thread/post/12709903#post12709903 "View Quoted Post")
> 
> Disliked
> 
> Next week I will reduce my pairs to trade to following 14 pairs: AUDJPY,AUDUSD,CHFJPY,EURCHF,EURGBP,EURJPY,EURUSD,GBPCHF,GBPJPY,GBPUSD,NZDJPY,NZDUSD,USDCHF,USDJPY I found them in a "basket trade" thread (thanks, Richard!). The reason for this combination is, that they hedge each others. I will analyze it on Demo first. Live account is too exciting in that early development stage. Though I made real (not much, but real) win last week.
> 
> Ignored

i've got my filtered pairs running on a better broker this week, will update Friday if it works out. ![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)  
  
if people are wondering about lot sizes and pairs then the document also talks about that, read: Portion Control. 

Attached File(s)

![File Type: pdf](https://assets.faireconomy.media/images/attach/pdf.gif) [blessing-3-v3.7-manual.pdf](/attachment/file/3532959?d=1579502277) 1.3 MB | 777 downloads 

grist for the mill

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#170](/thread/post/12710814#post12710814 "Post Permalink")

  * Edited 5:55pm  Jan 20, 2020 4:26pm | Edited 5:55pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar836530_33.gif) josi](josi)

  * Joined Aug 2019 | Status: Trader | [730 Posts](/search?do=process&provider=Member&searchuser=836530)

> [Quoting richard96816](/thread/post/12710062#post12710062 "View Quoted Post")
> 
> Disliked
> 
> {quote} Many different ways to go with pair selection and orientation. Correlated pairs will show you one set of behaviors and non-correlated pairs a whole different set. Non-correlated pairs might be more profitable and simpler, unless you've got a specific hedge scheme in mind. Non-correlated pairs suggest less chance of news affecting more than one pair, and better diversification. One of the main, easily attainable strengths of a multi-pair Blessing, I suspect.
> 
> Ignored

First one has to say that correlation changes over time and across TFs (simply check different TFs on correlation sites)  
Second:  
Trading correlated pairs doesn't make all that much sense because  
a) if pair one does well, the correlated pairs will do well by factor x (depending on correlation)  
b) if pair one does badly, the correlated pairs will do badly by factor x (depending on correlation)  
\- of course, this is somewhat oversimplified but it explains the general idea of the principle behind correlations.  
So: one would be better off using only the pair with the smallest slippage and adjust lot-size accordingly.  
Third:  
In a drastic event ("black swan") all pairs will be correlated. (Check historic evidence or read the books by Taleb, Nassim Nicholas)

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#171](/thread/post/12711150#post12711150 "Post Permalink")

  * Jan 20, 2020 8:01pm  Jan 20, 2020 8:01pm 

  * [ rath](rath)

  * | Joined Oct 2019  | Status: Trader | [4 Posts](/search?do=process&provider=Member&searchuser=868245)

> [Quoting ursinho4711](/thread/post/12709332#post12709332 "View Quoted Post")
> 
> Disliked
> 
> Thanks Richard! This is how I wanted the thread to run: as an open discussion about an open source. I am not the blessing programer. The approach is (still) to make the EA easier to handle and to overview when trading some pairs at the same time. I know that there is no set-file that works perfectly on all pairs. But maybe there is a setting that works good enough for many pairs. In the blessing thread I found this 5-minute timeframe setting that, according to the user, works well since three years on 14 pairs or so. Not making THE huge wins, but...
> 
> Ignored

Interesting ideas on this thread - very exciting to read!  
  
i don't have a lot of experience writing EAs but otherwise have been programming for a few years now. Here are my thoughts:  
I imagine the Blessing Dashboard to be an overarching aggregator/controller over multiple (implicit) instances of Blessing EA running for different pairs. It would be nice to keep the configuration of the overarching Dashboard relevant. I like Richard's earlier suggestion that each of those instances can be optimized separately. In absence of pair-specific optimization the EA can use a default set (which is similar to applying common set across pairs). I think it might be cool for the Blessing Dashboard to continuously assess which pairs are working well and boost trades on those pairs.  
Liked the idea with auto-optimization but not sure how that is possible with MT4 APIs - that would very smart, I think. On a separate note, I just started to toy around with automated optimization of Blessing ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
  
Excellent effort to extent Blessing to an exciting direction!  
  
/RATH 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#172](/thread/post/12711380#post12711380 "Post Permalink")

  * Jan 20, 2020 10:16pm  Jan 20, 2020 10:16pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar102021_3.gif) fx4money](fx4money)

  * Joined May 2009 | Status: Trader | [985 Posts](/search?do=process&provider=Member&searchuser=102021)

opened trades -26.XX , closed trades 37.XX on demo ![](https://resources.faireconomy.media/images/emojis/64/1f61c.png?v=15.1)  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: 20120 bless trades.png
Size: 186 KB](/attachment/image/3533209/thumbnail?d=1579526067)](/attachment/image/3533209?d=1579526067)   

  
  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: 20120 bless tradesclosed.png
Size: 186 KB](/attachment/image/3533210/thumbnail?d=1579526151)](/attachment/image/3533210?d=1579526151)   

golen trades

[2024 lucky gold trade](fx4money#30 "View Trade Explorer") All Time Return: -3.5%

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#173](/thread/post/12711394#post12711394 "Post Permalink")

  * Jan 20, 2020 10:21pm  Jan 20, 2020 10:21pm 

  * [ ultax](ultax)

  * | Joined Oct 2019  | Status: Trader | [85 Posts](/search?do=process&provider=Member&searchuser=872453)

> [Quoting ursinho4711](/thread/post/12698762#post12698762 "View Quoted Post")
> 
> Disliked
> 
> Remember that post? [https://www.forexfactory.com/showthr...7#post12551567](https://www.forexfactory.com/showthread.php?p=12551567#post12551567) Well, I used the settings and made a backtest from 01.Nov.2019 to 10.Jan.2020. 5 Minutes timeframe, for all 28 pairs. What can I say: that already looks like the winner to be tested on the Blessing-Multipair. Can't wait for Sidney open... Here are the results: {image}
> 
> Ignored

Hey how are you backtesting multi pair when mt4 can only test one pair at a time? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#174](/thread/post/12711434#post12711434 "Post Permalink")

  * Jan 20, 2020 10:39pm  Jan 20, 2020 10:39pm 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

> [Quoting ultax](/thread/post/12711394#post12711394 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hey how are you backtesting multi pair when mt4 can only test one pair at a time?
> 
> Ignored

I was backtesting one pair at the time. Using the "OncePerBar" in the EA and "Open Prices only" in the tester, this is quite fast.  
Should not make any difference in theory (not taking timing issues into account), as the EA is running all pairs one after the other in a big for-to loop.  
The only things I cannot test in backtest MT4 is the multipair functionality. I do this live on a demo.  
User fxtrue (thank you!) supplied a translated version into mql5 to me. Did not have time to test yet, though... (holidayyyyys!) 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#175](/thread/post/12715476#post12715476 "Post Permalink")

  * Jan 23, 2020 12:02am  Jan 23, 2020 12:02am 

  * [ IAmRetep](iamretep)

  * | Joined Oct 2014  | Status: Trader | [55 Posts](/search?do=process&provider=Member&searchuser=385194)

Hello, I just set up an ICMarkets demo account, trading the 28 most important pairs. Curious to see how that will develops.  
Greetings  
Peter 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#176](/thread/post/12715981#post12715981 "Post Permalink")

  * Jan 23, 2020 5:11am  Jan 23, 2020 5:11am 

  * [ kzean](kzean)

  * | Joined Aug 2014  | Status: Trader | [17 Posts](/search?do=process&provider=Member&searchuser=380085)

> [Quoting fx4money](/thread/post/12711380#post12711380 "View Quoted Post")
> 
> Disliked
> 
> opened trades -26.XX , closed trades 37.XX on demo ![](https://resources.faireconomy.media/images/emojis/64/1f61c.png?v=15.1) {image} {image}
> 
> Ignored

Hi,  
Pls clarify if we have to attach the EA with all charts of 28 currency pairs or attach the same with only pair. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#177](/thread/post/12716190#post12716190 "Post Permalink")

  * Jan 23, 2020 7:55am  Jan 23, 2020 7:55am 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

> [Quoting kzean](/thread/post/12715981#post12715981 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi, Pls clarify if we have to attach the EA with all charts of 28 currency pairs or attach the same with only pair.
> 
> Ignored

No! Only one chart! That's the idea of the multipair... 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#178](/thread/post/12716315#post12716315 "Post Permalink")

  * Edited 12:14pm  Jan 23, 2020 10:14am | Edited 12:14pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar3294_6.gif) JackJones](jackjones)

  * Joined Aug 2005 | Status: 888 | [1,021 Posts](/search?do=process&provider=Member&searchuser=3294)

Removing GBP and JPY due to risk events might be a good idea after all as AllPairs is in deep short GBP!! ![](https://resources.faireconomy.media/images/emojis/64/1f37f.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f37f.png?v=15.1)

grist for the mill

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#179](/thread/post/12716353#post12716353 "Post Permalink")

  * Jan 23, 2020 11:02am  Jan 23, 2020 11:02am 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

> [Quoting JackJones](/thread/post/12716315#post12716315 "View Quoted Post")
> 
> Disliked
> 
> Removing GBP and JPY due to risk events might be a good idea as AllPairs is in deep short GBP!! ![](https://resources.faireconomy.media/images/emojis/64/1f37f.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f37f.png?v=15.1)
> 
> Ignored

I am back to "Demo only" from today on. At least the Beta-Version did not do anything bad and I came out with a small profit (5%) after 8 trading days. Better than -1% from the ECB... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#180](/thread/post/12717745#post12717745 "Post Permalink")

  * Jan 24, 2020 12:42am  Jan 24, 2020 12:42am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar338950_1.gif) cescof](cescof)

  * Joined Jun 2013 | Status: Trader | [1,006 Posts](/search?do=process&provider=Member&searchuser=338950)

> [Quoting ursinho4711](/thread/post/12716353#post12716353 "View Quoted Post")
> 
> Disliked
> 
> {quote} I am back to "Demo only" from today on. At least the Beta-Version did not do anything bad and I came out with a small profit (5%) after 8 trading days. Better than -1% from the ECB...
> 
> Ignored

Hy... i'm in testing last version but backtesting for just one pair i've different result comparing with last blessing 3.96.13.beta... many more orders ... i supposed logic and code are quite the same...so i'm expecting same result but no way... any suggests?  
I've checked my set file many time and no difference...  
Any suggestion?  
Thanks  
Regards 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Blessing Multipair EA
  *   * [ **Reply to Thread** ](/thread/973998-blessing-multipair-ea/reply#reply)

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

[Trading multipair triangles, no stoploss](/thread/917648-trading-multipair-triangles-no-stoploss "Hello forex Folks! 
  
I'd like to share with You my system that I was comming to for many years. I am testing it these days and it gives...") 78 replies

['Blessing' EA Modification Wanted](/thread/271525-blessing-ea-modification-wanted "Hello. 
 
here is a version of BLESSING \(old\) love this version. 
I wonder if someone could if possible to change this code. 
 
I like that...") 3 replies

[Single, Few Pair Traders (1-4) vs. MultiPair Traders (8-20)](/thread/964171-single-few-pair-traders-1-4-vs-multipair-traders "Who gets better results ?? 
  
Put it in another way , if you went for a trading competition and want to achieve &gt;300% ~ 2000% , what would...") 0 replies

[Coding Request for Multipair MTF ADR Dashboard](/thread/683340-coding-request-for-multipair-mtf-adr-dashboard "Can someone code this into indicator???") 2 replies

[trying to make a multipair buy and sell script](/thread/241746-trying-to-make-a-multipair-buy-and-sell "what i like to do is that i add a script on a chart and it will do 
 
open 3 pairs buys or sells. 
 
for example 0.1 lot EURUSD 
          ...") 6 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/973998-blessing-multipair-ea/reply#reply)
  * Subscribe
  * [97](javascript:void\(0\);)

Attachments: Blessing Multipair EA

Tags: Blessing Multipair EA

#  [](/thread/973998-blessing-multipair-ea)Blessing Multipair EA 

  * 

  * [#181](/thread/post/12717820#post12717820 "Post Permalink")

  * Jan 24, 2020 1:05am  Jan 24, 2020 1:05am 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

> [Quoting cescof](/thread/post/12717745#post12717745 "View Quoted Post")
> 
> Disliked
> 
> Hy... i'm in testing last version but backtesting for just one pair i've different result comparing with last blessing 3.96.13.beta
> 
> Ignored

Hm, should not be a difference. That's one of my tests as well: using AUDCAD and afterwards XAUUSD to compare the results with "normal" Blessing.  
  
Try this version: it also has a better a ExitTrades. Just (I hope) the HolidayShutdown is an open point when it comes to Exit.  
Still open some grid and TP adjustments, that are global but should be related to TradePair.  
If you think that version suits, I will put in on post #1.  
  
Happy trading!  
  

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [BlessingLite_3_v3.9.6.32_gamma.ex4](/attachment/file/3536326?d=1579795455) 192 KB | 586 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#182](/thread/post/12717973#post12717973 "Post Permalink")

  * Jan 24, 2020 1:50am  Jan 24, 2020 1:50am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar338950_1.gif) cescof](cescof)

  * Joined Jun 2013 | Status: Trader | [1,006 Posts](/search?do=process&provider=Member&searchuser=338950)

> [Quoting ursinho4711](/thread/post/12717820#post12717820 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hm, should not be a difference. That's one of my tests as well: using AUDCAD and afterwards XAUUSD to compare the results with "normal" Blessing. Try this version: it also has a better a ExitTrades. Just (I hope) the HolidayShutdown is an open point when it comes to Exit. Still open some grid and TP adjustments, that are global but should be related to TradePair. If you think that version suits, I will put in on post #1. Happy trading! {file}
> 
> Ignored

OK thanks  
please try this setting tf5 GBPNZD  
Thanks  
Regards 

Attached File(s)

![File Type: rar](https://assets.faireconomy.media/images/attach/rar.gif) [BLESSINGGBPNZD5MINUTICONSERVATIVE.rar](/attachment/file/3536394?d=1579798251) 3 KB | 602 downloads 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#183](/thread/post/12718093#post12718093 "Post Permalink")

  * Jan 24, 2020 2:51am  Jan 24, 2020 2:51am 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

Strange... I thought everybody had this file...  
  
Put this  

Attached File(s)

![File Type: zip](https://assets.faireconomy.media/images/attach/zip.gif) [symbols.zip](/attachment/file/3536460?d=1579801851) 17 KB | 628 downloads 

  
into the folder  
\history\default  
  
It comes from the change I made, so pairs with a (broker) prefix can be used. Maybe I should have done it in a more simple way ;-) 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#184](/thread/post/12718110#post12718110 "Post Permalink")

  * Jan 24, 2020 3:03am  Jan 24, 2020 3:03am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar338950_1.gif) cescof](cescof)

  * Joined Jun 2013 | Status: Trader | [1,006 Posts](/search?do=process&provider=Member&searchuser=338950)

> [Quoting ursinho4711](/thread/post/12718093#post12718093 "View Quoted Post")
> 
> Disliked
> 
> Strange... I thought everybody had this file... Put this {file} into the folder \history\default It comes from the change I made, so pairs with a (broker) prefix can be used. Maybe I should have done it in a more simple way ;-)
> 
> Ignored

It was just a warning messsage.... Back test started.... 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#185](/thread/post/12718399#post12718399 "Post Permalink")

  * Jan 24, 2020 6:19am  Jan 24, 2020 6:19am 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

A typical "Blessing situation", where I probably would have lost trying to save the trade ;-)  
Blessing kept cool and decided at the right moment. After a huge DD it came back with almost zero. I have to analyze the grid though and TP level. A plus would even have been better... 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot1.png
Size: 23 KB](/attachment/image/3536654/thumbnail?d=1579814382)](/attachment/image/3536654?d=1579814382)   

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#186](/thread/post/12718429#post12718429 "Post Permalink")

  * Jan 24, 2020 6:55am  Jan 24, 2020 6:55am 

  * [ richard96816](richard96816)

  * Joined Dec 2018 | Status: Trader | [564 Posts](/search?do=process&provider=Member&searchuser=741833)

> [Quoting ursinho4711](/thread/post/12718399#post12718399 "View Quoted Post")
> 
> Disliked
> 
> A typical "Blessing situation", where I probably would have lost trying to save the trade ;-) Blessing kept cool and decided at the right moment. After a huge DD it came back with almost zero. I have to analyze the grid though and TP level. A plus would even have been better... {image}
> 
> Ignored

Might be helpful not to refer to MultiBlessing as Blessing. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#187](/thread/post/12718492#post12718492 "Post Permalink")

  * Jan 24, 2020 7:32am  Jan 24, 2020 7:32am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar3294_6.gif) JackJones](jackjones)

  * Joined Aug 2005 | Status: 888 | [1,021 Posts](/search?do=process&provider=Member&searchuser=3294)

> [Quoting ursinho4711](/thread/post/12718399#post12718399 "View Quoted Post")
> 
> Disliked
> 
> A typical "Blessing situation", where I probably would have lost trying to save the trade ;-) Blessing kept cool and decided at the right moment. After a huge DD it came back with almost zero. I have to analyze the grid though and TP level. A plus would even have been better... {image}
> 
> Ignored

V 3.9.6.24 not beta/gamma .30 ?? ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)  
  
Looks like my All-pairs MultiBless (Maddog) managed to get out of G/nzd but still short G/aud and currently has about 30 trades open. It's only just survived drawdown in a 1k demo account this week (possibly up to 50% at one point) so i would think 5k at a minimum, even than that's risky.  
  
my filtered pairs (10) demo was heavy on gbp pairs at the start of the week and has also survived, just.  
  
Would like to see it close off a few pairs and reduce risk on Friday but i'm not sure it thinks like that. I might help have to help it out during the euro session . 

grist for the mill

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#188](/thread/post/12718504#post12718504 "Post Permalink")

  * Jan 24, 2020 7:37am  Jan 24, 2020 7:37am 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

> [Quoting richard96816](/thread/post/12718429#post12718429 "View Quoted Post")
> 
> Disliked
> 
> {quote} Might be helpful not to refer to MultiBlessing as Blessing.
> 
> Ignored

Well, the heart is still the same and I try to keep it that way. Knowing that there are still some constructions ahead. But if you feel offended (or maybe there is a TM?) I can think of another name. "Praying" for example... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#189](/thread/post/12718516#post12718516 "Post Permalink")

  * Jan 24, 2020 7:40am  Jan 24, 2020 7:40am 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

> [Quoting JackJones](/thread/post/12718492#post12718492 "View Quoted Post")
> 
> Disliked
> 
> {quote} V 3.9.6.24 not beta/gamma .30
> 
> Ignored

It's just the comment string, I could even write MickeyMouse1.0... if the comment is too long, it occupies too much space in the terminal field. I am just with a small notebook here during my travel... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#190](/thread/post/12718757#post12718757 "Post Permalink")

  * Jan 24, 2020 1:01pm  Jan 24, 2020 1:01pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar3294_6.gif) JackJones](jackjones)

  * Joined Aug 2005 | Status: 888 | [1,021 Posts](/search?do=process&provider=Member&searchuser=3294)

> [Quoting ursinho4711](/thread/post/12718516#post12718516 "View Quoted Post")
> 
> Disliked
> 
> {quote} It's just the comment string, I could even write MickeyMouse1.0... if the comment is too long, it occupies too much space in the terminal field. I am just with a small notebook here during my travel...
> 
> Ignored

yes good point but 'blessing lite' also.. is this a super special custom AllPairs (rhetorical)? all good noted for future!  
  
btw looks like my demo account got out of the gbp/jpy long with $1.2 profit ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)

grist for the mill

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#191](/thread/post/12718825#post12718825 "Post Permalink")

  * Jan 24, 2020 2:38pm  Jan 24, 2020 2:38pm 

  * [ richard96816](richard96816)

  * Joined Dec 2018 | Status: Trader | [564 Posts](/search?do=process&provider=Member&searchuser=741833)

> [Quoting ursinho4711](/thread/post/12718504#post12718504 "View Quoted Post")
> 
> Disliked
> 
> {quote} Well, the heart is still the same and I try to keep it that way. Knowing that there are still some constructions ahead. But if you feel offended (or maybe there is a TM?) I can think of another name. "Praying" for example...
> 
> Ignored

I'm not offended. Just hoping to keep confusion down a bit. I look back and forth between the two groups and sometimes lose track of where I am. :-) 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#192](/thread/post/12719010#post12719010 "Post Permalink")

  * Jan 24, 2020 5:26pm  Jan 24, 2020 5:26pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar102021_3.gif) fx4money](fx4money)

  * Joined May 2009 | Status: Trader | [985 Posts](/search?do=process&provider=Member&searchuser=102021)

just need a confirmation, if the ea is able to detect 4 decimal or 5 decimal brokers. 

golen trades

[2024 lucky gold trade](fx4money#30 "View Trade Explorer") All Time Return: -3.5%

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#193](/thread/post/12719111#post12719111 "Post Permalink")

  * Jan 24, 2020 6:09pm  Jan 24, 2020 6:09pm 

  * [ IAmRetep](iamretep)

  * | Joined Oct 2014  | Status: Trader | [55 Posts](/search?do=process&provider=Member&searchuser=385194)

<https://www.forexfactory.com/iamretep>  
  
Hi there,  
Here you will find the result of the 28 currency pairs from the last three days. Trading started three days ago in the afternoon (GMT+1).  
With this forward test I want to find out how the current drawdown per tick is developing across all pairs.  
In a second step, I would like to filter the best portfolios from these 28 pairs. I hope this is helpful. However, at least 1,000 trades are likely to be required to evaluate this analysis, which will take approximately 10 weeks.  
Greetings  
Peter 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#194](/thread/post/12719187#post12719187 "Post Permalink")

  * Jan 24, 2020 6:49pm  Jan 24, 2020 6:49pm 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

> [Quoting fx4money](/thread/post/12719010#post12719010 "View Quoted Post")
> 
> Disliked
> 
> just need a confirmation, if the ea is able to detect 4 decimal or 5 decimal brokers.
> 
> Ignored

Hi!  
This is more a Blessing question and not a multipair question. Anyway I will answer: Yes! Take a look at the code:  
  

Inserted Code
    
    
    temp = (int) MarketInfo(TradePairs[Index]+suffix,MODE_DIGITS);
          if(temp % 2 == 1)pairinfo[Index].Pip *= 10;

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#195](/thread/post/12719303#post12719303 "Post Permalink")

  * Jan 24, 2020 7:40pm  Jan 24, 2020 7:40pm 

  * [ dejoo](dejoo)

  * | Joined Jan 2020  | Status: Trader | [8 Posts](/search?do=process&provider=Member&searchuser=909230)

I test the baby blessing ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1) with the pair of [ ursinho4711](https://www.forexfactory.com/ursinho4711), let's see what he does next week at Brexit,  
BlessingLite 3.9.6.24  
Demo: Roboforex ECNPro  
Pairs:  
AUDJPY, AUDUSD, CHFJPY, EURCHF, EURGBP, EURJPY, EURUSD, GBPCHF, GBPJPY, GBPUSD, NZDJPY, NZDUSD, USDCHF, USDJPY 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot_2.png
Size: 48 KB](/attachment/image/3537128/thumbnail?d=1579862331)](/attachment/image/3537128?d=1579862331)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#196](/thread/post/12719359#post12719359 "Post Permalink")

  * Jan 24, 2020 8:14pm  Jan 24, 2020 8:14pm 

  * [ farmabioq](farmabioq)

  * | Commercial User  | Joined Dec 2014 | [55 Posts](/search?do=process&provider=Member&searchuser=394496)

Hello. I have placed a news filter (the one from forex factory) to the gamma version, I hope it works.  

I have set the configuration of post 7: in TF: 5 minutes.  
(The news filter does not take into account those of low impact, if those of medium and high impact, I think this would solve several loss problems.) 

Attached File(s)

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [BlessingLite_3_v3.9.6.30_gamma_news.mq4](/attachment/file/3537143?d=1579863861) 129 KB | 528 downloads 

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [FFCal.mq4](/attachment/file/3537147?d=1579864073) 69 KB | 484 downloads 

[0 ](javascript:void\(0\);) [3 ](javascript:void\(0\);)

  * [#197](/thread/post/12719463#post12719463 "Post Permalink")

  * Jan 24, 2020 9:13pm  Jan 24, 2020 9:13pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar102021_3.gif) fx4money](fx4money)

  * Joined May 2009 | Status: Trader | [985 Posts](/search?do=process&provider=Member&searchuser=102021)

profit 113, float 77. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: 20124 blessmpairpopit.png
Size: 191 KB](/attachment/image/3537201/thumbnail?d=1579867986)](/attachment/image/3537201?d=1579867986)   

golen trades

[2024 lucky gold trade](fx4money#30 "View Trade Explorer") All Time Return: -3.5%

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#198](/thread/post/12719467#post12719467 "Post Permalink")

  * Jan 24, 2020 9:16pm  Jan 24, 2020 9:16pm 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

> [Quoting fx4money](/thread/post/12719463#post12719463 "View Quoted Post")
> 
> Disliked
> 
> profit 113, float 77. {image}
> 
> Ignored

Like a squirrel. Many small nuts fill a big basket ... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#199](/thread/post/12719492#post12719492 "Post Permalink")

  * Jan 24, 2020 9:28pm  Jan 24, 2020 9:28pm 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

> [Quoting fx4money](/thread/post/12719463#post12719463 "View Quoted Post")
> 
> Disliked
> 
> profit 113, float 77. {image}
> 
> Ignored

I took a look at your list: I have almost all of those trades as well. Thumbs up! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#200](/thread/post/12719518#post12719518 "Post Permalink")

  * Jan 24, 2020 9:37pm  Jan 24, 2020 9:37pm 

  * [ farmabioq](farmabioq)

  * | Commercial User  | Joined Dec 2014 | [55 Posts](/search?do=process&provider=Member&searchuser=394496)

ursinho4711: What TF do you use? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Blessing Multipair EA
  *   * [ **Reply to Thread** ](/thread/973998-blessing-multipair-ea/reply#reply)

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

[Trading multipair triangles, no stoploss](/thread/917648-trading-multipair-triangles-no-stoploss "Hello forex Folks! 
  
I'd like to share with You my system that I was comming to for many years. I am testing it these days and it gives...") 78 replies

['Blessing' EA Modification Wanted](/thread/271525-blessing-ea-modification-wanted "Hello. 
 
here is a version of BLESSING \(old\) love this version. 
I wonder if someone could if possible to change this code. 
 
I like that...") 3 replies

[Single, Few Pair Traders (1-4) vs. MultiPair Traders (8-20)](/thread/964171-single-few-pair-traders-1-4-vs-multipair-traders "Who gets better results ?? 
  
Put it in another way , if you went for a trading competition and want to achieve &gt;300% ~ 2000% , what would...") 0 replies

[Coding Request for Multipair MTF ADR Dashboard](/thread/683340-coding-request-for-multipair-mtf-adr-dashboard "Can someone code this into indicator???") 2 replies

[trying to make a multipair buy and sell script](/thread/241746-trying-to-make-a-multipair-buy-and-sell "what i like to do is that i add a script on a chart and it will do 
 
open 3 pairs buys or sells. 
 
for example 0.1 lot EURUSD 
          ...") 6 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/973998-blessing-multipair-ea/reply#reply)
  * Subscribe
  * [97](javascript:void\(0\);)

Attachments: Blessing Multipair EA

Tags: Blessing Multipair EA

#  [](/thread/973998-blessing-multipair-ea)Blessing Multipair EA 

  * 

  * [#201](/thread/post/12719533#post12719533 "Post Permalink")

  * Jan 24, 2020 9:46pm  Jan 24, 2020 9:46pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar3294_6.gif) JackJones](jackjones)

  * Joined Aug 2005 | Status: 888 | [1,021 Posts](/search?do=process&provider=Member&searchuser=3294)

> [Quoting farmabioq](/thread/post/12719359#post12719359 "View Quoted Post")
> 
> Disliked
> 

> 
> Ignored

Nice, i will try it out next week.. can you link to the news filter from FF? this one? <https://www.forexfactory.com/showthread.php?t=326551>

grist for the mill

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#202](/thread/post/12719567#post12719567 "Post Permalink")

  * Jan 24, 2020 10:02pm  Jan 24, 2020 10:02pm 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

> [Quoting farmabioq](/thread/post/12719518#post12719518 "View Quoted Post")
> 
> Disliked
> 
> ursinho4711: What TF do you use?
> 
> Ignored

5 Minutes. I use the set-file "5Minutes-for-all" from the original blessing thread. Also, as I am still in the trial phase, 5 minutes opens many, but not too many trades. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#203](/thread/post/12719579#post12719579 "Post Permalink")

  * Jan 24, 2020 10:10pm  Jan 24, 2020 10:10pm 

  * [ farmabioq](farmabioq)

  * | Commercial User  | Joined Dec 2014 | [55 Posts](/search?do=process&provider=Member&searchuser=394496)

set of : post 7. Pairs all? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#204](/thread/post/12719594#post12719594 "Post Permalink")

  * Jan 24, 2020 10:16pm  Jan 24, 2020 10:16pm 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

> [Quoting farmabioq](/thread/post/12719579#post12719579 "View Quoted Post")
> 
> Disliked
> 
> set of : post 7. Pairs all?
> 
> Ignored

Yes! And looks like fx4money uses the same. We have both the same entries and exits.  
I won't say that this is the holy grail. But in the other thread somebody is using that setup since three years and it works, he sais... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#205](/thread/post/12719613#post12719613 "Post Permalink")

  * Jan 24, 2020 10:25pm  Jan 24, 2020 10:25pm 

  * [ farmabioq](farmabioq)

  * | Commercial User  | Joined Dec 2014 | [55 Posts](/search?do=process&provider=Member&searchuser=394496)

Thanks friend. We'll see if it improves with the news filter yet. The good thing about using low tf with news filter, is that it avoids any rare, unthinkable fact that happens before a misplaced information for any Ea.  
  
Try it in demo account, let's see how it works. (It is not easy to make it work correctly) 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#206](/thread/post/12719621#post12719621 "Post Permalink")

  * Jan 24, 2020 10:29pm  Jan 24, 2020 10:29pm 

  * [ Mcxtrader](mcxtrader)

  * | Joined Jun 2017  | Status: Trader | [203 Posts](/search?do=process&provider=Member&searchuser=589792)

> [Quoting ursinho4711](/thread/post/12719567#post12719567 "View Quoted Post")
> 
> Disliked
> 
> {quote} 5 Minutes. I use the set-file "5Minutes-for-all" from the original blessing thread. Also, as I am still in the trial phase, 5 minutes opens many, but not too many trades.
> 
> Ignored

Could you please post the set file here.  
  
Thanks in advance. 

[1 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#207](/thread/post/12719685#post12719685 "Post Permalink")

  * Jan 24, 2020 10:57pm  Jan 24, 2020 10:57pm 

  * [ dejoo](dejoo)

  * | Joined Jan 2020  | Status: Trader | [8 Posts](/search?do=process&provider=Member&searchuser=909230)

> [Quoting Mcxtrader](/thread/post/12719621#post12719621 "View Quoted Post")
> 
> Disliked
> 
> {quote} Could you please post the set file here. Thanks in advance.
> 
> Ignored

  
Hi show this # post 7  
  
[BlessingLiteV24-5Min-AllPairs.set.txt](https://www.forexfactory.com/attachment.php/3527087?attachmentid=3527087&d=1578824928)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#208](/thread/post/12719692#post12719692 "Post Permalink")

  * Jan 24, 2020 11:01pm  Jan 24, 2020 11:01pm 

  * [ farmabioq](farmabioq)

  * | Commercial User  | Joined Dec 2014 | [55 Posts](/search?do=process&provider=Member&searchuser=394496)

Post 7. 

Attached File(s)

![File Type: txt](https://assets.faireconomy.media/images/attach/txt.gif) [BlessingLiteV24-5Min-AllPairs.set.txt](/attachment/file/3537278?d=1579874506) 2 KB | 444 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#209](/thread/post/12719697#post12719697 "Post Permalink")

  * Jan 24, 2020 11:05pm  Jan 24, 2020 11:05pm 

  * [ Mcxtrader](mcxtrader)

  * | Joined Jun 2017  | Status: Trader | [203 Posts](/search?do=process&provider=Member&searchuser=589792)

> [Quoting dejoo](/thread/post/12719685#post12719685 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi show this # post 7 [BlessingLiteV24-5Min-AllPairs.set.txt](https://www.forexfactory.com/attachment.php/3527087?attachmentid=3527087&d=1578824928)
> 
> Ignored

Thank you. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#210](/thread/post/12719698#post12719698 "Post Permalink")

  * Jan 24, 2020 11:06pm  Jan 24, 2020 11:06pm 

  * [ Mcxtrader](mcxtrader)

  * | Joined Jun 2017  | Status: Trader | [203 Posts](/search?do=process&provider=Member&searchuser=589792)

> [Quoting farmabioq](/thread/post/12719692#post12719692 "View Quoted Post")
> 
> Disliked
> 
> Post 7. {file}
> 
> Ignored

Thanks for your immediate response 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#211](/thread/post/12719932#post12719932 "Post Permalink")

  * Jan 25, 2020 1:06am  Jan 25, 2020 1:06am 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

> [Quoting farmabioq](/thread/post/12719613#post12719613 "View Quoted Post")
> 
> Disliked
> 
> We'll see if it improves with the news filter yet
> 
> Ignored

Thanks a lot for your cooperation! That's what I hoped from this thread. I do not want to be a lone warrior. The code is very complex and it is always good to have a shecond or third thought/idea...  
  
Another to-do, that should not be toooooo difficult but is kind of annoying:  
There is another check for holiday shutdown in the middle of the code. Only that the program never gets there as the first holiday check already inhibts entry into the for-to loop. Okay, not too much happens in there, deleting pending orders mainly.  
  

Inserted Code
    
    
          //+-----------------------------------------------------------------+
          //| Check Holiday Shutdown                                          |
          //+-----------------------------------------------------------------+
          if(UseHolidayShutdown)
            {
             if(HolShutDown == 1 && pairinfo[i].CbT == 0)
               {
                Print("Trading has been paused for holidays (", TimeToStr(HolFirst, TIME_DATE), " - ", TimeToStr(HolLast, TIME_DATE), ")");

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#212](/thread/post/12720230#post12720230 "Post Permalink")

  * Jan 25, 2020 3:28am  Jan 25, 2020 3:28am 

  * [ Mcxtrader](mcxtrader)

  * | Joined Jun 2017  | Status: Trader | [203 Posts](/search?do=process&provider=Member&searchuser=589792)

Hello,  
  
I have loaded version 32 gamma and loaded set file 5min all as well. I dont see any trade getting opened.  
  
Any idea please.  
  
Thanks in advance. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#213](/thread/post/12720409#post12720409 "Post Permalink")

  * Jan 25, 2020 5:17am  Jan 25, 2020 5:17am 

  * [ dejoo](dejoo)

  * | Joined Jan 2020  | Status: Trader | [8 Posts](/search?do=process&provider=Member&searchuser=909230)

> [Quoting Mcxtrader](/thread/post/12720230#post12720230 "View Quoted Post")
> 
> Disliked
> 
> Hello, I have loaded version 32 gamma and loaded set file 5min all as well. I dont see any trade getting opened. Any idea please. Thanks in advance.
> 
> Ignored

See your Spread Brooker and Blessing 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#214](/thread/post/12720546#post12720546 "Post Permalink")

  * Jan 25, 2020 6:57am  Jan 25, 2020 6:57am 

  * [ kzean](kzean)

  * | Joined Aug 2014  | Status: Trader | [17 Posts](/search?do=process&provider=Member&searchuser=380085)

> [Quoting ursinho4711](/thread/post/12719492#post12719492 "View Quoted Post")
> 
> Disliked
> 
> {quote} I took a look at your list: I have almost all of those trades as well. Thumbs up!
> 
> Ignored

Kindly attach EA and set files used. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#215](/thread/post/12720553#post12720553 "Post Permalink")

  * Jan 25, 2020 6:59am  Jan 25, 2020 6:59am 

  * [ farmabioq](farmabioq)

  * | Commercial User  | Joined Dec 2014 | [55 Posts](/search?do=process&provider=Member&searchuser=394496)

Thank ursinho. I think the presence of the Check Holiday code does not work if you put the option in: false before operating, regardless of this, do you want to eliminate this option? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#216](/thread/post/12720564#post12720564 "Post Permalink")

  * Jan 25, 2020 7:13am  Jan 25, 2020 7:13am 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

> [Quoting farmabioq](/thread/post/12720553#post12720553 "View Quoted Post")
> 
> Disliked
> 
> Thank ursinho. I think the presence of the Check Holiday code does not work if you put the option in: false before operating, regardless of this, do you want to eliminate this option?
> 
> Ignored

To be honest, I was thinking of this. We are adult people (though what we do is somehow childish) and nobody needs to remind me when there is a holiday ;-)  
If the EA was really THAT reliable that you could let it run for a year without watching...  
It so fast done manually: set the "ShutDown=true" and then delete the pending orders. When coming back, set the "ShutDown=false". The EA will start looking for entry conditions again.  
This holidayShutDown is a small neat feature, but it occupies alot of code. A LOT (haha, lot). I can live without it. What does the community say? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#217](/thread/post/12720568#post12720568 "Post Permalink")

  * Jan 25, 2020 7:22am  Jan 25, 2020 7:22am 

  * [ farmabioq](farmabioq)

  * | Commercial User  | Joined Dec 2014 | [55 Posts](/search?do=process&provider=Member&searchuser=394496)

There it is, delete it, see if it works well. 

Attached File(s)

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [BlessingLite_3_v3.9.6.30_gamma_news2.mq4](/attachment/file/3537654?d=1579904492) 122 KB | 556 downloads 

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#218](/thread/post/12720585#post12720585 "Post Permalink")

  * Jan 25, 2020 7:51am  Jan 25, 2020 7:51am 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

> [Quoting farmabioq](/thread/post/12720568#post12720568 "View Quoted Post")
> 
> Disliked
> 
> There it is
> 
> Ignored

Sent you a message... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#219](/thread/post/12720641#post12720641 "Post Permalink")

  * Jan 25, 2020 10:08am  Jan 25, 2020 10:08am 

  * [ farmabioq](farmabioq)

  * | Commercial User  | Joined Dec 2014 | [55 Posts](/search?do=process&provider=Member&searchuser=394496)

hello.I sent you my email, have you received it? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#220](/thread/post/12720675#post12720675 "Post Permalink")

  * Jan 25, 2020 11:25am  Jan 25, 2020 11:25am 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

> [Quoting farmabioq](/thread/post/12720641#post12720641 "View Quoted Post")
> 
> Disliked
> 
> hello.I sent you my email, have you received it?
> 
> Ignored

Sim, obrigado!  
Looks like we now have some coders who like to form a team. We should just avoid working on different versions. I was thinking of putting the mql onto GitHub. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Blessing Multipair EA
  *   * [ **Reply to Thread** ](/thread/973998-blessing-multipair-ea/reply#reply)

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

[Trading multipair triangles, no stoploss](/thread/917648-trading-multipair-triangles-no-stoploss "Hello forex Folks! 
  
I'd like to share with You my system that I was comming to for many years. I am testing it these days and it gives...") 78 replies

['Blessing' EA Modification Wanted](/thread/271525-blessing-ea-modification-wanted "Hello. 
 
here is a version of BLESSING \(old\) love this version. 
I wonder if someone could if possible to change this code. 
 
I like that...") 3 replies

[Single, Few Pair Traders (1-4) vs. MultiPair Traders (8-20)](/thread/964171-single-few-pair-traders-1-4-vs-multipair-traders "Who gets better results ?? 
  
Put it in another way , if you went for a trading competition and want to achieve &gt;300% ~ 2000% , what would...") 0 replies

[Coding Request for Multipair MTF ADR Dashboard](/thread/683340-coding-request-for-multipair-mtf-adr-dashboard "Can someone code this into indicator???") 2 replies

[trying to make a multipair buy and sell script](/thread/241746-trying-to-make-a-multipair-buy-and-sell "what i like to do is that i add a script on a chart and it will do 
 
open 3 pairs buys or sells. 
 
for example 0.1 lot EURUSD 
          ...") 6 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/973998-blessing-multipair-ea/reply#reply)
  * Subscribe
  * [97](javascript:void\(0\);)

Attachments: Blessing Multipair EA

Tags: Blessing Multipair EA

#  [](/thread/973998-blessing-multipair-ea)Blessing Multipair EA 

  * 

  * [#221](/thread/post/12720681#post12720681 "Post Permalink")

  * Jan 25, 2020 11:41am  Jan 25, 2020 11:41am 

  * [ farmabioq](farmabioq)

  * | Commercial User  | Joined Dec 2014 | [55 Posts](/search?do=process&provider=Member&searchuser=394496)

It is a good idea, but friend, people in general are selfish, hopefully this is not so much. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#222](/thread/post/12720730#post12720730 "Post Permalink")

  * Edited 2:55pm  Jan 25, 2020 2:44pm | Edited 2:55pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar3294_6.gif) JackJones](jackjones)

  * Joined Aug 2005 | Status: 888 | [1,021 Posts](/search?do=process&provider=Member&searchuser=3294)

going over the week and i'm taking gbp/aud gbp/nzd and gbp/cad out of filtered ATeam - only a small position in the later two which i will close monday morn and gbp/aud is still struggling but hopefully it will get out next week and i'll remove it from AllPairs(filtered#Ateam)Blessing(gamma 2.0) - nearly closed it out for near break-even Friday Asia session but left it (doh!) ![](https://resources.faireconomy.media/images/emojis/64/1f47b.png?v=15.1)  
  
likely going to replace gbp pairs with eur/aud , chf/jpy and nzd/usd (possibly also cad/chf) and start them on the Allpairs(filtered#Ateam) for Monday - a little concerned about chf/jpy as it's a beast at times but it has won 12 out of 13 last two weeks so it might be doing something right. 

grist for the mill

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#223](/thread/post/12720731#post12720731 "Post Permalink")

  * Jan 25, 2020 2:51pm  Jan 25, 2020 2:51pm 

  * [ goodways100](goodways100)

  * Joined Dec 2013 | Status: Trader | [615 Posts](/search?do=process&provider=Member&searchuser=358325)

Downloaded the ea today. will try on Monday. Thanks and  
Regards 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#224](/thread/post/12720789#post12720789 "Post Permalink")

  * Jan 25, 2020 6:04pm  Jan 25, 2020 6:04pm 

  * [ kzean](kzean)

  * | Joined Aug 2014  | Status: Trader | [17 Posts](/search?do=process&provider=Member&searchuser=380085)

> [Quoting ursinho4711](/thread/post/12719492#post12719492 "View Quoted Post")
> 
> Disliked
> 
> {quote} I took a look at your list: I have almost all of those trades as well. Thumbs up!
> 
> Ignored

Hi, There are various versions(bata, gamma) of Blessing Multipair EA. Which version are you trading/experimenting with, can you please provide a list of pairs and set file?  
Regards 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#225](/thread/post/12720864#post12720864 "Post Permalink")

  * Jan 25, 2020 8:04pm  Jan 25, 2020 8:04pm 

  * [ IAmRetep](iamretep)

  * | Joined Oct 2014  | Status: Trader | [55 Posts](/search?do=process&provider=Member&searchuser=385194)

To whom it may concern. Attached you find the results of the first trading week, from 2020.22.01 to 2020.24.01.  
  
Greetings  
Peter 

Attached File(s)

![File Type: pdf](https://assets.faireconomy.media/images/attach/pdf.gif) [1\. Week Blessing.pdf](/attachment/file/3537780?d=1579950169) 32 KB | 757 downloads 

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#226](/thread/post/12720874#post12720874 "Post Permalink")

  * Edited 8:33pm  Jan 25, 2020 8:22pm | Edited 8:33pm 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

> [Quoting IAmRetep](/thread/post/12720864#post12720864 "View Quoted Post")
> 
> Disliked
> 
> To whom it may concern.
> 
> Ignored

Moin Peter ;-)  
  
Thanks for sharing you results. Look similar to mine. What I have learned from other multipair systems in the past is, that at some point you have to make a restart. Close all open positions, even in red, and start from scratch.  
  

Attached Image

![](/attachment/image/3537796?d=1579951964)

  
  
Bury them, they are dead horses... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#227](/thread/post/12720881#post12720881 "Post Permalink")

  * Jan 25, 2020 8:30pm  Jan 25, 2020 8:30pm 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

> [Quoting kzean](/thread/post/12720789#post12720789 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi, There are various versions(bata, gamma) of Blessing Multipair EA. Which version are you trading/experimenting with, can you please provide a list of pairs and set file? Regards
> 
> Ignored

I am trying to put the latest trial version in post#1. Im now using version 33-gamma, no setfile as I put my defaults into the code. You are free to change them though. The defaults came from the so often mentioned 5-minutes-all-pairs setfile.  
  
Versions from version 30 on should not change the results for the pairs to trade anymore. Before I release a new version, I compare the results for a single pair with the results for the same pair in the "normal" Blessing version. Remember: the heart of the Blessing program has not been changed... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#228](/thread/post/12720895#post12720895 "Post Permalink")

  * Jan 25, 2020 8:49pm  Jan 25, 2020 8:49pm 

  * [ rath](rath)

  * | Joined Oct 2019  | Status: Trader | [4 Posts](/search?do=process&provider=Member&searchuser=868245)

> [Quoting ursinho4711](/thread/post/12720675#post12720675 "View Quoted Post")
> 
> Disliked
> 
> {quote} Sim, obrigado! Looks like we now have some coders who like to form a team. We should just avoid working on different versions. I was thinking of putting the mql onto GitHub.
> 
> Ignored

[+1]  
That would be great! Would be easier to submit pull requests for fixes and improved capabilities. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#229](/thread/post/12720900#post12720900 "Post Permalink")

  * Jan 25, 2020 8:59pm  Jan 25, 2020 8:59pm 

  * [ IAmRetep](iamretep)

  * | Joined Oct 2014  | Status: Trader | [55 Posts](/search?do=process&provider=Member&searchuser=385194)

> [Quoting ursinho4711](/thread/post/12720874#post12720874 "View Quoted Post")
> 
> Disliked
> 
> {quote} Moin Peter ;-) Thanks for sharing you results. Look similar to mine. What I have learned from other multipair systems in the past is, that at some point you have to make a restart. Close all open positions, even in red, and start from scratch. {image} Bury them, they are dead horses...
> 
> Ignored

Moin, Moin...  
  
OK, you are right. To find the best time for exits or entries I need roundabout 1.000 closed trades perhaps more. Next step will be to optimize the number of currency pairs.  
Greeting  
Peter  
  
..Servus 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#230](/thread/post/12721171#post12721171 "Post Permalink")

  * Jan 26, 2020 3:21am  Jan 26, 2020 3:21am 

  * [ IAmRetep](iamretep)

  * | Joined Oct 2014  | Status: Trader | [55 Posts](/search?do=process&provider=Member&searchuser=385194)

Hi,  
I think it is a good idea to develop Blessing Multipair EA in a team. However, I think we shouldn't put the cart before the horse.  
1.) The functional logic of your EA, thank you for sharing ursinho4711 :-), seems to be OK except perhaps just small details.  
2.) Now we should analyse how the EA behaves in forward testing. I don't think it makes sense to test additional filters at this stage. Blessing has enough alternatives and is powerful enough. At this point the question arises for me, do all filters really work as known from the original?  
3.) If yes, we can consider:  
a) At what times should we trade? (can we continue with the pending orders technology used),  
b) Which currency pairs are the most successful in combination?  
c) Is it worth building a .set file for each currency pair and is the performance of a MT4-dashboard sufficient for this? And  
d) What is the maximum drawdown or the risk of total loss in the interaction of the currency pairs on a tick basis?  
Greetings  
Peter 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#231](/thread/post/12721284#post12721284 "Post Permalink")

  * Jan 26, 2020 7:46am  Jan 26, 2020 7:46am 

  * [ richard96816](richard96816)

  * Joined Dec 2018 | Status: Trader | [564 Posts](/search?do=process&provider=Member&searchuser=741833)

How do you intend to leverage multi-pair operation?  
  
What mechanisms do you expect to build that will make Blessing more profitable than her single-pair incarnation? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#232](/thread/post/12721348#post12721348 "Post Permalink")

  * Jan 26, 2020 10:48am  Jan 26, 2020 10:48am 

  * [ ultax](ultax)

  * | Joined Oct 2019  | Status: Trader | [85 Posts](/search?do=process&provider=Member&searchuser=872453)

Can you make for MT5 so that we can backtest with multiple pairs?  
  
Also what indicator is it going on? Just mathematics or is something triggering the entry? What about using an index indicator or sar? 

[1 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#233](/thread/post/12721362#post12721362 "Post Permalink")

  * Jan 26, 2020 11:10am  Jan 26, 2020 11:10am 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

> [Quoting ultax](/thread/post/12721348#post12721348 "View Quoted Post")
> 
> Disliked
> 
> Also what indicator is it going on? Just mathematics or is something triggering the entry? What about using an index indicator or sar?
> 
> Ignored

Hi! Did you read the thread from beginning on...? Did you also already see the Search function in the forum software..?  
![](https://resources.faireconomy.media/images/emojis/64/1f61c.png?v=15.1)  
  
Here's something to read:  

Attached File(s)

![File Type: pdf](https://assets.faireconomy.media/images/attach/pdf.gif) [blessing_3_v3.3_manual.pdf](/attachment/file/3538075?d=1580004608) 712 KB | 750 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#234](/thread/post/12721667#post12721667 "Post Permalink")

  * Jan 26, 2020 10:38pm  Jan 26, 2020 10:38pm 

  * [ ultax](ultax)

  * | Joined Oct 2019  | Status: Trader | [85 Posts](/search?do=process&provider=Member&searchuser=872453)

> [Quoting ursinho4711](/thread/post/12721362#post12721362 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi! Did you read the thread from beginning on...? Did you also already see the Search function in the forum software..? ![](https://resources.faireconomy.media/images/emojis/64/1f61c.png?v=15.1) Here's something to read: {image}
> 
> Ignored

Yes... after my post!  
  
MT5 a possibility? Forward testing on MT4 isn't really viable to conclude using 28 pairs.... Far too many variables. 

[1 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#235](/thread/post/12721697#post12721697 "Post Permalink")

  * Jan 26, 2020 11:21pm  Jan 26, 2020 11:21pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar338950_1.gif) cescof](cescof)

  * Joined Jun 2013 | Status: Trader | [1,006 Posts](/search?do=process&provider=Member&searchuser=338950)

> [Quoting ultax](/thread/post/12721667#post12721667 "View Quoted Post")
> 
> Disliked
> 
> {quote} Yes... after my post! MT5 a possibility? Forward testing on MT4 isn't really viable to conclude using 28 pairs.... Far too many variables.
> 
> Ignored

Did you read the thread? Sure? Mt5 version is still avaible 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#236](/thread/post/12721725#post12721725 "Post Permalink")

  * Jan 26, 2020 11:45pm  Jan 26, 2020 11:45pm 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

New version V34-Gamma in post #1.  
Found two static variables inside the main program that probably caused a minor wrong calculation of the take profit when there was more than one pair. Moved the variables into the struct.  
  
**edit**  
I created a github repository. Whoever wants to participate has to register there and send me an e-mail. I will then try to add you to the team... 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#237](/thread/post/12721795#post12721795 "Post Permalink")

  * Jan 27, 2020 12:57am  Jan 27, 2020 12:57am 

  * [ ultax](ultax)

  * | Joined Oct 2019  | Status: Trader | [85 Posts](/search?do=process&provider=Member&searchuser=872453)

> [Quoting cescof](/thread/post/12721697#post12721697 "View Quoted Post")
> 
> Disliked
> 
> {quote} Did you read the thread? Sure? Mt5 version is still avaible
> 
> Ignored

Where I cannot find? If MT5 available why are you guys not testing multiple pairs in backtester? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#238](/thread/post/12721801#post12721801 "Post Permalink")

  * Jan 27, 2020 1:05am  Jan 27, 2020 1:05am 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

> [Quoting ultax](/thread/post/12721795#post12721795 "View Quoted Post")
> 
> Disliked
> 
> Where I cannot find?
> 
> Ignored

Hi! What about if you sit down and learn a little bit about the forum software. Read threads about Blessing... study documents...  
;-)  
Thanks and have a nice weekend!  
  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot1.png
Size: 59 KB](/attachment/image/3538303/thumbnail?d=1580054703)](/attachment/image/3538303?d=1580054703)   

  
  

> [Quoting ultax](/thread/post/12721795#post12721795 "View Quoted Post")
> 
> Disliked
> 
> If MT5 available why are you guys not testing multiple pairs in backtester?
> 
> Ignored

Because the day only has 24 hours and I also do not want to get divorced from my beloved wife... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#239](/thread/post/12721847#post12721847 "Post Permalink")

  * Jan 27, 2020 2:04am  Jan 27, 2020 2:04am 

  * [ ultax](ultax)

  * | Joined Oct 2019  | Status: Trader | [85 Posts](/search?do=process&provider=Member&searchuser=872453)

> [Quoting ursinho4711](/thread/post/12721801#post12721801 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi! What about if you sit down and learn a little bit about the forum software. Read threads about Blessing... study documents... ;-) Thanks and have a nice weekend! {image} {quote} Because the day only has 24 hours and I also do not want to get divorced from my beloved wife...
> 
> Ignored

Ah thank you did not know you could do that. So that mt5 version is the same as what you've done? Is there the mt5 version with hedging built in? thank you for your reply 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#240](/thread/post/12721853#post12721853 "Post Permalink")

  * Jan 27, 2020 2:18am  Jan 27, 2020 2:18am 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

> [Quoting ultax](/thread/post/12721847#post12721847 "View Quoted Post")
> 
> Disliked
> 
> Ah thank you did not know you could do that.
> 
> Ignored

No problem, we are here to learn, right?  
(and make some money later)  
  

> [Quoting ultax](/thread/post/12721847#post12721847 "View Quoted Post")
> 
> Disliked
> 
> So that mt5 version is the same as what you've done? Is there the mt5 version with hedging built in? thank you for your reply
> 
> Ignored

To be honest, I almost do not work with mt5. No time. Who made the "translation" was our friend fxtrue. Now we have a new version v34 which is already a lot better than that one from one week ago. I am fast making updates ;-)  
The hedging function I removed from the multipair version. I am still thinking to reactivate it, though. More to that later in the "Blessing Setfile" thread...  
  
Sun is shining, 38°C. I will go out and enjoy the day... 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Blessing Multipair EA
  *   * [ **Reply to Thread** ](/thread/973998-blessing-multipair-ea/reply#reply)

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

[Trading multipair triangles, no stoploss](/thread/917648-trading-multipair-triangles-no-stoploss "Hello forex Folks! 
  
I'd like to share with You my system that I was comming to for many years. I am testing it these days and it gives...") 78 replies

['Blessing' EA Modification Wanted](/thread/271525-blessing-ea-modification-wanted "Hello. 
 
here is a version of BLESSING \(old\) love this version. 
I wonder if someone could if possible to change this code. 
 
I like that...") 3 replies

[Single, Few Pair Traders (1-4) vs. MultiPair Traders (8-20)](/thread/964171-single-few-pair-traders-1-4-vs-multipair-traders "Who gets better results ?? 
  
Put it in another way , if you went for a trading competition and want to achieve &gt;300% ~ 2000% , what would...") 0 replies

[Coding Request for Multipair MTF ADR Dashboard](/thread/683340-coding-request-for-multipair-mtf-adr-dashboard "Can someone code this into indicator???") 2 replies

[trying to make a multipair buy and sell script](/thread/241746-trying-to-make-a-multipair-buy-and-sell "what i like to do is that i add a script on a chart and it will do 
 
open 3 pairs buys or sells. 
 
for example 0.1 lot EURUSD 
          ...") 6 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/973998-blessing-multipair-ea/reply#reply)
  * Subscribe
  * [97](javascript:void\(0\);)

Attachments: Blessing Multipair EA

Tags: Blessing Multipair EA

#  [](/thread/973998-blessing-multipair-ea)Blessing Multipair EA 

  * 

  * [#241](/thread/post/12722262#post12722262 "Post Permalink")

  * Jan 27, 2020 9:47am  Jan 27, 2020 9:47am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar102021_3.gif) fx4money](fx4money)

  * Joined May 2009 | Status: Trader | [985 Posts](/search?do=process&provider=Member&searchuser=102021)

> [Quoting ursinho4711](/thread/post/12721853#post12721853 "View Quoted Post")
> 
> Disliked
> 
> {quote} No problem, we are here to learn, right? (and make some money later) {quote} To be honest, I almost do not work with mt5. No time. Who made the "translation" was our friend fxtrue. Now we have a new version v34 which is already a lot better than that one from one week ago. I am fast making updates ;-) The hedging function I removed from the multipair version. I am still thinking to reactivate it, though. More to that later in the "Blessing Setfile" thread... Sun is shining, 38°C. I will go out and enjoy the day...
> 
> Ignored

hedging function is good to have. and i would suggest if possible that ea to close all at certain equity percentage increase. 

golen trades

[2024 lucky gold trade](fx4money#30 "View Trade Explorer") All Time Return: -3.5%

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#242](/thread/post/12722303#post12722303 "Post Permalink")

  * Jan 27, 2020 10:47am  Jan 27, 2020 10:47am 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

> [Quoting fx4money](/thread/post/12722262#post12722262 "View Quoted Post")
> 
> Disliked
> 
> i would suggest if possible that ea to close all at certain equity percentage increase.
> 
> Ignored

Should already do it. Should... no guarantee though. Please try on demo first. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#243](/thread/post/12722747#post12722747 "Post Permalink")

  * Jan 27, 2020 6:23pm  Jan 27, 2020 6:23pm 

  * [ ultax](ultax)

  * | Joined Oct 2019  | Status: Trader | [85 Posts](/search?do=process&provider=Member&searchuser=872453)

> [Quoting fx4money](/thread/post/12722262#post12722262 "View Quoted Post")
> 
> Disliked
> 
> {quote} hedging function is good to have. and _**i would suggest if possible that ea to close all at certain equity percentage increase.**_
> 
> Ignored

Agree, I was trying to find this option in the settings (not sure if the MT5 is different from your version ursinho4711?) 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#244](/thread/post/12723902#post12723902 "Post Permalink")

  * Edited 5:52am  Jan 28, 2020 5:41am | Edited 5:52am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar115254_1.gif) takrooni](takrooni)

  * | Commercial User  | Joined Sep 2009 | [21 Posts](/search?do=process&provider=Member&searchuser=115254)

> [Quoting ursinho4711](/thread/post/12722303#post12722303 "View Quoted Post")
> 
> Disliked
> 
> {quote} Should already do it. Should... no guarantee though. Please try on demo first.
> 
> Ignored

Hello  
Ursinho you really doing a very good job ,, these set working good with me specially on FXch0ice broker ,, but am wondering why EA don't opening any trades when  
( small lot account) function = true ? .  
  
thank you .. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#245](/thread/post/12723987#post12723987 "Post Permalink")

  * Jan 28, 2020 7:05am  Jan 28, 2020 7:05am 

  * [ richard96816](richard96816)

  * Joined Dec 2018 | Status: Trader | [564 Posts](/search?do=process&provider=Member&searchuser=741833)

> [Quoting takrooni](/thread/post/12723902#post12723902 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hello Ursinho you really doing a very good job ,, these set working good with me specially on FXch0ice broker ,, but am wondering why EA don't opening any trades when ( small lot account) function = true ? . thank you ..
> 
> Ignored

I assume you mean NanoAccount. I don't think FXChoice has NanoAccounts.  
  
That setting only changes some size multipliers. Use the one that works. Trust Strategy Tester. :-)  
  
Trust good results. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#246](/thread/post/12724008#post12724008 "Post Permalink")

  * Jan 28, 2020 7:24am  Jan 28, 2020 7:24am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar115254_1.gif) takrooni](takrooni)

  * | Commercial User  | Joined Sep 2009 | [21 Posts](/search?do=process&provider=Member&searchuser=115254)

> [Quoting richard96816](/thread/post/12723987#post12723987 "View Quoted Post")
> 
> Disliked
> 
> {quote} I assume you mean NanoAccount. I don't think FXChoice has NanoAccounts. That setting only changes some size multipliers. Use the one that works. Trust Strategy Tester. :-) Trust good results.
> 
> Ignored

  
O. K  
How to open trades with 0.01size only instead of 0.05? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#247](/thread/post/12724058#post12724058 "Post Permalink")

  * Edited 8:47am  Jan 28, 2020 8:18am | Edited 8:47am 

  * [ richard96816](richard96816)

  * Joined Dec 2018 | Status: Trader | [564 Posts](/search?do=process&provider=Member&searchuser=741833)

> [Quoting takrooni](/thread/post/12724008#post12724008 "View Quoted Post")
> 
> Disliked
> 
> {quote} O. K How to open trades with 0.01size only instead of 0.05?
> 
> Ignored

Read the manual. Use Strategy Tester. See what **LAF** and **Multiplier** do. 

[0 ](javascript:void\(0\);) [3 ](javascript:void\(0\);)

  * [#248](/thread/post/12726202#post12726202 "Post Permalink")

  * Jan 29, 2020 8:44am  Jan 29, 2020 8:44am 

  * [ richard96816](richard96816)

  * Joined Dec 2018 | Status: Trader | [564 Posts](/search?do=process&provider=Member&searchuser=741833)

If would probably be helpful to put all the double semicolons back on the external variables so that MPBlessing matches the manual again.  
  
I'm pretty sure the comment on **NanoAccount** is wrong.  
  
The double semicolons are necessary due to '#property strict'. The second semicolon presents MT4 with a null comment forcing it to use the old behavior showing the variable name, while the programmer still gets to see the comments.  
  
There are probably better ways to describe these variables in the menu, but the manual goes into a whole lot of detail so the discussion here hopefully doesn't have to. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#249](/thread/post/12726247#post12726247 "Post Permalink")

  * Jan 29, 2020 9:32am  Jan 29, 2020 9:32am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar102021_3.gif) fx4money](fx4money)

  * Joined May 2009 | Status: Trader | [985 Posts](/search?do=process&provider=Member&searchuser=102021)

i changed pairs to string DefaultPairs[] = {"AUDCAD","AUDUSD","EURAUD","EURCAD","EURUSD","USDCAD"};  
  
and ea only open for eurusd, and not opening other pairs..... any idea why? 

golen trades

[2024 lucky gold trade](fx4money#30 "View Trade Explorer") All Time Return: -3.5%

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#250](/thread/post/12726445#post12726445 "Post Permalink")

  * Jan 29, 2020 1:51pm  Jan 29, 2020 1:51pm 

  * [ Mcxtrader](mcxtrader)

  * | Joined Jun 2017  | Status: Trader | [203 Posts](/search?do=process&provider=Member&searchuser=589792)

Hi All.  
  
I set my lot size as .10. My first trade is opening correctly with .10 lot size.  
  
But I can see my sell/buy limit is opening with .003 and not with .30.  
  
Is it default behavior or is it bug.  
  
  
I am using 34 gamma.  
  
  
Thanks in advance. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot1.png
Size: 119 KB](/attachment/image/3540535/thumbnail?d=1580273463)](/attachment/image/3540535?d=1580273463)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#251](/thread/post/12727372#post12727372 "Post Permalink")

  * Jan 29, 2020 11:31pm  Jan 29, 2020 11:31pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar115254_1.gif) takrooni](takrooni)

  * | Commercial User  | Joined Sep 2009 | [21 Posts](/search?do=process&provider=Member&searchuser=115254)

Hii @Urshinho  
  
am facing problem with backtesting ,, useing post(1) sets ,, the problem on back test it's not opening any trades even i use Enable once peer bar and open price only mode .  
  
thank you . 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#252](/thread/post/12727426#post12727426 "Post Permalink")

  * Jan 30, 2020 12:04am  Jan 30, 2020 12:04am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar102021_3.gif) fx4money](fx4money)

  * Joined May 2009 | Status: Trader | [985 Posts](/search?do=process&provider=Member&searchuser=102021)

> [Quoting Mcxtrader](/thread/post/12726445#post12726445 "View Quoted Post")
> 
> Disliked
> 
> Hi All. I set my lot size as .10. My first trade is opening correctly with .10 lot size. But I can see my sell/buy limit is opening with .003 and not with .30. Is it default behavior or is it bug. I am using 34 gamma. Thanks in advance. {image}
> 
> Ignored

i believe there are still bugs in the coding. i tried to use different multiplier, but new post opened still using default 3.0 multiplier 

golen trades

[2024 lucky gold trade](fx4money#30 "View Trade Explorer") All Time Return: -3.5%

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#253](/thread/post/12727796#post12727796 "Post Permalink")

  * Jan 30, 2020 3:56am  Jan 30, 2020 3:56am 

  * [ richard96816](richard96816)

  * Joined Dec 2018 | Status: Trader | [564 Posts](/search?do=process&provider=Member&searchuser=741833)

> [Quoting fx4money](/thread/post/12727426#post12727426 "View Quoted Post")
> 
> Disliked
> 
> {quote} i believe there are still bugs in the coding. i tried to use different multiplier, but new post opened still using default 3.0 multiplier
> 
> Ignored

I just ran a quick optimization test. If you turn on Money Management it seems to work. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#254](/thread/post/12727802#post12727802 "Post Permalink")

  * Jan 30, 2020 3:59am  Jan 30, 2020 3:59am 

  * [ richard96816](richard96816)

  * Joined Dec 2018 | Status: Trader | [564 Posts](/search?do=process&provider=Member&searchuser=741833)

> [Quoting takrooni](/thread/post/12727372#post12727372 "View Quoted Post")
> 
> Disliked
> 
> Hii @Urshinho am facing problem with backtesting ,, useing post(1) sets ,, the problem on back test it's not opening any trades even i use Enable once peer bar and open price only mode . thank you .
> 
> Ignored

There are so many reasons for this to happen.  
  
Check your Journal tab for clues. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#255](/thread/post/12728209#post12728209 "Post Permalink")

  * Edited 10:03am  Jan 30, 2020 9:41am | Edited 10:03am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar3294_6.gif) JackJones](jackjones)

  * Joined Aug 2005 | Status: 888 | [1,021 Posts](/search?do=process&provider=Member&searchuser=3294)

> [Quoting richard96816](/thread/post/12727796#post12727796 "View Quoted Post")
> 
> Disliked
> 
> {quote} I just ran a quick optimization test. If you turn on Money Management it seems to work.
> 
> Ignored

when you say 'optimization test', do you mean you mean running the mt4 strategy tester over a pair and watching it trade visually? or something else?  
  
looking at my filtered #Ateam (Bless-Gamma2.0 ) and so far this week they are trading well, another week or two of this and I might take them live.. most are trading 80%+ win rate !!![](https://resources.faireconomy.media/images/emojis/64/1f631.png?v=15.1)

grist for the mill

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#256](/thread/post/12728633#post12728633 "Post Permalink")

  * Jan 30, 2020 5:51pm  Jan 30, 2020 5:51pm 

  * [ richard96816](richard96816)

  * Joined Dec 2018 | Status: Trader | [564 Posts](/search?do=process&provider=Member&searchuser=741833)

> [Quoting JackJones](/thread/post/12728209#post12728209 "View Quoted Post")
> 
> Disliked
> 
> {quote} when you say 'optimization test', do you mean you mean running the mt4 strategy tester over a pair and watching it trade visually? or something else? ...
> 
> Ignored

No visuals necessary. Strategy Tester and comparison of results. Varying **Multiplier** changes lot sizes and profits progressively just as it's supposed to. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#257](/thread/post/12728985#post12728985 "Post Permalink")

  * Jan 30, 2020 9:02pm  Jan 30, 2020 9:02pm 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

That looks like a promising one at the moment. Remember, that timing is important. Might be too late for y'all ;-)  
  

Attached File(s)

![File Type: txt](https://assets.faireconomy.media/images/attach/txt.gif) [BL-Multi-V34-BB_STOCHinv.set.txt](/attachment/file/3541724?d=1580385604) 2 KB | 556 downloads 

  
  
\--> takes a while as I uss BB and inverse Stochastic as entry.  
\--> takes a while for TP as I turned on AutoTP and moving TP/Trailing stop 

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#258](/thread/post/12729022#post12729022 "Post Permalink")

  * Jan 30, 2020 9:18pm  Jan 30, 2020 9:18pm 

  * [ ultax](ultax)

  * | Joined Oct 2019  | Status: Trader | [85 Posts](/search?do=process&provider=Member&searchuser=872453)

> [Quoting ursinho4711](/thread/post/12721853#post12721853 "View Quoted Post")
> 
> Disliked
> 
> {quote} No problem, we are here to learn, right? (and make some money later) {quote} To be honest, I almost do not work with mt5. No time. Who made the "translation" was our friend fxtrue. Now we have a new version v34 which is already a lot better than that one from one week ago. I am fast making updates ;-) The hedging function I removed from the multipair version. I am still thinking to reactivate it, though. More to that later in the "Blessing Setfile" thread... Sun is shining, 38°C. I will go out and enjoy the day...
> 
> Ignored

Thanks, yes it would be good to put it back in. Only reason I ask re: MT5 version is so that we can backtest on the strategy tester.... As you know MT4 limitation of only one pair means we can't get a grasp on performance. I know there is forward testing but... 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#259](/thread/post/12729058#post12729058 "Post Permalink")

  * Jan 30, 2020 9:31pm  Jan 30, 2020 9:31pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar3294_6.gif) JackJones](jackjones)

  * Joined Aug 2005 | Status: 888 | [1,021 Posts](/search?do=process&provider=Member&searchuser=3294)

> [Quoting richard96816](/thread/post/12728633#post12728633 "View Quoted Post")
> 
> Disliked
> 
> {quote} No visuals necessary. Strategy Tester and comparison of results. Varying Multiplier changes lot sizes and profits progressively just as it's supposed to.
> 
> Ignored

i see, i'm going about it slightly differently... i'm running about five demo accounts with MP Bless and Standard Blesssing on others and watching them trade live then looking at the results as i tweak variables (and I also get odd differences between accounts to boot which makes me wonder bugs or broker issues? argh!).. so no back-testing just forwarding testing. my PC is grinding hard these days so might be time for an upgrade. 

grist for the mill

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#260](/thread/post/12729640#post12729640 "Post Permalink")

  * Jan 31, 2020 2:07am  Jan 31, 2020 2:07am 

  * [ ultax](ultax)

  * | Joined Oct 2019  | Status: Trader | [85 Posts](/search?do=process&provider=Member&searchuser=872453)

Is this default Blessing settings or have they been changed for this specific MT5 version? Trying to use the manual but not coming across very clear to me. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Capture.PNG
Size: 26 KB](/attachment/image/3541986/thumbnail?d=1580404036)](/attachment/image/3541986?d=1580404036)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Blessing Multipair EA
  *   * [ **Reply to Thread** ](/thread/973998-blessing-multipair-ea/reply#reply)

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

[Trading multipair triangles, no stoploss](/thread/917648-trading-multipair-triangles-no-stoploss "Hello forex Folks! 
  
I'd like to share with You my system that I was comming to for many years. I am testing it these days and it gives...") 78 replies

['Blessing' EA Modification Wanted](/thread/271525-blessing-ea-modification-wanted "Hello. 
 
here is a version of BLESSING \(old\) love this version. 
I wonder if someone could if possible to change this code. 
 
I like that...") 3 replies

[Single, Few Pair Traders (1-4) vs. MultiPair Traders (8-20)](/thread/964171-single-few-pair-traders-1-4-vs-multipair-traders "Who gets better results ?? 
  
Put it in another way , if you went for a trading competition and want to achieve &gt;300% ~ 2000% , what would...") 0 replies

[Coding Request for Multipair MTF ADR Dashboard](/thread/683340-coding-request-for-multipair-mtf-adr-dashboard "Can someone code this into indicator???") 2 replies

[trying to make a multipair buy and sell script](/thread/241746-trying-to-make-a-multipair-buy-and-sell "what i like to do is that i add a script on a chart and it will do 
 
open 3 pairs buys or sells. 
 
for example 0.1 lot EURUSD 
          ...") 6 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/973998-blessing-multipair-ea/reply#reply)
  * Subscribe
  * [97](javascript:void\(0\);)

Attachments: Blessing Multipair EA

Tags: Blessing Multipair EA

#  [](/thread/973998-blessing-multipair-ea)Blessing Multipair EA 

  * 

  * [#261](/thread/post/12729680#post12729680 "Post Permalink")

  * Edited 2:42am  Jan 31, 2020 2:30am | Edited 2:42am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar115254_1.gif) takrooni](takrooni)

  * | Commercial User  | Joined Sep 2009 | [21 Posts](/search?do=process&provider=Member&searchuser=115254)

> [Quoting richard96816](/thread/post/12727802#post12727802 "View Quoted Post")
> 
> Disliked
> 
> {quote} There are so many reasons for this to happen. Check your Journal tab for clues.
> 
> Ignored

  
Hello  
i can see some error here on Fxchoice 

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: Screenshot2.png
Size: 46 KB](/attachment/image/3542016/thumbnail?d=1580405408)](/attachment/image/3542016?d=1580405408)   
[![Click to Enlarge

Name: Screenshot5.png
Size: 57 KB](/attachment/image/3542021/thumbnail?d=1580405787)](/attachment/image/3542021?d=1580405787)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#262](/thread/post/12730093#post12730093 "Post Permalink")

  * Edited 9:21am  Jan 31, 2020 6:50am | Edited 9:21am 

  * [ richard96816](richard96816)

  * Joined Dec 2018 | Status: Trader | [564 Posts](/search?do=process&provider=Member&searchuser=741833)

> [Quoting JackJones](/thread/post/12729058#post12729058 "View Quoted Post")
> 
> Disliked
> 
> {quote} i see, i'm going about it slightly differently... i'm running about five demo accounts with MP Bless and Standard Blesssing on others and watching them trade live then looking at the results as i tweak variables (and I also get odd differences between accounts to boot which makes me wonder bugs or broker issues? argh!).. so no back-testing just forwarding testing. my PC is grinding hard these days so might be time for an upgrade.
> 
> Ignored

So many millions of things to try, so little time.  
  
I'm currently running 22 MT4 terminal instances on this machine. And some MT5s too. With way too many EAs on each one. :-)  
  
Forward testing is the key to profiting with EAs.  
  
Never stopped to test the differences between instances with the same broker, though I know they exist.  
  
As I've **written in this thread many times** the differences between brokers are usually **quite large**. Largest in smaller timeframes. **Folks using set files from different brokers are making a big mistake.** I don't even use set files from one broker to start an optimization for another broker. Starting from scratch is better and faster.  
  
**Brokers all make up their own data. It's all different. Read your broker's contract!** This is why third-party and tick data are useless. This is why I added _EnableOncePerBar_ to Blessing.  
  
Read the rest of this thread for more information. It's all there.  
  
Edit: Make that the main Blessing thread.  
  
Good luck! 

[0 ](javascript:void\(0\);) [3 ](javascript:void\(0\);)

  * [#263](/thread/post/12730374#post12730374 "Post Permalink")

  * Jan 31, 2020 12:55pm  Jan 31, 2020 12:55pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar102021_3.gif) fx4money](fx4money)

  * Joined May 2009 | Status: Trader | [985 Posts](/search?do=process&provider=Member&searchuser=102021)

> [Quoting takrooni](/thread/post/12729680#post12729680 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hello i can see some error here on Fxchoice {image} {image}
> 
> Ignored

same for me ![](https://resources.faireconomy.media/images/emojis/64/1f61c.png?v=15.1)

golen trades

[2024 lucky gold trade](fx4money#30 "View Trade Explorer") All Time Return: -3.5%

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#264](/thread/post/12731057#post12731057 "Post Permalink")

  * Jan 31, 2020 8:22pm  Jan 31, 2020 8:22pm 

  * [ ultax](ultax)

  * | Joined Oct 2019  | Status: Trader | [85 Posts](/search?do=process&provider=Member&searchuser=872453)

_**It would be so good if we could get a fully original MT5 version, anyone up for doing it?**_

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#265](/thread/post/12731108#post12731108 "Post Permalink")

  * Jan 31, 2020 8:43pm  Jan 31, 2020 8:43pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar3294_6.gif) JackJones](jackjones)

  * Joined Aug 2005 | Status: 888 | [1,021 Posts](/search?do=process&provider=Member&searchuser=3294)

> [Quoting richard96816](/thread/post/12730093#post12730093 "View Quoted Post")
> 
> Disliked
> 
> {quote} So many millions of things to try, so little time. I'm currently running 22 MT4 terminal instances on this machine. And some MT5s too. With way too many EAs on each one. :-) Forward testing is the key to profiting with EAs
> 
> Ignored

which broker? i moved my demos to one broker the other week because i saw better results and just today they sent an email saying my demo accounts are "hyperactive" and they might close some of them down.. might have to split demos to another broker ![](https://resources.faireconomy.media/images/emojis/64/1f641.png?v=15.1) ![](https://resources.faireconomy.media/images/emojis/64/1f928.png?v=15.1)

grist for the mill

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#266](/thread/post/12731206#post12731206 "Post Permalink")

  * Jan 31, 2020 9:53pm  Jan 31, 2020 9:53pm 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

> [Quoting ultax](/thread/post/12731057#post12731057 "View Quoted Post")
> 
> Disliked
> 
> It would be so good if we could get a fully original MT5 version, anyone up for doing it?
> 
> Ignored

What about you? Will you volunteer to do so?  
  
Btw: I stayed up almost all night to learn about the differences mt4<->mt5 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#267](/thread/post/12731208#post12731208 "Post Permalink")

  * Jan 31, 2020 9:55pm  Jan 31, 2020 9:55pm 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

> [Quoting JackJones](/thread/post/12731108#post12731108 "View Quoted Post")
> 
> Disliked
> 
> and just today they sent an email saying my demo accounts are "hyperactive" and they might close some of them down.. might have to split demos to another broker ![](https://resources.faireconomy.media/images/emojis/64/1f641.png?v=15.1) ![](https://resources.faireconomy.media/images/emojis/64/1f928.png?v=15.1)
> 
> Ignored

You did not read this thread.  
  
@Richard: q.e.d. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#268](/thread/post/12731307#post12731307 "Post Permalink")

  * Jan 31, 2020 10:47pm  Jan 31, 2020 10:47pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar3294_6.gif) JackJones](jackjones)

  * Joined Aug 2005 | Status: 888 | [1,021 Posts](/search?do=process&provider=Member&searchuser=3294)

> [Quoting ursinho4711](/thread/post/12731208#post12731208 "View Quoted Post")
> 
> Disliked
> 
> {quote} You did not read this thread. @Richard: q.e.d.
> 
> Ignored

there is no mention of "hyperactivity" in this thread. it's the accounts running allpairs that have been mentioned by the broker, not he ones running single blessing, calm down, get some sleep ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)

grist for the mill

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#269](/thread/post/12731404#post12731404 "Post Permalink")

  * Jan 31, 2020 11:32pm  Jan 31, 2020 11:32pm 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

> [Quoting JackJones](/thread/post/12731307#post12731307 "View Quoted Post")
> 
> Disliked
> 
> get some sleep ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)
> 
> Ignored

Good idea...  
  
It was in the other thread:  
[https://www.forexfactory.com/showthr...9#post12682129](https://www.forexfactory.com/showthread.php?p=12682129#post12682129)  
  
When you use a 5 minute or higher timeframe and not only MA as entry, then your broker should not claim.  
  
Now I will sleep a little bit on the beach (until London Close ;-) ))) 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#270](/thread/post/12732300#post12732300 "Post Permalink")

  * Feb 1, 2020 10:56am  Feb 1, 2020 10:56am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar102021_3.gif) fx4money](fx4money)

  * Joined May 2009 | Status: Trader | [985 Posts](/search?do=process&provider=Member&searchuser=102021)

float 1473, profit 184 ![](https://resources.faireconomy.media/images/emojis/64/1f61c.png?v=15.1) not worth it ![](https://resources.faireconomy.media/images/emojis/64/1f61c.png?v=15.1)

golen trades

[2024 lucky gold trade](fx4money#30 "View Trade Explorer") All Time Return: -3.5%

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#271](/thread/post/12732307#post12732307 "Post Permalink")

  * Feb 1, 2020 11:23am  Feb 1, 2020 11:23am 

  * [ richard96816](richard96816)

  * Joined Dec 2018 | Status: Trader | [564 Posts](/search?do=process&provider=Member&searchuser=741833)

> [Quoting ursinho4711](/thread/post/12731206#post12731206 "View Quoted Post")
> 
> Disliked
> 
> {quote} What about you? Will you volunteer to do so? Btw: I stayed up almost all night to learn about the differences mt4<->mt5
> 
> Ignored

I just spent a couple days this week attempting to convert single-pair Blessing to mt5. (Had a few too many bug problems all at once this week with mt4.)  
  
Blessing was made 'strict' compatible with version .10 by a very helpful soul on that list. That was very helpful to the process.  
  
mt5 has so many gratuitous differences, it can be a pain.  
  
It's surprising there's not a more complete set of libraries available. Or maybe there is and I've missed it ... 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#272](/thread/post/12732310#post12732310 "Post Permalink")

  * Feb 1, 2020 11:34am  Feb 1, 2020 11:34am 

  * [ richard96816](richard96816)

  * Joined Dec 2018 | Status: Trader | [564 Posts](/search?do=process&provider=Member&searchuser=741833)

> [Quoting JackJones](/thread/post/12731307#post12731307 "View Quoted Post")
> 
> Disliked
> 
> {quote} there is no mention of "hyperactivity" in this thread. it's the accounts running allpairs that have been mentioned by the broker, not he ones running single blessing, calm down, get some sleep ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)
> 
> Ignored

Perhaps not using that word. But the discussion was had and exists. Has little to do with 'all pairs'. And probably not accounts but specific terminals or EAs. Lots of trades from lots of charts is usually okay. It's too many trades per pair that they don't like.  
  
Try reading the first post again. :-)  
  
Good luck! 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#273](/thread/post/12732373#post12732373 "Post Permalink")

  * Feb 1, 2020 3:29pm  Feb 1, 2020 3:29pm 

  * [ hinseng](hinseng)

  * | Joined Oct 2019  | Status: Trader | [4 Posts](/search?do=process&provider=Member&searchuser=864896)

Hello All!  
  
This is my first post.  
  
Attachments are the results I traded on a real account for one week.  
I started from 100,000 yen and added 200,000 from yesterday.  
All transactions are conducted with default settings.  
I think that it is a good EA, but starting trading at 100,000 yen is a risk. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Blessing34_gamma.jpg
Size: 554 KB](/attachment/image/3543435/thumbnail?d=1580538484)](/attachment/image/3543435?d=1580538484)   

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#274](/thread/post/12732541#post12732541 "Post Permalink")

  * Feb 1, 2020 10:23pm  Feb 1, 2020 10:23pm 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

Good morning @ll! Had a night of sleep, I really needed it. I will try to write down the zillions of thoughts I had about this EA while I was dreaming...  
  
First of all thanks to everyone who contributed in a helpful way...  
  
What is the benefit of this EA compared to single Blessings?  
Good question, maybe we will get more answers in the future. For now I see following: in cooperation with a dashboards, you can have a quick overview about the live performance when changing parameters. Can be used to help your real decisions or for training purposes.  
A Dashboard imho is a must when trading multiple pairs. Please google or use the search function of the forum. One hint: same magical (EAN) number.  
  
Merda, I had my head full of things to write down. I need another coffee... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#275](/thread/post/12732555#post12732555 "Post Permalink")

  * Feb 1, 2020 10:56pm  Feb 1, 2020 10:56pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar836530_33.gif) josi](josi)

  * Joined Aug 2019 | Status: Trader | [730 Posts](/search?do=process&provider=Member&searchuser=836530)

> [Quoting ursinho4711](/thread/post/12732541#post12732541 "View Quoted Post")
> 
> Disliked
> 
> For now I see following: in cooperation with a dashboards, you can have a quick overview about the live performance when changing parameters. Can be used to help your real decisions or for training purposes. A Dashboard imho is a must when trading multiple pairs. Please google or use the search function of the forum. One hint: same magical (EAN) number.
> 
> Ignored

  
As an interested beginner who wants to have a detailed look at the MP blessing.  
Are dashboard and EA integrated, i. e. are they one ex.4-file?  
Or are you in the process of doing that?  
If not - how would I go about doing/implementing that.  
Which dashboard? Reference to EA? Which file goes into which folder etc.  
I know you don't have the time or energy to give me detailed explanations but maybe you can direct a beginner to the links/threads on how to do this.  
Thanks in advance.  
By the way - I'm really impressed by all the work you (and a few others) are prepared to put into the Blessing-project.  
For me at least - it's not that I'm too lazy to get involved (as you sometimes complained when feedback was sparse) but I lack the technical expertise (as yet).  
  
So I am rather a pupil in awe. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#276](/thread/post/12732642#post12732642 "Post Permalink")

  * Feb 2, 2020 1:03am  Feb 2, 2020 1:03am 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

> [Quoting josi](/thread/post/12732555#post12732555 "View Quoted Post")
> 
> Disliked
> 
> {quote} As an interested beginner who wants to have a detailed look at the MP blessing. Are dashboard and EA integrated, i. e. are they one ex.4-file? Or are you in the process of doing that? If not - how would I go about doing/implementing that. Which dashboard? Reference to EA? Which file goes into which folder etc. I know you don't have the time or energy to give me detailed explanations but maybe you can direct a beginner to the links/threads on how to do this. Thanks in advance. By the way - I'm really impressed by all the work you (and a few...
> 
> Ignored

Just came back from the beach and will go to a party now. That's why here comes the short version only. Please use the (excellent) search function of the forum or use google. This is like a training for you: don't need to know everything, just to know where to find the information...  
  
1\. open two charts. Apply a template that makes them black. Move the Y-Scale away, sometimes some infos may disturb the screen...  
2\. on one chart apply the MultiPair-Blessing EA. Use the timeframe you want it to trade with  
3\. on the other chart put a dashboard. There are plenty of them in the forum. Read the dashboard thread and pick one that suits your needs. I am using some of the boards user Gvc posted (thanks alot, Gvc).  
4\. MultipairBlessing and Dashboard a) must have the same magical number b) should have the same list of pairs to trade. Both are settings in the EA settings and can be changed.  
  
That's it!  
  
<https://www.forexfactory.com/showthread.php?t=532236>

Attached File(s)

![File Type: tpl](https://assets.faireconomy.media/images/attach/tpl.gif) [BlackChart.tpl](/attachment/file/3543579?d=1580573012) < 1 KB | 303 downloads 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#277](/thread/post/12732666#post12732666 "Post Permalink")

  * Edited 3:56am  Feb 2, 2020 1:50am | Edited 3:56am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar115254_1.gif) takrooni](takrooni)

  * | Commercial User  | Joined Sep 2009 | [21 Posts](/search?do=process&provider=Member&searchuser=115254)

> [Quoting takrooni](/thread/post/12729680#post12729680 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hello i can see some error here on Fxchoice {image} {image}
> 
> Ignored

please guys need help with backtest ,,  
  
i have some error like

  1. open simple.raw fails
  2. no marketinfo for xauusd

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#278](/thread/post/12732847#post12732847 "Post Permalink")

  * Feb 2, 2020 9:05am  Feb 2, 2020 9:05am 

  * [ richard96816](richard96816)

  * Joined Dec 2018 | Status: Trader | [564 Posts](/search?do=process&provider=Member&searchuser=741833)

> [Quoting takrooni](/thread/post/12732666#post12732666 "View Quoted Post")
> 
> Disliked
> 
> {quote} please guys need help with backtest ,, i have some error like open simple.raw fails no marketinfo for xauusd
> 
> Ignored

Try a different symbol. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#279](/thread/post/12732954#post12732954 "Post Permalink")

  * Edited 3:50pm  Feb 2, 2020 3:28pm | Edited 3:50pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar3294_6.gif) JackJones](jackjones)

  * Joined Aug 2005 | Status: 888 | [1,021 Posts](/search?do=process&provider=Member&searchuser=3294)

> [Quoting hinseng](/thread/post/12732373#post12732373 "View Quoted Post")
> 
> Disliked
> 
> Hello All! This is my first post. Attachments are the results I traded on a real account for one week. I started from 100,000 yen and added 200,000 from yesterday. All transactions are conducted with default settings. I think that it is a good EA, but starting trading at 100,000 yen is a risk. {image}
> 
> Ignored

hows it looking this weekend? my raw AllPairs is taking another hit on GBP - RIP Europe!  
  
last week it got out of big DD gbpaud but didn't close at BE, it closed at a semi-reasonable loss. ![](https://resources.faireconomy.media/images/emojis/64/1f923.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f923.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f680.png?v=15.1)  
  
glad i removed gbp/nzd also from my #filteredAteam last week ![](https://resources.faireconomy.media/images/emojis/64/1f605.png?v=15.1)  
  
only one that might get pulled out next week is eur/aud as it's slipped under 80% win  
  
nzd/chf will play on Ateam next week.  
  
may the fx-gods be with you.  
  

> [Quoting ursinho4711](/thread/post/12731404#post12731404 "View Quoted Post")
> 
> Disliked
> 
> {quote} Good idea... It was in the other thread: [https://www.forexfactory.com/showthr...9#post12682129](https://www.forexfactory.com/showthread.php?p=12682129#post12682129) When you use a 5 minute or higher timeframe and not only MA as entry, then your broker should not claim. Now I will sleep a little bit on the beach (until London Close ;-) )))
> 
> Ignored

  
launching allpair EAs during brexit and global panic is a good test  
  
stay rested and hydrated party guy, stay sharp for the FX ![](https://resources.faireconomy.media/images/emojis/64/1f4aa.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f64f.png?v=15.1)  
  
might join you tho, i'm off for a 4 week jaunt myself next week, trading by the pool ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)

grist for the mill

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#280](/thread/post/12733041#post12733041 "Post Permalink")

  * Feb 2, 2020 6:33pm  Feb 2, 2020 6:33pm 

  * [ hinseng](hinseng)

  * | Joined Oct 2019  | Status: Trader | [4 Posts](/search?do=process&provider=Member&searchuser=864896)

> [Quoting JackJones](/thread/post/12732954#post12732954 "View Quoted Post")
> 
> Disliked
> 
> {quote} hows it looking this weekend? my raw AllPairs is taking another hit on GBP - RIP Europe! last week it got out of big DD gbpaud but didn't close at BE, it closed at a semi-reasonable loss. ![](https://resources.faireconomy.media/images/emojis/64/1f923.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f923.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f680.png?v=15.1) glad i removed gbp/nzd also from my #filteredAteam last week ![](https://resources.faireconomy.media/images/emojis/64/1f605.png?v=15.1) only one that might get pulled out next week is eur/aud as it's slipped under 80% win nzd/chf will play on Ateam next week. may the fx-gods be with you. {quote}
> 
> Ignored

Next week, the movement of the GBP pair will need careful attention.  
But I still want to see the results of the transaction with the default settings. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Blessing Multipair EA
  *   * [ **Reply to Thread** ](/thread/973998-blessing-multipair-ea/reply#reply)

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

[Trading multipair triangles, no stoploss](/thread/917648-trading-multipair-triangles-no-stoploss "Hello forex Folks! 
  
I'd like to share with You my system that I was comming to for many years. I am testing it these days and it gives...") 78 replies

['Blessing' EA Modification Wanted](/thread/271525-blessing-ea-modification-wanted "Hello. 
 
here is a version of BLESSING \(old\) love this version. 
I wonder if someone could if possible to change this code. 
 
I like that...") 3 replies

[Single, Few Pair Traders (1-4) vs. MultiPair Traders (8-20)](/thread/964171-single-few-pair-traders-1-4-vs-multipair-traders "Who gets better results ?? 
  
Put it in another way , if you went for a trading competition and want to achieve &gt;300% ~ 2000% , what would...") 0 replies

[Coding Request for Multipair MTF ADR Dashboard](/thread/683340-coding-request-for-multipair-mtf-adr-dashboard "Can someone code this into indicator???") 2 replies

[trying to make a multipair buy and sell script](/thread/241746-trying-to-make-a-multipair-buy-and-sell "what i like to do is that i add a script on a chart and it will do 
 
open 3 pairs buys or sells. 
 
for example 0.1 lot EURUSD 
          ...") 6 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/973998-blessing-multipair-ea/reply#reply)
  * Subscribe
  * [97](javascript:void\(0\);)

Attachments: Blessing Multipair EA

Tags: Blessing Multipair EA

#  [](/thread/973998-blessing-multipair-ea)Blessing Multipair EA 

  * 

  * [#281](/thread/post/12733742#post12733742 "Post Permalink")

  * Feb 3, 2020 11:35am  Feb 3, 2020 11:35am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar3294_6.gif) JackJones](jackjones)

  * Joined Aug 2005 | Status: 888 | [1,021 Posts](/search?do=process&provider=Member&searchuser=3294)

> [Quoting hinseng](/thread/post/12733041#post12733041 "View Quoted Post")
> 
> Disliked
> 
> {quote} Next week, the movement of the GBP pair will need careful attention. But I still want to see the results of the transaction with the default settings.
> 
> Ignored

one or two on default allpairs are about to pass level five so watch for how it will try get out of it.. ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1) i've changed one demo to only panic at level 8 this week so will see what happens. 

grist for the mill

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#282](/thread/post/12734364#post12734364 "Post Permalink")

  * Feb 3, 2020 8:16pm  Feb 3, 2020 8:16pm 

  * [ hinseng](hinseng)

  * | Joined Oct 2019  | Status: Trader | [4 Posts](/search?do=process&provider=Member&searchuser=864896)

> [Quoting JackJones](/thread/post/12733742#post12733742 "View Quoted Post")
> 
> Disliked
> 
> {quote} one or two on default allpairs are about to pass level five so watch for how it will try get out of it.. ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1) i've changed one demo to only panic at level 8 this week so will see what happens.
> 
> Ignored

Hello Jack,  
Thank you for your suggestions.  
This morning, I added 200,000 yen again and passed one pair of level 5.  
And I thing if the amount of this EA does not exceed 500,000 yen, there is a risk.  
But I will continue to test with my real account,  
and I will report the results again on this weekend. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#283](/thread/post/12735078#post12735078 "Post Permalink")

  * Edited 2:41am  Feb 4, 2020 1:05am | Edited 2:41am 

  * [ kzean](kzean)

  * | Joined Aug 2014  | Status: Trader | [17 Posts](/search?do=process&provider=Member&searchuser=380085)

Hi, [ ursinho4711](https://www.forexfactory.com/ursinho4711)  
  
EA (BlessingLite_3_v3.9.6.34_gamma) was installed on two demo MT4 of different brokers, but it is not executing trades on one MT4 and the following message is reflecting on the chart window.  
"Wait for the next tick".  
  
MT4 Journal Message:  
2020.02.03 21:33:40.669 BlessingLite_3_v3.9.6.34_gamma XAUUSD.p,M5: No MarketInfo for XAUUSD0.00000000  
  
Set File: [BlessingV24beta-XUSUSDTest.set.txt](https://www.forexfactory.com/attachment.php/3527008?attachmentid=3527008&d=1578802208)  
  
What might be the cause? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#284](/thread/post/12735527#post12735527 "Post Permalink")

  * Feb 4, 2020 6:24am  Feb 4, 2020 6:24am 

  * [ fxtrue](fxtrue)

  * | Joined May 2019  | Status: Trader | [46 Posts](/search?do=process&provider=Member&searchuser=801801)

> [Quoting kzean](/thread/post/12735078#post12735078 "View Quoted Post")
> 
> Disliked
> 
> Hi, [ ursinho4711](https://www.forexfactory.com/ursinho4711) EA (BlessingLite_3_v3.9.6.34_gamma) was installed on two demo MT4 of different brokers, but it is not executing trades on one MT4 and the following message is reflecting on the chart window. "Wait for the next tick". MT4 Journal Message: 2020.02.03 21:33:40.669 BlessingLite_3_v3.9.6.34_gamma XAUUSD.p,M5: No MarketInfo for XAUUSD0.00000000 Set File: [BlessingV24beta-XUSUSDTest.set.txt](https://www.forexfactory.com/attachment.php/3527008?attachmentid=3527008&d=1578802208)...
> 
> Ignored

I'm guessing that Gold is closed - it has different market hours from standard currency pairs. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#285](/thread/post/12735539#post12735539 "Post Permalink")

  * Feb 4, 2020 6:30am  Feb 4, 2020 6:30am 

  * [ fxtrue](fxtrue)

  * | Joined May 2019  | Status: Trader | [46 Posts](/search?do=process&provider=Member&searchuser=801801)

@ursinho ...if you can remember to post the latest mq4 file regularly then I'll try to keep up with you and provide MT5 versions ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#286](/thread/post/12735785#post12735785 "Post Permalink")

  * Feb 4, 2020 11:23am  Feb 4, 2020 11:23am 

  * [ richard96816](richard96816)

  * Joined Dec 2018 | Status: Trader | [564 Posts](/search?do=process&provider=Member&searchuser=741833)

> [Quoting fxtrue](/thread/post/12735539#post12735539 "View Quoted Post")
> 
> Disliked
> 
> @ursinho ...if you can remember to post the latest mq4 file regularly then I'll try to keep up with you and provide MT5 versions ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)
> 
> Ignored

mq5? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#287](/thread/post/12736745#post12736745 "Post Permalink")

  * Feb 4, 2020 9:34pm  Feb 4, 2020 9:34pm 

  * [ fxtrue](fxtrue)

  * | Joined May 2019  | Status: Trader | [46 Posts](/search?do=process&provider=Member&searchuser=801801)

> [Quoting richard96816](/thread/post/12735785#post12735785 "View Quoted Post")
> 
> Disliked
> 
> {quote} mq5?
> 
> Ignored

sadly not - ex5 only 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#288](/thread/post/12736891#post12736891 "Post Permalink")

  * Edited Feb 5, 2020 2:21am  Feb 4, 2020 10:47pm | Edited Feb 5, 2020 2:21am 

  * [ kzean](kzean)

  * | Joined Aug 2014  | Status: Trader | [17 Posts](/search?do=process&provider=Member&searchuser=380085)

Hi, [ursinho4711](https://www.forexfactory.com/ursinho4711)  
  
Could u pls provide mq4 file for BlessingLite_3_v3.9.6.34_gamma. I did not find it on the thread. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#289](/thread/post/12737727#post12737727 "Post Permalink")

  * Feb 5, 2020 6:01am  Feb 5, 2020 6:01am 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

> [Quoting fxtrue](/thread/post/12736745#post12736745 "View Quoted Post")
> 
> Disliked
> 
> {quote} sadly not - ex5 only
> 
> Ignored

I started it. Funny that the "easy things" take longer time: string functions for example. Many functions moved from return variables to parameter change via pointers (sorry for my C language...). Very annoying in nested code ("see how cool I can put everything in one line") 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#290](/thread/post/12737738#post12737738 "Post Permalink")

  * Feb 5, 2020 6:13am  Feb 5, 2020 6:13am 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

> [Quoting kzean](/thread/post/12736891#post12736891 "View Quoted Post")
> 
> Disliked
> 
> Hi, [ursinho4711](https://www.forexfactory.com/ursinho4711) Could u pls provide mq4 file for BlessingLite_3_v3.9.6.34_gamma. I did not find it on the thread.
> 
> Ignored

Hi!  
  
To be honest I did not put the mql4 file and only the ex4 in post #1 because I was kind of hmmm sad? Only three friends helped to take a look at the code. So I thought: %§#* leechers...  
I am in a good mood today, though everything is in red ;-) I will put it on post #1 again... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#291](/thread/post/12737859#post12737859 "Post Permalink")

  * Feb 5, 2020 8:01am  Feb 5, 2020 8:01am 

  * [ ultax](ultax)

  * | Joined Oct 2019  | Status: Trader | [85 Posts](/search?do=process&provider=Member&searchuser=872453)

> [Quoting ursinho4711](/thread/post/12731206#post12731206 "View Quoted Post")
> 
> Disliked
> 
> {quote} What about you? Will you volunteer to do so? Btw: I stayed up almost all night to learn about the differences mt4<->mt5
> 
> Ignored

I would like to, but I have zero and I mean zero code knowledge. I can contribute in terms of backtesting or forward testing if one would like.  
  
Seem strange someone would release multi currency EA and not for MT5 where you could backtest. I know useless in most case, but could at least see how it all interacts. Forward test is best I agree. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#292](/thread/post/12737964#post12737964 "Post Permalink")

  * Feb 5, 2020 10:39am  Feb 5, 2020 10:39am 

  * [ rexscrat](rexscrat)

  * | Membership Revoked  | Joined Nov 2019 | [13 Posts](/search?do=process&provider=Member&searchuser=878949)

This EA is making good results so far and I started this EA last night . The drawdown observed is low as of now. I am unable to do backrest as it creates trades on multiple pairs. Iam running it on demo account for forward test. I liked the concept.  
  
Attached the results of my account 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot_20200205-093615.jpg
Size: 390 KB](/attachment/image/3546140/thumbnail?d=1580866785)](/attachment/image/3546140?d=1580866785)   

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#293](/thread/post/12737968#post12737968 "Post Permalink")

  * Feb 5, 2020 10:42am  Feb 5, 2020 10:42am 

  * [ rexscrat](rexscrat)

  * | Membership Revoked  | Joined Nov 2019 | [13 Posts](/search?do=process&provider=Member&searchuser=878949)

> [Quoting kzean](/thread/post/12735078#post12735078 "View Quoted Post")
> 
> Disliked
> 
> Hi, [ ursinho4711](https://www.forexfactory.com/ursinho4711) EA (BlessingLite_3_v3.9.6.34_gamma) was installed on two demo MT4 of different brokers, but it is not executing trades on one MT4 and the following message is reflecting on the chart window. "Wait for the next tick". MT4 Journal Message: 2020.02.03 21:33:40.669 BlessingLite_3_v3.9.6.34_gamma XAUUSD.p,M5: No MarketInfo for XAUUSD0.00000000 Set File: [BlessingV24beta-XUSUSDTest.set.txt](https://www.forexfactory.com/attachment.php/3527008?attachmentid=3527008&d=1578802208)...
> 
> Ignored

  
Wait for the next tick message is showing until anew candle is being formed. I am testing it in demo initially in 15 mins tf. Even I was able to see the message. I have switched to m1 tf. As new candle is formed, the message was changed to running.later I switched back to m15. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#294](/thread/post/12738749#post12738749 "Post Permalink")

  * Feb 5, 2020 7:30pm  Feb 5, 2020 7:30pm 

  * [ Bcapital](bcapital)

  * | Joined Feb 2020  | Status: Trader | [2 Posts](/search?do=process&provider=Member&searchuser=914124)

> [Quoting cescof](/thread/post/12698792#post12698792 "View Quoted Post")
> 
> Disliked
> 
> {quote} Thanks for new 3dand new blessing multipairs... So if i understood the result above are backtested using the 5min set file from other 3d right? What about set file you posted xususd... ? And how many max pairs do you seggests to use to avoid broker limits? Thanks Regards
> 
> Ignored

..thanks dorbthe 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#295](/thread/post/12738758#post12738758 "Post Permalink")

  * Feb 5, 2020 7:33pm  Feb 5, 2020 7:33pm 

  * [ Bcapital](bcapital)

  * | Joined Feb 2020  | Status: Trader | [2 Posts](/search?do=process&provider=Member&searchuser=914124)

> [Quoting cescof](/thread/post/12698792#post12698792 "View Quoted Post")
> 
> Disliked
> 
> {quote} Thanks for new 3dand new blessing multipairs... So if i understood the result above are backtested using the 5min set file from other 3d right? What about set file you posted xususd... ? And how many max pairs do you seggests to use to avoid broker limits? Thanks Regards
> 
> Ignored

..thanks fo the EA how come it opens buy stops and sell stops for pairs that are not on the charts 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#296](/thread/post/12738913#post12738913 "Post Permalink")

  * Edited Feb 6, 2020 2:05am  Feb 5, 2020 8:43pm | Edited Feb 6, 2020 2:05am 

  * [ hualiuc](hualiuc)

  * | Joined Jun 2014  | Status: Trader | [3 Posts](/search?do=process&provider=Member&searchuser=375226)

why BlessingLite_3_v3.9.6.34_gamma  
  
Why does this happen after the BlessingLite_3_v3.9.6.34_gamma is load  
  
  
  
BlessingLite_3_v3.9.6.30_gamma No such situation  
  
thank you   
  
  
The problem has been solved because when setting up multiple foreign exchange pairs, I changed it to 23 pairs instead of 28 pairs. This problem arises 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: _20200205193715.png
Size: 55 KB](/attachment/image/3546545/thumbnail?d=1580903011)](/attachment/image/3546545?d=1580903011)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#297](/thread/post/12738924#post12738924 "Post Permalink")

  * Feb 5, 2020 8:47pm  Feb 5, 2020 8:47pm 

  * [ rexscrat](rexscrat)

  * | Membership Revoked  | Joined Nov 2019 | [13 Posts](/search?do=process&provider=Member&searchuser=878949)

> [Quoting hualiuc](/thread/post/12738913#post12738913 "View Quoted Post")
> 
> Disliked
> 
> why BlessingLite_3_v3.9.6.34_gamma Why does this happen after the BlessingLite_3_v3.9.6.34_gamma is load BlessingLite_3_v3.9.6.30_gamma No such situation {image}
> 
> Ignored

Are you trying to do backtest?? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#298](/thread/post/12739014#post12739014 "Post Permalink")

  * Feb 5, 2020 9:33pm  Feb 5, 2020 9:33pm 

  * [ richard96816](richard96816)

  * Joined Dec 2018 | Status: Trader | [564 Posts](/search?do=process&provider=Member&searchuser=741833)

> [Quoting fxtrue](/thread/post/12736745#post12736745 "View Quoted Post")
> 
> Disliked
> 
> {quote} sadly not - ex5 only
> 
> Ignored

Why? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#299](/thread/post/12739094#post12739094 "Post Permalink")

  * Feb 5, 2020 10:27pm  Feb 5, 2020 10:27pm 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

At the moment I have nice results on a H4 time frame with following strategy: 3 pairs that "hedge each others" (EURGBP,GBPJPY,EURJPY).  
Autogrid, Profit-Trailing and maybe more important: trailing stop loss. Avoids deep DD.  
Will let it run until Friday and then analyze...  
  
_**@all (almost)**_  
_**the EA is working. If you have problems, especially with the tester, it is YOUR setup and the problem might lie inbetween your ears.**_  
_**Please do not use this thread for basic MT4 questions. Use the help function, read books, search the forum...**_

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#300](/thread/post/12739670#post12739670 "Post Permalink")

  * Feb 6, 2020 2:32am  Feb 6, 2020 2:32am 

  * [ hualiuc](hualiuc)

  * | Joined Jun 2014  | Status: Trader | [3 Posts](/search?do=process&provider=Member&searchuser=375226)

For multiple foreign exchange pairs, I'd like to make a suggestion, because the system adopts Martin method to add warehouse, but using this idea, when EA has a foreign exchange pair entering more than two layers of adding orders, if the system is always unilateral, it will be very dangerous. You can use other foreign exchange pairs to solve the foreign exchange loss pair that has already made profits, and even out the profit and loss sheets, the rest are profitable If the foreign exchange pair is running in the system, then there will be no dangerous situation in the EA system. I don't know if I can. The attachment is the reference system. Thank you  
  
sorry My English is so poor  
  
  
void CheckOverlapping()  
{  
//BUY--->  
TotalBuyOrders = CountOfOrders(MagicNumberBuy);  
if (TotalBuyOrders >= 2)   
{  
Lpos = 0; Cpos = 0; Lprofit = 0; Cprofit = 0;  
Lpos = LidingProfitOrder(MagicNumberBuy);  
Cpos = CloseProfitOrder(MagicNumberBuy);  
  
if(Lprofit > 0 && Lprofit1 <= 0)  
{  
if(Lprofit + Cprofit > 0 && (Lprofit + Cprofit)*100/Lprofit > ProfitPersent)   
{  
Lpos1 = 0;  
CloseSelectOrder(MagicNumberBuy);   
}  
}  
else if(Lprofit > 0 && Lprofit1 > 0)  
{  
if(Lprofit + Lprofit1 + Cprofit > 0 && (Lprofit + Lprofit1 + Cprofit)*100/(Lprofit + Lprofit1) > SecondProfitPersent) CloseSelectOrder(MagicNumberBuy);   
}  
}   
//<\---BUY  
//SELL--->  
TotalSellOrders = CountOfOrders(MagicNumberSell);  
if (TotalSellOrders >= 2)   
{  
Lpos = 0; Cpos = 0; Lprofit = 0; Cprofit = 0;  
Lpos = LidingProfitOrder(MagicNumberSell);  
Cpos = CloseProfitOrder(MagicNumberSell);  
  
if(Lprofit > 0 && Lprofit1 <= 0)  
{  
if(Lprofit + Cprofit > 0 && (Lprofit + Cprofit)*100/Lprofit > ProfitPersent)   
{  
Lpos1 = 0;  
CloseSelectOrder(MagicNumberSell);   
}  
}   
if(Lprofit > 0 && Lprofit1 > 0)  
{  
if(Lprofit + Lprofit1 + Cprofit > 0 && (Lprofit + Lprofit1 + Cprofit)*100/(Lprofit + Lprofit1) > SecondProfitPersent) CloseSelectOrder(MagicNumberSell);   
}  
}   
//<\---SELL  
} 

Attached File(s)

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [OM_2WAY_v3.6c_EN.mq4](/attachment/file/3546834?d=1580923927) 34 KB | 529 downloads 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Blessing Multipair EA
  *   * [ **Reply to Thread** ](/thread/973998-blessing-multipair-ea/reply#reply)

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

[Trading multipair triangles, no stoploss](/thread/917648-trading-multipair-triangles-no-stoploss "Hello forex Folks! 
  
I'd like to share with You my system that I was comming to for many years. I am testing it these days and it gives...") 78 replies

['Blessing' EA Modification Wanted](/thread/271525-blessing-ea-modification-wanted "Hello. 
 
here is a version of BLESSING \(old\) love this version. 
I wonder if someone could if possible to change this code. 
 
I like that...") 3 replies

[Single, Few Pair Traders (1-4) vs. MultiPair Traders (8-20)](/thread/964171-single-few-pair-traders-1-4-vs-multipair-traders "Who gets better results ?? 
  
Put it in another way , if you went for a trading competition and want to achieve &gt;300% ~ 2000% , what would...") 0 replies

[Coding Request for Multipair MTF ADR Dashboard](/thread/683340-coding-request-for-multipair-mtf-adr-dashboard "Can someone code this into indicator???") 2 replies

[trying to make a multipair buy and sell script](/thread/241746-trying-to-make-a-multipair-buy-and-sell "what i like to do is that i add a script on a chart and it will do 
 
open 3 pairs buys or sells. 
 
for example 0.1 lot EURUSD 
          ...") 6 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/973998-blessing-multipair-ea/reply#reply)
  * Subscribe
  * [97](javascript:void\(0\);)

Attachments: Blessing Multipair EA

Tags: Blessing Multipair EA

#  [](/thread/973998-blessing-multipair-ea)Blessing Multipair EA 

  * 

  * [#301](/thread/post/12739936#post12739936 "Post Permalink")

  * Feb 6, 2020 6:04am  Feb 6, 2020 6:04am 

  * [ richard96816](richard96816)

  * Joined Dec 2018 | Status: Trader | [564 Posts](/search?do=process&provider=Member&searchuser=741833)

> [Quoting ursinho4711](/thread/post/12739094#post12739094 "View Quoted Post")
> 
> Disliked
> 
> At the moment I have nice results on a H4 time frame with following strategy: 3 pairs that "hedge each others" (EURGBP,GBPJPY,EURJPY). Autogrid, Profit-Trailing and maybe more important: trailing stop loss. Avoids deep DD. Will let it run until Friday and then analyze...
> 
> Ignored

Good to see you going up the timeframe scale. H4 is usually the most profitable with multi-pairs using the same, relatively simple setups.  
  
What do you mean by 'hedge each other'? Are you actually hedging them in some way? (I doubt it.) If not they're actually increasing risk exposure.  
  
Deep DD is a double edged sword. It's good to control, but systems with greater drawdown often make more money. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#302](/thread/post/12739949#post12739949 "Post Permalink")

  * Feb 6, 2020 6:10am  Feb 6, 2020 6:10am 

  * [ richard96816](richard96816)

  * Joined Dec 2018 | Status: Trader | [564 Posts](/search?do=process&provider=Member&searchuser=741833)

> [Quoting fxtrue](/thread/post/12736745#post12736745 "View Quoted Post")
> 
> Disliked
> 
> {quote} sadly not - ex5 only
> 
> Ignored

Why not.  
  
The reason you have code to use at all is because of Blessing's long tradition of open source.  
  
You have something else, possibly nefarious, in mind? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#303](/thread/post/12740020#post12740020 "Post Permalink")

  * Edited 7:13am  Feb 6, 2020 7:01am | Edited 7:13am 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

> [Quoting richard96816](/thread/post/12739936#post12739936 "View Quoted Post")
> 
> Disliked
> 
> What do you mean by 'hedge each other'? Are you actually hedging them in some way? (I doubt it.) If not they're actually increasing risk exposure.
> 
> Ignored

No, that is why I put it in "". Maybe the "circle secure" fits better? The setup I made, at least it is my idea, is to let the wins run and to bury the dead horses early.  
I know that Blessing can handle DDs very well. But as I am already using the London Close EA also on another account, that is enough emotional tension for me.  
Need something more slow and calm... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#304](/thread/post/12740100#post12740100 "Post Permalink")

  * Feb 6, 2020 8:02am  Feb 6, 2020 8:02am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar86801_11.gif) emmanuel7788](emmanuel7788)

  * Joined Nov 2008 | Status: Trader | [47,707 Posts](/search?do=process&provider=Member&searchuser=86801)

> [Quoting richard96816](/thread/post/12739949#post12739949 "View Quoted Post")
> 
> Disliked
> 
> {quote} Why not. The reason you have code to use at all is because of Blessing's long tradition of open source. You have something else, possibly nefarious, in mind?
> 
> Ignored

  
Blessing3 is open source.  
  
however BlessingPro is not and become a commercial product by jtatoday.  
  
the newer versions like Evolution are all non-open source. 

Honesty is a very expensive gift. You wont find it in cheap people.WBuffett

[1 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#305](/thread/post/12740146#post12740146 "Post Permalink")

  * Feb 6, 2020 9:06am  Feb 6, 2020 9:06am 

  * [ richard96816](richard96816)

  * Joined Dec 2018 | Status: Trader | [564 Posts](/search?do=process&provider=Member&searchuser=741833)

> [Quoting emmanuel7788](/thread/post/12740100#post12740100 "View Quoted Post")
> 
> Disliked
> 
> {quote} Blessing3 is open source. however BlessingPro is not and become a commercial product by jtatoday. the newer versions like Evolution are all non-open source.
> 
> Ignored

These groups all exist because of the open source version of Blessing that a group of traders built starting years ago. JTA helped with coding of more recent versions and was allowed to offer for-pay versions. That mess is all gone now. And the open source remains. I and others are contributing to make it better. The newest versions of Blessing are open source.  
  
Non open source outgrowths are not appreciated. Not fair. Not right.  
  
We can't continue to build on each others work without source code. 

[0 ](javascript:void\(0\);) [3 ](javascript:void\(0\);)

  * [#306](/thread/post/12740169#post12740169 "Post Permalink")

  * Feb 6, 2020 9:36am  Feb 6, 2020 9:36am 

  * [ ezoin](ezoin)

  * | Additional Username  | Joined Feb 2020 | [1 Post](/search?do=process&provider=Member&searchuser=914524)

I see this EA is doing martingale. not sure how many levels. Any one tried it for long time? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#307](/thread/post/12743732#post12743732 "Post Permalink")

  * Feb 8, 2020 1:50am  Feb 8, 2020 1:50am 

  * [ Mcxtrader](mcxtrader)

  * | Joined Jun 2017  | Status: Trader | [203 Posts](/search?do=process&provider=Member&searchuser=589792)

One more thing noticed today. While closing the trades it is closing the trade with loss. Since enabled minimal loss, it is not considering the trades opened before one level. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot1.png
Size: 16 KB](/attachment/image/3548673/thumbnail?d=1581094170)](/attachment/image/3548673?d=1581094170)   

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#308](/thread/post/12743837#post12743837 "Post Permalink")

  * Feb 8, 2020 2:45am  Feb 8, 2020 2:45am 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

> [Quoting Mcxtrader](/thread/post/12743732#post12743732 "View Quoted Post")
> 
> Disliked
> 
> One more thing noticed today. While closing the trades it is closing the trade with loss. Since enabled minimal loss, it is not considering the trades opened before one level. {image}
> 
> Ignored

Would be good to know if this happens (with exactly the same setup and exactly the same entry date/time) on the "normal" blessing (version 3.9.6.09 to 3.9.6.13) as well.  
  
Can this be seen on backtest as well? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#309](/thread/post/12743911#post12743911 "Post Permalink")

  * Feb 8, 2020 3:40am  Feb 8, 2020 3:40am 

  * [ Mcxtrader](mcxtrader)

  * | Joined Jun 2017  | Status: Trader | [203 Posts](/search?do=process&provider=Member&searchuser=589792)

> [Quoting ursinho4711](/thread/post/12743837#post12743837 "View Quoted Post")
> 
> Disliked
> 
> {quote} Would be good to know if this happens (with exactly the same setup and exactly the same entry date/time) on the "normal" blessing (version 3.9.6.09 to 3.9.6.13) as well. Can this be seen on backtest as well?
> 
> Ignored

  
This is not seen in normal blessing. (version 3.9.6.09 to 3.9.6.13) Normal blessings works fine and handle this situation well. Right now am testing in Demo account. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#310](/thread/post/12743918#post12743918 "Post Permalink")

  * Edited 3:58am  Feb 8, 2020 3:45am | Edited 3:58am 

  * [ kzean](kzean)

  * | Joined Aug 2014  | Status: Trader | [17 Posts](/search?do=process&provider=Member&searchuser=380085)

Hi, ursinho4711  
  
BlessingV24beta-XUSUSDTest.set.tx  
BlessingLite_3_v3.9.6.34_gamma.ex  
  
EA is being tested on XAUUSD with 15m tf, but the alarming thing is that the EA keeps on selling in oversold and buying in overbought territories causing undue DD and loss. If Stochastic is enabled to determine Overbought and Oversold, then EA does not open trades. Pls advise to overcome the problem. Secondly, whats the best tf to trade XAUUSD? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#311](/thread/post/12743924#post12743924 "Post Permalink")

  * Feb 8, 2020 3:49am  Feb 8, 2020 3:49am 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

> [Quoting kzean](/thread/post/12743918#post12743918 "View Quoted Post")
> 
> Disliked
> 
> Hi, ursinho4711 BlessingV24beta-XUSUSDTest.set.tx BlessingLite_3_v3.9.6.34_gamma.ex EA is being tested on XAUUSD with 15m tf, but the alarming thing is that the EA keeps on trading in oversold and overbought territory causing undue DD and loss. If Stochastic is enabled to determine Overbought and Oversold, then EA does not open trades. Pls advise to overcome the problem. Secondly, whats the best tf to trade?
> 
> Ignored

THE question: does this happen with the "normal" Blessing as well? Then I do not have to look into the code rather you into your settings... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#312](/thread/post/12743928#post12743928 "Post Permalink")

  * Feb 8, 2020 3:53am  Feb 8, 2020 3:53am 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

> [Quoting Mcxtrader](/thread/post/12743911#post12743911 "View Quoted Post")
> 
> Disliked
> 
> {quote} This is not seen in normal blessing.
> 
> Ignored

Hm, not good. Then I have to dive into the code...  
Can you please send me the setup-file that you used when this happend? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#313](/thread/post/12743947#post12743947 "Post Permalink")

  * Feb 8, 2020 4:02am  Feb 8, 2020 4:02am 

  * [ kzean](kzean)

  * | Joined Aug 2014  | Status: Trader | [17 Posts](/search?do=process&provider=Member&searchuser=380085)

> [Quoting ursinho4711](/thread/post/12743928#post12743928 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hm, not good. Then I have to dive into the code... Can you please send me the setup-file that you used when this happend?
> 
> Ignored

BlessingV24beta-XUSUSDTest.set.tx 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#314](/thread/post/12743986#post12743986 "Post Permalink")

  * Feb 8, 2020 5:00am  Feb 8, 2020 5:00am 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

again...  
@all (almost)  
  
Remember: the "original" Blessing is open source and everyone can find out how it works. There are planty of threads, documentation, examples.  
The "multipair" version is "just" a stripped version of 3.9.6.13 that runs in a for-to loop over selected pairs.  
Also this mutlipair-version can be studied as source in post#1.  
I am doing this project

  1. to learn about blessing
  2. to find a way to use it over multi-pairs without deep testing of single pairs
  3. to brush up my coding skills
  4. because it is interesting

I am NOT a professional finance guy, just an engineer who studied digital signal processing. I have a real job in the real life and a real family.  
Please try to contribute and not see me as the service guy who has to solve (your?) problems.  
I was hoping on a discussion about the code and not just "something is not working".  
If there should be something that might obviously relate to the multipair migration, please provide as much information as possible. Every detail is important.  
Do you go to the doctor and say: "hm, today I am not feeling good. Tell me what it is" Or do you rather provide infos like "where it hurts, symptoms, since when, what happened..."  
This is an open project. Contribute, cooperate, collaborate.  
...or forever hold your peace... 

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#315](/thread/post/12744042#post12744042 "Post Permalink")

  * Feb 8, 2020 5:58am  Feb 8, 2020 5:58am 

  * [ richard96816](richard96816)

  * Joined Dec 2018 | Status: Trader | [564 Posts](/search?do=process&provider=Member&searchuser=741833)

> [Quoting ezoin](/thread/post/12740169#post12740169 "View Quoted Post")
> 
> Disliked
> 
> I see this EA is doing martingale. not sure how many levels. Any one tried it for long time?
> 
> Ignored

Blessing does not and can not do martingale. The manual is wrong and should never have used that term.  
  
Martingale is a stupid and completely discredited betting system from the 18th century. If you have an infinitely large account martingale will probably work for you. Otherwise, you will most likely lose all your money.  
  
Unlike martingale, Blessing can and does make money consistently if carefully applied. Blessing is a Grid system which means it usually makes lots of trades, the sizes and multiples of which are controllable. Blessing can even make single, non-grid trades successfully by setting the grid size to one. It's a very configurable system. But it **can not do martingale**.  
  
Someone needs to edit the Blessing manual and remove 'martingale' references from the text.  
  
[https://en.wikipedia.org/wiki/Martin...betting_system](https://en.wikipedia.org/wiki/Martingale_\(betting_system)) 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#316](/thread/post/12744050#post12744050 "Post Permalink")

  * Feb 8, 2020 6:10am  Feb 8, 2020 6:10am 

  * [ richard96816](richard96816)

  * Joined Dec 2018 | Status: Trader | [564 Posts](/search?do=process&provider=Member&searchuser=741833)

> [Quoting ursinho4711](/thread/post/12743986#post12743986 "View Quoted Post")
> 
> Disliked
> 
> again... Please try to contribute and not see me as the service guy who has to solve (your?) problems. ...
> 
> Ignored

Thanks for all you do. The concepts and execution are interesting and inspiring. Your efforts are most appreciated.  
  
Hopefully readers will see themselves as important contributors and invest a little time delving more deeply into problems and questions before posting. Experience and testing of the system can be as important as programming.  
  
Good luck! 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#317](/thread/post/12744060#post12744060 "Post Permalink")

  * Feb 8, 2020 6:24am  Feb 8, 2020 6:24am 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

> [Quoting richard96816](/thread/post/12744050#post12744050 "View Quoted Post")
> 
> Disliked
> 
> Experience and testing of the system can be as important as programming
> 
> Ignored

Thanks, Rich, for your encouraging words. Saved my (and my family's) weekend...  
  
To one of the above posts about basket closing in minus: I just did a backtest "old" and "multipair" with the same settings. And what can I say?  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Image1.png
Size: 50 KB](/attachment/image/3548814/thumbnail?d=1581110421)](/attachment/image/3548814?d=1581110421)   

  
  
Maybe, and this I cannot test until I have a good MT5 (source) program, it only happens when there is more than one pair? Wrong TP calculation for example... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#318](/thread/post/12744254#post12744254 "Post Permalink")

  * Feb 8, 2020 1:33pm  Feb 8, 2020 1:33pm 

  * [ Mcxtrader](mcxtrader)

  * | Joined Jun 2017  | Status: Trader | [203 Posts](/search?do=process&provider=Member&searchuser=589792)

> [Quoting ursinho4711](/thread/post/12743928#post12743928 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hm, not good. Then I have to dive into the code... Can you please send me the setup-file that you used when this happend?
> 
> Ignored

Thanks. It is the same set file which was shared in post1. 

Attached File(s)

![File Type: txt](https://assets.faireconomy.media/images/attach/txt.gif) [BlessingLiteV24-5Min-AllPairs.set.txt](/attachment/file/3548951?d=1581136373) 2 KB | 450 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#319](/thread/post/12744343#post12744343 "Post Permalink")

  * Feb 8, 2020 5:48pm  Feb 8, 2020 5:48pm 

  * [ hinseng](hinseng)

  * | Joined Oct 2019  | Status: Trader | [4 Posts](/search?do=process&provider=Member&searchuser=864896)

> [Quoting hinseng](/thread/post/12732373#post12732373 "View Quoted Post")
> 
> Disliked
> 
> Hello All! This is my first post. Attachments are the results I traded on a real account for one week. I started from 100,000 yen and added 200,000 from yesterday. All transactions are conducted with default settings. I think that it is a good EA, but starting trading at 100,000 yen is a risk. {image}
> 
> Ignored

This is the result of the second week.  
After adding the deposit up to 500,000 yen trading are well.  
The total profit for the two weeks was 12,479 yen.  
I will continue to test this EA. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Blessing34_gamma_week2.jpg
Size: 554 KB](/attachment/image/3548995/thumbnail?d=1581151691)](/attachment/image/3548995?d=1581151691)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#320](/thread/post/12744506#post12744506 "Post Permalink")

  * Feb 8, 2020 9:36pm  Feb 8, 2020 9:36pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar3294_6.gif) JackJones](jackjones)

  * Joined Aug 2005 | Status: 888 | [1,021 Posts](/search?do=process&provider=Member&searchuser=3294)

All pairs raw, filtered v1 - v3 survived another week. A-team kicked ass going well with no level 3 trades this week. Ill post more if I can but busy sipping iced teas by the pool n all ,) have a good one. 

grist for the mill

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Blessing Multipair EA
  *   * [ **Reply to Thread** ](/thread/973998-blessing-multipair-ea/reply#reply)

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

[Trading multipair triangles, no stoploss](/thread/917648-trading-multipair-triangles-no-stoploss "Hello forex Folks! 
  
I'd like to share with You my system that I was comming to for many years. I am testing it these days and it gives...") 78 replies

['Blessing' EA Modification Wanted](/thread/271525-blessing-ea-modification-wanted "Hello. 
 
here is a version of BLESSING \(old\) love this version. 
I wonder if someone could if possible to change this code. 
 
I like that...") 3 replies

[Single, Few Pair Traders (1-4) vs. MultiPair Traders (8-20)](/thread/964171-single-few-pair-traders-1-4-vs-multipair-traders "Who gets better results ?? 
  
Put it in another way , if you went for a trading competition and want to achieve &gt;300% ~ 2000% , what would...") 0 replies

[Coding Request for Multipair MTF ADR Dashboard](/thread/683340-coding-request-for-multipair-mtf-adr-dashboard "Can someone code this into indicator???") 2 replies

[trying to make a multipair buy and sell script](/thread/241746-trying-to-make-a-multipair-buy-and-sell "what i like to do is that i add a script on a chart and it will do 
 
open 3 pairs buys or sells. 
 
for example 0.1 lot EURUSD 
          ...") 6 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/973998-blessing-multipair-ea/reply#reply)
  * Subscribe
  * [97](javascript:void\(0\);)

Attachments: Blessing Multipair EA

Tags: Blessing Multipair EA

#  [](/thread/973998-blessing-multipair-ea)Blessing Multipair EA 

  * 

  * [#321](/thread/post/12744900#post12744900 "Post Permalink")

  * Feb 9, 2020 9:02am  Feb 9, 2020 9:02am 

  * [ fxtrue](fxtrue)

  * | Joined May 2019  | Status: Trader | [46 Posts](/search?do=process&provider=Member&searchuser=801801)

> [Quoting richard96816](/thread/post/12739949#post12739949 "View Quoted Post")
> 
> Disliked
> 
> {quote} Why not. The reason you have code to use at all is because of Blessing's long tradition of open source. You have something else, possibly nefarious, in mind?
> 
> Ignored

Why not?...  
1) because I have an MQL4->MQL5 converter, so the "source" is basically unchanged  
2) because the objective of the exercise was to help Ursinho spot errors much faster than he would have if relying on forward-testing  
  
The reason you have code to use at all is because of Blessing's long tradition of open source.  
\- that's great... but who are you to presume that I even use Blessing at all? (for the record, I don't)  
  
You have something else, possibly nefarious, in mind?  
\- sad to see you belittle yourself with that snide comment ![](https://resources.faireconomy.media/images/emojis/64/1f641.png?v=15.1)

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#322](/thread/post/12744909#post12744909 "Post Permalink")

  * Feb 9, 2020 9:54am  Feb 9, 2020 9:54am 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

> [Quoting fxtrue](/thread/post/12744900#post12744900 "View Quoted Post")
> 
> Disliked
> 
> 1) because I have an MQL4->MQL5 converter, so the "source" is basically unchanged 2) because the objective of the exercise was to help Ursinho spot errors much faster than he would have if relying on forward-testing
> 
> Ignored

1) already thought so ;-)  
2) really appreciate it, thanks alot  
  
And more of all I would be happy if we could focus on the code and settings. Battles are wasted time and energy. 

[0 ](javascript:void\(0\);) [3 ](javascript:void\(0\);)

  * [#323](/thread/post/12745279#post12745279 "Post Permalink")

  * Feb 10, 2020 12:39am  Feb 10, 2020 12:39am 

  * [ fxtrue](fxtrue)

  * | Joined May 2019  | Status: Trader | [46 Posts](/search?do=process&provider=Member&searchuser=801801)

I'm attaching my edited source code version of "gamma" (for MT4) plus a compiled MT5 version.  
  
Please note that the following:  
  
1) there are almost 40 edits / fixes in this version - several of which are critical (they can be located by searching for "fxtrue")  
  
2) I would appreciate my changes being carried through to all new versions of BlessingLite - particularly as many are needed for the MT5 version and I don't have time to waste re-implementing the same fixes over and over  
  
3) there is a potentially-serious underlying issue with incorrectly initialised variables (they intermittently equate to EMPTY_VALUE and result in erroneous values further down the computational chain - sometimes causing 'divide by zero' critical errors) - I have applied fixes to the places I have identified, but the code would benefit greatly from someone trawling through it and finding the root causes  
  
4) the edited source code compiles happily in MT4 and *appears* to run happily in MT5... but I promise nothing, so use entirely at your own risk  
  
So, have fun and report any oddities you discover ![](https://resources.faireconomy.media/images/emojis/64/1f913.png?v=15.1)

Attached File(s)

![File Type: ex5](https://assets.faireconomy.media/images/attach/ex5.gif) [BlessingLite_3_v3.9.6.34_gamma_fxtrue.ex5](/attachment/file/3549492?d=1581262762) 788 KB | 987 downloads 

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [BlessingLite_3_v3.9.6.34_gamma_fxtrue.mq4](/attachment/file/3549494?d=1581262762) 134 KB | 1,322 downloads 

[0 ](javascript:void\(0\);) [9 ](javascript:void\(0\);)

  * [#324](/thread/post/12745353#post12745353 "Post Permalink")

  * Feb 10, 2020 2:02am  Feb 10, 2020 2:02am 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

First of all: thanks again for your help, fxtrue! That's the cooperation I was hoping for. Thumbs up and many pips for you!  
  

> [Quoting fxtrue](/thread/post/12745279#post12745279 "View Quoted Post")
> 
> Disliked
> 
> 3) there is a potentially-serious underlying issue with incorrectly initialised variables (they intermittently equate to EMPTY_VALUE and result in erroneous values further down the computational chain - sometimes causing 'divide by zero' critical errors) - I have applied fixes to the places I have identified, but the code would benefit greatly from someone trawling through it and finding the root causes
> 
> Ignored

This is an issue in the "original blessings" already. I was really surprised when I did the transmission to the multi-pair and went through the code.  
No secure against divide by zero. Variables declared, never got initial values (even if it is a zero) yet used.  
I thought -as the program was open such a long time and was coded by professionals- that this would not appear in a ...09 version anymore.  
  
This weekend I was playing with setfiles of the "original blessing" and you cannot believe how often the EA crashed because of zero divides. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#325](/thread/post/12745607#post12745607 "Post Permalink")

  * Feb 10, 2020 7:42am  Feb 10, 2020 7:42am 

  * [ richard96816](richard96816)

  * Joined Dec 2018 | Status: Trader | [564 Posts](/search?do=process&provider=Member&searchuser=741833)

> [Quoting ursinho4711](/thread/post/12745353#post12745353 "View Quoted Post")
> 
> Disliked
> 
> ... This is an issue in the "original blessings" already. I was really surprised when I did the transmission to the multi-pair and went through the code. No secure against divide by zero. Variables declared, never got initial values (even if it is a zero) yet used. I thought -as the program was open such a long time and was coded by professionals- that this would not appear in a ...09 version anymore. This weekend I was playing with setfiles of the "original blessing" and you cannot believe how often the EA crashed because of zero divides.
> 
> Ignored

I'm not sure about that 'coded by professionals' claim. Version .09 has been around quite a long time. It works surprisingly well when it works. I think there's been a realization by many that it needs to be rewritten. But that's a big job, given the poor debugging tools available and many other factors. I think most folks tend to respect the code and try to make as few changes as possible. That's a common approach taken by 'professionals' when fixing bugs or making small changes on someone else's code.  
  
Code produced by groups is problematic, especially without coherent rules.  
  
Blessing still needs a complete rewrite. I'm too busy using it. That may change. If you see errors that can be easily fixed please point them out when it's convenient. I am admittedly more a user than a writer on this project and my time is sometimes limited.  
  
Thanks. 

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#326](/thread/post/12745880#post12745880 "Post Permalink")

  * Feb 10, 2020 1:38pm  Feb 10, 2020 1:38pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar709398_3.gif) muggle](muggle)

  * | Joined Aug 2018  | Status: Trader | [31 Posts](/search?do=process&provider=Member&searchuser=709398)

> [Quoting fxtrue](/thread/post/12745279#post12745279 "View Quoted Post")
> 
> Disliked
> 
> I'm attaching my edited source code version of "gamma" (for MT4) plus a compiled MT5 version. Please note that the following: 1) there are almost 40 edits / fixes in this version - several of which are critical (they can be located by searching for "fxtrue") 2) I would appreciate my changes being carried through to all new versions of BlessingLite - particularly as many are needed for the MT5 version and I don't have time to waste re-implementing the same fixes over and over 3) there is a potentially-serious underlying issue with incorrectly initialised...
> 
> Ignored

Hi,fxtrue  
I would like to try optimize the setting value  
for MT5 version BlessingLite_3_v3.9.6.34_gamma_fxtrue.ex5  
Could you please help to modify a little for me can testing?  
all indicator has an option on the setting value, MA, CCI, Bollinger bands, stochastic, MACD  
Can possible add setting with all value of indicators more like time frame and shift value   
and all code Period() or _Period change it to ENUM input for select on setting (dropdown like on smart grid setting)  
if you can help to modify a little testing optimize version will be great, I can try to optimize the best value for everyone.  
Thank you 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#327](/thread/post/12746509#post12746509 "Post Permalink")

  * Feb 10, 2020 10:34pm  Feb 10, 2020 10:34pm 

  * [ fxtrue](fxtrue)

  * | Joined May 2019  | Status: Trader | [46 Posts](/search?do=process&provider=Member&searchuser=801801)

> [Quoting muggle](/thread/post/12745880#post12745880 "View Quoted Post")
> 
> Disliked
> 
> {quote} Could you please help to modify a little for me can testing?
> 
> Ignored

I'm sorry, but I have to decline - the last thing I want to do is create yet another fork of Blessing, but I'm happy to create MT5 versions of whatever Ursinho releases. 

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#328](/thread/post/12748072#post12748072 "Post Permalink")

  * Feb 11, 2020 7:08pm  Feb 11, 2020 7:08pm 

  * [ fxtrue](fxtrue)

  * | Joined May 2019  | Status: Trader | [46 Posts](/search?do=process&provider=Member&searchuser=801801)

> [Quoting ursinho4711](/thread/post/12745353#post12745353 "View Quoted Post")
> 
> Disliked
> 
> I was really surprised when I did the transmission to the multi-pair and went through the code. No secure against divide by zero. Variables declared, never got initial values (even if it is a zero) yet used.
> 
> Ignored

The core issue is that Blessing was originally coded by "enthusiastic amateurs" prior to build 600 of MT4 (when "strict" came into being) and those earlier versions of MQL4 were very tolerant of sloppy coding, so variables would be automatically initialised if the coder forgot to do it, and variable types were not enforced. This meant that double types were often used in place of integer parameters and integers were used for dates and/or booleans, so calculations that should have returned "int" values might have unplanned decimal portions, "decimal" results may have been unwittingly truncated, etc. ....fun times ![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#329](/thread/post/12748947#post12748947 "Post Permalink")

  * Feb 12, 2020 3:18am  Feb 12, 2020 3:18am 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

> [Quoting fxtrue](/thread/post/12748072#post12748072 "View Quoted Post")
> 
> Disliked
> 
> ....fun times
> 
> Ignored

I already learned more than thirty years ago not to do things like that. But these times were also fun (more than today) ![](https://resources.faireconomy.media/images/emojis/64/1f37a.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#330](/thread/post/12751729#post12751729 "Post Permalink")

  * Edited 3:45pm  Feb 13, 2020 11:20am | Edited 3:45pm 

  * [ Dowde](dowde)

  * | Joined Feb 2020  | Status: Trader | [4 Posts](/search?do=process&provider=Member&searchuser=916801)

Thank you Mike McKeough, the Blessing Development Group, ursinho4711 and fxtrue (and everyone) for the work you've put into this. I've been testing it live for the second day now... interesting. I basically used your set file settings ursinho4711, with some exceptions (nano account). I'll attempt to keep you posted with results and any potential suggestions. I've never done any coding (unless you count a year back in 7th grade, in which I really don't remember a thing), or even really even looked into a code. The last two days, however, I actually took the moment to open up this EA, and take a look at it's guts. It's very interesting how it's all laid out and is seemingly in "layers." It shows how much time was really put into this. ![](https://resources.faireconomy.media/images/emojis/64/1f44c.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/261d-fe0f.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#331](/thread/post/12751751#post12751751 "Post Permalink")

  * Feb 13, 2020 11:46am  Feb 13, 2020 11:46am 

  * [ mercilez](mercilez)

  * | Joined Jun 2015  | Status: Trader | [84 Posts](/search?do=process&provider=Member&searchuser=415096)

> [Quoting ursinho4711](/thread/post/12698762#post12698762 "View Quoted Post")
> 
> Disliked
> 
> Remember that post? [https://www.forexfactory.com/showthr...7#post12551567](https://www.forexfactory.com/showthread.php?p=12551567#post12551567) Well, I used the settings and made a backtest from 01.Nov.2019 to 10.Jan.2020. 5 Minutes timeframe, for all 28 pairs. What can I say: that already looks like the winner to be tested on the Blessing-Multipair. Can't wait for Sidney open... Here are the results: {image}
> 
> Ignored

hi ursinho, account size did this test perform on? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#332](/thread/post/12752016#post12752016 "Post Permalink")

  * Feb 13, 2020 4:00pm  Feb 13, 2020 4:00pm 

  * [ Dowde](dowde)

  * | Joined Feb 2020  | Status: Trader | [4 Posts](/search?do=process&provider=Member&searchuser=916801)

As a cautionary heads up (I'm not quite sure what happened, yet), I had the settings set for 10 trades at once. I went away and came back to my computer to see more than 20 active trades. I then went into the properties and changed the setting to ***NO NEW TRADES***, turned it to True, and after hitting ok, it immediately Closed ALL the trades. It was not ***CLOSE ALL NOW***, but no new trades. So, not sure what happened there. After reloading chart with EA and getting 25 more trades, I had to just turn all entries to disable to stop more trades. I didn't even think there could be more than 15 at once. Hmm... Will do more testing. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#333](/thread/post/12753442#post12753442 "Post Permalink")

  * Feb 14, 2020 1:13am  Feb 14, 2020 1:13am 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

> [Quoting Dowde](/thread/post/12752016#post12752016 "View Quoted Post")
> 
> Disliked
> 
> As a cautionary heads up (I'm not quite sure what happened, yet), I had the settings set for 10 trades at once. I went away and came back to my computer to see more than 20 active trades. I then went into the properties and changed the setting to ***NO NEW TRADES***, turned it to True, and after hitting ok, it immediately Closed ALL the trades. It was not ***CLOSE ALL NOW***, but no new trades. So, not sure what happened there. After reloading chart with EA and getting 25 more trades, I had to just turn all entries to disable to stop more trades....
> 
> Ignored

Hi Dowde, thanks for the feedback!  
  
Number of trades is still from the "old" blessing and relates to one pair, not all pairs of the list. So if you have list of 28 pairs there could be 280 trades.  
We should install a new parameter "pairs at once".  
"No new trades" should not close all, just not allow new trades (as the name sais). That's a bug, thanks for reporting it. At the moment, this is what I also do, is to set all entries to disable, as you did correctly... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#334](/thread/post/12754162#post12754162 "Post Permalink")

  * Feb 14, 2020 11:39am  Feb 14, 2020 11:39am 

  * [ richard96816](richard96816)

  * Joined Dec 2018 | Status: Trader | [564 Posts](/search?do=process&provider=Member&searchuser=741833)

> [Quoting ursinho4711](/thread/post/12753442#post12753442 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi Dowde, thanks for the feedback! Number of trades is still from the "old" blessing and relates to one pair, not all pairs of the list. So if you have list of 28 pairs there could be 280 trades. We should install a new parameter "pairs at once". "No new trades" should not close all, just not allow new trades (as the name sais). That's a bug, thanks for reporting it. At the moment, this is what I also do, is to set all entries to disable, as you did correctly...
> 
> Ignored

The **NO NEW TRADES** entry controls the **ShutDown** variable.  
  
To be precise, it stops allowing trades once the basket is closed and the number of open trades drops to zero.  
  
The intent is to allow the current basket, if any, to run to completion.  
  
There are all kinds of ways of controlling your level of trading and the impact on your account. None of them is really perfect for all situations. (Other than simply keeping a surplus of extra cash in your account! Which is a very good idea.)  
  
**MinMarginPercent** may be helpful. There are various other controls that could be added. Some multi-pair EAs provide quite a list of selections. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#335](/thread/post/12755440#post12755440 "Post Permalink")

  * Feb 15, 2020 12:23am  Feb 15, 2020 12:23am 

  * [ farmabioq](farmabioq)

  * | Commercial User  | Joined Dec 2014 | [55 Posts](/search?do=process&provider=Member&searchuser=394496)

Hello. You can publish the template, the best template that is working, and the optimal time frame to place the Ea. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#336](/thread/post/12760457#post12760457 "Post Permalink")

  * Feb 18, 2020 8:47pm  Feb 18, 2020 8:47pm 

  * [ Kirk65](kirk65)

  * | Joined Dec 2019  | Status: Trader | [31 Posts](/search?do=process&provider=Member&searchuser=892378)

[quote=ursinho4711;12744909]{quote} 1)  
  
Here are those to files we should work with and code in the Blessing Multi pair.   
  
Cheers. 

Attached File(s)

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [RSIOMA Alert.mq4](/attachment/file/3556573?d=1582026406) 3 KB | 404 downloads 

Attached File(s)

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [RSIOMA.mq4](/attachment/file/3556574?d=1582026406) 6 KB | 435 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#337](/thread/post/12761959#post12761959 "Post Permalink")

  * Feb 19, 2020 2:05pm  Feb 19, 2020 2:05pm 

  * [ Dowde](dowde)

  * | Joined Feb 2020  | Status: Trader | [4 Posts](/search?do=process&provider=Member&searchuser=916801)

It's nice having all the entry possibilities. So far I've only been using MA and Stochastic with decent results. It would be interesting if we, with the EA, had the ability to Enter a trade only when two or more of the parameters were met, e.g., MA and Bollinger both hit. Obviously, this may give us more precise trades... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#338](/thread/post/12762051#post12762051 "Post Permalink")

  * Feb 19, 2020 3:50pm  Feb 19, 2020 3:50pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar338950_1.gif) cescof](cescof)

  * Joined Jun 2013 | Status: Trader | [1,006 Posts](/search?do=process&provider=Member&searchuser=338950)

> [Quoting Dowde](/thread/post/12761959#post12761959 "View Quoted Post")
> 
> Disliked
> 
> It's nice having all the entry possibilities. So far I've only been using MA and Stochastic with decent results. It would be interesting if we, with the EA, had the ability to Enter a trade only when two or more of the parameters were met, e.g., MA and Bollinger both hit. Obviously, this may give us more precise trades...
> 
> Ignored

You can it's just possibile by Ea 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#339](/thread/post/12763262#post12763262 "Post Permalink")

  * Feb 20, 2020 2:10am  Feb 20, 2020 2:10am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar849348_1.gif) Shazzie](shazzie)

  * | Joined Sep 2019  | Status: Trader | [24 Posts](/search?do=process&provider=Member&searchuser=849348)

Emmanuel,  
  
where would one find Evolution? I’ve tried but the links on his website don’t work...  
  
thankyou.  
  

> [Quoting emmanuel7788](/thread/post/12740100#post12740100 "View Quoted Post")
> 
> Disliked
> 
> {quote} Blessing3 is open source. however BlessingPro is not and become a commercial product by jtatoday. the newer versions like Evolution are all non-open source.
> 
> Ignored

Never Givin' Up..

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#340](/thread/post/12774677#post12774677 "Post Permalink")

  * Feb 26, 2020 2:46am  Feb 26, 2020 2:46am 

  * [ laharjaya](laharjaya)

  * | Joined Jun 2008  | Status: Trader | [136 Posts](/search?do=process&provider=Member&searchuser=72657)

By using this setting [BlessingV24beta-XUSUSDTest.set.txt](https://www.forexfactory.com/attachment.php/3527008?attachmentid=3527008&d=1578802208) , can we trade GU by replace xususd wih GU ? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Blessing Multipair EA
  *   * [ **Reply to Thread** ](/thread/973998-blessing-multipair-ea/reply#reply)

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

[Trading multipair triangles, no stoploss](/thread/917648-trading-multipair-triangles-no-stoploss "Hello forex Folks! 
  
I'd like to share with You my system that I was comming to for many years. I am testing it these days and it gives...") 78 replies

['Blessing' EA Modification Wanted](/thread/271525-blessing-ea-modification-wanted "Hello. 
 
here is a version of BLESSING \(old\) love this version. 
I wonder if someone could if possible to change this code. 
 
I like that...") 3 replies

[Single, Few Pair Traders (1-4) vs. MultiPair Traders (8-20)](/thread/964171-single-few-pair-traders-1-4-vs-multipair-traders "Who gets better results ?? 
  
Put it in another way , if you went for a trading competition and want to achieve &gt;300% ~ 2000% , what would...") 0 replies

[Coding Request for Multipair MTF ADR Dashboard](/thread/683340-coding-request-for-multipair-mtf-adr-dashboard "Can someone code this into indicator???") 2 replies

[trying to make a multipair buy and sell script](/thread/241746-trying-to-make-a-multipair-buy-and-sell "what i like to do is that i add a script on a chart and it will do 
 
open 3 pairs buys or sells. 
 
for example 0.1 lot EURUSD 
          ...") 6 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/973998-blessing-multipair-ea/reply#reply)
  * Subscribe
  * [97](javascript:void\(0\);)

Attachments: Blessing Multipair EA

Tags: Blessing Multipair EA

#  [](/thread/973998-blessing-multipair-ea)Blessing Multipair EA 

  * 

  * [#341](/thread/post/12780594#post12780594 "Post Permalink")

  * Edited 5:46pm  Feb 28, 2020 4:57pm | Edited 5:46pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar817367_1.gif) ecryptom](ecryptom)

  * | Joined Jun 2019  | Status: Trader | [140 Posts](/search?do=process&provider=Member&searchuser=817367)

**Please Add prefix suffix option**  
  
a)  
BlessingLite_3_v3.9.6.34_gamma GBPUSDi,M5: Dashboard detected suffix: i  
  
how i fix that ?  
  
the issue is i leave it default and have the above message  
b) when i put manual the pairs  
like that  
  
EURUSDi,AUDUSDi,NZDUSDi,GBPUSDi,USDCADi,USDCHFi,USDJPYi,EURAUDi,EURNZDi,EURGBPi,EURCADi,EURCHFi,EURJPYi,GBPAUDi,GBPNZDi,GBPCADi,GBPCHFi,GBPJPYi,AUDNZDi,AUDCADi,AUDCHFi,AUDJPYi,NZDCADi,NZDCHFi,NZDJPYi,CADCHFi,CADJPYi,CHFJPYi  
  
i have these multiple messages for each pair ..  
  
BlessingLite_3_v3.9.6.34_gamma GBPUSDi,M5: No MarketInfo for EURUSDii0.00000000  
  
c) if i put the list of pairs with out the prefix "i" i have also error messages ..  
  
any ideas ? 

Everything flows. Learn to Earn.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#342](/thread/post/12783112#post12783112 "Post Permalink")

  * Mar 1, 2020 2:07am  Mar 1, 2020 2:07am 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

> [Quoting ecryptom](/thread/post/12780594#post12780594 "View Quoted Post")
> 
> Disliked
> 
> any ideas ?
> 
> Ignored

Yes of course.  
  
You can easily coment out the part in the init function of the programm and then use your list with EURUSDi,CADCHFi.  
  
somewhere in line 421, put the two // so that you have this line:  
// getPrefixSuffix(prefix,suffix); 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#343](/thread/post/12783245#post12783245 "Post Permalink")

  * Mar 1, 2020 5:16am  Mar 1, 2020 5:16am 

  * [ ultax](ultax)

  * | Joined Oct 2019  | Status: Trader | [85 Posts](/search?do=process&provider=Member&searchuser=872453)

> [Quoting Shazzie](/thread/post/12763262#post12763262 "View Quoted Post")
> 
> Disliked
> 
> Emmanuel, where would one find Evolution? I’ve tried but the links on his website don’t work... thankyou. {quote}
> 
> Ignored

I am also wondering this! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#344](/thread/post/12785132#post12785132 "Post Permalink")

  * Edited Mar 3, 2020 10:44am  Mar 2, 2020 6:22pm | Edited Mar 3, 2020 10:44am 

  * [ rindhn](rindhn)

  * | Joined Mar 2018  | Status: Trader | [5 Posts](/search?do=process&provider=Member&searchuser=664965)

Can you add maxdd code? i Can't Find it. Or Add the code to close all orders with money loss? Thanks

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#345](/thread/post/12785372#post12785372 "Post Permalink")

  * Mar 2, 2020 8:17pm  Mar 2, 2020 8:17pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar817367_1.gif) ecryptom](ecryptom)

  * | Joined Jun 2019  | Status: Trader | [140 Posts](/search?do=process&provider=Member&searchuser=817367)

> [Quoting ursinho4711](/thread/post/12783112#post12783112 "View Quoted Post")
> 
> Disliked
> 
> {quote} Yes of course. You can easily coment out the part in the init function of the programm and then use your list with EURUSDi,CADCHFi. somewhere in line 421, put the two // so that you have this line: // getPrefixSuffix(prefix,suffix);
> 
> Ignored

  
thank you for your replay, i tried it today but**didnt work**  
  
any other ideas ? i wonder nobody tested in an ECN broker ? 

Everything flows. Learn to Earn.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#346](/thread/post/12801746#post12801746 "Post Permalink")

  * Mar 10, 2020 2:19pm  Mar 10, 2020 2:19pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar3294_6.gif) JackJones](jackjones)

  * Joined Aug 2005 | Status: 888 | [1,021 Posts](/search?do=process&provider=Member&searchuser=3294)

a 5k demo (grew to 8k) running 15 pairs lasted two months only to go bust on cad/jpy and gbp/chf this week trading 7.29 lots at the peak it ran out of equity.. to survive further min equity would have need to be 15-20k - other MP Blessing with limited pairs are still trading as i removed jpg chf gbp and eur pairs a few weeks ago ![](https://resources.faireconomy.media/images/emojis/64/1f3a2.png?v=15.1) \-- i'm running three pairs live and its going slow but and only one pair went to 0.09 lots in these last two weeks of chaos. ![](https://resources.faireconomy.media/images/emojis/64/1f4aa.png?v=15.1) going to reset all pairs demo with 50k to resume forward test. 

grist for the mill

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#347](/thread/post/12812099#post12812099 "Post Permalink")

  * Mar 14, 2020 8:13am  Mar 14, 2020 8:13am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar746461_1.gif) gogo11](gogo11)

  * | Joined Dec 2018  | Status: Trader | [17 Posts](/search?do=process&provider=Member&searchuser=746461)

Hey guys,  
Tried with 200 usd, 1k usd and 3k usd.  
200 died after 2 days, 1k looks ok with 40% dd and 3k had 17% dd till now but I need more time in order to know what can survive.  
Gonna try with 700 usd next week.   
I'm trying to find the minimal deposit that this EA could last for 1 month. Share your experience about the initial deposit. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#348](/thread/post/12815710#post12815710 "Post Permalink")

  * Mar 16, 2020 10:13pm  Mar 16, 2020 10:13pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar469735_1.gif) cdsaa](cdsaa)

  * Joined Jun 2016 | Status: Trader | [621 Posts](/search?do=process&provider=Member&searchuser=469735)

> [Quoting ursinho4711](/thread/post/12698714#post12698714 "View Quoted Post")
> 
> Disliked
> 
> My first thread in this forum, I am so excited... The idea for this EA started in another thread: <https://www.forexfactory.com/showthread.php?t=792598> Therefore this EA is based on the wonderful EA called “Blessing 3 v3.9.6.09”. The idea to try to build a multipair version came up in the above mentioned thread. After some brainstorming I began to like the idea. Though Blessing and multipair is kind of a contradiction. Blessing has so many parameters to finetune the EA exactly to your pair to trade, the time frame, your risk and and and....
> 
> Ignored

  
Good work. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#349](/thread/post/12819367#post12819367 "Post Permalink")

  * Mar 18, 2020 2:45am  Mar 18, 2020 2:45am 

  * [ auzea](auzea)

  * | Joined Mar 2020  | Status: Trader | [2 Posts](/search?do=process&provider=Member&searchuser=927842)

Maybe if you shutdown the expert during nfp it can be very cool 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#350](/thread/post/12819629#post12819629 "Post Permalink")

  * Mar 18, 2020 5:19am  Mar 18, 2020 5:19am 

  * [ Sugryy](sugryy)

  * | Joined Mar 2020  | Status: Trader | [1 Post](/search?do=process&provider=Member&searchuser=927873)

> [Quoting ursinho4711](/thread/post/12783112#post12783112 "View Quoted Post")
> 
> Disliked
> 
> {quote} Yes of course. You can easily coment out the part in the init function of the programm and then use your list with EURUSDi,CADCHFi. somewhere in line 421, put the two // so that you have this line: // getPrefixSuffix(prefix,suffix);
> 
> Ignored

  
Good day...please i noticed that the blessinglite ea dosnt pick any trade...since i started using it...it only picked trades on the first day....and since then nothing more..  
What could be the problem 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#351](/thread/post/12820040#post12820040 "Post Permalink")

  * Mar 18, 2020 10:58am  Mar 18, 2020 10:58am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar746461_1.gif) gogo11](gogo11)

  * | Joined Dec 2018  | Status: Trader | [17 Posts](/search?do=process&provider=Member&searchuser=746461)

> [Quoting JackJones](/thread/post/12801746#post12801746 "View Quoted Post")
> 
> Disliked
> 
> a 5k demo (grew to 8k) running 15 pairs lasted two months only to go bust on cad/jpy and gbp/chf this week trading 7.29 lots at the peak it ran out of equity.. to survive further min equity would have need to be 15-20k - other MP Blessing with limited pairs are still trading as i removed jpg chf gbp and eur pairs a few weeks ago ![](https://resources.faireconomy.media/images/emojis/64/1f3a2.png?v=15.1) \-- i'm running three pairs live and its going slow but and only one pair went to 0.09 lots in these last two weeks of chaos. ![](https://resources.faireconomy.media/images/emojis/64/1f4aa.png?v=15.1) going to reset all pairs demo with 50k to resume forward test.
> 
> Ignored

What is the starting lot?  
I think that disabling the MM and use 0.01 only is the best approach.  
7.29 lots sound bad... Seems like you used MM. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#352](/thread/post/12820576#post12820576 "Post Permalink")

  * Mar 18, 2020 5:29pm  Mar 18, 2020 5:29pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar3294_6.gif) JackJones](jackjones)

  * Joined Aug 2005 | Status: 888 | [1,021 Posts](/search?do=process&provider=Member&searchuser=3294)

> [Quoting gogo11](/thread/post/12820040#post12820040 "View Quoted Post")
> 
> Disliked
> 
> {quote} What is the starting lot? I think that disabling the MM and use 0.01 only is the best approach. 7.29 lots sound bad... Seems like you used MM.
> 
> Ignored

MM is False but the multiplier is 3 so with 0.01 starting only takes level 7 to get to 7.29 and to survive it would have needed to keeping buying until level 10 and with a multi of 3 level 10 is 196 lots... so not enough equity for sure if that is how this EA works without MM, lol. maybe the math needs to be looked at past level 4 if you want a true EA or that's where MM will help you ? if my live one ever gets to l4 i will disable it and manage it myself. 

grist for the mill

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#353](/thread/post/12820589#post12820589 "Post Permalink")

  * Mar 18, 2020 5:34pm  Mar 18, 2020 5:34pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar86801_11.gif) emmanuel7788](emmanuel7788)

  * Joined Nov 2008 | Status: Trader | [47,707 Posts](/search?do=process&provider=Member&searchuser=86801)

> [Quoting JackJones](/thread/post/12820576#post12820576 "View Quoted Post")
> 
> Disliked
> 
> {quote} MM is False but the multiplier is 1.3 so with 0.01 starting only takes level 7 to get to 7.29 and to survive it would have needed to keeping buying until level 10 and with a multi of 3 level 10 is 196 lots... so not enough equity for sure, lol. maybe the math needs to be looked at past level 4 if you want a true EA- if my live one ever gets to l4 i will disable it and manage it myself.
> 
> Ignored

  
with the multiplier ,  
one option is to consider close oldest position when you open #5  
  
close #1 open #6  
close #2 open #7  
close#3 open #8  
....  
  
keep only a maximum 5 open positions (in one basket) at any one time.  
if you keep opening more and more without close oldest, your margin cannot handle the increasing DD. 

Honesty is a very expensive gift. You wont find it in cheap people.WBuffett

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#354](/thread/post/12820591#post12820591 "Post Permalink")

  * Mar 18, 2020 5:35pm  Mar 18, 2020 5:35pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar746461_1.gif) gogo11](gogo11)

  * | Joined Dec 2018  | Status: Trader | [17 Posts](/search?do=process&provider=Member&searchuser=746461)

> [Quoting JackJones](/thread/post/12820576#post12820576 "View Quoted Post")
> 
> Disliked
> 
> {quote} MM is False but the multiplier is 3 so with 0.01 starting only takes level 7 to get to 7.29 and to survive it would have needed to keeping buying until level 10 and with a multi of 3 level 10 is 196 lots... so not enough equity for sure if that is how this EA works without MM, lol. maybe the math needs to be looked at past level 4 if you want a true EA or that's where MM will help you ? if my live one ever gets to l4 i will disable it and manage it myself.
> 
> Ignored

Yes but maybe with a multiplier of 3, you will cut the positions faster? Try to run both demos 1.3 and 3 in parallel and let us know which one survived. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#355](/thread/post/12820612#post12820612 "Post Permalink")

  * Mar 18, 2020 5:48pm  Mar 18, 2020 5:48pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar3294_6.gif) JackJones](jackjones)

  * Joined Aug 2005 | Status: 888 | [1,021 Posts](/search?do=process&provider=Member&searchuser=3294)

> [Quoting gogo11](/thread/post/12820591#post12820591 "View Quoted Post")
> 
> Disliked
> 
> {quote} Yes but maybe with a multiplier of 3, you will cut the positions faster? Try to run both demos 1.3 and 3 in parallel and let us know which one survived.
> 
> Ignored

i noticed a pattern in that if a pair starts trading to l3 once or twice chances are it will soon get itself in a trade past l3, so i simply removed pairs that the EA gets stuck on l3 often even though they often had the highest profits.  
  
thing is it will get some decent profits due to vol out of l3 trades now and then but for how long? maybe only two or three times, sometiems 6 but if im live i want to protect equity not max risk it.. i'd rather bet on the weather.  
  
1.3 might be worth trying but it would depend on how it grids the rebuys.. better re-buying max adrs imo and getting out quick (like you say) otherwise you might as well be buying round numbers or magic lines as you will often be holding negative carries. 

grist for the mill

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#356](/thread/post/12820678#post12820678 "Post Permalink")

  * Mar 18, 2020 6:16pm  Mar 18, 2020 6:16pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar746461_1.gif) gogo11](gogo11)

  * | Joined Dec 2018  | Status: Trader | [17 Posts](/search?do=process&provider=Member&searchuser=746461)

> [Quoting JackJones](/thread/post/12820612#post12820612 "View Quoted Post")
> 
> Disliked
> 
> {quote} i noticed a pattern in that if a pair starts trading to l3 once or twice chances are it will soon get itself in a trade past l3, so i simply removed pairs that the EA gets stuck on l3 often even though they often had the highest profits. thing is it will get some decent profits due to vol out of l3 trades now and then but for how long? maybe only two or three times, sometiems 6 but if im live i want to protect equity not max risk it.. i'd rather bet on the weather. 1.3 might be worth trying but it would depend on how it grids the rebuys.....
> 
> Ignored

I'm using a preset I found here somewhere, trying now 1k,1.5k, 3k, removed a few gbp pairs.   
Will drop the results once ill double. Cheers 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#357](/thread/post/12820687#post12820687 "Post Permalink")

  * Mar 18, 2020 6:20pm  Mar 18, 2020 6:20pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar387904_2.gif) ionone](ionone)

  * | Commercial User  | Joined Oct 2014 | [447 Posts](/search?do=process&provider=Member&searchuser=387904)

> [Quoting ursinho4711](/thread/post/12698762#post12698762 "View Quoted Post")
> 
> Disliked
> 
> Remember that post? [https://www.forexfactory.com/showthr...7#post12551567](https://www.forexfactory.com/showthread.php?p=12551567#post12551567) Well, I used the settings and made a backtest from 01.Nov.2019 to 10.Jan.2020. 5 Minutes timeframe, for all 28 pairs. What can I say: that already looks like the winner to be tested on the Blessing-Multipair. Can't wait for Sidney open... Here are the results: {image}
> 
> Ignored

the DD is too high, you run on 28 pairs so you need 0.8% DD max per pair  
otherwise you'll burn your account 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#358](/thread/post/12821330#post12821330 "Post Permalink")

  * Mar 18, 2020 10:29pm  Mar 18, 2020 10:29pm 

  * [ buddys](buddys)

  * | Joined Mar 2020  | Status: Trader | [1 Post](/search?do=process&provider=Member&searchuser=928139)

how to limit the pair order (28pair) "MaxTradesPerPair" ? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#359](/thread/post/12824443#post12824443 "Post Permalink")

  * Edited Mar 20, 2020 1:08am  Mar 19, 2020 11:41pm | Edited Mar 20, 2020 1:08am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar746461_1.gif) gogo11](gogo11)

  * | Joined Dec 2018  | Status: Trader | [17 Posts](/search?do=process&provider=Member&searchuser=746461)

> [Quoting ecryptom](/thread/post/12780594#post12780594 "View Quoted Post")
> 
> Disliked
> 
> Please Add prefix suffix option a) BlessingLite_3_v3.9.6.34_gamma GBPUSDi,M5: Dashboard detected suffix: i how i fix that ? the issue is i leave it default and have the above message b) when i put manual the pairs like that EURUSDi,AUDUSDi,NZDUSDi,GBPUSDi,USDCADi,USDCHFi,USDJPYi,EURAUDi,EURNZDi,EURGBPi,EURCADi,EURCHFi,EURJPYi,GBPAUDi,GBPNZDi,GBPCADi,GBPCHFi,GBPJPYi,AUDNZDi,AUDCADi,AUDCHFi,AUDJPYi,NZDCADi,NZDCHFi,NZDJPYi,CADCHFi,CADJPYi,CHFJPYi i have these multiple messages for each pair .. BlessingLite_3_v3.9.6.34_gamma GBPUSDi,M5: No MarketInfo...
> 
> Ignored

Same here.  
Using a broker that has ".uk"  
I edited the source and even added all pairs as custom pairs, got this message:  
  
2020.03.19 16:39:53.198 BlessingLite_3_v3.9.6.34_gamma USDCAD.uk,M5: No MarketInfo for USDCA0.00000000  
\--  
I commented:  
// getPrefixSuffix(prefix,suffix);  
And using defaults.  
  
Now, under experts:  
2020.03.19 16:59:39.943 BlessingLite_3_v3.9.6.34_gamma EURUSD.uk,M5: Broker has disallowed EAs on this account  
  
under journal:  
2020.03.19 16:59:40.146 '89394': order sell limit 0.01 GBPCHF.uk opening at 1.14950 sl: 0.00000 tp: 0.00000 failed [Trade is disabled]  
  
  
The broker claims that he doesnt block EAs and I have another account with other EAs - no issues.  
Testing another EA on this account.  
  
update: fixed. broker's issue. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#360](/thread/post/12824633#post12824633 "Post Permalink")

  * Mar 20, 2020 12:50am  Mar 20, 2020 12:50am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar772212_1.gif) Mikiburger](mikiburger)

  * | Joined Feb 2019  | Status: Trader | [9 Posts](/search?do=process&provider=Member&searchuser=772212)

Forward testing on demo account.  
Blow my 3000$ account (1:500) in 3 days.  
It is possible to select the pairs for trading ?  
28 pairs must be to high for limited account. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Blessing Multipair EA
  *   * [ **Reply to Thread** ](/thread/973998-blessing-multipair-ea/reply#reply)

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

[Trading multipair triangles, no stoploss](/thread/917648-trading-multipair-triangles-no-stoploss "Hello forex Folks! 
  
I'd like to share with You my system that I was comming to for many years. I am testing it these days and it gives...") 78 replies

['Blessing' EA Modification Wanted](/thread/271525-blessing-ea-modification-wanted "Hello. 
 
here is a version of BLESSING \(old\) love this version. 
I wonder if someone could if possible to change this code. 
 
I like that...") 3 replies

[Single, Few Pair Traders (1-4) vs. MultiPair Traders (8-20)](/thread/964171-single-few-pair-traders-1-4-vs-multipair-traders "Who gets better results ?? 
  
Put it in another way , if you went for a trading competition and want to achieve &gt;300% ~ 2000% , what would...") 0 replies

[Coding Request for Multipair MTF ADR Dashboard](/thread/683340-coding-request-for-multipair-mtf-adr-dashboard "Can someone code this into indicator???") 2 replies

[trying to make a multipair buy and sell script](/thread/241746-trying-to-make-a-multipair-buy-and-sell "what i like to do is that i add a script on a chart and it will do 
 
open 3 pairs buys or sells. 
 
for example 0.1 lot EURUSD 
          ...") 6 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/973998-blessing-multipair-ea/reply#reply)
  * Subscribe
  * [97](javascript:void\(0\);)

Attachments: Blessing Multipair EA

Tags: Blessing Multipair EA

#  [](/thread/973998-blessing-multipair-ea)Blessing Multipair EA 

  * 

  * [#361](/thread/post/12824660#post12824660 "Post Permalink")

  * Mar 20, 2020 1:00am  Mar 20, 2020 1:00am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar469735_1.gif) cdsaa](cdsaa)

  * Joined Jun 2016 | Status: Trader | [621 Posts](/search?do=process&provider=Member&searchuser=469735)

there is a crash of EA asking for restart. As it was on VPN didnt see how and when it happened.  
  
Did any one else experienced it. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#362](/thread/post/12824789#post12824789 "Post Permalink")

  * Mar 20, 2020 1:50am  Mar 20, 2020 1:50am 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

> [Quoting Mikiburger](/thread/post/12824633#post12824633 "View Quoted Post")
> 
> Disliked
> 
> Forward testing on demo account. Blow my 3000$ account (1:500) in 3 days. It is possible to select the pairs for trading ? 28 pairs must be to high for limited account.
> 
> Ignored

Sure, very easy! In the settings, instead of using the 28 default pairs, you can make your own list. Even XAUUSD or whatever is possible. Or EURMXN...  
The list must be comma separated like XAUUSD,EURMXN,EURUSD,CHFJPY 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#363](/thread/post/12826068#post12826068 "Post Permalink")

  * Mar 20, 2020 4:32pm  Mar 20, 2020 4:32pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar469735_1.gif) cdsaa](cdsaa)

  * Joined Jun 2016 | Status: Trader | [621 Posts](/search?do=process&provider=Member&searchuser=469735)

"According to Metaquotes guidelines, an account is considered hyperactive when it exceeds 2,000 messages per day. We are flexible with this guideline and will only contact clients when this threshold is breached by some margin. Your server messages have exceeded 5,000, so we must ask you to take immediate action to bring these down to an acceptable level"  
  
Can you check this. It looks like it is sending messages to server way too many times. Can you check this part. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#364](/thread/post/12861013#post12861013 "Post Permalink")

  * Apr 7, 2020 3:01am  Apr 7, 2020 3:01am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar719265_4.gif) chandana47](chandana47)

  * | Joined Sep 2018  | Status: Trader | [232 Posts](/search?do=process&provider=Member&searchuser=719265)

Want to test this! 

Swimming with sharks!

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#365](/thread/post/12866213#post12866213 "Post Permalink")

  * Apr 9, 2020 6:47am  Apr 9, 2020 6:47am 

  * [ Gonzalez74](gonzalez74)

  * | Joined Jan 2017  | Status: Trader | [67 Posts](/search?do=process&provider=Member&searchuser=544031)

> [Quoting ursinho4711](/thread/post/12698714#post12698714 "View Quoted Post")
> 
> Disliked
> 
> My first thread in this forum, I am so excited... The idea for this EA started in another thread: <https://www.forexfactory.com/showthread.php?t=792598> Therefore this EA is based on the wonderful EA called “Blessing 3 v3.9.6.09”. The idea to try to build a multipair version came up in the above mentioned thread. After some brainstorming I began to like the idea. Though Blessing and multipair is kind of a contradiction. Blessing has so many parameters to finetune the EA exactly to your pair to trade, the time frame, your risk and and and....
> 
> Ignored

Hello!  
This version have a **negative Trailling Stop**? (TSLPips= -10)  
Thank you so much for your work and for sharing. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#366](/thread/post/12867881#post12867881 "Post Permalink")

  * Apr 9, 2020 11:32pm  Apr 9, 2020 11:32pm 

  * [ Gonzalez74](gonzalez74)

  * | Joined Jan 2017  | Status: Trader | [67 Posts](/search?do=process&provider=Member&searchuser=544031)

> [Quoting ursinho4711](/thread/post/12737738#post12737738 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi! To be honest I did not put the mql4 file and only the ex4 in post #1 because I was kind of hmmm sad? Only three friends helped to take a look at the code. So I thought: %§#* leechers... I am in a good mood today, though everything is in red ;-) I will put it on post #1 again...
> 
> Ignored

Thank You! ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#367](/thread/post/12867903#post12867903 "Post Permalink")

  * Apr 9, 2020 11:39pm  Apr 9, 2020 11:39pm 

  * [ Gonzalez74](gonzalez74)

  * | Joined Jan 2017  | Status: Trader | [67 Posts](/search?do=process&provider=Member&searchuser=544031)

> [Quoting ursinho4711](/thread/post/12731206#post12731206 "View Quoted Post")
> 
> Disliked
> 
> {quote} What about you? Will you volunteer to do so? Btw: I stayed up almost all night to learn about the differences mt4<->mt5
> 
> Ignored

Not knowing anything about code, is there anything I can do to help the project? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#368](/thread/post/12924822#post12924822 "Post Permalink")

  * May 7, 2020 8:00pm  May 7, 2020 8:00pm 

  * [ Mcxtrader](mcxtrader)

  * | Joined Jun 2017  | Status: Trader | [203 Posts](/search?do=process&provider=Member&searchuser=589792)

When I close MT4 open trades are getting closed automatically when it opens again.  
  
Any idea please. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#369](/thread/post/12959921#post12959921 "Post Permalink")

  * May 24, 2020 5:46am  May 24, 2020 5:46am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar707416_2.gif) Mardin](mardin)

  * | Commercial User  | Joined Aug 2018 | [12 Posts](/search?do=process&provider=Member&searchuser=707416)

> [Quoting ursinho4711](/thread/post/12698714#post12698714 "View Quoted Post")
> 
> Disliked
> 
> My first thread in this forum, I am so excited... The idea for this EA started in another thread: <https://www.forexfactory.com/showthread.php?t=792598> Therefore this EA is based on the wonderful EA called “Blessing 3 v3.9.6.09”. The idea to try to build a multipair version came up in the above mentioned thread. After some brainstorming I began to like the idea. Though Blessing and multipair is kind of a contradiction. Blessing has so many parameters to finetune the EA exactly to your pair to trade, the time frame, your risk and and and....
> 
> Ignored

can you change it ea will order based on 1 pair signal? for example if the sell signal is eurusd then all pairs make a sell order together, thanks 

Get profit together

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#370](/thread/post/12985630#post12985630 "Post Permalink")

  * Jun 5, 2020 8:50pm  Jun 5, 2020 8:50pm 

  * [ takeda1312](takeda1312)

  * | Joined Jun 2020  | Status: Trader | [3 Posts](/search?do=process&provider=Member&searchuser=962065)

> [Quoting ursinho4711](/thread/post/12698714#post12698714 "View Quoted Post")
> 
> Disliked
> 
> My first thread in this forum, I am so excited... The idea for this EA started in another thread: <https://www.forexfactory.com/showthread.php?t=792598> Therefore this EA is based on the wonderful EA called “Blessing 3 v3.9.6.09”. The idea to try to build a multipair version came up in the above mentioned thread. After some brainstorming I began to like the idea. Though Blessing and multipair is kind of a contradiction. Blessing has so many parameters to finetune the EA exactly to your pair to trade, the time frame, your risk and and and....
> 
> Ignored

Hello.  
I have only known forex since early 2020. I am unemployed and trying to find work after the Covid-19 epidemic. I have a savings of $ 250. Can I use this capital for your Blessing Multipair EA to trade with real money? I need a passive income to support my family before I can find a job. If you have any other EA that can generate an income of $ 250 / month with a capital of $ 10000, please sell me. I can borrow to buy it.  
Look forward to receiving your feedback. (I am from Vietnam, my English is not good so I use Google Transler) 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#371](/thread/post/12986981#post12986981 "Post Permalink")

  * Jun 6, 2020 6:19am  Jun 6, 2020 6:19am 

  * [ carolco](carolco)

  * | Joined Jan 2010  | Status: Trader | [178 Posts](/search?do=process&provider=Member&searchuser=129269)

Dear takeda1312,  
Only a fool can think, that 250USD robot or system could make you money. It is very very hard to stay in green numbers in a world of Forex.  
The process of learning and finding the best system that suits you and makes you money is a painful process. Guess how I know. No robot or system for sale wont make you money.  
  
There are however goldmine threads here, where you can learn how to be constantly profitable for free.  
  
This one f.e.  
  
<https://www.forexfactory.com/showthread.php?t=574351>  
  
Be safe  
C. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#372](/thread/post/12987192#post12987192 "Post Permalink")

  * Jun 6, 2020 1:02pm  Jun 6, 2020 1:02pm 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

> [Quoting carolco](/thread/post/12986981#post12986981 "View Quoted Post")
> 
> Disliked
> 
> Guess how I know. No robot or system for sale wont make you money.
> 
> Ignored

Totally agreed. Same with books "How to make Billions in Forex". If I had this holy grail knowledge and the billions... why would I waste time writing a book? I would enjoy champagne on my yacht in Monaco. If I had the perfect system I would not need to sell it... just let it run and enjoy...  
  
The only thing EAs can do is help you and take over some stuff you would do manually anyway. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#373](/thread/post/12987288#post12987288 "Post Permalink")

  * Jun 6, 2020 5:14pm  Jun 6, 2020 5:14pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar836530_33.gif) josi](josi)

  * Joined Aug 2019 | Status: Trader | [730 Posts](/search?do=process&provider=Member&searchuser=836530)

> [Quoting ursinho4711](/thread/post/12987192#post12987192 "View Quoted Post")
> 
> Disliked
> 
> {quote} If I had this holy grail knowledge and the billions... why would I waste time writing a book? I would enjoy champagne on my yacht in Monaco.
> 
> Ignored

Really - the cliché of a successful trader's life?  
Nothing better comes to mind?  
Whatever happened to the word "shallow"?  
If money - if you have it - only leads to repetitive (or competitive?) accumulative consumption it's not worth the effort. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#374](/thread/post/12987326#post12987326 "Post Permalink")

  * Jun 6, 2020 6:14pm  Jun 6, 2020 6:14pm 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

> [Quoting josi](/thread/post/12987288#post12987288 "View Quoted Post")
> 
> Disliked
> 
> {quote} Really - the cliché of a successful trader's life? Nothing better comes to mind? Whatever happened to the word "shallow"? If money - if you have it - only leads to repetitive (or competitive?) accumulative consumption it's not worth the effort.
> 
> Ignored

Thanks for the (philosophic) answer. Maybe you did not get the intention of my answer: it was not about what to do with billions rather to warn that there are too many people around wanting your money with the promise to make you a billionaire...  
If I had these $$$ I would not waste my time in Monaco. Wife and children know where to find my credit card ;-) 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#375](/thread/post/12987442#post12987442 "Post Permalink")

  * Jun 6, 2020 8:15pm  Jun 6, 2020 8:15pm 

  * [ cyberdude3](cyberdude3)

  * | Joined May 2020  | Status: Trader | [12 Posts](/search?do=process&provider=Member&searchuser=956069)

> [Quoting ursinho4711](/thread/post/12987192#post12987192 "View Quoted Post")
> 
> Disliked
> 
> {quote} Totally agreed. Same with books "How to make Billions in Forex". If I had this holy grail knowledge and the billions... why would I waste time writing a book? I would enjoy champagne on my yacht in Monaco. If I had the perfect system I would not need to sell it... just let it run and enjoy... The only thing EAs can do is help you and take over some stuff you would do manually anyway.
> 
> Ignored

Earning from Forex Market is more about advertising, dummy workshops, offering tools and offering courses from so called guru's who do not trade anymore. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#376](/thread/post/12990144#post12990144 "Post Permalink")

  * Edited 11:00pm  Jun 8, 2020 10:41pm | Edited 11:00pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar417608_1.gif) scalperpeak](scalperpeak)

  * | Joined Jun 2015  | Status: Trader | [50 Posts](/search?do=process&provider=Member&searchuser=417608)

Hi Ursinho,  
Thank you for your humble efforts. I downloaded the 34 version. Tried this.  
I tested the set file which was already uploaded here before on EURUSD  
test date - 6th May,2015 to 16th July 2015.. a test time of approx. a week more than 2 months  
Dukascopy Demo.  
I am unable to figure why the sudden collapse in the last part of the trade. Is it normal with others. Or is it because I used a set file which is not for EURUSD?  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: resultof5minduk.png
Size: 19 KB](/attachment/image/3658204/thumbnail?d=1591623482)](/attachment/image/3658204?d=1591623482)   

Attached Image (click to enlarge)

[![Click to Enlarge

Name: teston5mindukascopy.png
Size: 49 KB](/attachment/image/3658205/thumbnail?d=1591623483)](/attachment/image/3658205?d=1591623483)   

  
  
It works very slow on data and took time around 1 hour or more to complete the test.  
EDIT -- here is the set file

Attached File(s)

![File Type: txt](https://assets.faireconomy.media/images/attach/txt.gif) [200530-euraud-m5-CL.set.txt](/attachment/file/3658231?d=1591624593) 12 KB | 344 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#377](/thread/post/12990325#post12990325 "Post Permalink")

  * Jun 8, 2020 11:41pm  Jun 8, 2020 11:41pm 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

> [Quoting scalperpeak](/thread/post/12990144#post12990144 "View Quoted Post")
> 
> Disliked
> 
> Hi Ursinho, Thank you for your humble efforts. I downloaded the 34 version. Tried this. I tested the set file which was already uploaded here before on EURUSD test date - 6th May,2015 to 16th July 2015.. a test time of approx. a week more than 2 months Dukascopy Demo. I am unable to figure why the sudden collapse in the last part of the trade. Is it normal with others. Or is it because I used a set file which is not for EURUSD? {image}{image} It works very slow on data and took time around 1 hour or more to complete the test. EDIT -- here is the...
> 
> Ignored

Hi!  
I need to see the last results of the results tab and the last messages of the journal tab. The "loss" at the end can have following reasons for example:  
\- Equity stop  
\- Close all orders due to end of test (most probable, according to the graph)  
or other money management reasons... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#378](/thread/post/12990997#post12990997 "Post Permalink")

  * Jun 9, 2020 6:15am  Jun 9, 2020 6:15am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar417608_1.gif) scalperpeak](scalperpeak)

  * | Joined Jun 2015  | Status: Trader | [50 Posts](/search?do=process&provider=Member&searchuser=417608)

> [Quoting ursinho4711](/thread/post/12990325#post12990325 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi! I need to see the last results of the results tab and the last messages of the journal tab. The "loss" at the end can have following reasons for example: - Equity stop - Close all orders due to end of test (most probable, according to the graph) or other money management reasons...
> 
> Ignored

I think it was due to close all orders. I re-tested with longer time frame and it worked.   
Thank you for your prompt reply.  
Will post some more test inputs.  
![](https://resources.faireconomy.media/images/emojis/64/1f642.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#379](/thread/post/12991113#post12991113 "Post Permalink")

  * Jun 9, 2020 7:57am  Jun 9, 2020 7:57am 

  * [ richard96816](richard96816)

  * Joined Dec 2018 | Status: Trader | [564 Posts](/search?do=process&provider=Member&searchuser=741833)

> [Quoting scalperpeak](/thread/post/12990144#post12990144 "View Quoted Post")
> 
> Disliked
> 
> Hi Ursinho, Thank you for your humble efforts. I downloaded the 34 version. Tried this. I tested the set file which was already uploaded here before on EURUSD test date - 6th May,2015 to 16th July 2015.. a test time of approx. a week more than 2 months Dukascopy Demo. I am unable to figure why the sudden collapse in the last part of the trade. Is it normal with others. Or is it because I used a set file which is not for EURUSD? {image}{image} It works very slow on data and took time around 1 hour or more to complete the test. EDIT -- here is the...
> 
> Ignored

Strategy Tester doesn't know how to end a test with open positions. So it sometimes ends with a false large loss if there was a big drawdown at the end.  
  
It may signify that your system is experiencing large drawdowns or trading without stops. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#380](/thread/post/12995707#post12995707 "Post Permalink")

  * Jun 11, 2020 1:07am  Jun 11, 2020 1:07am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar102021_3.gif) fx4money](fx4money)

  * Joined May 2009 | Status: Trader | [985 Posts](/search?do=process&provider=Member&searchuser=102021)

> [Quoting takeda1312](/thread/post/12985630#post12985630 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hello. I have only known forex since early 2020. I am unemployed and trying to find work after the Covid-19 epidemic. I have a savings of $ 250. Can I use this capital for your Blessing Multipair EA to trade with real money? I need a passive income to support my family before I can find a job. If you have any other EA that can generate an income of $ 250 / month with a capital of $ 10000, please sell me. I can borrow to buy it. Look forward to receiving your feedback. (I am from Vietnam, my English is not good so I use Google Transler)
> 
> Ignored

don't use this ea to trade, trading too many pairs at the same time with martingale is very dangerous. there will be few times in a year when pair moving trending (just like last 2 weeks) when most counter trend martingale strategy traders lost a lot ![](https://resources.faireconomy.media/images/emojis/64/1f61c.png?v=15.1)

golen trades

[2024 lucky gold trade](fx4money#30 "View Trade Explorer") All Time Return: -3.5%

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Blessing Multipair EA
  *   * [ **Reply to Thread** ](/thread/973998-blessing-multipair-ea/reply#reply)

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

[Trading multipair triangles, no stoploss](/thread/917648-trading-multipair-triangles-no-stoploss "Hello forex Folks! 
  
I'd like to share with You my system that I was comming to for many years. I am testing it these days and it gives...") 78 replies

['Blessing' EA Modification Wanted](/thread/271525-blessing-ea-modification-wanted "Hello. 
 
here is a version of BLESSING \(old\) love this version. 
I wonder if someone could if possible to change this code. 
 
I like that...") 3 replies

[Single, Few Pair Traders (1-4) vs. MultiPair Traders (8-20)](/thread/964171-single-few-pair-traders-1-4-vs-multipair-traders "Who gets better results ?? 
  
Put it in another way , if you went for a trading competition and want to achieve &gt;300% ~ 2000% , what would...") 0 replies

[Coding Request for Multipair MTF ADR Dashboard](/thread/683340-coding-request-for-multipair-mtf-adr-dashboard "Can someone code this into indicator???") 2 replies

[trying to make a multipair buy and sell script](/thread/241746-trying-to-make-a-multipair-buy-and-sell "what i like to do is that i add a script on a chart and it will do 
 
open 3 pairs buys or sells. 
 
for example 0.1 lot EURUSD 
          ...") 6 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/973998-blessing-multipair-ea/reply#reply)
  * Subscribe
  * [97](javascript:void\(0\);)

Attachments: Blessing Multipair EA

Tags: Blessing Multipair EA

#  [](/thread/973998-blessing-multipair-ea)Blessing Multipair EA 

  * 

  * [#381](/thread/post/12996640#post12996640 "Post Permalink")

  * Jun 11, 2020 10:18am  Jun 11, 2020 10:18am 

  * [ richard96816](richard96816)

  * Joined Dec 2018 | Status: Trader | [564 Posts](/search?do=process&provider=Member&searchuser=741833)

> [Quoting fx4money](/thread/post/12995707#post12995707 "View Quoted Post")
> 
> Disliked
> 
> {quote} don't use this ea to trade, trading too many pairs at the same time with martingale is very dangerous. there will be few times in a year when pair moving trending (just like last 2 weeks) when most counter trend martingale strategy traders lost a lot ![](https://resources.faireconomy.media/images/emojis/64/1f61c.png?v=15.1)
> 
> Ignored

Who said anything about Martingale? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#382](/thread/post/12996676#post12996676 "Post Permalink")

  * Jun 11, 2020 10:44am  Jun 11, 2020 10:44am 

  * [ sloshliuxin](sloshliuxin)

  * | Joined Jun 2020  | Status: Trader | [50 Posts](/search?do=process&provider=Member&searchuser=965350)

Hello,  
I am newer here.And use this EA is so good so far.  
But in my Alpari broker,i just found a error:  
2020.06.11 09:37:15.174 BlessingLite_3_v3.9.6.34_gamma EURUSD,M5: zero divide in 'BlessingLite_3_v3.9.6.34_gamma.mq4' (1625,67)  
What is this issue?  
And i found that i set use all 28 paris,but there are not all 28 paris opend,but in my other broker it works good,so what is my mistake? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#383](/thread/post/12996856#post12996856 "Post Permalink")

  * Jun 11, 2020 1:41pm  Jun 11, 2020 1:41pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar102021_3.gif) fx4money](fx4money)

  * Joined May 2009 | Status: Trader | [985 Posts](/search?do=process&provider=Member&searchuser=102021)

> [Quoting richard96816](/thread/post/12996640#post12996640 "View Quoted Post")
> 
> Disliked
> 
> {quote} Who said anything about Martingale?
> 
> Ignored

this ea is not martingale? what does the multiplier in the code for?  
  
input string LabelLS = ""; // ----------- LOT SIZE -----------  
input bool UseMM = false; // UseMM (Money Management)  
input double LAF = 0.5; // Adjusts MM base lot for large accounts  
input double Lot = 0.01; // Starting lots if Money Management is off  
input double Multiplier = 3.0; // Multiplier on each level 

golen trades

[2024 lucky gold trade](fx4money#30 "View Trade Explorer") All Time Return: -3.5%

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#384](/thread/post/12996926#post12996926 "Post Permalink")

  * Jun 11, 2020 2:34pm  Jun 11, 2020 2:34pm 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

> [Quoting fx4money](/thread/post/12996856#post12996856 "View Quoted Post")
> 
> Disliked
> 
> this ea is not martingale? what does the multiplier in the code for?
> 
> Ignored

You could if you wanted to. But you do not need to. I know, even the (original) documentation uses the word martingale. "Real" martingale uses a doubling of the lots (or jetons in roulette) to at least win the initial bet.  
Doubling, as we know from the rice grain/chessboard story, soon leads to astronomics sums. 16 levels martingale does not sound much. Looking at the result of 2^16 is opening your eyes.  
Back to the EA: you can adjust the lots per grid and use TP/SL. Martingale only, if you let it run with doubling the lots in a fixed grid. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#385](/thread/post/12996962#post12996962 "Post Permalink")

  * Jun 11, 2020 2:49pm  Jun 11, 2020 2:49pm 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

> [Quoting sloshliuxin](/thread/post/12996676#post12996676 "View Quoted Post")
> 
> Disliked
> 
> What is this issue? And i found that i set use all 28 paris,but there are not all 28 paris opend,but in my other broker it works good,so what is my mistake?
> 
> Ignored

Can have many, many reasons. What is your entry based on? Maybe (probably) the maximum spread?  
  
Anyway, to clarify something: this multipair EA is more for testing purposes on demo accounts than for live trading. With one set-file you can overview many pairs at the same time.  
IF (!) you found a setting that works for more pairs, then it is a good "live-tool". Combined with a dashboard, or you might loose overview quickly. Basket take profit for all used pairs... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#386](/thread/post/12997544#post12997544 "Post Permalink")

  * Jun 11, 2020 7:32pm  Jun 11, 2020 7:32pm 

  * [ richard96816](richard96816)

  * Joined Dec 2018 | Status: Trader | [564 Posts](/search?do=process&provider=Member&searchuser=741833)

Martingale requires the **doubling of bet size for each LOSS**. That's the simple definition.   
Blessing certainly cannot do that without changing the code. I doubt Multipair Blessing can either.  
  
A small string of losses would bankrupt any account that isn't infinite.  
  
I know the Blessing manual mentions Martingale. That's very unfortunate. And very wrong. The simple idea of increasing lot size for subsequent (usually winning) trades makes a lot of sense and is very common in effective trading systems.  
  
No one said you had to DOUBLE the size every time. Even if you do it's still not the absurd Martingale betting scheme. Still not doubling in response to a LOSS. That's idiotic. Increasing the trade size incrementally helps with many things including FIFO. With different trade sizes most brokers will allow you to side-step FIFO rules. No doubling necessary. You can close trades in any order.  
  
[https://en.wikipedia.org/wiki/Martin...betting_system](https://en.wikipedia.org/wiki/Martingale_\(betting_system))  
  
Increasing size in the same basket makes sense, that's why grid systems are so popular. It actually reduces risk while increasing potential profit. The thing that scares some traders away is you're no longer trading just one lot. You need a little larger account. And computing risk is a little more complex. You have to know how to add. :-)  
  
The manual provides some useful guidelines for controlling risk.  
  
Good luck! 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#387](/thread/post/13002339#post13002339 "Post Permalink")

  * Jun 14, 2020 12:11am  Jun 14, 2020 12:11am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar417608_1.gif) scalperpeak](scalperpeak)

  * | Joined Jun 2015  | Status: Trader | [50 Posts](/search?do=process&provider=Member&searchuser=417608)

> [Quoting richard96816](/thread/post/12991113#post12991113 "View Quoted Post")
> 
> Disliked
> 
> {quote} Strategy Tester doesn't know how to end a test with open positions. So it sometimes ends with a false large loss if there was a big drawdown at the end. It may signify that your system is experiencing large drawdowns or trading without stops.
> 
> Ignored

yes. Thanks. I got the point. I am trying to create new set files testing over 5 years but it hits stop out so its a tough task on mt4. I wish this EA was converted to Mt5. I think it would save time in testing I guess. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#388](/thread/post/13002589#post13002589 "Post Permalink")

  * Jun 14, 2020 7:50am  Jun 14, 2020 7:50am 

  * [ richard96816](richard96816)

  * Joined Dec 2018 | Status: Trader | [564 Posts](/search?do=process&provider=Member&searchuser=741833)

> [Quoting scalperpeak](/thread/post/13002339#post13002339 "View Quoted Post")
> 
> Disliked
> 
> {quote} yes. Thanks. I got the point. I am trying to create new set files testing over 5 years but it hits stop out so its a tough task on mt4. I wish this EA was converted to Mt5. I think it would save time in testing I guess.
> 
> Ignored

I understand testing over long periods to develop a new trading strategy. The original Blessing authors probably did that a lot. I'm not sure why you would test over more than a few months with a mature and profitable EA.  
  
You're worried about saving time, but you're doing the best thing to waste it.  
  
There are perhaps tiny repeating patterns to be found in the market mirroring many days and weeks and months. Then there are the larger, more profitable, repeating patterns that only go back a few weeks or months. The market changes all the time.  
  
If you're not writing a new EA testing over years of history is a waste of time. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#389](/thread/post/13002604#post13002604 "Post Permalink")

  * Jun 14, 2020 8:18am  Jun 14, 2020 8:18am 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

> [Quoting richard96816](/thread/post/13002589#post13002589 "View Quoted Post")
> 
> Disliked
> 
> There are perhaps tiny repeating patterns to be found in the market mirroring many days and weeks and months. Then there are the larger, more profitable, repeating patterns that only go back a few weeks or months.
> 
> Ignored

Imho it is a good strategy to find extreme situations in the history. Extreme can be high volatility as well as slow but steady moves. Spikes, that just pass by to hit stop losses. If the EA can survive these exreme situations and works well in a normal environment...: congrats!  
  
I was already thinking of opening a new thread "extreme hsitoric situations" to test EAs and settings at these points. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#390](/thread/post/13002647#post13002647 "Post Permalink")

  * Jun 14, 2020 10:18am  Jun 14, 2020 10:18am 

  * [ richard96816](richard96816)

  * Joined Dec 2018 | Status: Trader | [564 Posts](/search?do=process&provider=Member&searchuser=741833)

> [Quoting ursinho4711](/thread/post/13002604#post13002604 "View Quoted Post")
> 
> Disliked
> 
> {quote} Imho it is a good strategy to find extreme situations in the history. Extreme can be high volatility as well as slow but steady moves. Spikes, that just pass by to hit stop losses. If the EA can survive these extreme situations and works well in a normal environment...: congrats! I was already thinking of opening a new thread "extreme historic situations" to test EAs and settings at these points.
> 
> Ignored

Sure. Good for testing a new strategy to see how resilient it is. Not for tuning an existing EA to trade live.   
  
Primary testing has already been done with Blessing. You can rewrite it if you want and perhaps make it more adaptable, that would be great. Or you can learn how to use what we've got and make money. :-)  
  
I tend to want to edit out extremes in the data, since the likelihood of them happening again is very low. And there are so many different kinds of extremes! I'm not building the EA as much now, I'm using it. If you prefer to optimize just once a year (and accept much lower returns) then maybe keeping those extremes in the data makes sense.  
  
Open source means many wonderful things are possible. Everyone is free to build their own version. 

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#391](/thread/post/13002770#post13002770 "Post Permalink")

  * Jun 14, 2020 4:14pm  Jun 14, 2020 4:14pm 

  * [ ursinho4711](ursinho4711)

  * Joined Nov 2019 | Status: Trader | [1,121 Posts](/search?do=process&provider=Member&searchuser=876169)

> [Quoting richard96816](/thread/post/13002647#post13002647 "View Quoted Post")
> 
> Disliked
> 
> You can rewrite it if you want and perhaps make it more adaptable, that would be great. Or you can learn how to use what we've got and make money. :-) I tend to want to edit out extremes in the data, since the likelihood of them happening again is very low.
> 
> Ignored

Thanks for your (as always) helpful answer!  
Regarding blessing I do not see much to change or improve. As you wrote, it has been tested for such a long time. When I was talking about surviving extremes, I also referred to the settings of an EA. Especially with grid traders I had so many beautiful steady lines in the graph until some events came. And they come, at the moment even more often.  
With the setfiles and the tester you can try to imagine how high the DD could be. I can guarantee, that the higher the risk the higher the DD will be. So if you want to have a calm life accept small wins here and there. If your strategy test shows a huge DD, you should at least have enough liquidity when going live. This reduces the percentual win though. If you set your "close all at a certain DD" too tight you will see a saw tooth pattern going south.  
Money management is maybe more important to learn than "readings signals"...  
  
Coming back to Blessing (and other grid trading systems): one thing I would like to change or add, is the possibility to use percentage instead of pips. Every pair has a different pip/percentage ratio, but all (?) seem to use Fibo-lines as reference. Which makes sense, the professional programs (probably still programmed in COBOL) use them as well. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#392](/thread/post/13013324#post13013324 "Post Permalink")

  * Jun 19, 2020 6:42am  Jun 19, 2020 6:42am 

  * [ gazzamc20](gazzamc20)

  * | Joined Jun 2020  | Status: Trader | [6 Posts](/search?do=process&provider=Member&searchuser=968817)

Hello All  
  
i recently joined and am delighted so far with the version of blessinglite which was uploaded here a little while ago. version 3.9.6.31 gamma i believe. In just 2 days of using it, it profited me around 36 pound sterling, starting from a 160 balance. i was wondering if this was the latest verion or if there is a better one out there you guys have developed.  
  
Regards  
Gary 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#393](/thread/post/13015800#post13015800 "Post Permalink")

  * Jun 20, 2020 7:16am  Jun 20, 2020 7:16am 

  * [ bluemustang](bluemustang)

  * | Joined Jun 2020  | Status: Trader | [1 Post](/search?do=process&provider=Member&searchuser=969205)

> [Quoting gazzamc20](/thread/post/13013324#post13013324 "View Quoted Post")
> 
> Disliked
> 
> Hello All i recently joined and am delighted so far with the version of blessinglite which was uploaded here a little while ago. version 3.9.6.31 gamma i believe. In just 2 days of using it, it profited me around 36 pound sterling, starting from a 160 balance. i was wondering if this was the latest verion or if there is a better one out there you guys have developed. Regards Gary
> 
> Ignored

  
Hi gazzamc20 where did you find the ea can I test it?  
  
Thanks 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#394](/thread/post/13017263#post13017263 "Post Permalink")

  * Jun 22, 2020 5:15am  Jun 22, 2020 5:15am 

  * [ gazzamc20](gazzamc20)

  * | Joined Jun 2020  | Status: Trader | [6 Posts](/search?do=process&provider=Member&searchuser=968817)

> [Quoting bluemustang](/thread/post/13015800#post13015800 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi gazzamc20 where did you find the ea can I test it? Thanks
> 
> Ignored

  
hello there, it was added as an attachment on one of the first few pages by a member called Ursinho, believe its called BlessingLite_3_v3.9.6.34_gamma.  
you can test it whenevr you like and adjust it to your needs ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#395](/thread/post/13019501#post13019501 "Post Permalink")

  * Jun 23, 2020 3:36am  Jun 23, 2020 3:36am 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

is it possible to program a set file for this ea in this way for every pair:  
1 - first lot 0.15  
2 - next open trade 20 pips against the trade with 0.14 and so on for 14 levels till 0.02.  
3 - when each trade goes 10pips in profit close it  
4 - no stop loss  
5 - when equity is >= EquityTarget close all and restart again.  
is it possoble to make this adding only equititarget variable? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#396](/thread/post/13024535#post13024535 "Post Permalink")

  * Jun 25, 2020 1:33am  Jun 25, 2020 1:33am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar102021_3.gif) fx4money](fx4money)

  * Joined May 2009 | Status: Trader | [985 Posts](/search?do=process&provider=Member&searchuser=102021)

> [Quoting ursinho4711](/thread/post/13002604#post13002604 "View Quoted Post")
> 
> Disliked
> 
> {quote} Imho it is a good strategy to find extreme situations in the history. Extreme can be high volatility as well as slow but steady moves. Spikes, that just pass by to hit stop losses. If the EA can survive these exreme situations and works well in a normal environment...: congrats! I was already thinking of opening a new thread "extreme hsitoric situations" to test EAs and settings at these points.
> 
> Ignored

hi ursinho,  
  
is it possible to make the ea to open post like bellow:  
  
1\. sell 0.01 lot after say price 25pip move up, open  
2\. sell 0.02 lot, condition as above  
3\. sell 0.03lot (all 1,2,3 have average tp)  
4\. sell 0.01lot after above 25pip of 3rd sell  
5\. sell 0.02lot as above  
6\. sell 0.03lot (all 4,5,6 have another average tp)  
  
and so on.  
  
and may i know the indicators in your current Blessing multipair? ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

golen trades

[2024 lucky gold trade](fx4money#30 "View Trade Explorer") All Time Return: -3.5%

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#397](/thread/post/13082070#post13082070 "Post Permalink")

  * Jul 28, 2020 3:32am  Jul 28, 2020 3:32am 

  * [ AllMachines](allmachines)

  * | Joined Nov 2019  | Status: Trader | [4 Posts](/search?do=process&provider=Member&searchuser=879590)

How much, to sell blessinglite.mq5 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#398](/thread/post/13083321#post13083321 "Post Permalink")

  * Jul 28, 2020 7:54pm  Jul 28, 2020 7:54pm 

  * [ AllMachines](allmachines)

  * | Joined Nov 2019  | Status: Trader | [4 Posts](/search?do=process&provider=Member&searchuser=879590)

hi ursinho!  
And so the blessinglite.mq5, do you can to pass to me? I need friend! I have blessinglite.ex5, and I want to transforme in scalping ea to me, my use. Thanks you! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#399](/thread/post/13085675#post13085675 "Post Permalink")

  * Jul 29, 2020 10:37pm  Jul 29, 2020 10:37pm 

  * [ AllMachines](allmachines)

  * | Joined Nov 2019  | Status: Trader | [4 Posts](/search?do=process&provider=Member&searchuser=879590)

Thanks ursinho4711!  
I already managed to convert blessinglite.ex5 to .mq5.  
Thank you very much 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#400](/thread/post/13115365#post13115365 "Post Permalink")

  * Aug 16, 2020 1:52am  Aug 16, 2020 1:52am 

  * [ Vertical](vertical)

  * | Joined Aug 2020  | Status: Trader | [1 Post](/search?do=process&provider=Member&searchuser=991485)

I am using old version Blessing 3, v 3.9.6.09 long time. Now I get a new version 3.9.6.34 gamma.   
I have question - how can I optimize in MT4 all 3 parameters of Grid Size?   
In old Blessing I can do it but in new version I can not. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Blessing Multipair EA
  *   * [ **Reply to Thread** ](/thread/973998-blessing-multipair-ea/reply#reply)

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

[Trading multipair triangles, no stoploss](/thread/917648-trading-multipair-triangles-no-stoploss "Hello forex Folks! 
  
I'd like to share with You my system that I was comming to for many years. I am testing it these days and it gives...") 78 replies

['Blessing' EA Modification Wanted](/thread/271525-blessing-ea-modification-wanted "Hello. 
 
here is a version of BLESSING \(old\) love this version. 
I wonder if someone could if possible to change this code. 
 
I like that...") 3 replies

[Single, Few Pair Traders (1-4) vs. MultiPair Traders (8-20)](/thread/964171-single-few-pair-traders-1-4-vs-multipair-traders "Who gets better results ?? 
  
Put it in another way , if you went for a trading competition and want to achieve &gt;300% ~ 2000% , what would...") 0 replies

[Coding Request for Multipair MTF ADR Dashboard](/thread/683340-coding-request-for-multipair-mtf-adr-dashboard "Can someone code this into indicator???") 2 replies

[trying to make a multipair buy and sell script](/thread/241746-trying-to-make-a-multipair-buy-and-sell "what i like to do is that i add a script on a chart and it will do 
 
open 3 pairs buys or sells. 
 
for example 0.1 lot EURUSD 
          ...") 6 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/973998-blessing-multipair-ea/reply#reply)
  * Subscribe
  * [97](javascript:void\(0\);)

Attachments: Blessing Multipair EA

Tags: Blessing Multipair EA

#  [](/thread/973998-blessing-multipair-ea)Blessing Multipair EA 

  * 

  * [#401](/thread/post/13115967#post13115967 "Post Permalink")

  * Aug 17, 2020 2:49am  Aug 17, 2020 2:49am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar946848_7.gif) ryuryu](ryuryu)

  * Joined Apr 2020 | Status: Trader | [1,922 Posts](/search?do=process&provider=Member&searchuser=946848)

For me hedge is much better than SL. I tried every strategy, every indicator, have created tons of EAs, but there is no chance to use SLs.  
Also I have a very clean vision that trading has two parts: magic/luck or maths. Martin, grid, averaging, hard SL and TP, hard global profit TP and so on is just a magic. No math here. Also this is useless to create sets for pairs. Today they works next day not.  
  
Strange that we all are using math (indicators, setups, sequences, calculation) for entries, but not think/program the exits.  
  
For me the main question is not where to enter the trade. There are tons of ways to determine good entry. The main question is where to exit the trade.  
  
Averaging against trend and waiting (praying) for reversal is pure magic/luck/casino. Wishing good trades recover loss trades - the same. What if we try to program exits?   
  
I have noticed that stoch with 100/3/3 settings are good most time for exit. But the problem is that sometimes they (signals) are not appear. Any ideas? 

Observer effect

[1 ](javascript:void\(0\);) [4 ](javascript:void\(0\);)

  * [#402](/thread/post/13121181#post13121181 "Post Permalink")

  * Aug 19, 2020 11:24pm  Aug 19, 2020 11:24pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar102477_4.gif) wardi](wardi)

  * | Commercial User  | Joined May 2009 | [590 Posts](/search?do=process&provider=Member&searchuser=102477)

monitor this demo acount  
i use 3 preset for this account  
  
ACCOUNT NO 9283299  
server [FBS](/brokers/fbs "View FBS Broker Profile")-Demo  
IP Pro3333 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: ScreenshotNaN.png
Size: 591 KB](/attachment/image/3719765/thumbnail?d=1597847336)](/attachment/image/3719765?d=1597847336)   

Attached File(s)

![File Type: rar](https://assets.faireconomy.media/images/attach/rar.gif) [set.rar](/attachment/file/3719758?d=1597847089) 4 KB | 786 downloads 

SANTAI FX EA

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#403](/thread/post/13128459#post13128459 "Post Permalink")

  * Aug 24, 2020 10:35pm  Aug 24, 2020 10:35pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar942784_1.gif) Ismaelgz](ismaelgz)

  * | Joined Apr 2020  | Status: Trader | [6 Posts](/search?do=process&provider=Member&searchuser=942784)

hello everyone can you tell me why you are giving this error? thank you in advance! 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot_20200824-103312.png
Size: 308 KB](/attachment/image/3723482/thumbnail?d=1598276082)](/attachment/image/3723482?d=1598276082)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#404](/thread/post/13148714#post13148714 "Post Permalink")

  * Sep 4, 2020 3:27pm  Sep 4, 2020 3:27pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar746461_1.gif) gogo11](gogo11)

  * | Joined Dec 2018  | Status: Trader | [17 Posts](/search?do=process&provider=Member&searchuser=746461)

Hi all!  
First of all, I must say that I love this EA and the multipair version!  
I'm running it for a while in live/real accounts and the results are great with multiplier 2.  
Is it possible to fix the NO NEW TRADES parameter?   
It closes all positions after one minute.  
Thanks 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#405](/thread/post/13211979#post13211979 "Post Permalink")

  * Oct 14, 2020 1:40am  Oct 14, 2020 1:40am 

  * [ Pascalv1](pascalv1)

  * | Joined Oct 2020  | Status: Trader | [2 Posts](/search?do=process&provider=Member&searchuser=1015359)

Hello I am new here, I love the adventure of trading. I would like to use this robot; Blessing, in its most recent (better) version. 1. Can I have it please? 2. How do I configure it for my real account? Thank you very much in advance  
Hello I am new here, I love the adventure of trading. I would like to use this robot; Blessing, in its most recent (better) version. 1. Can I have it please? 2. How do I configure it for my real account? Thank you very much in advance 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#406](/thread/post/13217717#post13217717 "Post Permalink")

  * Oct 16, 2020 9:10pm  Oct 16, 2020 9:10pm 

  * [ jmcfarland11](jmcfarland11)

  * | Joined Sep 2020  | Status: Trader | [13 Posts](/search?do=process&provider=Member&searchuser=1001423)

So this version of Blessing is the exact same thing as B3, except you can trade all 28 currency pairs on it at once on a single chart? So it still uses the grid style approach then? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#407](/thread/post/13273037#post13273037 "Post Permalink")

  * Nov 20, 2020 5:24am  Nov 20, 2020 5:24am 

  * [ hossein681](hossein681)

  * | Joined Feb 2020  | Status: Trader | [1 Post](/search?do=process&provider=Member&searchuser=920830)

Hello, does this version not work on real accounts? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#408](/thread/post/13329009#post13329009 "Post Permalink")

  * Dec 24, 2020 4:32pm  Dec 24, 2020 4:32pm 

  * [ oberton](oberton)

  * | Joined Dec 2020  | Status: Trader | [2 Posts](/search?do=process&provider=Member&searchuser=1042960)

Thanks for this EA. I have tried it on real account with my set and here is pic of my result for two weeks of trading: started on 2-dec-2020 with $300 and before Christmas I have $600. I am using MA for entry, 5m chart, 1.4 multiplier and 8 currency pairs. MM is false, starting lot is 0.01 and this EA makes around $25 per day with these settings. But I think I am lucky, because $300 as started balance is not enough. Now I am waiting for new year to continue trading with new currency pairs without GBP (I have stopped for the holidays), because currency pairs with GBP are dangerous with that Brexit. But you decide how to risk your money. Cheers and Merry Xmas to all of you. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: amrealDetailedStatement.gif
Size: 6 KB](/attachment/image/3820252/thumbnail?d=1608793593)](/attachment/image/3820252?d=1608793593)   

Attached File(s)

![File Type: txt](https://assets.faireconomy.media/images/attach/txt.gif) [blessing.set.txt](/attachment/file/3820258?d=1608794623) 2 KB | 972 downloads 

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#409](/thread/post/13330289#post13330289 "Post Permalink")

  * Dec 25, 2020 7:33pm  Dec 25, 2020 7:33pm 

  * [ richard55](richard55)

  * | Joined Dec 2014  | Status: Trader | [36 Posts](/search?do=process&provider=Member&searchuser=394387)

Hello oberton,  
  
many thanks for your contribution with the GBP pairs ( MA for entry, 5m chart, 1.4 multiplier and 8 currency pairs) being positive.  
  
I have tried it in December as well with 28 pairs (MA for entry, 5m chart, 1.4 multiplier) but it was a compete loss! a few positive but the majority ended up in a loss in my demo account and stopped it.  
  
The Brexit problem seems to be solved now. I am starting new in January 2021 with your 8 pairs only Moving average is a tricky thing 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#410](/thread/post/13370328#post13370328 "Post Permalink")

  * Jan 21, 2021 8:31pm  Jan 21, 2021 8:31pm 

  * [ muppbg](muppbg)

  * | Joined Dec 2020  | Status: Trader | [1 Post](/search?do=process&provider=Member&searchuser=1040780)

EA get stucked on w8thing for the next tick and never opens a trade should i w8 it more? i Run it one real cent account! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#411](/thread/post/13373413#post13373413 "Post Permalink")

  * Jan 23, 2021 12:20pm  Jan 23, 2021 12:20pm 

  * [ Airdon](airdon)

  * | Joined Aug 2018  | Status: Trader | [1 Post](/search?do=process&provider=Member&searchuser=707961)

This is an interesting thread![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1).  
One thought that I have is that the concept of running blessing on a basket of pairs is good, but we need to be careful with correlation between the pairs.  
Blessings profitability comes from a range of fairly simple entry signals backed up by the hedging/averaging strategy that puts in multiple trades when things go against you. So you will always see steady small profits with occasional large drawdowns. The trick is to pick your settings so you can cope with the large drawdowns.  
So if you are trading 28 pairs all the time a lot will be dependant on say the usd, and if an event drives the dxy down then you are likely to see many of your pairs going into drawdown together, which will be harder for your account to cope with.  
A way around this may be to set your basket with uncorrelated pairs like  
euripy,gbpaud,usdcad,nzdchf and maybe commodities and indices, there are multiple options for this.  
cheers  
Don 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#412](/thread/post/13377067#post13377067 "Post Permalink")

  * Jan 26, 2021 4:04pm  Jan 26, 2021 4:04pm 

  * [ mukundh](mukundh)

  * | Joined Jan 2021  | Status: Trader | [1 Post](/search?do=process&provider=Member&searchuser=1057407)

Good Day to all  
  
I am interested in forward testing this EA on a demo account. I was able to test it out on strategy tester on single pairs and was happy with the drawdowns and performance.  
  
Can someone guide me on applying this EA? Which timeframes and what charts?  
  
I applied it on a single EURUSD M15 chart and i get the smiley face showing its working but it still says waiting for the next tic.  
  
Thanks to all 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#413](/thread/post/13390984#post13390984 "Post Permalink")

  * Edited 4:02am  Feb 3, 2021 3:10am | Edited 4:02am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1061035_1.gif) belami](belami)

  * | Joined Feb 2021  | Status: Trader | [2 Posts](/search?do=process&provider=Member&searchuser=1061035)

Hi all. I've been reading through the forum for a long time but it's the first time I'm going to write.  
  
I'm using Blessing, it seems to me a great EA. But I have a problem that I can't solve and I haven't seen anything in the manual.  
  
I use all the pairs and I use the multiplier X3 and I use it in the 4 hour timeframe. The problem is that sometimes Martinlanga does not do well, I give an example.  
  
If my initial lot is 0.1 in the next trade it should be 0.3 and it almost always is, but sometimes he randomly makes the trade of 0.03. It has happened to me many times and I don't know how to solve it.  
  
I have a lot of free margin to spare, and I don't know why, or if there is any option that may influence, but reading in the manual I can't find an explanation.  
  
I'm using the multipair Blessinglite in this post to download 3.9.6.34 gamma fxtrue, real count in cents from roboforex  
  
I would appreciate any help. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#414](/thread/post/13391058#post13391058 "Post Permalink")

  * Feb 3, 2021 4:01am  Feb 3, 2021 4:01am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1061035_1.gif) belami](belami)

  * | Joined Feb 2021  | Status: Trader | [2 Posts](/search?do=process&provider=Member&searchuser=1061035)

I leave a capture of the problem, the first lot in the real account is 0.08 and the next operation 0.03, that is the error that I am commenting on. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Captura de pantalla 2021-02-02 a las 19.58.22.png
Size: 133 KB](/attachment/image/3852944/thumbnail?d=1612292429)](/attachment/image/3852944?d=1612292429)   

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#415](/thread/post/13398902#post13398902 "Post Permalink")

  * Feb 8, 2021 4:03pm  Feb 8, 2021 4:03pm 

  * [ twonny](twonny)

  * | Joined Mar 2012  | Status: Trader | [39 Posts](/search?do=process&provider=Member&searchuser=242828)

I am having the same problem, the ea isnt working with a start lot size greater than 0.01, as the corresponding trades are calculated incorrectly. I get 0.3, 0.6, 0.04. Can someone fix this problem? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#416](/thread/post/13405611#post13405611 "Post Permalink")

  * Feb 12, 2021 4:22am  Feb 12, 2021 4:22am 

  * [ oberton](oberton)

  * | Joined Dec 2020  | Status: Trader | [2 Posts](/search?do=process&provider=Member&searchuser=1042960)

> [Quoting oberton](/thread/post/13329009#post13329009 "View Quoted Post")
> 
> Disliked
> 
> Thanks for this EA. I have tried it on real account with my set and here is pic of my result for two weeks of trading: started on 2-dec-2020 with $300 and before Christmas I have $600. I am using MA for entry, 5m chart, 1.4 multiplier and 8 currency pairs. MM is false, starting lot is 0.01 and this EA makes around $25 per day with these settings. But I think I am lucky, because $300 as started balance is not enough. Now I am waiting for new year to continue trading with new currency pairs without GBP (I have stopped for the holidays), because currency...
> 
> Ignored

My first investment of $300 now growed up to $1000. My leverage is 1:500 and what I see is that _$100 per currency pair is good balance for 0.01 as starting lot_. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#417](/thread/post/13412266#post13412266 "Post Permalink")

  * Feb 17, 2021 3:39am  Feb 17, 2021 3:39am 

  * [ Gianma](gianma)

  * | Joined Dec 2015  | Status: Trader | [47 Posts](/search?do=process&provider=Member&searchuser=439018)

Hi everyone! Im new here, i read about this Ea and i decided to try it too, just like many of you i saw this Ea dosen't respect some rules same times, for example i can't make it work the pair or the limit of spread that i select. For example if i put " limit spread 10 " the Ea open position on pair with 30 spread or more... Or if i select just EurUsd and UsdYpn the Ea opens other pairs too...  
Anyway i'll will try to fix it later, for now i just want to see how it works and the results.  
My settings now are the same of Oberton, after a week i'll try new strategies 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#418](/thread/post/13423011#post13423011 "Post Permalink")

  * Feb 23, 2021 9:50pm  Feb 23, 2021 9:50pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1049170_5.gif) orderblock](orderblock)

  * Joined Jan 2021 | Status: Trader | [197 Posts](/search?do=process&provider=Member&searchuser=1049170)

Prueba  
  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Captura.PNG
Size: 137 KB](/attachment/image/3871578/thumbnail?d=1614084642)](/attachment/image/3871578?d=1614084642)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#419](/thread/post/13436908#post13436908 "Post Permalink")

  * Mar 4, 2021 2:23pm  Mar 4, 2021 2:23pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar555516_1.gif) phrixusong](phrixusong)

  * Joined Feb 2017 | Status: Trader | [114 Posts](/search?do=process&provider=Member&searchuser=555516)

> [Quoting ursinho4711](/thread/post/12698714#post12698714 "View Quoted Post")
> 
> Disliked
> 
> My first thread in this forum, I am so excited... The idea for this EA started in another thread: <https://www.forexfactory.com/showthread.php?t=792598> Therefore this EA is based on the wonderful EA called “Blessing 3 v3.9.6.09”. The idea to try to build a multipair version came up in the above mentioned thread. After some brainstorming I began to like the idea. Though Blessing and multipair is kind of a contradiction. Blessing has so many parameters to finetune the EA exactly to your pair to trade, the time frame, your risk and and and....
> 
> Ignored

why u disable hedge? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#420](/thread/post/13446470#post13446470 "Post Permalink")

  * Mar 11, 2021 9:13am  Mar 11, 2021 9:13am 

  * [ Btxtrades](btxtrades)

  * | Joined Feb 2021  | Status: Trader | [10 Posts](/search?do=process&provider=Member&searchuser=1070953)

> [Quoting Ismaelgz](/thread/post/13128459#post13128459 "View Quoted Post")
> 
> Disliked
> 
> hello everyone can you tell me why you are giving this error? thank you in advance! {image}
> 
> Ignored

Your file as .txt file extension. remove this and it should work. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Blessing Multipair EA
  *   * [ **Reply to Thread** ](/thread/973998-blessing-multipair-ea/reply#reply)

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

[Trading multipair triangles, no stoploss](/thread/917648-trading-multipair-triangles-no-stoploss "Hello forex Folks! 
  
I'd like to share with You my system that I was comming to for many years. I am testing it these days and it gives...") 78 replies

['Blessing' EA Modification Wanted](/thread/271525-blessing-ea-modification-wanted "Hello. 
 
here is a version of BLESSING \(old\) love this version. 
I wonder if someone could if possible to change this code. 
 
I like that...") 3 replies

[Single, Few Pair Traders (1-4) vs. MultiPair Traders (8-20)](/thread/964171-single-few-pair-traders-1-4-vs-multipair-traders "Who gets better results ?? 
  
Put it in another way , if you went for a trading competition and want to achieve &gt;300% ~ 2000% , what would...") 0 replies

[Coding Request for Multipair MTF ADR Dashboard](/thread/683340-coding-request-for-multipair-mtf-adr-dashboard "Can someone code this into indicator???") 2 replies

[trying to make a multipair buy and sell script](/thread/241746-trying-to-make-a-multipair-buy-and-sell "what i like to do is that i add a script on a chart and it will do 
 
open 3 pairs buys or sells. 
 
for example 0.1 lot EURUSD 
          ...") 6 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/973998-blessing-multipair-ea/reply#reply)
  * Subscribe
  * [97](javascript:void\(0\);)

Attachments: Blessing Multipair EA

Tags: Blessing Multipair EA

#  [](/thread/973998-blessing-multipair-ea)Blessing Multipair EA 

  * 

  * [#421](/thread/post/13446500#post13446500 "Post Permalink")

  * Mar 11, 2021 10:10am  Mar 11, 2021 10:10am 

  * [ Btxtrades](btxtrades)

  * | Joined Feb 2021  | Status: Trader | [10 Posts](/search?do=process&provider=Member&searchuser=1070953)

Just started testing this on a demo account. I'm using oberton's set files and trading the same 8 pairs.  
  
Do I need to just apply it to one chart? or do I have to open each individual chart?  
  
Thanks 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#422](/thread/post/13450857#post13450857 "Post Permalink")

  * Mar 14, 2021 12:57pm  Mar 14, 2021 12:57pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar985431_2.gif) CoolBuddy](coolbuddy)

  * | Joined Jul 2020  | Status: Trader | [67 Posts](/search?do=process&provider=Member&searchuser=985431)

> [Quoting oberton](/thread/post/13405611#post13405611 "View Quoted Post")
> 
> Disliked
> 
> {quote} My first investment of $300 now growed up to $1000. My leverage is 1:500 and what I see is that $100 per currency pair is good balance for 0.01 as starting lot.
> 
> Ignored

Dear oberton,  
How is your account grow by now 

On my way!

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#423](/thread/post/13451573#post13451573 "Post Permalink")

  * Mar 15, 2021 2:06pm  Mar 15, 2021 2:06pm 

  * [ jagankris](jagankris)

  * | Joined Mar 2021  | Status: Trader | [4 Posts](/search?do=process&provider=Member&searchuser=1079194)

Hello Friends,  
  
Jagan newbie trader here and my first post.  
I am newbie to forex algo trading.  
Attached the blessings EA in charts in demo version.  
It is not picking any trades.  
Not sure what mistake I am making.  
  
Any inputs in this regard will be of great help.  
  
Thanks. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#424](/thread/post/13460641#post13460641 "Post Permalink")

  * Mar 20, 2021 3:41am  Mar 20, 2021 3:41am 

  * [ Mtlguy](mtlguy)

  * | Joined Sep 2020  | Status: Trader | [30 Posts](/search?do=process&provider=Member&searchuser=1004086)

I have been running Blessing .34 gamma, with default parameters with a 1000$ demo ECN account for a exactly a week.  
  
Return is 18.5% and P/L -20$, lowest P/L was about -90$.  
  
I will keep it running for another week. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#425](/thread/post/13467135#post13467135 "Post Permalink")

  * Mar 24, 2021 10:37pm  Mar 24, 2021 10:37pm 

  * [ Mtlguy](mtlguy)

  * | Joined Sep 2020  | Status: Trader | [30 Posts](/search?do=process&provider=Member&searchuser=1004086)

> [Quoting Mtlguy](/thread/post/13460641#post13460641 "View Quoted Post")
> 
> Disliked
> 
> I have been running Blessing .34 gamma, with default parameters with a 1000$ demo ECN account for a exactly a week. Return is 18.5% and P/L -20$, lowest P/L was about -90$. I will keep it running for another week.
> 
> Ignored

Well well, the account is wiped because of NZD. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#426](/thread/post/13468759#post13468759 "Post Permalink")

  * Mar 25, 2021 7:32pm  Mar 25, 2021 7:32pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar985431_2.gif) CoolBuddy](coolbuddy)

  * | Joined Jul 2020  | Status: Trader | [67 Posts](/search?do=process&provider=Member&searchuser=985431)

> [Quoting Mtlguy](/thread/post/13467135#post13467135 "View Quoted Post")
> 
> Disliked
> 
> {quote} Well well, the account is wiped because of NZD.
> 
> Ignored

Feels bad man 

On my way!

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#427](/thread/post/13471350#post13471350 "Post Permalink")

  * Mar 27, 2021 1:41am  Mar 27, 2021 1:41am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar555516_1.gif) phrixusong](phrixusong)

  * Joined Feb 2017 | Status: Trader | [114 Posts](/search?do=process&provider=Member&searchuser=555516)

> [Quoting richard96816](/thread/post/12997544#post12997544 "View Quoted Post")
> 
> Disliked
> 
> Martingale requires the doubling of bet size for each LOSS. That's the simple definition. Blessing certainly cannot do that without changing the code. I doubt Multipair Blessing can either. A small string of losses would bankrupt any account that isn't infinite. I know the Blessing manual mentions Martingale. That's very unfortunate. And very wrong. The simple idea of increasing lot size for subsequent (usually winning) trades makes a lot of sense and is very common in effective trading systems. No one said you had to DOUBLE the size every time....
> 
> Ignored

Can you disable Multiplier for the trades within the same setcountarray block? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#428](/thread/post/13471376#post13471376 "Post Permalink")

  * Mar 27, 2021 2:02am  Mar 27, 2021 2:02am 

  * [ Mtlguy](mtlguy)

  * | Joined Sep 2020  | Status: Trader | [30 Posts](/search?do=process&provider=Member&searchuser=1004086)

> [Quoting CoolBuddy](/thread/post/13468759#post13468759 "View Quoted Post")
> 
> Disliked
> 
> {quote} Feels bad man
> 
> Ignored

i have started another demo account with only 5 pairs that are less correlated than the 28 (minus chf) that come with this EA. Let see how it goes. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#429](/thread/post/13471548#post13471548 "Post Permalink")

  * Mar 27, 2021 4:37am  Mar 27, 2021 4:37am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar222411_10.gif) salimc](salimc)

  * | Joined Jan 2012  | Status: Trader | [1,328 Posts](/search?do=process&provider=Member&searchuser=222411)

> [Quoting oberton](/thread/post/13405611#post13405611 "View Quoted Post")
> 
> Disliked
> 
> {quote} My first investment of $300 now growed up to $1000. My leverage is 1:500 and what I see is that $100 per currency pair is good balance for 0.01 as starting lot.
> 
> Ignored

Hi oberton,  
  
How is the EA working now? which pairs are you using?  
Thanks,  
Salim 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#430](/thread/post/13471552#post13471552 "Post Permalink")

  * Mar 27, 2021 4:39am  Mar 27, 2021 4:39am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar222411_10.gif) salimc](salimc)

  * | Joined Jan 2012  | Status: Trader | [1,328 Posts](/search?do=process&provider=Member&searchuser=222411)

> [Quoting Mtlguy](/thread/post/13471376#post13471376 "View Quoted Post")
> 
> Disliked
> 
> {quote} i have started another demo account with only 5 pairs that are less correlated than the 28 (minus chf) that come with this EA. Let see how it goes.
> 
> Ignored

Hello mate,  
Which pairs are you using now? Thanks.  
Salim 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#431](/thread/post/13472335#post13472335 "Post Permalink")

  * Mar 29, 2021 7:58am  Mar 29, 2021 7:58am 

  * [ Mtlguy](mtlguy)

  * | Joined Sep 2020  | Status: Trader | [30 Posts](/search?do=process&provider=Member&searchuser=1004086)

> [Quoting salimc](/thread/post/13471552#post13471552 "View Quoted Post")
> 
> Disliked
> 
> {quote} hello mate, which pairs are you using now? Thanks. Salim
> 
> Ignored

eurusd, eurcad, gbpaud, nzdcad, usdjpy 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#432](/thread/post/13472610#post13472610 "Post Permalink")

  * Mar 29, 2021 3:33pm  Mar 29, 2021 3:33pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar222411_10.gif) salimc](salimc)

  * | Joined Jan 2012  | Status: Trader | [1,328 Posts](/search?do=process&provider=Member&searchuser=222411)

> [Quoting Btxtrades](/thread/post/13446500#post13446500 "View Quoted Post")
> 
> Disliked
> 
> Just started testing this on a demo account. I'm using oberton's set files and trading the same 8 pairs. Do I need to just apply it to one chart? or do I have to open each individual chart? Thanks
> 
> Ignored

Only one chart. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#433](/thread/post/13472737#post13472737 "Post Permalink")

  * Mar 29, 2021 5:14pm  Mar 29, 2021 5:14pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar222411_10.gif) salimc](salimc)

  * | Joined Jan 2012  | Status: Trader | [1,328 Posts](/search?do=process&provider=Member&searchuser=222411)

> [Quoting Mtlguy](/thread/post/13472335#post13472335 "View Quoted Post")
> 
> Disliked
> 
> {quote} eurusd, eurcad, gbpaud, nzdcad, usdjpy
> 
> Ignored

Hi mate,  
Thank you for your input. Every weekend do you turn the holiday shut down feature to false?  
In that case, do you manually close the open and pending trades? Thanks. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#434](/thread/post/13473065#post13473065 "Post Permalink")

  * Mar 29, 2021 8:49pm  Mar 29, 2021 8:49pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar86801_11.gif) emmanuel7788](emmanuel7788)

  * Joined Nov 2008 | Status: Trader | [47,707 Posts](/search?do=process&provider=Member&searchuser=86801)

> [Quoting Mtlguy](/thread/post/13472335#post13472335 "View Quoted Post")
> 
> Disliked
> 
> {quote} eurusd, eurcad, gbpaud, nzdcad, usdjpy
> 
> Ignored

  
>>>>**eurusd, eurcad, gbpaud, nzdcad, usdjpy![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)**  
  
that's what I call a 'balanced choice' to pick one pair from each group to trade in a basket of currency pairs.  
  
Trading Currency Pairs – Groups 2021  
**Group#1**  
AUDUSD  
**EURUSD**  
GBPUSD  
USDCAD  
NZDUSD  
  
**Group#2**  
EURAUD  
EURNZD  
**EURCAD**  
EURGBP***  
  
**Group#3**  
**GBPAUD**  
GBPNZD  
GBPCAD  
  
**Group#4**  
**USDJPY**  
AUDJPY  
EURJPY  
GBPJPY  
SGDJPY  
  
**Group#5**  
AUDCAD  
AUDNZD  
**NZDCAD**  
  
**Group#6**  
AUDSGD  
EURSGD  
GBPSGD  
USDSGD  
NZDSGD 

Honesty is a very expensive gift. You wont find it in cheap people.WBuffett

[1 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#435](/thread/post/13473386#post13473386 "Post Permalink")

  * Mar 29, 2021 11:45pm  Mar 29, 2021 11:45pm 

  * [ Mtlguy](mtlguy)

  * | Joined Sep 2020  | Status: Trader | [30 Posts](/search?do=process&provider=Member&searchuser=1004086)

> [Quoting salimc](/thread/post/13472737#post13472737 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi mate, Thank you for your input. Every weekend do you turn the holiday shut down feature to false? In that case, do you manually close the open and pending trades? Thanks.
> 
> Ignored

no i don’t bother with that, I leave it open. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#436](/thread/post/13473389#post13473389 "Post Permalink")

  * Mar 29, 2021 11:46pm  Mar 29, 2021 11:46pm 

  * [ Mtlguy](mtlguy)

  * | Joined Sep 2020  | Status: Trader | [30 Posts](/search?do=process&provider=Member&searchuser=1004086)

> [Quoting emmanuel7788](/thread/post/13473065#post13473065 "View Quoted Post")
> 
> Disliked
> 
> {quote} >>>> eurusd, eurcad, gbpaud, nzdcad, usdjpy ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1) that's what I call a 'balanced choice' to pick one pair from each group to trade in a basket of currency pairs. Trading Currency Pairs – Groups 2021 Group#1 AUDUSD EURUSD GBPUSD USDCAD NZDUSD Group#2 EURAUD EURNZD EURCAD EURGBP*** Group#3 GBPAUD GBPNZD GBPCAD Group#4 USDJPY AUDJPY EURJPY GBPJPY SGDJPY Group#5 AUDCAD AUDNZD NZDCAD Group#6 AUDSGD EURSGD GBPSGD USDSGD NZDSGD
> 
> Ignored

actually I built that list from one of your older posts. I take no credit for this idea. Thanks a lot.   
  
i see you added a 6th group; which one do you recommend in that group in respect to my list ? Thanks! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#437](/thread/post/13475817#post13475817 "Post Permalink")

  * Mar 31, 2021 9:56am  Mar 31, 2021 9:56am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar86801_11.gif) emmanuel7788](emmanuel7788)

  * Joined Nov 2008 | Status: Trader | [47,707 Posts](/search?do=process&provider=Member&searchuser=86801)

> [Quoting Mtlguy](/thread/post/13473389#post13473389 "View Quoted Post")
> 
> Disliked
> 
> {quote} actually I built that list from one of your older posts. I take no credit for this idea. Thanks a lot. i see you added a 6th group; which one do you recommend in that group in respect to my list ? Thanks!
> 
> Ignored

from   
**Group#6**  
AUDSGD  
EURSGD  
GBPSGD  
USDSGD  
NZDSGD  
  
  
my favourite pairs are AUDSGD and USDSGD,  
  
but pick only the one from the five SGD pairs with the best setup and show Weekly conditions for swing trading. Avoid narrow range weekly market type conditions. 

Honesty is a very expensive gift. You wont find it in cheap people.WBuffett

[1 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#438](/thread/post/13479528#post13479528 "Post Permalink")

  * Apr 2, 2021 7:24pm  Apr 2, 2021 7:24pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar945375_1.gif) shadmar](shadmar)

  * | Joined Apr 2020  | Status: Trader | [89 Posts](/search?do=process&provider=Member&searchuser=945375)

Are you guys able to make this run stable, it seems to crash atleast once per day, on my end.   
I ended up going for the Blessing single pair instead, running many in parallel. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#439](/thread/post/13480893#post13480893 "Post Permalink")

  * Apr 4, 2021 6:17pm  Apr 4, 2021 6:17pm 

  * [ aliaksandrb](aliaksandrb)

  * | Joined Apr 2021  | Status: Trader | [3 Posts](/search?do=process&provider=Member&searchuser=1087439)

good ea 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#440](/thread/post/13507361#post13507361 "Post Permalink")

  * Apr 23, 2021 1:34am  Apr 23, 2021 1:34am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1094540_1.gif) FX6588](fx6588)

  * | Joined Apr 2021  | Status: Trader | [79 Posts](/search?do=process&provider=Member&searchuser=1094540)

[quote = oberton; 13329009]感谢您使用此EA。我已经用我的套装在真实帐户中尝试过了，这是我连续两周的交易结果的图片：始于2020年12月2日，价格为300美元，圣诞节前为600美元。我正在使用MA进行输入，5m图表，1.4乘数和8个货币对。MM是错误的，起始手数是0.01，使用这些设置，此EA每天大约能赚25美元。但是我觉得我很幸运，因为$ 300的初始余额还不够。现在我正在等待新年继续使用不含GBP的新货币对进行交易（我已假期休假），因为含英镑的货币对在英国退欧中是危险的。但是您决定如何冒险。祝大家圣诞快乐。{image} {file} [/ quote]  
Are you still using this EA? What is your TF? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Blessing Multipair EA
  *   * [ **Reply to Thread** ](/thread/973998-blessing-multipair-ea/reply#reply)

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

[Trading multipair triangles, no stoploss](/thread/917648-trading-multipair-triangles-no-stoploss "Hello forex Folks! 
  
I'd like to share with You my system that I was comming to for many years. I am testing it these days and it gives...") 78 replies

['Blessing' EA Modification Wanted](/thread/271525-blessing-ea-modification-wanted "Hello. 
 
here is a version of BLESSING \(old\) love this version. 
I wonder if someone could if possible to change this code. 
 
I like that...") 3 replies

[Single, Few Pair Traders (1-4) vs. MultiPair Traders (8-20)](/thread/964171-single-few-pair-traders-1-4-vs-multipair-traders "Who gets better results ?? 
  
Put it in another way , if you went for a trading competition and want to achieve &gt;300% ~ 2000% , what would...") 0 replies

[Coding Request for Multipair MTF ADR Dashboard](/thread/683340-coding-request-for-multipair-mtf-adr-dashboard "Can someone code this into indicator???") 2 replies

[trying to make a multipair buy and sell script](/thread/241746-trying-to-make-a-multipair-buy-and-sell "what i like to do is that i add a script on a chart and it will do 
 
open 3 pairs buys or sells. 
 
for example 0.1 lot EURUSD 
          ...") 6 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/973998-blessing-multipair-ea/reply#reply)
  * Subscribe
  * [97](javascript:void\(0\);)

Attachments: Blessing Multipair EA

Tags: Blessing Multipair EA

#  [](/thread/973998-blessing-multipair-ea)Blessing Multipair EA 

  * 

  * [#441](/thread/post/13550389#post13550389 "Post Permalink")

  * May 24, 2021 3:50pm  May 24, 2021 3:50pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar555516_1.gif) phrixusong](phrixusong)

  * Joined Feb 2017 | Status: Trader | [114 Posts](/search?do=process&provider=Member&searchuser=555516)

> [Quoting fxtrue](/thread/post/12745279#post12745279 "View Quoted Post")
> 
> Disliked
> 
> I'm attaching my edited source code version of "gamma" (for MT4) plus a compiled MT5 version. Please note that the following: 1) there are almost 40 edits / fixes in this version - several of which are critical (they can be located by searching for "fxtrue") 2) I would appreciate my changes being carried through to all new versions of BlessingLite - particularly as many are needed for the MT5 version and I don't have time to waste re-implementing the same fixes over and over 3) there is a potentially-serious underlying issue with incorrectly initialised...
> 
> Ignored

I amended some codes which could potentially produce errors.  
Besides, I added "LevelLinearLots" in 

> [Quoting rob123490](/thread/post/12231976#post12231976 "View Quoted Post")
> 
> Disliked
> 
> Eventually, I have found an alternative version of b3 using multi-indicators that I would like to share with the community, I didn't test it yet, might be you want to try it. please just share your comments if perform well or not. {file}
> 
> Ignored

, which could allow EA to start multiply at levels you define, which could reduce DD. 

Attached File(s)

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [BlessingLite_3_v3.9.6.34_gamma_fxtrue_P.mq4](/attachment/file/3946391?d=1621839070) 134 KB | 1,299 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#442](/thread/post/13589694#post13589694 "Post Permalink")

  * Jun 18, 2021 4:36pm  Jun 18, 2021 4:36pm 

  * [ nckenn](nckenn)

  * | Joined May 2021  | Status: Trader | [3 Posts](/search?do=process&provider=Member&searchuser=1105591)

> [Quoting oberton](/thread/post/13405611#post13405611 "View Quoted Post")
> 
> Disliked
> 
> {quote} My first investment of $300 now growed up to $1000. My leverage is 1:500 and what I see is that $100 per currency pair is good balance for 0.01 as starting lot.
> 
> Ignored

Do you still use your set now? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#443](/thread/post/13591166#post13591166 "Post Permalink")

  * Jun 19, 2021 3:56pm  Jun 19, 2021 3:56pm 

  * [ genozzolo](genozzolo)

  * | Joined Jul 2020  | Status: Trader | [4 Posts](/search?do=process&provider=Member&searchuser=974609)

Hi, great work and thanks for sharing.  
  
I would like to ask, Im trying MT5 version in strategy tester.  
  
On BlessingLite_3_v3.9.6.34_gamma_fxtrue version I get this error :  
  
  
2021.06.19 08:55:31.612 Core 1 2018.01.03 21:28:20 cannot load indicator 'Moving Average' [4805]  
2021.06.19 08:55:31.612 Core 1 2018.01.03 21:28:20 The iMA object was not created: Error4805  
  
It disappear if I use debug True, but I would like to ask if I did something wrong on my side  
  
Another question, also with BlessingLite_3_v3.9.6.34_gamma_fxtrue I should use enable once per bar FALSE ?   
  
Thanks! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#444](/thread/post/13599365#post13599365 "Post Permalink")

  * Jun 25, 2021 11:19am  Jun 25, 2021 11:19am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar555516_1.gif) phrixusong](phrixusong)

  * Joined Feb 2017 | Status: Trader | [114 Posts](/search?do=process&provider=Member&searchuser=555516)

> [Quoting genozzolo](/thread/post/13591166#post13591166 "View Quoted Post")
> 
> Disliked
> 
> Hi, great work and thanks for sharing. I would like to ask, Im trying MT5 version in strategy tester. On BlessingLite_3_v3.9.6.34_gamma_fxtrue version I get this error : 2021.06.19 08:55:31.612 Core 1 2018.01.03 21:28:20 cannot load indicator 'Moving Average' [4805] 2021.06.19 08:55:31.612 Core 1 2018.01.03 21:28:20 The iMA object was not created: Error4805 It disappear if I use debug True, but I would like to ask if I did something wrong on my side Another question, also with BlessingLite_3_v3.9.6.34_gamma_fxtrue I should use enable once per bar...
> 
> Ignored

1\. No error generated   
2\. Use enable once per bar TRUE.  
(But you can test if FALSE works as well)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#445](/thread/post/13618629#post13618629 "Post Permalink")

  * Jul 9, 2021 4:43am  Jul 9, 2021 4:43am 

  * [ genozzolo](genozzolo)

  * | Joined Jul 2020  | Status: Trader | [4 Posts](/search?do=process&provider=Member&searchuser=974609)

Hi  
  
Incredibile EA, just 1 annoying problem, it doesnt end backtest, instead I get at end of log a spam of  
"  
2021.07.08 21:42:11.610 Core 1 2020.10.29 23:59:59 Reason; Blessing Removed  
"  
  
It get stuck and Ive to end it manually and restart MT5, so I also dont get report and stuffs to check data.  
  
Any solution ?  
  
thanks! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#446](/thread/post/13647453#post13647453 "Post Permalink")

  * Jul 29, 2021 10:29pm  Jul 29, 2021 10:29pm 

  * [ EpicSeo](epicseo)

  * | Joined Jun 2021  | Status: Trader | [6 Posts](/search?do=process&provider=Member&searchuser=1148649)

Hi upon doing some back test it says no market info for audcad but im ticking it with eurusd  
  
how come? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#447](/thread/post/13655131#post13655131 "Post Permalink")

  * Aug 5, 2021 12:40am  Aug 5, 2021 12:40am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar337765_5.gif) dokopy](dokopy)

  * Joined May 2013 | Status: Trader | [894 Posts](/search?do=process&provider=Member&searchuser=337765)

> [Quoting ursinho4711](/thread/post/12698714#post12698714 "View Quoted Post")
> 
> Disliked
> 
> My first thread in this forum, I am so excited... The idea for this EA started in another thread: <https://www.forexfactory.com/showthread.php?t=792598> Therefore this EA is based on the wonderful EA called “Blessing 3 v3.9.6.09”. The idea to try to build a multipair version came up in the above mentioned thread. After some brainstorming I began to like the idea. Though Blessing and multipair is kind of a contradiction. Blessing has so many parameters to finetune the EA exactly to your pair to trade, the time frame, your risk and and and....
> 
> Ignored

I only try EA with one pair. Restarting the profile closes all positions. Is there anything you can do about it? EA gets out of a larger drawdown, but premature closure is very undesirable. 

Please excuse the bad English via Google Translate.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#448](/thread/post/13692680#post13692680 "Post Permalink")

  * Sep 3, 2021 5:06pm  Sep 3, 2021 5:06pm 

  * [ ayush9342](ayush9342)

  * | Joined Nov 2019  | Status: Trader | [10 Posts](/search?do=process&provider=Member&searchuser=885838)

I think there is a bug in the ea as i have attached the image where sometimes the ea keep on modifying the orders without any reason. I have set max trades to 3 but the ea isnt closing the trades for almost 5 months and then finally closes at a loss. Before that it works properly like it closes the trades when it reaches max trades=3 but sometimes like in the picture it keeps the trades running. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#449](/thread/post/14810121#post14810121 "Post Permalink")

  * Mar 27, 2024 10:30pm  Mar 27, 2024 10:30pm 

  * [ MarcoOne](marcoone)

  * | Joined Feb 2024  | Status: Trader | [4 Posts](/search?do=process&provider=Member&searchuser=1792394)

Hi guys ,this Ea never opening from a several days 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#450](/thread/post/14823537#post14823537 "Post Permalink")

  * Apr 9, 2024 1:00pm  Apr 9, 2024 1:00pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar555516_1.gif) phrixusong](phrixusong)

  * Joined Feb 2017 | Status: Trader | [114 Posts](/search?do=process&provider=Member&searchuser=555516)

> [Quoting dokopy](/thread/post/13655131#post13655131 "View Quoted Post")
> 
> Disliked
> 
> {quote} I only try EA with one pair. Restarting the profile closes all positions. Is there anything you can do about it? EA gets out of a larger drawdown, but premature closure is very undesirable.
> 
> Ignored

you can remove JPY pairs in the code line 251 to prevent large drawdown. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#451](/thread/post/14916385#post14916385 "Post Permalink")

  * Jun 30, 2024 8:07pm  Jun 30, 2024 8:07pm 

  * [ ibdoma](ibdoma)

  * | Joined Jul 2022  | Status: Trader | [3 Posts](/search?do=process&provider=Member&searchuser=1475208)

please I can someone help Implement the trading logic in blessing mt4 version to this code 

Attached File(s)

![File Type: txt](https://assets.faireconomy.media/images/attach/txt.gif) [mql5.txt](/attachment/file/4749063?d=1719745629) 9 KB | 54 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#452](/thread/post/14932194#post14932194 "Post Permalink")

  * Last Post: Jul 16, 2024 3:49am  Jul 16, 2024 3:49am 

  * [ iorinhoj](iorinhoj)

  * | Joined Mar 2023  | Status: Trader | [1 Post](/search?do=process&provider=Member&searchuser=1607506)

Hi guys, need help on this error, testing this EA to mt5 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 51 KB](/attachment/image/4759122/thumbnail?d=1721069332)](/attachment/image/4759122?d=1721069332)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Blessing Multipair EA
  *   * [ **Reply to Thread** ](/thread/973998-blessing-multipair-ea/reply#reply)

[](https://www.forexfactory.com "Homepage")

  * [Forums](forums)
  * [Trades](trades)
  * [Calendar](calendar)
  * [News](news)
  * [Market](market)
  * [Brokers](brokers)

****

[](https://www.faireconomy.com/)
