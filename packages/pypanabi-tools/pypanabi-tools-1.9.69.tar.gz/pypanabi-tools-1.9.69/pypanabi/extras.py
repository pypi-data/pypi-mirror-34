#!/usr/bin/env python

import re
import os
import pytz
import jenkins
import logging
import smtplib
from datetime import datetime, timedelta
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

MILLIS_FORMAT = "%Y%m%d%H%M%S%f"
DATE_FORMAT = "%Y-%m-%d"
TS_MILLIS_FORMAT = "%Y-%m-%d %H:%M:%S.%f"
TS_FORMAT = "%Y-%m-%d %H:%M:%S"
HOUR_FORMAT = "%H"
MINUTE_FORMAT = "%M"
SECOND_FORMAT = "%S"
EPOCH_FORMAT = "%s"
MONTH_FORMAT = "%Y%m"
YEAR_FORMAT = "%Y"

logger = logging.getLogger(__name__)

#####################################
#        Location Functions         #
#####################################
COUNTRIES = {
    'ru': {'country_name': 'Russia', 'business_region': 'russia', 'aws_region': 'unknown'},
    'in': {'country_name': 'India', 'business_region': 'asia', 'aws_region': 'ap-southeast-1'},
    'pl': {'country_name': 'Poland', 'business_region': 'eu', 'aws_region': 'eu-west-1'},
    'pt': {'country_name': 'Portugal', 'business_region': 'eu', 'aws_region': 'eu-west-1'},
    'ro': {'country_name': 'Romania', 'business_region': 'eu', 'aws_region': 'eu-west-1'},
    'ar': {'country_name': 'Argentina', 'business_region': 'latam', 'aws_region': 'us-east-1'},
    'co': {'country_name': 'Colombia', 'business_region': 'latam', 'aws_region': 'us-east-1'},
    'ec': {'country_name': 'Ecuador', 'business_region': 'latam', 'aws_region': 'us-east-1'},
    'pe': {'country_name': 'Peru', 'business_region': 'latam', 'aws_region': 'us-east-1'},
    'tr': {'country_name': 'Turkey', 'business_region': 'asia', 'aws_region': 'ap-southeast-1'},
    'be': {'country_name': 'Belgium', 'business_region': 'eu', 'aws_region': 'eu-west-1'},
    'cz': {'country_name': 'Czech Republic', 'business_region': 'eu', 'aws_region': 'eu-west-1'},
    'hr': {'country_name': 'Croatia', 'business_region': 'eu', 'aws_region': 'eu-west-1'},
    'nl': {'country_name': 'Netherlands', 'business_region': 'eu', 'aws_region': 'eu-west-1'},
    'si': {'country_name': 'Slovenia', 'business_region': 'eu', 'aws_region': 'eu-west-1'},
    'sk': {'country_name': 'Slovakia', 'business_region': 'eu', 'aws_region': 'eu-west-1'},
    'ua': {'country_name': 'Ukraine', 'business_region': 'eu', 'aws_region': 'eu-west-1'},
    'hn': {'country_name': 'Honduras', 'business_region': 'latam', 'aws_region': 'us-east-1'},
    'ae': {'country_name': 'Uae', 'business_region': 'mea', 'aws_region': 'eu-west-1'},
    'qa': {'country_name': 'Qatar', 'business_region': 'mea', 'aws_region': 'eu-west-1'},
    'za': {'country_name': 'South Africa', 'business_region': 'mea', 'aws_region': 'eu-west-1'},
    'ca': {'country_name': 'Canada', 'business_region': 'na', 'aws_region': 'us-east-1'},
    'us': {'country_name': 'United States', 'business_region': 'na', 'aws_region': 'us-east-1'},
    'br': {'country_name': 'Brazil', 'business_region': 'brazil', 'aws_region': 'unknown'},
    'bd': {'country_name': 'Bangladesh', 'business_region': 'asia', 'aws_region': 'ap-southeast-1'},
    'id': {'country_name': 'Indonesia', 'business_region': 'asia', 'aws_region': 'ap-southeast-1'},
    'ph': {'country_name': 'Philippines', 'business_region': 'asia', 'aws_region': 'ap-southeast-1'},
    'ao': {'country_name': 'Angola', 'business_region': 'eu', 'aws_region': 'eu-west-1'},
    'ba': {'country_name': 'Bosnia', 'business_region': 'eu', 'aws_region': 'eu-west-1'},
    'bg': {'country_name': 'Bulgaria', 'business_region': 'eu', 'aws_region': 'eu-west-1'},
    'by': {'country_name': 'Belarus', 'business_region': 'eu', 'aws_region': 'eu-west-1'},
    'es': {'country_name': 'Spain', 'business_region': 'eu', 'aws_region': 'eu-west-1'},
    'fr': {'country_name': 'France', 'business_region': 'eu', 'aws_region': 'eu-west-1'},
    'kz': {'country_name': 'Kazakhstan', 'business_region': 'eu', 'aws_region': 'eu-west-1'},
    'mz': {'country_name': 'Mozambique', 'business_region': 'eu', 'aws_region': 'eu-west-1'},
    'uz': {'country_name': 'Uzbekistan', 'business_region': 'eu', 'aws_region': 'eu-west-1'},
    'bo': {'country_name': 'Bolivia', 'business_region': 'latam', 'aws_region': 'us-east-1'},
    'cr': {'country_name': 'Costa Rica', 'business_region': 'latam', 'aws_region': 'us-east-1'},
    'gt': {'country_name': 'Guatemala', 'business_region': 'latam', 'aws_region': 'us-east-1'},
    'ni': {'country_name': 'Nicaragua', 'business_region': 'latam', 'aws_region': 'us-east-1'},
    'pa': {'country_name': 'Panama', 'business_region': 'latam', 'aws_region': 'us-east-1'},
    'py': {'country_name': 'Paraguay', 'business_region': 'latam', 'aws_region': 'us-east-1'},
    'sv': {'country_name': 'El Salvador', 'business_region': 'latam', 'aws_region': 'us-east-1'},
    'uy': {'country_name': 'Uruguay', 'business_region': 'latam', 'aws_region': 'us-east-1'},
    've': {'country_name': 'Venezuela', 'business_region': 'latam', 'aws_region': 'us-east-1'},
    'bh': {'country_name': 'Bahrain', 'business_region': 'mea', 'aws_region': 'eu-west-1'},
    'cm': {'country_name': 'Cameroon', 'business_region': 'mea', 'aws_region': 'eu-west-1'},
    'eg': {'country_name': 'Egypt', 'business_region': 'mea', 'aws_region': 'eu-west-1'},
    'gh': {'country_name': 'Ghana', 'business_region': 'mea', 'aws_region': 'eu-west-1'},
    'jo': {'country_name': 'Jordan', 'business_region': 'mea', 'aws_region': 'eu-west-1'},
    'ke': {'country_name': 'Kenya', 'business_region': 'mea', 'aws_region': 'eu-west-1'},
    'kw': {'country_name': 'Kuwait', 'business_region': 'mea', 'aws_region': 'eu-west-1'},
    'lb': {'country_name': 'Lebanon', 'business_region': 'mea', 'aws_region': 'eu-west-1'},
    'ng': {'country_name': 'Nigeria', 'business_region': 'mea', 'aws_region': 'eu-west-1'},
    'om': {'country_name': 'Oman', 'business_region': 'mea', 'aws_region': 'eu-west-1'},
    'pk': {'country_name': 'Pakistan', 'business_region': 'mea', 'aws_region': 'ap-southeast-1'},
    'sa': {'country_name': 'Saudi Arabia', 'business_region': 'mea', 'aws_region': 'eu-west-1'},
    'tz': {'country_name': 'Tanzania', 'business_region': 'mea', 'aws_region': 'eu-west-1'},
    'ug': {'country_name': 'Uganda', 'business_region': 'mea', 'aws_region': 'eu-west-1'},
    'unknown': {'country_name': 'Unknown', 'business_region': 'unknown', 'aws_region': 'unknown'}
}

