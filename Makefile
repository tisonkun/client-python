apis: apis/engula/v1
	python3 -m grpc_tools.protoc -Iapis --python_out=. --grpc_python_out=. apis/engula/v1/*.proto