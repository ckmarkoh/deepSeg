# -*- encoding:utf-8 -*-
import theano.tensor as T
import theano
import os
import numpy as np
from deepseg_util import read_json, get_widx
from collections import OrderedDict
from platform import python_version


class DeepSeg(object):

    def __init__(self):

        #   U B L I
        # U
        # B
        # L
        # I
        self.VALID_TRANS = np.matrix([
            [1, 1, 0, 0],
            [0, 0, 1, 1],
            [1, 1, 0, 0],
            [0, 0, 1, 1],
        ])

        dict_path = os.path.normpath(os.path.join(os.getcwd(), "model/as_dict.json"))
        self.word_dict = read_json(dict_path)
        model_path = os.path.normpath(os.path.join(os.getcwd(), "model/as_model.json"))
        model_params = read_json(model_path)
        self.network = self.__build_networks(model_params)

    def __weight_init_val(self, w_val):

        return theano.shared(np.array(w_val).astype(theano.config.floatX))

    def __build_networks(self, pre_model_params):

        s_embed = np.array(pre_model_params['wb']['w_embed']).shape[1]

        wb = OrderedDict()
        wb['w_embed'] = self.__weight_init_val(pre_model_params['wb']['w_embed'])
        wb['w_hidden'] = self.__weight_init_val(pre_model_params['wb']['w_hidden'])
        wb['b_hidden'] = self.__weight_init_val(pre_model_params['wb']['b_hidden'])
        wb['w_out'] = self.__weight_init_val(pre_model_params['wb']['w_out'])
        wb['b_out'] = self.__weight_init_val(pre_model_params['wb']['b_out'])

        x_in = T.imatrix()

        emb_lookup = wb["w_embed"][x_in]
        hidden_input = T.reshape(emb_lookup, newshape=(x_in.shape[0], x_in.shape[1] * s_embed))
        hidden_result = T.tanh(T.dot(hidden_input, wb["w_hidden"]) + wb["b_hidden"])
        out_result = T.nnet.softmax(T.dot(hidden_result, wb["w_out"]) + wb["b_out"])
        out_result_log = T.log(out_result)

        func = theano.function(inputs=[x_in], outputs=[out_result_log], allow_input_downcast=True)

        return func

    def __gen_input_line(self, line, s_window, pad_id):

        line_word = [pad_id] * (s_window // 2) + line + [pad_id] * (
            s_window // 2)
        case_raw = [line_word[i:i + s_window] for i in range(len(line_word) + 1 - s_window)]

        return case_raw

    def __viterbi(self, tag_prob):

        max_prob = -np.inf * np.ones(tag_prob.shape)
        max_prob_bt = -1 * np.ones(tag_prob.shape)
        for i in range(tag_prob.shape[0]):
            for j in range(tag_prob.shape[1]):
                if i == 0:
                    max_prob[i, j] = tag_prob[i, j]
                else:
                    max_prob_temp = -np.inf
                    max_prob_id = -1
                    for k in range(tag_prob.shape[1]):
                        if self.VALID_TRANS[k, j] == 1:
                            if max_prob[i - 1, k] >= max_prob_temp:
                                max_prob_temp = max_prob[i - 1, k]
                                max_prob_id = k
                    assert max_prob_id != -1
                    max_prob[i, j] = tag_prob[i, j] + max_prob_temp
                    max_prob_bt[i, j] = max_prob_id

        bt_seq = [int(np.argmax(max_prob[-1, :]))]
        for i in range(1, max_prob.shape[0]):
            bt_seq.append(int(max_prob_bt[-i, bt_seq[-1]]))
        bt_seq.reverse()

        return bt_seq

    def word_segmentation(self, input_line):

        s_window = 5
        pad_id = len(self.word_dict) - 1
        output_line = []

        for line in input_line:
            line2 = [w.strip() for w in line if len(w.strip()) > 0]
            line_write = []
            for w in line2:
                w_idx = get_widx(w, self.word_dict)
                line_write.append(w_idx)
            if len(line2) >= 1:
                input_data = self.__gen_input_line(line_write, s_window, pad_id)
                tag_prob = self.network(input_data)
                tag_result = self.__viterbi(tag_prob[0])
                temp_term = u""
                for w, t in zip(line2, tag_result):
                    temp_term += w
                    if t == 0 or t == 2:
                        output_line.append(temp_term)
                        temp_term = u""
            output_line.append("\n")

        return output_line

    def cut(self, doc_in):

        line_in = doc_in.split("\n")
        results = self.word_segmentation(line_in)

        return results
