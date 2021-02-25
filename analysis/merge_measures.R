args = commandArgs(trailingOnly=TRUE)

measures_folder <- "./output/measures/"
current_folder <- paste(measures_folder, args[1], sep="")

measures <- list.files(path = current_folder, pattern="*_stp.csv", full.names=TRUE, recursive=FALSE, ignore.case = TRUE)

filename = paste(paste(measures_folder, args[1], sep="/"), ".csv", sep="")

measure_count <- length(measures)

if (measure_count == 1){
	
	write.csv(read.csv(measures[1]), filename)

} else {

	population_group_column_name <- "age_group"
	
	if(length(args)==2){
		population_group_column_name <- args[2]
	}
	
	library(plyr)

	import.list <- llply(measures, read.csv)

	import.list <- llply(import.list, subset, select=-c(value))
	
	data <- Reduce(	
		function(x, y) 
		merge(x, y, by=c('stp', population_group_column_name,'population', 'date'), all=TRUE), 
		import.list
	)

	write.csv(data, filename)
}