from torch import nn
import torch

class TCELoss(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, pred_logits, truths, weight=None):
        self.criterion = nn.BCEWithLogitsLoss(reduction='none')
        B, T, H = pred_logits.size()
        truths = truths.float()
        weight = weight.float()
        # _debug(pred_logits, truths, weight)
        loss = self.criterion(pred_logits, truths)
        # return loss.sum()
        missing = weight.sum().item()
        assert (missing != 0)
        return ((loss * weight).sum()/missing)



def _debug(pred_logits, truths, weight):
    B, T, H = pred_logits.size()
    # pred_logits = pred_logits.view(-1, H)
    # truths = truths.view(-1)
    for b in range(B):
        print("preds", torch.sigmoid(pred_logits[b, :, :].view(-1)))
        print("truths", truths[b, :, :].view(-1))
        # print("weight", weight[b, :].view(-1))
        # print("Weighted:", nn.BCEWithLogitsLoss(reduce=False)(pred_logits, truths) * weight)
        break