REGIONS = {
    'unknown': {'business_region_name': 'Unknown'},
    'brazil': {'business_region_name': 'Brazil'},
    'na': {'business_region_name': 'North America'},
    'latam': {'business_region_name': 'Latin America'},
    'mea': {'business_region_name': 'Middle East and Africa'},
    'eu': {'business_region_name': 'Europe'},
    'asia': {'business_region_name': 'Asia'},
    'russia': {'business_region_name': 'Russia'}
}

AWS_REGIONS = {
    'us-east-1': {'aws_region_name': 'Virginia', 'alias': 'america'},
    'us-west-2': {'aws_region_name': 'Oregon', 'alias': 'america'},
    'eu-west-1': {'aws_region_name': 'Ireland', 'alias': 'europe'},
    'ap-southeast-1': {'aws_region_name': 'Singapur', 'alias': 'asia'},
    'unknown': {'aws_region_name': 'Unknown', 'alias': 'unknown'}
}

MAP_CLASSIC_REGIONS = {
    'ssa': {'business_region': 'mea'},
    'mena': {'business_region': 'mea'},
    'menapk': {'business_region': 'mea'},
    'id': {'business_region': 'asia'},
    'ph': {'business_region': 'asia'},
    'sa': {'business_region': 'asia'},
    'cee': {'business_region': 'eu'},
    'latam': {'business_region': 'latam'}
}


