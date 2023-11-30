import click
import argparse
from compute_distance.functions import compute_distance_debug

@click.command()
@click.option('--apath', '-a', 'admin_path', type = click.Path(exists = True, dir_okay = False), help = 'Path to admin0 file')
@click.option('--apath', '-v', 'vector_file_path', type = click.Path(exists = True, dir_okay = False), help = 'Path to vector file')
@click.option('--apath', '-r', 'raster_template_path', type = click.Path(exists = True, dir_okay = False), help = 'Path to raster template file')
@click.option('--apath', '-o', 'outdir_path', type = click.Path(exists = True, dir_okay = True), help = 'Path to output directory')
def cli(admin_path, vector_file_path, raster_template_path, outdir_path) -> None:
    print('Start of Distance Computation')
    compute_distance_debug(admin_path, vector_file_path, raster_template_path, outdir_path)

    pass



# def main() -> None:
#     parser = argparse.ArgumentParser(description='Compute distance using CLI')
#     parser.add_argument('admin0_path', help='Path to admin0 file')
#     parser.add_argument('vector_file_path', help='Path to vector file')
#     parser.add_argument('meta_data_path', help='Path to raster template')
#     parser.add_argument('out_path', help='Path for output')
#     parser.add_argument('image_save_path', help='Path to save images')

#     args = parser.parse_args()
#     compute_distance(
#         args.admin0_path,
#         args.vector_file_path,
#         args.meta_data_path,
#         args.out_path,
#         args.image_save_path
#     )

# if __name__ == '__main__':
#     main()
