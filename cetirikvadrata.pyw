import turtle as t, time
n = 100

def main():
	for m in range(4):
		for i in range(4):
			t.forward(n)
			t.left(90)
		t.right(90)
	
	time.sleep(1.5)

if __name__ == '__main__':
	main()