def is_valid_config(config, mandatory_keypaths):
    """
    Check if all mandatory keys are present in the configuration file
    :param config: Configuration [JSONFile]
    :param mandatory_keypaths: Mandatory keys to check [List<String>]
    :return: Missing keys [List<String>]
    """
    missing_keypaths = set()

    for keypath in mandatory_keypaths:
        missing_keypaths.union(is_valid_path(config, keypath))

    return missing_keypaths


def is_valid_path(config, keypath, step=0):
    """
    Check recursively if the keypath exists in the configuration given
    :param config: configuration object [List | Dict]
    :param keypath: path to key [String]
    :param step: index of keypath to check [Integer]
    :return: set of missing keypaths in the configuration [Set<String>]
    """
    keys = keypath.split('/')
    missing_keys = []

    if step < len(keys):
        key = keys[step]

        if isinstance(config, dict):
            if key in config:
                missing_keys += is_valid_path(config[key], keypath, step + 1)
            else:
                missing_keys.append(keypath)
        elif isinstance(config, list):
            for e in config:
                if key in e:
                    missing_keys += is_valid_path(e[key], keypath, step + 1)
                else:
                    missing_keys.append(keypath)

    return set(missing_keys)


def get_business_region_for_classic_region(classic_region):
    """
    Get business region for classic region
    :param classic_region: classic region name [String]
    :return: business region [String]
    """
    business_region = None
    if classic_region in MAP_CLASSIC_REGIONS:
        business_region = MAP_CLASSIC_REGIONS[classic_region]['business_region']
    return business_region


def get_business_regions(all_group=False):
    """
    Get business regions
    :param all_group: indicates if all regions must be included [Boolean]
    :return: All regions name [List<String<]
    """
    if all_group:
        l_regions = [COUNTRIES[x]['business_region'] for x in COUNTRIES if COUNTRIES[x]['business_region'] != 'unknown']
    else:
        l_regions = [COUNTRIES[x]['business_region'] for x in COUNTRIES if COUNTRIES[x]['business_region'] not in ['unknown',
                                                                                                                   'russia',
                                                                                                                   'na',
                                                                                                                   'brazil']]
    return set(l_regions)


def get_countries_in_business_region(region):
    """
    Get countries in the region specified
    :param region: business region [String]
    :return: ISO country codes included in the region [List<String>]
    """
    region = region.lower()

    l_countries = [x for x in COUNTRIES if COUNTRIES[x]['business_region'] == region]
    return l_countries


