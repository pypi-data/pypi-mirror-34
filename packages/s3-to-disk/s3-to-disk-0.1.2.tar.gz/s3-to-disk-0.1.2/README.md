# S3ToDisk

This is a simple tool to synchronizes S3 to a local folder. It uses `aws s3 sync` command behind the scene.

This package works on Python versions:

* 2.7.x and greater
* 3.6.x and greater

## Usage

Set your aws credentials as explained in [aws-cli/getting-started](https://github.com/aws/aws-cli#getting-started)

Run `s3-to-disk --help` to get more information about parameters.

Run `s3-to-disk -D s3 -L log --dry-run` to clone all your S3
