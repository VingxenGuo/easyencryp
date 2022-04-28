ori_sqc = 'abcdefghijklmnopqrstuvwxyz'
front3 = ori_sqc[:3]
end23 = ori_sqc[3:]
new_sqc = end23 + front3
encry = dict(zip(ori_sqc, new_sqc))
print(encry)

cipher = []
beforestr = input('請輸入欲加密字串:')
for i in beforestr:
    v = encry[i]
    cipher.append(v)
print('原始輸入值:', ' '.join(beforestr))
print('轉換後:', ' '.join(cipher))