def get_countries_in_aws_region(aws_region):
    """
    Get countries in the region specified
    :param aws_region: aws region or business region [String]
    :return: ISO country codes included in the region [List<String>]
    """
    aws_region = aws_region.lower()

    l_countries = [x for x in COUNTRIES if COUNTRIES[x]['aws_region'] == aws_region]
    return l_countries


def get_country_information(country_iso_code):
    """
    Get country information
    :param country_iso_code: ISO code of the country [String]
    :return: Country information [Dictionary]
    """
    country_iso_code = country_iso_code.lower()

    if country_iso_code not in COUNTRIES:
        country_iso_code = 'unknown'

    country_info = COUNTRIES[country_iso_code]
    region_info = REGIONS[country_info['region']]
    return dict(country_info.items() + region_info.items())


def get_business_region_information(region):
    """
    Get country information
    :param region: business region name [String]
    :return: Region information [Dictionary]
    """
    region = region.lower()

    if region not in REGIONS:
        region = 'unknown'

    return REGIONS[region]


def get_aws_region_information(aws_region):
    """
    Get country information
    :param aws_region: aws region name [String]
    :return: Region information [Dictionary]
    """
    aws_region = aws_region.lower()

    if aws_region not in AWS_REGIONS:
        aws_region = 'unknown'

    return AWS_REGIONS[aws_region]


def get_current_datetime_country(country_iso_code):
    """
    Get current date for a given country
    :param country_iso_code: ISO country code [String]
    :return: Current timestamp [Datetime]
    """
    date = datetime.utcnow()
    from_zone = pytz.timezone('UTC')
    local_tz = get_timezone_country(country_iso_code)
    if not local_tz:
        return None
    to_zone = pytz.timezone(local_tz)

    utc_date = from_zone.localize(date)
    local_date = utc_date.astimezone(to_zone)

    return local_date


def get_timezone_country(country_iso_code):
    """
    Get timezone for a given country
    :param country_iso_code: ISO country code [String]
    :return: Timezone [String]
    """
    tz = None
    for country in pytz.country_timezones.items():
        if country[0] == country_iso_code.upper():
            tz = country[1][0]
            break
    return tz


def get_timezone_offset(tz):
    """
    Return offset from UTC timezone
    :param tz: timezone [pytz timezone]
    :return: offset [float]
    """
    try:
        if tz:
            offset = datetime.now(pytz.timezone(tz)).utcoffset().total_seconds() / 60 / 60
        else:
            offset = None
        return offset
    except Exception as ex:
        logger.error(repr(ex))


def get_min_timezone_in_business_region(region):
    """
    Min timezone in a given region
    :param region: business region name [String]
    :return: Tuple with timezone and offset [Tuple<pytz timezone, offset]
    """
    l_countries = get_countries_in_business_region(region=region)

    max_tz = None
    max_offset = 99
    for country in l_countries:
        tz = get_timezone_country(country)
        offset = get_timezone_offset(tz)

        if offset < max_offset:
            max_tz = tz
            max_offset = offset

    return max_tz, max_offset


def get_min_timezone_in_aws_region(aws_region):
    """
    Min timezone in a given region
    :param aws_region: aws region name [String]
    :return: Tuple with timezone and offset [Tuple<pytz timezone, offset]
    """
    l_countries = get_countries_in_aws_region(aws_region=aws_region)

    max_tz = None
    max_offset = 99
    for country in l_countries:
        tz = get_timezone_country(country)
        offset = get_timezone_offset(tz)

        if offset < max_offset:
            max_tz = tz
            max_offset = offset

    return max_tz, max_offset


#####################################
#           JSON Functions          #
#####################################


#####################################
#        JENKINS Functions          #
#####################################
class Jenkins(object):
    def __init__(self, host='localhost:8080', username=None, password=None):
        """
        Constructor
        :param host: Full host path, hostname:port. Default: localhost:8080 [String]
        :param username: User name [String]
        :param password: Password [String]
        """
        self._logger = logging.getLogger(__name__)
        self._server = jenkins.Jenkins(host, username=username, password=password)


