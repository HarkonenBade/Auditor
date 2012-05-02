export PYTHONPATH=/home/tom/prj:/home/tom/src/stagger-read-only
cd mp3
echo "BEGIN MP3"
#echo "PERFECT"
#cd perfect
#python ../../percep_accuracy.py per scan
#python ../../percep_accuracy.py per gather
#cd ../
echo "SCRAMBLE"
cd scramble
python ../../percep_accuracy.py scr scan
python ../../percep_accuracy.py scr gather
cd ../
echo "DLSCRAM"
cd dlscram
python ../../percep_accuracy.py dls scan
python ../../percep_accuracy.py dls gather
cd ../
cd ../
echo "END MP3"

cd img
echo "BEGIN IMG"
#echo "PERFECT"
#cd perfect
#python ../../percep_accuracy.py per scan
#python ../../percep_accuracy.py per gather
#cd ../
echo "SCRAMBLE"
cd scramble
python ../../percep_accuracy.py scr scan
python ../../percep_accuracy.py scr gather
cd ../
echo "DLSCRAM"
cd dlscram
python ../../percep_accuracy.py dls scan
python ../../percep_accuracy.py dls gather
cd ../
cd ../
echo "END IMG"

cd mp3img
echo "BEGIN MP3IMG"
#echo "PERFECT"
#cd perfect
#python ../../percep_accuracy.py per scan
#python ../../percep_accuracy.py per gather
#cd ../
#echo "SCRAMBLE"
#cd scramble
#python ../../percep_accuracy.py scr scan
#python ../../percep_accuracy.py scr gather
#cd ../
echo "DLSCRAM"
cd dlscram
python ../../percep_accuracy.py dls scan
python ../../percep_accuracy.py dls gather
cd ../
cd ../
echo "END MP3IMG"

