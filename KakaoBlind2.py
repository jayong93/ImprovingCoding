def calcurate_score(score_str):
    is_check_num = False
    nums = []
    ops = []
    last_idx = 0

    for i, ch in enumerate(score_str):
        if is_check_num and ('0' <= ch <= '9'):
            ops.append(score_str[last_idx:i])
            last_idx = i
            is_check_num = False if is_check_num else True
        elif is_check_num == False and ('0' <= ch <= '9') == False:
            nums.append(int(score_str[last_idx:i]))
            last_idx = i
            is_check_num = False if is_check_num else True
    ops.append(score_str[last_idx:])
            
    if len(nums) != len(ops):
        print("Wrong Input")
        return

    for i, op in enumerate(ops):
        for ch in op:
            if ch == 'S': continue
            elif ch == 'D': nums[i] = nums[i]**2
            elif ch == 'T': nums[i] = nums[i]**3
            elif ch == '*':
                if i > 0:
                    for offset in range(2): nums[i-offset] *= 2
                else:
                    nums[i] *= 2
            elif ch == '#': nums[i] *= -1

    print(sum(nums))

calcurate_score("1S2D*3T")
calcurate_score("1D2S#10S")
calcurate_score("1D2S0T")
calcurate_score("1S*2T*3S")
calcurate_score("1D#2S*3S")
calcurate_score("1T2D3D#")
calcurate_score("1D2S3T*")