#####################################
#           S3 Functions            #
#####################################
def build_prefix(prefix, full_prefix=False, **args):
    """
    Build keys replacing variables with values provided in args
    :param prefix: S3 prefix with variables to be replaced in format {<variable>} [String]
    :param full_prefix: full prefix or just prefix wo bucket [String]
    :param args: Variables as dictionary, with value to be replaced [Dictionary]
    :return: S3 prefix formatted [String]
    """
    def variables_to_replace(string, format_regex='{([^}]+)'):
        vars = re.findall(format_regex, string)
        vars = list(set(vars))
        return vars

    # Formatting prefix
    sep = '/'
    if not full_prefix:
        prefix_formatted = sep.join([x for x in prefix.split(sep) if x.strip()])
        if prefix_formatted.lower().startswith('s3'):
            prefix_formatted = sep.join(prefix_formatted.split('/')[2:])
    else:
        prefix_formatted = prefix

    # Checking variables
    vars_rep = variables_to_replace(prefix_formatted)

    if len(vars_rep) != 0 and args:
        check = any(x for x in variables_to_replace(prefix_formatted) if x not in args)
        if check:
            raise Exception('Number of variables to replace do not match with number of values provided')
        else:
            prefix_formatted = prefix_formatted.format(**args)
    elif len(vars_rep) != 0 and not args:
        raise Exception('No values provided for variables in prefix')

    return prefix_formatted


def full_s3_path(bucket_name, prefix):
    """
    Get S3 full path
    :param bucket_name: Bucket name, in case that another bucket be required [String]
    :param prefix: S3 prefix or key [String]
    :return: S3 full path in format s3://<bucket/<prefix> [String]

    """
    # Formatting prefix
    sep = '/'
    prefix = sep.join([x for x in prefix.split(sep) if x.strip()])

    return sep.join(['s3:/', bucket_name, prefix])


def generate_manifest(bucket, keys, mandatory=False):
    """
    Generate manifest with all prefixes
    :param bucket: bucket name [String]
    :param keys: lists of keys [List<String>]
    :param mandatory: check s3 path [String]
    :return: json manifest [Dictionary]

    """
    entries = []
    for key in keys:
        s3_path = full_s3_path(bucket_name=bucket, prefix=key)
        entry = {
            "url": s3_path,
            "mandatory": mandatory
        }
        entries.append(entry)

    return {"entries": entries}


#####################################
#           OS Functions            #
#####################################
def get_environment_variables():
    """
    Get all environment variables
    :return: Dictionary with environment variables [Dictionary]
    """
    return os.environ


def clean_directory(local_path):
    """
    Clean local directory recursively
    :param local_path: Full path of the folder to clean [String]
    :return: None
    """
    try:
        emptyDirs = []
        tree = os.walk(local_path)

        for directory in tree:
            for file in directory[2]:
                os.remove(directory[0] + os.sep + file)
            emptyDirs.insert(0, directory[0])

        for dir in emptyDirs:
            os.rmdir(dir)
    except OSError as ex:
        logger.error(repr(ex))
        raise


def create_directory(local_path):
    """
    Create local directory
    :param local_path: Full path of the folder to create [String]
    :return: None
    """
    try:
        dirname = os.path.dirname(local_path)
        if not os.path.exists(dirname):
            os.makedirs(dirname)
    except OSError as ex:
        print(repr(ex))
        raise


def change_working_directory(local_path):
    """
    Change current working directory
    :param local_path: Full path of the folder to convert in current working directory [String]
    :return: None
    """
    try:
        os.chdir(local_path)
    except OSError as ex:
        logger.error(repr(ex))
        raise


