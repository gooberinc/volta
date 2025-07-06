import time
from main import translations, LOCALE, find_locales_dirs, module_dir, working_dir, RESET
from main import load_translations 

YELLOW = "\033[93m"

def check_missing_translations():

    load_translations()

    if "en" not in translations:
        print("English translations (en.json) missing from assets/locales. Exiting.")
        return

    en_keys = set(translations["en"].keys())
    total_keys = len(en_keys)

    report_lines = []
    report_lines.append(f"Total keys in English locale: {total_keys}\n")

    for locale, trans_dict in translations.items():
        if locale in ("en", "empty"):
            continue
        locale_keys = set(trans_dict.keys())
        missing_keys = en_keys - locale_keys
        missing_count = len(missing_keys)
        percent_missing = (missing_count / total_keys) * 100 if total_keys > 0 else 0

        if missing_count > 0:
            print(f"{YELLOW}Warning: {missing_count}/{total_keys} keys missing in locale '{locale}' ({percent_missing:.1f}%)!{RESET}")
            for key in sorted(missing_keys):
                print(f"  - {key}")
            time.sleep(1)
        else:
            print(f"All translation keys present for locale: {locale}")

        report_lines.append(f"Locale: {locale}\n")
        report_lines.append(f"Missing keys ({missing_count}/{total_keys}): {percent_missing:.1f}%\n")
        if missing_count > 0:
            for key in sorted(missing_keys):
                report_lines.append(f"  - {key}\n")
        report_lines.append("\n")

    with open("translation_report.txt", "w", encoding="utf-8") as f:
        f.writelines(report_lines)

    print("\nTranslation report written to translation_report.txt")

if __name__ == "__main__":
    check_missing_translations()
