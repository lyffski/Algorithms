import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
style.use("ggplot")

class Support_Vector_Machine:
   def __init__(self, visualization=True):
      self.visualization = visualization
      self.color = {1:"r", -1:"b"}
      if self.visualization:
         self.fig = plt.figure()
         self.ax = self.fig.add_subplot(1,1,1) # fig(1,1,1) 1st and 2rd are the grid so 1x1 grid  the 3rd 1 the the id of subplot
   
   def fit(self, data):
      self.data = data
      opt_dict = {} # ||w||: [w,b] // ||w|| is the key to the assign "w" and "b" values
      transforms = [[1,1],
                    [-1,1],
                    [-1,-1],
                    [1,-1],]
      
      all_data = []
      for yi in self.data: # cast all data into "all_data"
         for featureset in self.data[yi]:
            for feature in featureset:
               all_data.append(feature) 

      self.max_feature_value = max(all_data)
      self.min_feature_value = min(all_data)
      all_data = None
      #each stepsize is a order of norms smaller
      #suprot vectors yi (xi.w+b) = 1 //for both negative and positive "classes/sign" of equation at least to be the nearest to 1 ;;; the logic for stepping down of step values
      step_sizes = [self.max_feature_value * 0.1,  # big step to find the loweste value of convex; if exceed (the low value been increased) do smaller steps
                    self.max_feature_value *0.01, # if exceed => you step now with lowest range (each step on x-axis to reach the lowest point of convex; ballquadratic)
                    # point of expense:
                    self.max_feature_value * 0.001,] 

      # extremely expensive
      b_multiple_range = 5 # as value as precises so big step of "b"
      # we do not need to take as small steps with b as we do with w, but IMPORTANT you can use the same stepping with b as with w, but cost time
      b_multiple = 5 
      latest_optimum = self.max_feature_value*10 # start as the first (and highest element) of vector "w"

      for step in step_sizes:
         w = np.array([latest_optimum, latest_optimum]) # reassign as the steps continues
         optimized = False # able, since it convex problem, if no then you should ensure that you will add some further steps.
         while not optimized:
            for b in np.arange(-1*(self.max_feature_value * b_multiple_range), self.max_feature_value * b_multiple_range, step * b_multiple):
               for transformation in transforms: #loop runs from the highest w, for example if 8 is, since it is multiply with *10 so it would run through a bench "w" that are in between -80 and 80
                  w_t = w*transformation 
                  found_option = True
                  #SMO attempts to fix this a bit
                  #yi(xi.w+b0) >= 1 
                  # weakest link in the SVM fundamentally, since you have to run there through ALL data given to the program to make sure it fits
                  for i in self.data: # "i" is "yi" the classifier, positive or negative
                     for xi in self.data[i]:
                        yi = i # for clearness
                        if not yi*(np.dot(w_t,xi)+b) >= 1: # if one of the sample do not fit the definition => all have to throw out
                           found_option = False
                           break
                        #print(xi,":",yi*(np.dot(w_t,xi)+b)) #not needed

                  if found_option: # if everything have been validated
                     opt_dict[np.linalg.norm(w_t)] = [w_t,b] #norm of x_t <=> ||w|| as key  =   the complied values of w (transformed) and b  
                     
            if w[0] < 0: # w[0] the value of w are the same;  and we do not have to go further then zero, since we had the transfrom already done. 
               optimized = True
               print("Optimized a step.")
            else:
               w = w - step # so: [w][w] - [step, step]
         norms = sorted([n for n in opt_dict]) # sorting the list of the norms asc 
         #||w|| : [w,b] //norm of w key to value of w and b
         opt_choice = opt_dict[norms[0]] #after sort, we want take as the optimal choice the lowest norm value
         self.w = opt_choice[0] # opt_choice is dictionar so can save multiply values under one key
         self.b = opt_choice[1]
         latest_optimum = opt_choice[0][0]+step*2 #latest_optimum (is normal value) := [var][var] //IMPORTANT if loop reaped have the lowest value already
       
      for i in self.data:
         for xi in self.data[i]:
            yi = i
            print(xi,":",yi*(np.dot(self.w,xi)+self.b))

   def predict(self, features):
      # sign(x.w+b) // sign := is "+" or "-" sign, so this is the classification itself
      classification = np.sign(np.dot(np.array(features),self.w) + self.b) # instead of "np.sign" use lambda/anonymous func
      if classification !=0 and self.visualization:
         self.ax.scatter(features[0],features[1], s=200, marker="*", c=self.color[classification])
      return classification

   def visualize(self):
      [[self.ax.scatter(x[0],x[1],s=100,color=self.color[i]) for x in data_dict[i]] for i in data_dict]
      #hyperplane = x.w+b
      #v= x.w+b
      #psv = 1
      #nsv = -1
      #dec_bound = 0
      def hyperplane(x,w,b,v):
         return (-w[0]*x-b+v) / w[1]

      datarange = (self.min_feature_value*0.9,self.max_feature_value*1.1)
      hyp_x_min = datarange[0]
      hyp_x_max = datarange[1]

      #(w.x+b) = 1
      #positive support vector hyperplane
      psv1 = hyperplane(hyp_x_min, self.w, self.b, 1)
      psv2 = hyperplane(hyp_x_max, self.w, self.b, 1)
      self.ax.plot([hyp_x_min, hyp_x_max], [psv1,psv2])

       #(w.x+b) = -1
      #negative support vector hyperplane
      nsv1 = hyperplane(hyp_x_min, self.w, self.b, -1)
      nsv2 = hyperplane(hyp_x_max, self.w, self.b, -1)
      self.ax.plot([hyp_x_min, hyp_x_max], [nsv1,nsv2])

       #(w.x+b) = 0
      #boundary support vector hyperplane
      dec_bound1 = hyperplane(hyp_x_min, self.w, self.b, 0)
      dec_bound2 = hyperplane(hyp_x_max, self.w, self.b, 0)
      self.ax.plot([hyp_x_min, hyp_x_max], [dec_bound1,dec_bound2])


data_dict = {-1:np.array([[1,7],
                         [2,8],
                         [3,8],]),
            1:np.array([[5,1],
                        [6,-1],
                        [7,3],])}



svm = Support_Vector_Machine()
svm.fit(data=data_dict)

predict_us = [[0,10],
              [1,5],
              [4,6],
              [4,4],
              [6,4],
              [5,8],]
for p in predict_us:
   svm.predict(p)

svm.visualize()

   