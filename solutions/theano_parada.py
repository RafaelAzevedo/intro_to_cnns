def train(train_fn, valid_fn, x_train, y_train, x_val, y_val, max_iterations, epsilon):
    cost_history = []  
    val_cost_history = []
    for i in range(max_iterations):
        cost, acc = train_fn(x_train,y_train)
        cost_history.append(cost)

        val_cost, val_acc = valid_fn(x_val, y_val)
        val_cost_history.append(val_cost)

        if (i > 2) and (cost_history[-2] - cost_history[-1]) < epsilon:
            print 'Terminando apos %d iteracoes' % (i+1)
            break
    return cost_history, val_cost_history
