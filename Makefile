train-gender:
	@python ./gender/knn/train.py
train-age:
	@python ./age/knn/train.py
predict-age:
	@python ./age/knn/predict.py
predict-gender:
	@python ./gender/knn/predict.py
face:
	@python ./face-recognizer/recognizer.py