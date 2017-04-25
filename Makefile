train-gender:
	@python ./gender/knn/train.py
train-age:
	@python ./age/knn/train.py
predict-age:
	@python ./age/knn/predict.py
predict-gender:
	@python ./gender/knn/predict.py
ros-gender:
	@python ./gender/ros/predict.py
ros-age:
	@python ./age/ros/predict.py	
ros-recognizer:
	@python ./face-recognizer/ros/launch.py
face:
	@python ./face-recognizer/recognizer.py