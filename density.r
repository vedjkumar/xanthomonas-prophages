library(ggplot2)
library(ggridges)

ggplot(completeness, aes(x=completeness,y=organism)) + geom_density_ridges(rel_min_height=0.01)
