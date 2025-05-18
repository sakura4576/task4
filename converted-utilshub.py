import sys
def min_moves_to_equal(nums):
    nums.sort()
    median = nums[len(nums) // 2]
    moves = sum(abs(x - median) for x in nums)
    return moves
def main():
    if len(sys.argv) != 2:
        print("Использование: python script.py input.txt")
        return
    input_path = sys.argv[1]
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            nums = [int(line.strip()) for line in f if line.strip()]
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return
    result = min_moves_to_equal(nums)
    print(result)
if __name__ == "__main__":
    main()
        
   



