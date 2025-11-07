def train_epoch(adapter, data_loader):
    for batch in data-loader:
        grads=
model.forward_backward(batch, adapter)
        adapter.optim_step(grads)