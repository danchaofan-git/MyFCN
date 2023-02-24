f = open('r.txt', 'r')
r1 = open('results/loss.csv', 'w')
r2 = open('results/miou.csv', 'w')
r3 = open('results/f1.csv', 'w')
r4 = open('results/precision.csv', 'w')
r5 = open('results/recall.csv', 'w')
r6 = open('results/correct.csv', 'w')
txt = f.readlines()
for i in range(0, 200):
    loss = txt[1 + i * 12]
    cor = txt[4 + i * 12]
    iou = txt[5 + i * 12]
    miou = txt[6 + i * 12]
    pre = txt[7 + i * 12]
    rec = txt[9 + i * 12]
    f1   = txt[11 + i * 12]

    train_loss = float((loss.strip()).split(':')[-1])
    mIOU = float((miou.strip()).split(':')[-1])
    precision = float((pre.strip()).split(':')[-1])
    recall = float((rec.strip()).split(':')[-1])
    correct = float((cor.strip()).split(':')[-1])
    F1 = float((f1.strip()).split(':')[-1])
    r1.write(str(train_loss) + '\n')
    r2.write(str(mIOU) + '\n')
    r3.write(str(F1) + '\n')
    r4.write(str(precision) + '\n')
    r5.write(str(recall) + '\n')
    r6.write(str(correct) + '\n')
r1.close()
r2.close()
r3.close()
r4.close()
r5.close()
r6.close()