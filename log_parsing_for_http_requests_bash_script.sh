#!/bin/bash
filename='sample.log'
s=$(cat $fname | grep -e '" 404' | wc -l)
echo Total number of http 404 error count in $fname is : $s
cnt=0
while read p; do
         echo $p | grep -q 'HTTP/1.1"'
         if [ $? == 0 ]; then
                myvar=`echo $p  | cut -d " " -f10`
                  echo "HTTP $myvar"
                # cnt=$((cnt+1))
         fi
                 echo $p | grep -q 'HTTP/1.0"'
         if [ $? == 0 ]; then
                myvar=`echo ${p/\*/-} | cut -d " " -f10`
                  echo "HTTP $myvar"
                # cnt=$((cnt+1))
         fi

done < $filename





