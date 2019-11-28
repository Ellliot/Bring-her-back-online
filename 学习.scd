"Hello World".postln;
{SinOsc.ar}.plays;
s.volume.gui;
{SinOsc.ar(LFNoise0.kr(10).range(500,1500), mul: 0.1)}.play;

{RLPF.ar(Dust.ar([12.15]), LFNoise1.ar([0.3,0.2]).range(100,3000), 0.02)}.play;
2+2;
"I am SuperCollider 3".speak;
{Pan2.ar(SinOsc.ar(440,0,0.01,10),0.0)}.play;
{Pan2.ar(SinOsc.ar(MouseX.kr(261.6,880),0,0.1),0.0)}.play;
//A cool synth sound that can change according to mouse movement
(
{
	var n = 11;

	Resonz.ar(
		Mix.fill(n,{

			var freq = rrand(50,560.3);
			var numcps = rrand(2,20);

			Pan2.ar(Gendy1.ar(6.rand,6.rand,1.0.rand,1.0.rand, freq, freq, 1.0.rand,1.0.rand, numcps, SinOsc.kr(exprand(0.02,0.2), 0, numcps/2, numcps/2), 0.5/(n.sqrt)), 1.0.rand2)
		}),
		2100,//MouseX.kr(100,2000),
		1//MouseY.kr(0.01,1.0)
		);
	}.play
)
( //This is exciting

{
	Pan2.ar(SinOsc.ar(440,0,0.1)+Pulse.kr(261,0.6,0.05))}.play
)
//Rising bubbles
( // select everything between the two parentheses
{ CombN.ar(
	SinOsc.ar(
		LFNoise1.kr(
			4, // freq
			24, // range
			LFSaw.kr(
				[8,7.23],//freq
				0,
				3, // range
				80 // offset
			)
		).midicps,
		0,
		0.04
	),
	0.2, // max delay
	0.2, // actual delay
	4 // decay
)
}.play
)


FreqScope.new;
(
{Pan2.ar(HPF.ar(
	Blip.ar(
		100,
		10
	),
	Line.kr(10000,1000,10)
)
)
}.scope)

{Resonz.ar(LFNoise0.ar(400),1000,0.1)}.scope
{SinOsc.ar([400,600,870],0,0.1)}.scope
{Pan2.ar(WhiteNoise.ar(0.1), MouseX.kr(-1,1))}.scope
{Mix(SinOsc.ar([400,660]),0,0.1)}.scope
(
{
	var n = 10;
	var wave = Mix.fill(10,{|i|
	var mult = ((-1)**i)*(0.5/((i+1)));
	SinOsc.ar(440*(i+1))*mult
	});
	Pan2.ar(wave/n,0.0);

}.scope;
)

{Mix(SinOsc.ar(500*[0.5,1,1.19,1.56,2,2.51,2.66,3.01,4.1],0,0.1))}.scope

{Mix(SinOsc.ar(500*[0.5,1,1.19,1.56,2,2.51,2.66,3.01,4.1],0,0.1*[0.25,1,0.8,0.5,0.9,0.4,0.3,0.6,0.1]))}.scope
(1..10)
(
var n = 10;

{Mix(SinOsc.ar(250*(1..n),0,1/n))}.scope;

)
{SinOsc.ar(mul:2.0)}.scope
{SinOsc.ar(mul:MouseY.kr(1.0,0.1))}.scope
{SinOsc.ar(MouseX.kr(440,880), 0.0, 0.1, 0.0)}.scope
{SinOsc.ar(mul:MouseY.kr(1.0,0.1))}.scope
{SinOsc.ar(mul:0.1, add:MouseY.kr(0.9,-0.9))}.scope
{SinOsc.ar(mul:MouseX.kr(0.1,1.0), add:MouseY.kr(0.9,-0.9))}.scope
(
{
	//cutoff values need to be sensible frequencies in Hz; here sine output turned from -1 to 1 into 2000+-1700
	//var cutoff = 	SinOsc.ar(1,mul:MouseX.kr(0.0,1700.0), add:2000.0);
	var cutoff = SinOsc.ar(1)*1700.0 + 2000.0;  //same thing
	LPF.ar(WhiteNoise.ar,freq:cutoff);
}.scope
)
{SinOsc.ar(SinOsc.ar(3,mul:40,add:440),0,0.1)}.scope
a = {SinOsc.ar(440)*0.1}.play
a.run(false)
a.run
a.free
a = {arg freq =440; SinOsc.ar(freq)*0.1}.play
a.set(\freq,330)
a = {arg freq=440, amp = 0.1; SinOsc.ar(freq)*amp}.play
a.set(\freq,rrand(220,440), \amp, rrand(0.05,0.2))

