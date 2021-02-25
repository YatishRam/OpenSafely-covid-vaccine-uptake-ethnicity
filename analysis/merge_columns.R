args = commandArgs(trailingOnly=TRUE)

measures_folder <- "./output/measures/"
current_folder <- paste(measures_folder, args[1], sep="")

measures <- list.files(path = current_folder, pattern="*_stp.csv", full.names=TRUE, recursive=FALSE, ignore.case = TRUE)


for (measure in measures){
	df <- read.csv(measure)
	
	if(startsWith(args[1], "gender")){
		df <- within(df, age_group <- paste(age_group, sex, sep="_"))
		df <- subset(df, select=-c(sex))
	}
	
	if(startsWith(args[1], "ethnicity")){
		df <- within(df, age_group <- paste(age_group, ethnicity, sep="_"))
		df <- subset(df, select=-c(ethnicity))
	}

	write.csv(df, measure, row.names=FALSE)
}
