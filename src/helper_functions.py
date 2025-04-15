# filenameSave1 = path_project_plots + signal_name
# figure_file_no_ext = f'{path_project_plots_vault}{signal_name}'
# figure_file = f'{figure_file_no_ext}.jpg'
# obsidian_figure_note = f'{path_figure_blocks}figure__block_{signal_name}.md'
def plot_in_Obsidian(plt, filenameSave1, figure_file_no_ext, obsidian_figure_note, signal_name = 'signal_'):
	extensions = ['.pdf', '.jpg', '.png']
	has_extension = np.any([filenameSave1.endswith(ext) for ext in extensions])
	plt.savefig(filenameSave1 + '.jpg'*(not has_extension))
	plt.close()
	
	# create figure note file
	with open(path_figure_block_template, 'r') as file:
		lines = file.readlines()
		
  
	figure_file = f'{figure_file_no_ext}.jpg'
	lines.append('\n'+f"![[{figure_file}]]".replace('\\', '/')+'\n')
 
	with open(obsidian_figure_note, 'w') as file:
		file.writelines(lines)
	
	figBlockFileName = f'figure__block_{signal_name}'
	figureFileSim = f'{path_figure_blocks}{figBlockFileName}.md'
	fields_1 = default_fields__sim_res_signal_file
	if os.path.exists(filenameSave1+'.md'):
		fields_1 = get_fields_from_Obsidian_note(filenameSave1+'.md', expected_fields__sim_res_signal_file)

	dum1 = '#sig_qual/'
	with open(filenameSave1+'.md', 'w', encoding='utf8') as file:
		write1 = [
			'%%',
			f'{expected_fields__sim_res_signal_file[0]}{dum1}{fields_1[0].replace(dum1, "")}',
			f'{expected_fields__sim_res_signal_file[1]}{fields_1[1]}',
			'%%',
			'# %% fig %%',
			'`=replace(this.quality, "#sig_qual/", "")`'
			]
		write1.append(f'![[{figBlockFileName}#fig]]'+'\n')
		file.write("\n".join(write1))  # Write filenames in the specified format

	return figureFileSim
