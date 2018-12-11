# Copyright 2016 Xinyi Wang All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
testFile = "/Users/wangxinyi/Desktop/artificial intelligence/bayes/bayes_template.py"
trainDir = "/Users/wangxinyi/Desktop/artificial intelligence/bayes/movies_reviews/"
testDir = "/Users/wangxinyi/Desktop/artificial intelligence/bayes/movies_reviews/"

exec(open(testFile).read())
bc = Bayes_Classifier(trainDir)
	
iFileList = []

for fFileObj in os.walk(trainDir + "/"):
	iFileList = fFileObj[2]
	break
print('%d test reviews.' % len(iFileList))

results = {"negative":0, "neutral":0, "positive":0}

print("\nFile Classifications:")

for filename in iFileList:
	fileText = bc.loadFile(testDir + filename)
	result = bc.classify(fileText)
	print("%s: %s" % (filename, result))
	results[result] += 1

print("\nResults Summary:")

for r in results:
	print("%s: %d" % (r, results[r]))
