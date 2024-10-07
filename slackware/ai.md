

# A.I

As you know artificial intelligence is has to do more with hardware than software to run locally. <br>
**Hardware** is your business... <br>

**Software** is like this:
Slackware dont split libraries like other distros to liba , liba-dev etc...<br>  
In Slackware when a library is installed , then user know that all library source is installed. `;)`
<br>
There are several deps and 3rd programs to run locally an ai-model and if some deps are not already in the installation you will find them on SBo repo. <br>
In special cases you might need to use `pip` but thats ok!.<br>
*NOTE*: that in Slackware you also have all Qt(x) installer in your installation! 

*LLAMA.cpp* , *ollama*, *GPT4All* etc... are fine in a Slackware system if you know how to install and use them...<br>


#### security issues

In any case be carefully when you ran local an AI model or when use its API and give it access to your local files (docs,images etc...)<br>
AIs want your data, that is something it must be clear. THEY WANT YOUR DATA.<br>
If a company is know as personal data tracker from other projects it has... how you can trust it now? Because ?<br>
Some small project say that run locally and private. Maybe its true maybe not, maybe its true now maybe not in future...who knows? who read 1.000.000 python code lines to be sure?<br>
Some other had simple code easy to read in theory but a sqlite exist in `~/.config/some_name/12345/54321/some_other_name/wtf/*` <br>
hm...<br>
If you are interesting for privacy be smart before use them, else...do what you like!. <br>


---

#### TIPS

There is script written from scratch for Slackware-current but it ll also work in other Linux systems.<br>
It download locally from `https://huggingface.co/` the model you want and Quantizing it using LlamaCpp to a gguf model for locally use!<br>
Requires: `numpy,sentencepiece,gguf` from python and `git lfs`<br>
You can find it [here](https://raw.githubusercontent.com/rizitis/Quantizing_with_LlamaCpp/refs/heads/main/quantizing_ai_models.sh)
<br>
After that you can use model as you like with the correct app of your choice... ;)
