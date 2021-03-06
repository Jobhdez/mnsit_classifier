import datetime

def training_loop(
        n_epochs,
        optimizer,
        model,
        loss_fn,
        train_loader,
        device):
    for epoch in range(1, n_epochs + 1):
        loss_train = 0.0
        for i, (imgs, labels) in enumerate(train_loader):

            imgs = imgs.to(device=device)
            labels = labels.to(device=device)

            outputs = model(imgs)

            loss = loss_fn(outputs, labels)

            optimizer.zero_grad()

            loss.backward()

            optimizer.step()

            loss_train += loss.item()

        if epoch == 1 or epoch % 10 == 0:
            print('{} Epoch {}, Training loss {}'.format(
                datetime.datetime.now(),
                epoch,
                loss_train / len(train_loader)))