def search_project_root_path(main_script_path, project_name):
    """
    Get full path of the project root folder
    :param main_script_path: Full path of the main parent script, caller of this function [String]
    :param project_name: Project name to find [String]
    :return: Full path of the project root folder. If the project was not found, return current working
             directory [String]
    """
    try:
        cwd = os.getcwd()
        l_cwd = os.path.dirname(main_script_path).split(os.sep)
        count = len(l_cwd)

        while count > 0:
            dirname = l_cwd[-1]

            if dirname == project_name:
                cwd = os.sep.join(l_cwd)
                count = -1
            else:
                count -= 1
                l_cwd = l_cwd[:-1]

        return cwd
    except Exception as ex:
        logger.error(repr(ex))
        raise


#####################################
#        Datetime Functions         #
#####################################
def get_current_timestamp():
    """
    Get current datetime in UTC
    :return: Current datetime in UTC [Datetime]
    """
    return datetime.utcnow()


def get_epoch_timestamp(date=None, milliseconds=True):
    """
    Get date in epoch format
    :param date: Datetime. Default: utcnow() [Datetime]
    :param milliseconds: epoch with milliseconds or not [Boolean]
    :return: Datetime in epoch format [Integer]
    """
    factor = 1
    if milliseconds:
        factor *= 1000

    if date:
        utcnow = date
    else:
        utcnow = datetime.utcnow()

    epoch = datetime.utcfromtimestamp(0)

    return int((utcnow - epoch).total_seconds() * factor)


def get_date_format(date):
    """
    Get date format
    :param date: Date in string format [String]
    :return: Format [String]
    """
    format = None
    try:
        date_format = "%Y-%m-%d"
        datetime.strptime(date, date_format)
        format = date_format
    except Exception:
        try:
            ts_format = "%Y-%m-%d %H:%M:%S"
            datetime.strptime(date, ts_format)
            format = ts_format
        except Exception:
            pass
        pass
    return format


def string_to_datetime(date, format=None):
    """
    Convert string date to datetime format
    :param date: Date in string format
    :param format: Format to parse date. Default: calculated using function get_date_format() [String]
    :return: Date [Datetime]
    """
    try:
        if not format:
            format = get_date_format(date)
        date_formatted = datetime.strptime(date, format)
        return date_formatted
    except Exception as ex:
        logger.error(repr(ex))
        raise


def generate_datetime_serie(date, shift=0, hop='hours'):
    """
    Generate serie with all dates between 2 dates provided
    :param date: Base date to calculate shifted date [Datetime]
    :param shift: Delta days/hours [Integer]
    :param hop: Hop type, days or hours. Default: hours [String]
    :return: List of all dates [List<Datetime>]
    """
    l_dates = []

    # Delta/Factor
    if shift == 0:
        factor = shift
    else:
        factor = shift / abs(shift)
    delta = dict()
    index = 0

    while index <= abs(shift):
        delta[hop] = index * factor
        l_dates.append(date + timedelta(**delta))
        index += 1

    l_dates.sort()

    return l_dates


def datetime_to_json(date):
    """
    Convert datetime in a dictionary
    :param date: Date in datetime format [Datetime]
    :return: Dictionary with all components of the date: year, month, day, hour, minute, second [Dictionary]
    """
    year = str(date.year)
    month = str(date.month).zfill(2)
    day = str(date.day).zfill(2)
    hour = str(date.hour).zfill(2)
    minute = str(date.minute).zfill(2)
    second = str(date.second).zfill(2)

    json_date = {'year': year,
                 'month': month,
                 'day': day,
                 'hour': hour,
                 'minute': minute,
                 'second': second}

    return json_date


def shift_datetime(date, shift=0):
    """
    Generate range of dates
    :param date: Base date to calculate shifted date [Datetime]
    :param shift: Delta days [Integer]
    :return: Dictionary with from and to key [Dictionary]
    """
    try:
        range = dict()
        date_shifted = date + timedelta(days=shift)
        if shift < 0:
            range['from'] = date_shifted
            range['to'] = date
        else:
            range['from'] = date
            range['to'] = date_shifted
        return range
    except Exception as ex:
        logger.error(repr(ex))
        raise


