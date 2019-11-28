SynthDef(\sine, { |out = 0, freq = 440.0, gain = 0.0|
	Out.ar(out, Pan2.ar(SinOsc.ar(freq, mul:gain)));
}).store;


SynthDef(\playbuf,{ arg out=0,bufnum=0, rate=1, trigger=1, startPos=0, loop=1;
	Out.ar(out,
		Pan2.ar(PlayBuf.ar(1,bufnum, BufRateScale.kr(bufnum)*rate, trigger, BufFrames.ir(bufnum)*startPos, loop),0.0)
	)
}).store;

(
SynthDef(\event1, { arg freq= 440, amp= 0.1, pan= 0.0;
	var env;

	env = EnvGen.ar( Env([0,1,1,0], [0.01, 0.1, 0.2]), doneAction:2);
	Out.ar(0, Pan2.ar(Saw.ar(Rand(440, 880)) * env * amp, pan))}).store;

)
(
SynthDef(\event2, { arg freq= 440, amp= 0.5, pan= 0.0;
	var env;

	env = EnvGen.ar( Env([0,1,1,0], [0.01, 0.1, 0.2]), doneAction:2);
	Out.ar(0, Pan2.ar(SinOsc.ar(Rand(440, 880)) * env * amp, pan))}).store;

)

SynthDef(\bubbly, { |out = 0, decay = 4, delay = 0.2, range = 7.23, freq = 4, gain = 0.0|
	Out.ar(0, Pan2.ar(CombN.ar(SinOsc.ar(LFNoise1.kr(freq, 24,
		LFSaw.kr([8,range],0,3,80)).midicps,0,0.04),0.2, delay,  decay
)))
}).store;
a = Synth(\blue);

(
SynthDef(\atari2600, {|out= 0, gate= 1, tone0= 5,tone1= 8, freq0= 10, freq1= 20, amp= 0.1, pan= 0|
	var e, z;
	e= EnvGen.kr(Env.asr(0.01, amp, 0.05), gate, doneAction:2);
	z= Atari2600.ar(tone0, tone1, freq0, freq1, 15, 15);
	Out.ar(out, Pan2.ar(z*e, pan));
}).store
)

SynthDef( \resonz,
{ |freq = 100,  bwr = 0.01|
	var n = 11;
	Out.ar( 0,
			Resonz.ar(
		Mix.fill(n,{

			var freq = rrand(50,560.3);
			var numcps = rrand(2,20);

			Pan2.ar(Gendy1.ar(6.rand,6.rand,1.0.rand,1.0.rand, freq, freq, 1.0.rand,1.0.rand, numcps,
						SinOsc.kr(exprand(0.02,0.2), 0, numcps/2, numcps/2), 0.5/(n.sqrt)), 1.0.rand2)
		}),
		freq, //MouseX.kr(100,2000),
		bwr//MouseY.kr(0.01,1.0)
		);
	)}
).store;

Platform.systemExtensionDir;

{Atari2600.ar}.play
Soundfile examples

(
Pbind(
\instrument, \atari2600,
\dur, Pseq([0.25, 0.25, 0.25, 0.45], inf),
\amp, 0.8,
\tone0, Pseq([Pseq([2, 5], 32), Pseq([3, 5], 32)], inf),
\tone1, 14,
\freq0, Pseq([Pbrown(28, 31, 1, 32),
Pbrown(23, 26, 3, 32)], inf),
\freq1, Pseq([Pn(10, 16), Pn(11, 16)], inf)
).play
)

SynthDef(\sawPad, { arg freq = 440, amp = 0.1, att = 0.02, sus = 5, lofreq = 100, hifreq = 3000, out, gate = 1, release = 0.1;
    var env, snd, gen;
    env = Env.adsr(att, release, amp);
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
}).store;

b = Buffer.read(s,Platform.resourceDir +/+ "sounds/a11wlk01.wav"); //store handle to Buffer in global variable b
c = Buffer.read(s,"/Users/Fred/Desktop/PinCollider/An Adventure.wav");
d = Buffer.read(s,"/Users/Fred/Desktop/PinCollider/An Adventure beginning.wav");
e = Buffer.read(s,"/Users/Fred/Desktop/PinCollider/Yellow.wav");
