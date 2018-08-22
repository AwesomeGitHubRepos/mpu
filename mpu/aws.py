#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Convenience functions for AWS interactions."""

# core modules
import os

# 3rd party modules
import boto3


def list_files(bucket, profile_name=None):
    """
    List up to 1000 files in a bucket.

    Parameters
    ----------
    bucket : str
    profile_name : str, optional
        AWS profile

    Returns
    -------
    s3_paths : list
    """
    session = boto3.Session(profile_name=profile_name)
    conn = session.client('s3')
    keys = []
    ret = conn.list_objects(Bucket=bucket)
    print(ret)
    if 'Contents' not in ret:
        return []
    # Make this a generator in future and use the marker:
    # https://boto3.readthedocs.io/en/latest/reference/services/
    #     s3.html#S3.Client.list_objects
    for key in conn.list_objects(Bucket=bucket)['Contents']:
        keys.append('s3://' + bucket + '/' + key['Key'])
    return keys


def s3_download(source, destination,
                exists_strategy='raise',
                profile_name=None):
    """
    Copy a file from an S3 source to a local destination.

    Parameters
    ----------
    source : str
        Path starting with s3://, e.g. 's3://bucket-name/key/foo.bar'
    destination : str
    exists_strategy : {'raise', 'replace', 'abort'}
        What is done when the destination already exists?
    profile_name : str, optional
        AWS profile

    Raises
    ------
    botocore.exceptions.NoCredentialsError
        Botocore is not able to find your credentials. Either specify
        profile_name or add the environment variables AWS_ACCESS_KEY_ID,
        AWS_SECRET_ACCESS_KEY and AWS_SESSION_TOKEN.
        See https://boto3.readthedocs.io/en/latest/guide/configuration.html
    """
    exists_strategies = ['raise', 'replace', 'abort']
    if exists_strategy not in exists_strategies:
        raise ValueError('exists_strategy \'{}\' is not in {}'
                         .format(exists_strategy, exists_strategies))
    session = boto3.Session(profile_name=profile_name)
    s3 = session.resource('s3')
    bucket_name, key = _s3_path_split(source)
    if os.path.isfile(destination):
        if exists_strategy is 'raise':
            raise RuntimeError('File \'{}\' already exists.'
                               .format(destination))
        elif exists_strategy is 'abort':
            return
    s3.Bucket(bucket_name).download_file(key, destination)


def s3_upload(source, destination, profile_name=None):
    """
    Copy a file from a local source to an S3 destination.

    Parameters
    ----------
    source : str
    destination : str
        Path starting with s3://, e.g. 's3://bucket-name/key/foo.bar'
    profile_name : str, optional
        AWS profile
    """
    session = boto3.Session(profile_name=profile_name)
    s3 = session.resource('s3')
    bucket_name, key = _s3_path_split(destination)
    with open(source, 'rb') as data:
        s3.Bucket(bucket_name).put_object(Key=key, Body=data)


def _s3_path_split(s3_path):
    """
    Split an S3 path into bucket and key.

    Parameters
    ----------
    s3_path : str

    Returns
    -------
    splitted : (str, str)
        (bucket, key)

    Examples
    --------
    >>> _s3_path_split('s3://my-bucket/foo/bar.jpg')
    ('my-bucket', 'foo/bar.jpg')
    """
    if not s3_path.startswith('s3://'):
        raise ValueError('s3_path is expected to start with \'s3://\', '
                         'but was {}'.format(s3_path))
    bucket_key = s3_path[len('s3://'):]
    bucket_name, key = bucket_key.split('/', 1)
    return bucket_name, key