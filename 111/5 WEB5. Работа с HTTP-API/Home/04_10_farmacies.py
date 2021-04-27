import sys

from Samples.business import find_businesses
from Samples.geocoder import get_coordinates
from Samples.mapapi_PG import show_map


def main():
    toponym_to_find = " ".join(sys.argv[1:])

    if not toponym_to_find:
        print('No data')
        exit(1)

    lat, lon = get_coordinates(toponym_to_find)
    address_ll = f"{lat},{lon}"

    # Подбираем масштаб, чтобы получить минимум 10 аптек.
    delta = 0.01
    organizations = []
    while delta < 100 and len(organizations) < 10:
        delta *= 2.0
        span = f"{delta},{delta}"
        organizations = find_businesses(address_ll, span, "аптека")

    # Формируем список из координат аптек и их круглосуточности
    farmacies_with_time = []
    for org in organizations:
        point = org["geometry"]["coordinates"]
        hours = org["properties"]["CompanyMetaData"].get("Hours", None)
        if hours:  # У организации есть данные о времени работы
            available = hours["Availabilities"][0]
            is_24x7 = available.get("Everyday", False) and available.get("TwentyFourHours", False)
        else:  # Данных о времени работы нет.
            is_24x7 = None
        # Запоминаем полученные данные.
        farmacies_with_time.append((point, is_24x7))

    # Формируем параметр с точками
    points_param = "pt=" + "~".join([
        f'{point[0]},{point[1]},pm2{"gn" if is_24x7 else ("lb" if not is_24x7 else "gr")}l'
        for point, is_24x7 in farmacies_with_time])

    # Используем автопозиционирование карты по всем меткам.
    show_map(map_type="map", add_params=points_param)


if __name__ == "__main__":
    main()