def get_difference(date_from, date_to, mode='days'):
    """
    Get difference in days or hours between to dates
    :param date_from: Date from value [Datetime]
    :param date_to: Date to value [Datetime]
    :param mode: Days or hours values allowed [String]
    :return: Difference in days or hours [Integer]
    """
    # Deltas
    delta_by_mode = dict()
    delta_by_mode[mode] = 1

    # Checking dates
    if date_from > date_to:
        aux = date_from
        date_from = date_to
        date_to = aux

    # Calculating shift
    shift = 0
    while date_from <= date_to:
        shift += delta_by_mode[mode]
        date_from = date_from + timedelta(**delta_by_mode)

    return shift


#####################################
#         String Functions          #
#####################################
def get_variables_to_replace(query, pattern='\{(.*)\}'):
    """
    Get list of variables to replace in string
    :param query: Query to check [String}
    :param pattern: Regular expression to match with the variables [String]
    :return: List of variables to be replaces [List<String>]
    """
    regex = re.compile(pattern)
    return re.findall(regex, query)


#####################################
#           Mix Functions           #
#####################################
class OLXMailer(object):
    def __init__(self, host='gmail-smtp-in.l.google.com', port=25, starttls=False):
        """
        Constructor
        :param host: Host name [String]
        :param port: Port number [Integer]
        """
        self._logger = logging.getLogger(__name__)
        self._client = smtplib.SMTP(host=host, port=port)
        self._client.ehlo('mail.olx.com')
        if starttls:
            self._client.starttls()
        self._client.set_debuglevel(1)
        self._message = MIMEMultipart('alternative')
        self._sender = 'panamera-bi@olx.com'
        self._receiver = None

    def sender(self, email):
        """
        Define sender email
        :param email: Email [String]
        :return: None
        """
        self._sender = email
        self._message['From'] = email

    def receiver(self, emails):
        """
        Define receiver emails
        :param emails: List of emails [List<Strings>]
        :return: None
        """
        self._receiver = emails
        self._message['To'] = ', '.join(emails)

    def subject(self, subject):
        """
        Define Subject
        :param subject: Subject [String]
        :return: None
        """
        self._message['Subject'] = subject

    def body(self, body, is_html=False):
        """
        Define message body
        :param body: Message [String]
        :param is_html: Indicates if the body is html or not [Boolean]
        :return: None
        """
        if is_html:
            self._message.attach(MIMEText(body, 'html'))
        else:
            self._message.attach(MIMEText(body, 'plain'))

    def attachment(self, files):
        """
        Attach files
        :param files: Files to be attached [List<String>]
        :return: None
        """
        for file in files or []:
            with open(file, "rb") as f:
                part = MIMEApplication(f.read(), Name=os.path.basename(file))

            # After the file is closed
            part['Content-Disposition'] = 'attachment; filename="%s"' % os.path.basename(file)
            self._message.attach(part)

    def message(self, From=None, To=None, Subject=None, Body=None, is_html=False):
        """
        Create message
        :param From: From email [String]
        :param To: To list emails [List<String>]
        :param Subject: Subject [String]
        :param Body: Message [String]
        :param is_html: Indicates if the body is html or not [Boolean]
        :return: None
        """
        if From:
            self._sender = From

        if To:
            self._receiver = To
        else:
            self._receiver = self._sender

        if not Subject:
            Subject = ''

        if not Body:
            Body = ''
            is_html = False

        self._message['From'] = self._sender
        self._message['To'] = ', '.join(self._receiver)
        self._message['Subject'] = Subject

        if is_html:
            self._message.attach(MIMEText(Body, 'html'))
        else:
            self._message.attach(MIMEText(Body, 'plain'))

    def send(self):
        """
        Send Message
        :return: None
        """
        try:
            self._logger.debug(self._message.as_string())
            self._client.sendmail(self._sender, self._receiver, self._message.as_string())
        except Exception as ex:
            self._logger.error(repr(ex))
            raise

    def close(self):
        """
        Close client
        :return: None
        """
        self._client.quit()




