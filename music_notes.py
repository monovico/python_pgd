# To run this code on CodeBug, visit:
#
#     http://www.codebug.org.uk/learn/activity/66/tethering-codebug-with-python/#step585
#
import codebug_tether
from codebug_tether import (IO_DIGITAL_OUTPUT,
                            IO_DIGITAL_INPUT,
                            IO_PWM_OUTPUT,
                            IO_ANALOG_INPUT)
import codebug_tether.music
import time
import random

codebug = codebug_tether.CodeBug()
codebug.set_leg_io(0, IO_DIGITAL_INPUT);
codebug.set_leg_io(1, IO_PWM_OUTPUT);
codebug.set_leg_io(2, IO_DIGITAL_INPUT);
codebug.set_leg_io(3, IO_DIGITAL_INPUT);
codebug.set_leg_io(4, IO_DIGITAL_INPUT);
codebug.set_leg_io(5, IO_DIGITAL_INPUT);
codebug.set_leg_io(6, IO_DIGITAL_INPUT);
codebug.set_leg_io(7, IO_DIGITAL_INPUT);


while True:
  while codebug.get_input('A') == 1:
    codebug.clear();
    codebug.pwm_freq(3520)
    time.sleep(codebug_tether.music.get_time_ms(codebug_tether.music.MUSIC_DEMISEMIQUAVER)/1000)
    codebug.pwm_off()
    codebug.set_pixel((random.randint(0, 4)), (random.randint(0, 4)), 1);
    codebug.pwm_freq(3135)
    time.sleep(codebug_tether.music.get_time_ms(codebug_tether.music.MUSIC_DEMISEMIQUAVER)/1000)
    codebug.pwm_off()
    codebug.set_pixel((random.randint(0, 4)), (random.randint(0, 4)), 1);
    codebug.pwm_freq(2637)
    time.sleep(codebug_tether.music.get_time_ms(codebug_tether.music.MUSIC_DEMISEMIQUAVER)/1000)
    codebug.pwm_off()
    codebug.set_pixel((random.randint(0, 4)), (random.randint(0, 4)), 1);
    codebug.pwm_freq(2093)
    time.sleep(codebug_tether.music.get_time_ms(codebug_tether.music.MUSIC_DEMISEMIQUAVER)/1000)
    codebug.pwm_off()
    codebug.set_pixel((random.randint(0, 4)), (random.randint(0, 4)), 1);
    codebug.pwm_freq(2349)
    time.sleep(codebug_tether.music.get_time_ms(codebug_tether.music.MUSIC_DEMISEMIQUAVER)/1000)
    codebug.pwm_off()
    codebug.set_pixel((random.randint(0, 4)), (random.randint(0, 4)), 1);
    codebug.pwm_freq(3951)
    time.sleep(codebug_tether.music.get_time_ms(codebug_tether.music.MUSIC_DEMISEMIQUAVER)/1000)
    codebug.pwm_off()
    codebug.set_pixel((random.randint(0, 4)), (random.randint(0, 4)), 1);
    codebug.pwm_freq(2793)
    time.sleep(codebug_tether.music.get_time_ms(codebug_tether.music.MUSIC_DEMISEMIQUAVER)/1000)
    codebug.pwm_off()
    codebug.set_pixel((random.randint(0, 4)), (random.randint(0, 4)), 1);
    codebug.pwm_freq(4186)
    time.sleep(codebug_tether.music.get_time_ms(codebug_tether.music.MUSIC_DEMISEMIQUAVER)/1000)
    codebug.pwm_off()
    codebug.set_pixel((random.randint(0, 4)), (random.randint(0, 4)), 1);
    codebug.pwm_freq(3520)
    time.sleep(codebug_tether.music.get_time_ms(codebug_tether.music.MUSIC_DEMISEMIQUAVER)/1000)
    codebug.pwm_off()
    codebug.set_pixel((random.randint(0, 4)), (random.randint(0, 4)), 1);
    codebug.pwm_freq(3135)
    time.sleep(codebug_tether.music.get_time_ms(codebug_tether.music.MUSIC_DEMISEMIQUAVER)/1000)
    codebug.pwm_off()
    codebug.set_pixel((random.randint(0, 4)), (random.randint(0, 4)), 1);
    codebug.pwm_freq(2637)
    time.sleep(codebug_tether.music.get_time_ms(codebug_tether.music.MUSIC_DEMISEMIQUAVER)/1000)
    codebug.pwm_off()
    codebug.set_pixel((random.randint(0, 4)), (random.randint(0, 4)), 1);
    codebug.pwm_freq(2093)
    time.sleep(codebug_tether.music.get_time_ms(codebug_tether.music.MUSIC_DEMISEMIQUAVER)/1000)
    codebug.pwm_off()
    codebug.set_pixel((random.randint(0, 4)), (random.randint(0, 4)), 1);
    codebug.pwm_freq(2349)
    time.sleep(codebug_tether.music.get_time_ms(codebug_tether.music.MUSIC_DEMISEMIQUAVER)/1000)
    codebug.pwm_off()
    codebug.set_pixel((random.randint(0, 4)), (random.randint(0, 4)), 1);
    codebug.pwm_freq(3951)
    time.sleep(codebug_tether.music.get_time_ms(codebug_tether.music.MUSIC_DEMISEMIQUAVER)/1000)
    codebug.pwm_off()
    codebug.set_pixel((random.randint(0, 4)), (random.randint(0, 4)), 1);
    codebug.pwm_freq(2793)
    time.sleep(codebug_tether.music.get_time_ms(codebug_tether.music.MUSIC_DEMISEMIQUAVER)/1000)
    codebug.pwm_off()
    codebug.set_pixel((random.randint(0, 4)), (random.randint(0, 4)), 1);
    codebug.pwm_freq(4186)
    time.sleep(codebug_tether.music.get_time_ms(codebug_tether.music.MUSIC_DEMISEMIQUAVER)/1000)
    codebug.pwm_off()
    codebug.set_pixel((random.randint(0, 4)), (random.randint(0, 4)), 1);
    time.sleep(500/1000);
    codebug.pwm_freq(3520)
    time.sleep(codebug_tether.music.get_time_ms(codebug_tether.music.MUSIC_DEMISEMIQUAVER)/1000)
    codebug.pwm_off()
    codebug.set_pixel((random.randint(0, 4)), (random.randint(0, 4)), 1);
    codebug.pwm_freq(3135)
    time.sleep(codebug_tether.music.get_time_ms(codebug_tether.music.MUSIC_DEMISEMIQUAVER)/1000)
    codebug.pwm_off()
    codebug.set_pixel((random.randint(0, 4)), (random.randint(0, 4)), 1);
    codebug.pwm_freq(2637)
    time.sleep(codebug_tether.music.get_time_ms(codebug_tether.music.MUSIC_DEMISEMIQUAVER)/1000)
    codebug.pwm_off()
    codebug.set_pixel((random.randint(0, 4)), (random.randint(0, 4)), 1);
    codebug.pwm_freq(2093)
    time.sleep(codebug_tether.music.get_time_ms(codebug_tether.music.MUSIC_DEMISEMIQUAVER)/1000)
    codebug.pwm_off()
    codebug.set_pixel((random.randint(0, 4)), (random.randint(0, 4)), 1);
    codebug.pwm_freq(2349)
    time.sleep(codebug_tether.music.get_time_ms(codebug_tether.music.MUSIC_DEMISEMIQUAVER)/1000)
    codebug.pwm_off()
    codebug.set_pixel((random.randint(0, 4)), (random.randint(0, 4)), 1);
    codebug.pwm_freq(3951)
    time.sleep(codebug_tether.music.get_time_ms(codebug_tether.music.MUSIC_DEMISEMIQUAVER)/1000)
    codebug.pwm_off()
    codebug.set_pixel((random.randint(0, 4)), (random.randint(0, 4)), 1);
    codebug.pwm_freq(2793)
    time.sleep(codebug_tether.music.get_time_ms(codebug_tether.music.MUSIC_DEMISEMIQUAVER)/1000)
    codebug.pwm_off()
    codebug.set_pixel((random.randint(0, 4)), (random.randint(0, 4)), 1);
    codebug.pwm_freq(4186)
    time.sleep(codebug_tether.music.get_time_ms(codebug_tether.music.MUSIC_DEMISEMIQUAVER)/1000)
    codebug.pwm_off()
    codebug.set_pixel((random.randint(0, 4)), (random.randint(0, 4)), 1);
    codebug.pwm_freq(3520)
    time.sleep(codebug_tether.music.get_time_ms(codebug_tether.music.MUSIC_DEMISEMIQUAVER)/1000)
    codebug.pwm_off()
    codebug.set_pixel((random.randint(0, 4)), (random.randint(0, 4)), 1);
    codebug.pwm_freq(3135)
    time.sleep(codebug_tether.music.get_time_ms(codebug_tether.music.MUSIC_DEMISEMIQUAVER)/1000)
    codebug.pwm_off()
    codebug.set_pixel((random.randint(0, 4)), (random.randint(0, 4)), 1);
    codebug.pwm_freq(2637)
    time.sleep(codebug_tether.music.get_time_ms(codebug_tether.music.MUSIC_DEMISEMIQUAVER)/1000)
    codebug.pwm_off()
    codebug.set_pixel((random.randint(0, 4)), (random.randint(0, 4)), 1);
    codebug.pwm_freq(2093)
    time.sleep(codebug_tether.music.get_time_ms(codebug_tether.music.MUSIC_DEMISEMIQUAVER)/1000)
    codebug.pwm_off()
    codebug.set_pixel((random.randint(0, 4)), (random.randint(0, 4)), 1);
    codebug.pwm_freq(2349)
    time.sleep(codebug_tether.music.get_time_ms(codebug_tether.music.MUSIC_DEMISEMIQUAVER)/1000)
    codebug.pwm_off()
    codebug.set_pixel((random.randint(0, 4)), (random.randint(0, 4)), 1);
    codebug.pwm_freq(3951)
    time.sleep(codebug_tether.music.get_time_ms(codebug_tether.music.MUSIC_DEMISEMIQUAVER)/1000)
    codebug.pwm_off()
    codebug.set_pixel((random.randint(0, 4)), (random.randint(0, 4)), 1);
    codebug.pwm_freq(2793)
    time.sleep(codebug_tether.music.get_time_ms(codebug_tether.music.MUSIC_DEMISEMIQUAVER)/1000)
    codebug.pwm_off()
    codebug.set_pixel((random.randint(0, 4)), (random.randint(0, 4)), 1);
    codebug.pwm_freq(4186)
    time.sleep(codebug_tether.music.get_time_ms(codebug_tether.music.MUSIC_DEMISEMIQUAVER)/1000)
    codebug.pwm_off()
    codebug.set_pixel((random.randint(0, 4)), (random.randint(0, 4)), 1);
    time.sleep(2000/1000);
    codebug.clear();
