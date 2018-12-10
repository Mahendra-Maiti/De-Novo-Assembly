# k-Mer generation and De Bruin Graph algo


# install.packages(c("stringr","readr","seqinr","ape","poppr","zoo","igraph"))
require(stringr)
require(readr)
require(seqinr)
require(ape)
require(poppr)
require(zoo)
require(igraph)

args = commandArgs(trailingOnly=TRUE)

filepath <- getwd()

filepath1 <- paste(filepath,args[1],sep = "/")

filepath2 <- paste(filepath1,"Substrings.txt",sep = "/")

data <- read_table2(file = filepath2,col_names = FALSE)

data <- data.frame(data)

str <- "ZABCDABEFABY"

str2 <- "a_long_long_long_time"

genKMers <- function(strn,k){
  
  len <- str_length(strn)
  kmers <- matrix(nrow = (len-k))
  t <- (len-k+1)
  
  #print(t)
  
  for(i in 1:t){
    
    kmers[i]<-str_sub(strn,i,i+k-1)
    print(str_sub(strn,i,i+k-1))
    
  }
  
  return(kmers)
}


genEdges <- function(kmers,k){
  
  nodes <- matrix(nrow=length(kmers)*2)
  edges <- matrix(ncol = 2,nrow = length(kmers))
  
  
  for(i in 1:length(kmers)){
    
    node1 <- str_sub(kmers[i],1,k-1)
    node2 <- str_sub(kmers[i],2,k)
    
    edges[i,] <- c(node1,node2)
    
  }
  return(edges)
}

# km <- genKMers(str,3)
# edges <- genEdges(km,3)
# 
# write.table(edges,file = "~/Desktop/Genomics/edges.csv",col.names = FALSE,row.names = FALSE,sep = "\t")
# 
# km <- genKMers(str2,5)
# edges2 <- genEdges(km,5)
# 
# write.table(edges,file = "~/Desktop/Genomics/edges2.csv",col.names = FALSE,row.names = FALSE,sep = "\t")


createEdgeList <- function(data){
  
  edges <- matrix(ncol=2,nrow=0)
  
  str_len <- str_length(data[1,])
  k <- str_len-2
  
  len <- nrow(data)
  
  for(i in 1:len){
    
    str <- data[i,]
    
    kmers <- genKMers(str,k)
    edge_m <- genEdges(kmers,k)
    
    edges <- rbind(edges,edge_m)
    
  }
  
  return(edges)
  
}

eds <- createEdgeList(data)


filepath3 <- paste(filepath1,"edge_list",sep = "/")
write.table(eds,file = filepath3,col.names = FALSE, row.names = FALSE,sep = "\t", quote= FALSE)

g <- graph_from_edgelist(eds, directed = TRUE)


jpeg(paste(filepath1,"plot.jpg",sep="/"))
plot(g)
dev.off()

