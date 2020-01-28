# samplegit
sample
1. channels and kernels:


(i) channels:


                    channels contains features that features was extracted by using kernels in every convolution layer. Channels are input/output.
(ii) kernels:


                    kernels help to extract the features from channels.Kernels are used for blurring,edge detection and more.
                    Kernel = filters = feature detector
 
2. we (nearly) always use 3x3 kernels.






 kernels has parameter. If we use large number parameter the network will be slow and the training process is longer.
 
It takes more RAM too.

If we use less number of parameters the network will fast and training process is easy.

So, We use 3x3  kernel which has 9 parameters.

 2x2 kernel has 4 parameters but we can't detect edges .
 
In 2x2 only starting and ending we can detect the centre we can't detect .

In 3x3 has starting ,centre and ending too.
 

3. How many times to we need to perform 3x3 convolutions operations to reach close to 1x1 from 199x199 ?

           we need to perform 100 3x3 convolution operation to reach close to 1x1 from 199x199
           
199 x 199 > 197 x 197
197 x 197 > 195 x 195
195 x 195 > 193 x 193
193 x 193 > 191 x 191
191 x 191 > 189 x 189
189 x 189 > 187 x 187
187 x 187 > 185 x 185
185 x 185 > 183 x 183
183 x 183 > 181 x 181
181 x 181 > 179 x 179
179 x 179 > 177 x 177
177 x 177 > 175 x 175
175 x 175 > 173 x 173
173 x 173 > 171 x 171
171 x 171 > 169 x 169
169 x 169 > 167 x 167
167 x 167 > 165 x 165
165 x 165 > 163 x 163
163 x 163 > 161 x 161
161 x 161 > 159 x 159
159 x 159 > 157 x 157
157 x 157 > 155 x 155
155 x 155 > 153 x 153
153 x 153 > 151 x 151
151 x 151 > 149 x 149
149 x 149 > 147 x 147
147 x 147 > 145 x 145
145 x 145 > 143 x 143
143 x 143 > 141 x 141
141 x 141 > 139 x 139
139 x 139 > 137 x 137
137 x 137 > 135 x 135
135 x 135 > 133 x 133
133 x 133 > 131 x 131
131 x 131 > 129 x 129
129 x 129 > 127 x 127
127 x 127 > 125 x 125
125 x 125 > 123 x 123
123 x 123 > 121 x 121
121 x 121 > 119 x 119
119 x 119 > 117 x 117
117 x 117 > 115 x 115
115 x 115 > 113 x 113
113 x 113 > 111 x 111
111 x 111 > 109 x 109
109 x 109 > 107 x 107
107 x 107 > 105 x 105
105 x 105 > 103 x 103
103 x 103 > 101 x 101
101 x 101 > 99 x 99
99 x 99 > 97 x 97
97 x 97 > 95 x 95
95 x 95 > 93 x 93
93 x 93 > 91 x 91
91 x 91 > 89 x 89
89 x 89 > 87 x 87
87 x 87 > 85 x 85
85 x 85 > 83 x 83
83 x 83 > 81 x 81
81 x 81 > 79 x 79
79 x 79 > 77 x 77
77 x 77 > 75 x 75
75 x 75 > 73 x 73
73 x 73 > 71 x 71
71 x 71 > 69 x 69
69 x 69 > 67 x 67
67 x 67 > 65 x 65
65 x 65 > 63 x 63
63 x 63 > 61 x 61
61 x 61 > 59 x 59
59 x 59 > 57 x 57
57 x 57 > 55 x 55
55 x 55 > 53 x 53
53 x 53 > 51 x 51
51 x 51 > 49 x 49
49 x 49 > 47 x 47
47 x 47 > 45 x 45
45 x 45 > 43 x 43
43 x 43 > 41 x 41
41 x 41 > 39 x 39
39 x 39 > 37 x 37
37 x 37 > 35 x 35
35 x 35 > 33 x 33
33 x 33 > 31 x 31
31 x 31 > 29 x 29
29 x 29 > 27 x 27
27 x 27 > 25 x 25
25 x 25 > 23 x 23
23 x 23 > 21 x 21
21 x 21 > 19 x 19
19 x 19 > 17 x 17
17 x 17 > 15 x 15
15 x 15 > 13 x 13
13 x 13 > 11 x 11
11 x 11 > 9 x 9
9 x 9 > 7 x 7
7 x 7 > 5 x 5
5 x 5 > 3 x 3
3 x 3 > 1 x 1
 
4. kernels initialized:


                         Kernels are initialized randomly. We generally use 3x3 kernels . A 3x3 Kernel has 9 random values which it is initialized.
                         
         Each kernel is initialized by the random values. That 9 random values are multiple with the each pixel of input image .
         
        Y= (W1xA1)+(W2xA2)+(W3xA3)+.........+(W9xA9)
        
          W=parameter in kernel
          
           A=Pixel in input image
 
5. The training of a DNN:

               During training of Deep neural network. From the input image the kernel will extract the features and the features goes
               
to the convolution layer and activation function takes place like Rectified linear unit(ReLU) y=max(0,x)  . The value which are less

(or) equal to zero will represent it as zero . Which are more than zero will represent as same value. During (ReLU) no negative values 

will present. Same process will take place in next layer and it is known as forward propagation . We get output for input image . If the 

output is wrong  back propagation takes place and correct the error  by updating the parameters of kernel and do forward propagation and 

see the output . If the output is not correct we need to do back propagation again until the output is correct .                         
 
 