(
{
	var carrier, modulator, carrfreq, modfreq;`

	carrfreq = MouseX.kr(440,5000,'exponential');
	modfreq = MouseY.kr(1,5000,'exponential');

	carrier = SinOsc.ar(carrfreq, 0, 0.5);
	modulator = SinOsc.ar(modfreq, 0, 0.25, 0.25);

	carrier*modulator;
}.scope
)

(
var w, carrfreqslider, modfreqslider, moddepthslider,synth;

w = Window("frequency modulation", Rect(100,400,400,300));

w.view.decorator = FlowLayout(w.view.bounds);

synth= {arg carrfreq=440, modfreq=1, moddepth=0.01;

	SinOsc.ar(carrfreq+(moddepth*SinOsc.ar(modfreq)), 0, 0.25)}.scope;

carrfreqslider = EZSlider(w, 300@50, "carrfreq", ControlSpec(20,5000,'exponential', 10, 440), {|ez| synth.set(\carrfreq, ez.value)});
w.view.decorator.nextLine;

modfreqslider= EZSlider(w, 300@50, "modfreq", ControlSpec(1,5000, 'exponential', 1,1), {|ez| synth.set(\modfreq, ez.value)});
w.view.decorator.nextLine;

moddepthslider= EZSlider(w, 300@50, "moddepth", ControlSpec(0.01, 5000, 'linear', 0.01, 0.01), {|ez|  synth.set(\moddepth, ez.value)});

w.front;
)


SynthDef(\sine, {Out.ar(0, SinOsc.ar(Rand(440, 880), 0, 0.1))}).add

a=Synth(\sine);
b=Synth(\sine);
c=Synth(\sine);

a.free;
b.free;
c.free;
(
SynthDef(\event, { arg freq= 440, amp= 0.5, pan= 0.0;
	var env;

	env = EnvGen.ar( Env([0,1,1,0], [0.01, 0.1, 0.2]), doneAction:2);
	Out.ar(0, Pan2.ar(SinOsc.ar(Rand(440, 880)) * env * amp, pan))}).add;

)
Synth(\event);
(
{
	Synth(\event);

	1.0.wait;

	Synth(\event);

}.fork;
)
(
{

	8.do{
		Synth(\event);
		0.5.wait;
	};

}.fork;
)

4.do{arg repeatnumber; repeatnumber.postln; "iteration complete".postln;};

(
w = Window.new("I catch keystrokes");
w.view.keyDownAction = { arg view, char, modifiers, unicode, keycode;  [char, keycode].postln; };
w.front;
)

// then execute this and then press the 'j' key
(
w = Window.new("I catch keystrokes");
w.front; // something safe to type on
{SinOsc.ar(800, 0, KeyState.kr(38, 0, 1)) }.play;
)

(
SynthDef(\cello1, {
  var freq = \freq.kr(440);
  var amp = \amp.kr(0.5);
  var gate = \gate.kr(1);
  var osc1 = Pulse.ar(freq, 0.1);
  //var osc1 = Saw.ar(freq);
  var osc2 = Pulse.ar(freq);
  var lfo = 0.1 * SinOsc.kr(7.5);
  var out = (osc1 + osc2) * 0.5;
  var aenv = EnvGen.ar(Env.asr(0.06, 1, 0.3), gate, doneAction: Done.freeSelf);
  out = DFM1.ar(out, EnvGen.kr(Env.adsr(0, 3.29, 0.78, 3), gate).linexp(0, 1, 40,  10000), 0) * aenv;
  Out.ar(\bus.kr(0), out * (1 + lfo));
}).add
)
(
Pbind(
  \instrument, \cello1,
  \degree, Pseq([0, 2, 4, 2], inf),
  \octave, 4,
  \dur, 1,
  \amp, 0.4
).play)

SynthDef(\softfrog, {
arg out, freq=440, prate=180, pwidth=0.5,
sustain=0.3, amp=0.1;
var env, u;
env = Env.linen(Rand(0.001, 0.003), Rand(0.1, 0.3), 0.01);
freq = freq + LFNoise2.kr(5, 10);
u = SinOsc.ar(
freq,
LFPulse.perform(x,
prate,
0,
Line.kr(pwidth, 0, sustain)
),
amp
);
u = BRF.ar(u, freq, 0.1) * EnvGen.kr(env, doneAction:2);
Out.ar(out, Pan2.ar(u, Rand(-1,1)))
}).add;

SynthDef(\reed, {
    |out = 0, freq = 440, amp = 0.1, gate = 1, attack = 0.3, release = 0.3|
    var snd, blow;
    // pulse with modulating width
    snd = Pulse.ar((Rand(-0.03, 0.05) + freq.cpsmidi).midicps, 0.48 + LFNoise1.kr(0.06, 0.1), 0.2);
    // add a little "grit" to the reed
    snd = Disintegrator.ar(snd, 0.5, 0.7);
    // a little ebb and flow in volume
    snd = snd * LFNoise2.kr(5, 0.05, 1);
    // use the same signal to control both the resonant freq and the amplitude
    blow = EnvGen.ar(Env.asr(attack, 1.0, release), gate, doneAction: 2);
    snd = snd + BPF.ar(snd, blow.linexp(0, 1, 2000, 2442), 0.3, 3);
    // boost the high end a bit to get a buzzier sound
    snd = BHiShelf.ar(snd, 1200, 1, 3);
    snd = snd * blow;
    Out.ar(out, Pan2.ar(snd, 0, amp));
}).add;

a = Synth(\reed);
Pbind(
    \instrument, \reed,
    \amp, 0.1*(2**Pgauss(0, 0.1)),
    \dur, 5.0,
    \legato, 1,
    \root, 1,
    \attack, 0.2,
    \release, 0.2,
    \degree, Pseq([[-7, -3, 0, 2], [-7, -2, 0, 3], [-7, -1, 1, 4]].mirror1, inf)
).play;



(
var genPolynom = { arg depart ... l;
	var function =
	"{arg x; %% }".format(
		depart,
		l.collect({ arg v, i;
		  " + (% * ( x div: % ))".format(v, i + 1)
	    }).join
	);
	function.compile().value;
};

var un = genPolynom.(0, 1);
var deux = genPolynom.(2, 4, 1);
var trois = genPolynom.(5, 5, -1);

a = (..20).collect({ arg i;
	[un.(i), trois.(i) ] % 7
})
)

(
Pdef(\a,
Pbind(
	\tempo, 2,
	\degree, Pseq(a).repeat,
		\octave, [3, 5],
		\amp, [2, 1] * 0.1,
		)).play
)
Env.shapeNames;
SynthDef("sawSynth", { arg freq = 440, amp = 0.1, att = 0.1, sus = 5, lofreq = 100, hifreq = 3000, out, gate = 1, release = 0.1;
    var env, snd, gen;
    env = Env.adsr(0.02, release, amp);
	gen = EnvGen.kr(env, gate, doneAction: Done.freeSelf);
    snd = Saw.ar(freq: freq * [0.99, 1, 1.001, 1.008], mul: gen);
	snd = LPF.ar(
		in: snd,
		freq: LFNoise2.kr(1).range(lofreq, hifreq)
	);
    snd = Splay.ar(snd);
    Out.ar(0, snd);
// Basic saw synth for chords and bass
//By Bruno Ruviaro
//http://sccode.org/1-54H
}).add;

a = Synth(\sawSynth);
b = Synth(\sawSynth, [\release, 2]);
a.release;
a.set(\gate, 0); // alternatively, you can write a.release;
b.set(\gate, 0);

SynthDef(\apad_mh, {
	arg
	//Standard Values:
	out = 0, pan = 0, freq = 880, amp = 0.5, att = 0.4, dec = 0.5, sus = 0.8, rel = 1.0, gate = 1,
	//Other Controls:
	vibratoRate = 4, vibratoDepth = 0.015, tremoloRate = 5,
	//These controls go from 0 to 1:
	tremoloDepth = 0.5, reverbMix = 0.5, roomSize = 1, damp = 0.5;

	var env, snd, vibrato, tremolo, mod2, mod3;

	env = Env.adsr(att, dec, sus, rel).kr(gate: gate);
	vibrato = SinOsc.kr(vibratoRate).range(freq * (1 - vibratoDepth), freq * (1 + vibratoDepth));
	tremolo = LFNoise2.kr(1).range(0.2, 1) * SinOsc.kr(tremoloRate).range((1 - tremoloDepth), 1);

	snd = SinOsc.ar(freq: [freq, vibrato], mul:(env * tremolo * amp)).distort;
	snd = Mix.ar([snd]);
	snd = FreeVerb.ar(snd, reverbMix, roomSize, damp);

	DetectSilence.ar(snd, 0.0001, 0.2, doneAction: 2);
	Out.ar(out, Pan2.ar(snd, pan));
},
metadata:(
	credit: "Mike Hairston",
	tags: [\pad, \vibrato, \sustained]
	)
).add

a = Synth(\apad_mh)
Platform.resourceDir;
(
//this loads into a buffer the default sound that comes with SuperCollider
//.read brings in the whole sound at once
b = Buffer.read(s,Platform.resourceDir +/+ "sounds/a11wlk01.wav"); //store handle to Buffer in global variable b
c = Buffer.read(s,"/Users/Fred/Desktop/PinCollider/An Adventure.wav");
d = Buffer.read(s,"/Users/Fred/Desktop/PinCollider/An Adventure beginning.wav");
e = Buffer.read(s,"/Users/Fred/Desktop/PinCollider/Yellow.wav");

SynthDef("playbuf",{ arg out=0,bufnum=2, rate=1, trigger=1, startPos=0, loop=1;
	Out.ar(out,
		Pan2.ar(PlayBuf.ar(1,bufnum, BufRateScale.kr(bufnum)*rate, trigger, BufFrames.ir(bufnum)*startPos, loop),0.0)
	)
}).add;
)


Synth(\playbuf, [\out, 0, \bufnum, b.bufnum, \rate, 0.5]);
a = Synth(\playbuf)